  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">
  
# Common Queries &amp; Pitfalls

1. [Returning Stack Objects](#returning-stack-objects)
2. [Retuning Inside a Try Block](#returning-inside-try-block)
3. [Garbage Collecting Objects Early](#garbage-collecting-early)
4. [Modifying Collections during Iteration](#modifying-collections-during-iteration)
5. [Types Without struct Prefix](#types-without-struct-prefix)
6. [Stack Trace using MinGW](#stack-trace-using-mingw)


## Returning Stack Objects <a name="returning-stack-objects"></a>

One of the first things most people do when they start using Cello is write a 
function that looks something like the following:

    var add_ints(var i0, var i1) {
      int64_t total = c_int(i0) + c_int(i1);
      return $I(total);
    }

And when they actually try to run this function it segfaults as soon as they 
try to do anything with the return value.
    
    void print_addition(void) {
      var x = add_ints($I(1), $I(2));
      print("%i", x);
    }
    
The reason is simple but not obvious. The returned value of the function 
`add_ints` is a pointer (all `var` means is _pointer_) to some data allocated 
on the called function's stack frame. As soon as that function ends and 
returns, the data the returned pointer was actually pointing to is 
already deallocated, and so doing anything with it usually results in a crash.

There are a couple of ways to achieve the desired result in Cello. If you 
actually want to assign the value to some stack item allocated by the caller 
you should make an output parameter and use the `assign` function. This is the 
recommended method.

    void add_ints(var out, var i0, var i1) {
      int64_t total = c_int(i0) + c_int(i1);
      assign(out, $I(total));
    }
    
    void print_addition(void) {
      var x = $I(0);
      add_ints(x, $I(1), $I(2));
      print("%i", x);
    }
    
But you could also allocate the return value on the heap to avoid it being 
deallocated once the call ends. As a word of warning this can be slow if you do 
it for lots of small objects.

    var add_ints(var i0, var i1) {
      int64_t total = c_int(i0) + c_int(i1);
      return new(Int, $I(total));
    }
    
    void print_addition(void) {
      var x = add_ints($I(1), $I(2));
      print("%i", x);
    }


## Returning Inside a Try Block <a name="returning-inside-try-block"></a>

Because of the way exceptions work in Cello (using Macros) it is very important 
that the `catch` part of an exception block is always provided, and always 
evaluated. If this doesn't happen the internal state the manages exceptions 
gets messed up and will break things nastily.

    try {
      do_something();
      return true;
    } catch (e in IOError) {
      return false;
    }
    
Please instead only return from outside of the `try` block.
    
    bool success = true;
    
    try {
      do_something();
    } catch (e in IOError) {
      success = false;
    }
    
    return success;

## Garbage Collecting Objects Early <a name="garbage-collecting-early"></a>

The [Cello Garbage Collector](/learn/garbage-collection) will collect any 
objects which it cannot reach. An object is reachable if there are any local 
variables on the stack pointing to it _or_ if it is pointer to from any other 
reachable Cello object.

This means objects stored in global variables, or in C structures which are not 
Cello objects, _aren't_ reachable by the Garbage Collector and so will be 
deleted almost immediately after construction.

You can block objects from being deleted by the Garbage Collector by allocating 
them with the function `new_root`. If you do this just remember to manually 
delete them with `del` once you are done.


## Modifying Collections during Iteration <a name="modifying-collections-during-iteration"></a>

It is very tempting to modify collections while you are iterating over them. 
For example you might write something like this, to remove all the elements 
from a table where `"hello"` is a sub-string of the key.

    foreach (k in table) {
      if (mem(k, $S("hello"))) {
        rem(table, k);
      }
    }

But because modifying collections can move around the elements within them this 
can result in very odd iteration behaviour including skipping over keys and 
returning some keys multiple times. 

If you need to iterate over a collection and modify it you should do so in two 
steps. First record all the modifications you want to make in some separate 
object and then apply them.

    var keys = new(Array, String);
    
    foreach (k in table) {
      if (mem(k, $S("hello")) {
        push(keys, k);
      }
    }
    
    foreach (k in keys) { rem(table, k); }
    
    
## Types Without struct Prefix <a name="types-without-struct-prefix"></a>

If you want to register structs with Cello the type name should have the 
`struct` prefix. Cello type objects also use the convention of CamelCase 
naming. Both of these conditions might not always be something you have 
control over, for example if you are wrapping external libraries. For 
example there might be a type like this you want to make available from Cello.

    typedef struct {
      Mix_Chunk* sample;
    } sound;

The solution here is to just wrap this in your own struct declaration. 
Providing it is the only struct member the pointer types should be fully 
compatible to cast between and so you can use the two types interchangeably.

    struct Sound {
      sound _;
    };
  
    var Sound = Cello(Sound);

    int main(int argc, char** argv) {
      sound* s = new(Sound);
      sound_play(s);
      return 0;
    }

    
## Stack Trace using MinGW <a name="stack-trace-using-mingw"></a>

If you're using MinGW on Windows you'll probably get stack traces that look 
something like this.

    !!
    !!      Uncaught ValueError
    !!
    !!               cast expected type Int, got type String
    !!
    !!      Stack Trace:
    !!
    !!              [0] ???
    !!              [1] ???
    !!              [2] ???
    !!              [3] ???
    !!              [4] ???
    !!              [5] ???
    !!              [6] ???
    !!              [7] ???
    !!              [8] BaseThreadInitThunk
    !!              [9] RtlUserThreadStart
    !!

This is because MinGW executables use the Dwarf debugging format while Cello 
expects debugging information on Windows to be in the standard `.pdb` format. 
You can generate a `.pdb` file from an executable with debugging information 
using a great little tool called [cv2pdb](https://github.com/rainers/cv2pdb).

Simply run this on your executable `cv2pdb test.exe`, it'll generate a 
corresponding `.pdb` file and you'll be ready to rock.

    !!
    !!      Uncaught ValueError
    !!
    !!               cast expected type Int, got type String
    !!
    !!      Stack Trace:
    !!
    !!              [0] src\Thread.c:708 Exception_Error
    !!              [1] src\Thread.c:830 exception_throw
    !!              [2] src\Type.c:46 cast
    !!              [3] src\Map.c:530 Map_Rem
    !!              [4] tests\data.c:924 test_map_get
    !!              [5] tests\ptest.c:247 pt_run
    !!              [6] tests\test.c:20 gc_main
    !!              [7] tests\test.c:9 main
    !!              [8] BaseThreadInitThunk
    !!              [9] RtlUserThreadStart
    !!

For more information you can see my 
[blog post](http://theorangeduck.com/page/printing-stack-trace-mingw) on the 
subject.
    
    
    
* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>