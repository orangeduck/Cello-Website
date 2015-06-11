  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# A Fat Pointer Library

When you first see Cello, it's hard to understand exactly what it is. You might 
think of Cello a framework, or perhaps as a syntax layer, or even a totally new 
programming language, but the best way I've found to think of it is as 
_A Fat Pointer Library_. Let me explain...

## The Proposal

Fat Pointers were [proposed](http://www.drdobbs.com/architecture-and-design/cs-biggest-mistake/228701625) 
by Walter Bright (inventor of the D programming language) as an extension to 
C, aimed to avoid the numerous pitfalls that come from the relationship between 
pointers and arrays.

The problem is this. In C when you pass an array to a function it _decays_ to a
pointer - meaning what you actually pass is just a pointer to the first element 
in the array. This means there is no way to know how many elements are in the 
Array you've been passed.

The conventional way to deal with this is to also pass in the array size
separately - or - as is done by C strings, use some special value to represent the 
end of the array. But both of these methods are famously prone to abuse. It is 
simply too unreliable to get programmers (or malicious users) to provide this 
extra information accurately.

Walter's proposal was simple. Introduce some new syntax for passing a 
_Fat Pointer_. This is just a pointer with the additional peice of information 
saying how many elements are in the array. Now this wouldn't do anything to fix 
existing C code, but would hopefully improve future C, and because 
_Fat Pointers_ would still just be pointers of a sort, it wouldn't break 
anything along the way.

This proposal wasn't accepted into the C standard, but it turns out this sort 
of thing doesn't have to be a language extension, we can actually emulate Fat 
Pointers in C ourselves.

The trick is to place the value representing the number of items in the array 
in memory _just before_ the pointer we actually pass to functions. This pointer 
is fully compatible with normal pointers, and if we need to know how many 
elements it points to we just move back a step in memory to get it.

        
              |--------------|  <-- Pointer to number of items
              |  ptr.length  |
              |==============|  <-- Pointer passed to functions
              |  ptr.item[0] |
              |--------------|
              |  ptr.item[1] |
              |--------------|
              |     ....     |
              |--------------|
        
        
This is exactly the approach used by the C strings library 
[sds](https://github.com/antirez/sds). This allows for strings that are safer, 
faster, and more efficient than C strings, but which are also compatible with 
standard C string functions.

The only caveat is that because the pointer passed around is not actually the 
address we got from the memory allocation routine (such as `malloc`) it can't be
freed or resized in the normal way with `free` or `realloc`. Instead we have to 
move back a step in memory and free _that_ pointer. So allocation, freeing, and 
resizing must all be done via special functions. But any good C interface 
should not assume pointers are heap allocated anyway.

## Runtime

To change a language's behaviour one must either change the compiler or the 
runtime. A language like C has no runtime system but we can add one ourselves. 
We can _tag_ objects with some extra information which our runtime 
system can make use of. In old versions of Cello this was done by directly 
embedding the information in C structs that were Cello compatible. This was okay
but it meant specfically editing every struct we want to make avaliable for use 
with Cello. 

Instead we can use the ideas behind _Fat Pointers_, and store our runtime 
information in the memory space _before_ pointers. In essence we make all our 
pointers to Cello objects _Fat_. Then Cello pointers would be fully 
compatible with standard C pointers and functions (with the exception of `free` 
and `realloc`), but also have the information to be used by our runtime system. 
In this sense our runtime really does _extended_ the language rather than 
create something that is conflicting.

In Cello this extra information is pretty simple. All we store is a pointer to 
the type such as `Int`, `Float` or `Array`.

    typedef void* var;

    struct Header {
      var type;
    };

We can then allocate Fat Pointers on the heap with some simple pointer 
arithmetic. Here is a modified version of the Cello function that does that.

    var alloc(size_t data_size) {
      struct Header* head = calloc(1, sizeof(struct Header) + data_size);
      head->type = type;
      return ((var)head) + sizeof(struct Header);
    }

And here is the deallocation function.

    void dealloc(var self) {
      struct Header* head = self - sizeof(struct Header);
      free(head);
    }

We can also allocate Fat Pointers on the stack. This takes two steps. First we 
allocate memory big enough for the data using a `char[]` and then we call a 
function to copy in the header details and return a pointer offset to point
to the data.

    #define alloc_stack(T) header_init( \
      (char[sizeof(struct Header) + sizeof(struct T)]){0}, T)

    var header_init(var head, var type) {
      struct Header* self = head;
      self->type = type;
      return ((char*)self) + sizeof(struct Header);
    }

We can also copy in some initial values to the members of this structure 
allocation. In Cello this is the `$` macro. It allocates an anonymous structure
of the given type, with the given members, and copies it into the allocation 
found by `alloc_stack`.

    #define $(T, ...) \
      memcpy(alloc_stack(T), &((struct T){__VA_ARGS__}), sizeof(struct T))

And now this gives us all we need to get started with our runtime. The next step
is to design the format of the extra information tagged onto our data - 
_the type_.

## Type Object

The _type_ is the meta-data associated with an object which tells us how it 
should behave. For example if we wish to add some generic `new` and `del` to a 
language, our _type_ must be able to tell us the size of the memory to 
allocate, or what action to perform on construction / destruction.

How we design our _type_ data should reflect the features we want available in 
the language. In Cello I chose a very simple design. The type object is just a
list of instances of [Type Classes](http://en.wikipedia.org/wiki/Type_class) 
(a.k.a Interfaces) which the object implements and some identifier for each. 
For example say we want some type to be able to be `get` or `set` using some 
keys and values - then we can provide it with an instance of the `Get` type 
class. 

In Cello a _type class_ is just a description of various behaviours with names, 
so it can be easily represented as a struct full of function pointers.

    struct Get {
      var  (*get)(var, var);
      void (*set)(var, var, var);
      var  (*mem)(var, var);
      void (*rem)(var, var);
    };

The actual type object structure in Cello is pretty complicated, but a 
simplified example might end up looking something like this under the hood.

    var Int = (struct TypeEntry[]){
      { "Size", &((struct Size){ Int_Size })
      { "New",  &((struct  New){ Int_New, Int_Del }) },
      { "Cmp",  &((struct  Cmp){ Int_Cmp }) },
      {  NULL,  NULL  }
    };

Then when (for example), we wish to call `new` to make an `Int`, we just lookup 
the type object, and if it implements the `New` _type class_ we can find the 
function pointer for that particular instance of the class, and call the 
function. This is very much like the concept of a 
[vtable](http://en.wikipedia.org/wiki/Virtual_method_table) from C++.


    if (type_implements(type, New)) {
        struct New* inst = type_instance(type, New);
        return inst->new(self, args);
    }


Perhaps the most surprising thing about this is that this single feature (of 
_type classes_ or _interfaces_) is powerful enough to support all of the 
advanced features you see in Cello. It isn't just used for things like 
constructors and destructors, it is used for everything, ranging from 
Garbage Collection to generating the Documentation.

It is well known now that family style inheritance is generally pretty bad for 
structuring things, and that single _interface_ inheritances tends to work a 
lot better - but Cello is a good example of how neat and practical a library 
can be designed around this single concept - and that if you are really forced
to stick to it you end up writing a lot of code in a very algorithmic, 
expressive, and readable way.

## Conclusion

Cello is a _Fat Pointer Library_. It lets you create pointers which are 
tagged with additional runtime information, which can then be used for a whole 
host of other tasks and features. In reality it is a little more complicated 
than the shallow explanation here, but hopefully this gives you a vague idea of 
how it works under the hood.

I've always tried to be objective about Cello. It is a hack on top of C, and 
hacks don't always end up celebrated. I've admitted there are many reasons I 
wouldn't use it for a project, and I don't expect others to either. I'm 
sometimes uncomfortable singing it's praises because I know it has issues. But 
I also think it has potential.

I believe the reason people get excited about Cello is because they see it 
similarly to what [underscore.js](http://underscorejs.org/) or 
[jquery](http://jquery.com/) did for Javascript. Suddenly a language that 
appeared stale, exhausted, and difficult was transformed into something that 
looked, and felt, completely different. Even if the transformation was somehow 
shallow underneither it is still very cool to see this happen just using a 
library. This inspired a lot of people, and a lot of libraries started popping 
up. The Javascript floodgates opened and it became something totally different.

Cello still has a lot of oddities and awkard bits, but so far Cello is the only 
_Fat Pointer Library_ I know of that tries to do everything, packaging it up 
in a nice syntax. The key thing to take away from this project is that it isn't 
entirerly unsuccessful, and that Cello is just one design of a runtime. There 
are many possible ways in which a Runtime could be designed with different 
strengths and ideas. I'd love to see what other people can do with this 
combination of thoughts, and just perhaps the _Fat Pointer_ has the potential 
to give C another breath of life, like Javascript was so lucky to have.

 
* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
