  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Hacking C to its limits

* How to declare types statically
* Optimisations to type lookup
* Foreach
* With
* Exceptions
* Closures
* True False
* Syntax -> Scripting Language

## Overview

I started libCello (then called C+) as a fun experiment to play around with the various implementations of _Object Orientation in C_. Most had some fun features and cool tricks but tended to break down around about the time of inheritence. Assertions began to pile up, syntax became horrible, or the programmer had to do too many things manually. Several based around message passing relied too heavily on error-prone strings.

One thing I did notice is that essentially they begin to resemble the C backend to scripting languages such as Python.

I wondered if by making different or simplified assumptions it would allow for nicer syntax, cleaner semantics and fewer manual steps for the programmer. I thought I might be able to create scripting language like semantics, but with the performance and frontend of C.

libCello consists of some global changes and a number of cute hacks. The global changes are not too original, but combined with the cute hacks create a library that is fairly comfortable to use.

I've tried to make this article short so have skipped somewhat on the nitty gritty details. Anyone interested is encouraged to send me an e-mail or take a peek at the source code!


### Types

To change a language behaviour one must either change the compiler or the runtime. A language like C essentially has no runtime system. It generates object code that looks like any other. But we can add one ourselves. We only need to add one powerful construct to do almost anything we want. This is the familiar _type_.

For example if we wish to add `new` and `delete` to a language, our system (the runtime), must know the size of the memory to allocate. This is just _metadata_ also known as _type_ information. We must store this somewhere while the program is running. It could be in a separate table, but is often useful to tie to the object we wish to manipulate itself.

For example we can make all _rich_ objects contain some pointer to their _type_ or _metadata_ at the beginning of the struct.

    typedef struct {
      type_t* meta_data;
      int other_data;
    } some_struct;

When we wish to manipulating these objects we can then follow the pointer to the metadata and extract the information we need. If this entry is always the first entry in the struct, whatever struct we encounter, we always know where to find it. It is a simple system, but unfortunately introduces our first and somewhat unavoidable assumption.

All _rich_ objects must start with this entry - but adding it is at the discretion of the programmer, __who may forget__.

As we know, C is famous for having no hidden costs. You pay only for what you use. This is why it is unavoidable. C allows you no way to insert this entry into a programmer's structs unknowingly. Doing so would be dishonest, and C hates liars.

What about having the type information in a separate table which we index using the struct memory location? This does work well, but also means any structure creation must go via some function we define (so we can add the type information to our table). In many cases this is fine, but sometimes it is more useful to have usable data come from outside of this function, for example created on the stack (see _The Dollar_).

Anyway, if we swallow this cost, we can add many new behaviours to the language that seem like magic to the outside world. Onto the next stage, designing our _metadata_ object!


### Metadata

There are many ways to design a metadata object, but we must be careful. Already we have one constraint. Our metadata should be a _rich_ object. Meaning its first entry must be a pointer to _its_ type. But what is the type of a Type object? Well its type is just _Type_, who's type is _Type_ again.

Confused? Another problem is in constant initializers. In C many data types can't be used to initialize a metadata structure at compile time. But no one wants to have to declare all their types at runtime! This is why it must be carefully designed. The entries must be constant literals. The first entry must be its type. Yet it must express everything we need about an object.

In libCello I use a NULL terminated list of pairs. Each pair consists of a pointer to something and a string identifier.

    var MyType = {
      { Type,       "Type" },
      { MyTypeName, "Name" },
      { MyTypeNew,  "New"  },
      { MyTypeOrd,  "Ord"  },
      { NULL,       NULL   }
    };

More specifically each entry is a pointer to a Typeclass (or some other information such as a name), but more on that later.

The constant initializer problem still crops up here and there, but workarounds can be had. Onto bigger and better - to make practical use of this!


### Generic Functions

If, for example, we wished to add functions such as `print` or `hash` to the language we would wish for them to be able to work on any type that they make sense for. That they should be _generic_. This poses a problem in C - the type checker wont allow for this kind of behaviour. It has no idea what things make sense on what types. However we _can_ declare functions to take `void*`. This ignores type checking and makes the function work for _all_ pointer types.

So comes our second major assumption. We forgo the compiler's type checking to allow for generic functions. We _can_ still do runtime type checking using our newly declared runtime Types, accessing our rich objects' metadata, but it is a painful compromise.

There is no real solution to this. Still. Dynamic languages are trendy. Just rename `void*` to `var` and we have something that resembles modern scripting languages. If runtime type checking is good enough for them it is good enough for us.

### Typeclasses

To know if a certain operation (such as ordering) makes sense on a certain type we need to get the programmer to tell us. This is where typeclasses come in. Also known as interfaces; these let the programmer give a specification of the behaviour of a Type under a certain operation. Perhaps suprisingly they can be used to express almost all higher level concepts.

In libCello a typeclass is just a struct, usually containing a bunch of function pointers. Types can then make instances of these, and point to them in their metadata entries.
  
  
    typedef struct {
      var (*iter_start)(var);
      var (*iter_end)(var);
      var (*iter_next)(var, var);
    } Iter;

    static Iter ListIter = { List_Iter_Start, List_Iter_End, List_Iter_Next };


Early on I decided typeclasses were going to be the core of what is inside a Type. This simplified things exceptionally compared to many _message passing_ or _Object Oriented_ systems in C which have elaborate metadata structures.


### Is that all?

Really this ends the global ideas behind libCello and many similar projects. The fun comes from the rich and powerful systems we can build into our runtime system.

### What about memory management?

Yes there will always be one skeleton in the closest. Manual memory management.

I say we can build more or less anything into our runtime system but Garbage collection is just one step too far. The dynamic and complex systems that run garbage collectors just introduce too many hidden operations into a language. Like adding the type at the beginning of a struct, C does its best to disallow any hidden costs. And GC is all or nothing. Even the tiniest memory leak is unacceptable.

Even more troubling is that manual memory management simply doesn't work well with many higher level constructs.

But nevermind - we can still allow for some simple things such as pools and references. The fact is manual memory management is the law in C. It can't be hacked out.


## Tricks

### The Dollar

`$` or clef as I like to think of it, is what allows programmers to declare simple _rich_ objects on the stack. This is super important in reducing the mental overhead of using libCello, as cleaning up hundreds of heap allocated objects manually quickly gets out of hand.

The macro is fairly simple and uses a struct initialization trick C programmers have used for decades. It just wraps a literal struct declaration in a single element array - to get a pointer to it.

    #define $(T, ...) (T##Data[]){{T, __VA_ARGS__}}

It doesn't call destructors/constructors, and we have to use the fact that types are named like `IntData` to get the struct name but it is more than functional for simple boxed objects.

When I first picked `$` I was just looking for a symbol that tended to mean variable. Only later when I tried with `@` did I realize that `$` is technically an invalid preprocessor token. All preprocessor tokens must be valid identifiers obeying the same rules as variables. So why the hell was GCC letting it pass?

Turns out GCC treats `$` as a letter for compatibility with some systems, such as VMS, where `$` is commonly used in system-defined function and object names. While not the most sensible decision for portability reasons it is too great a hack to take out!


### Foreach

With typeclasses `foreach` was fairly trivial to implement. We make an `Iter` typeclass which has functions `iter_start`, `iter_end` and `iter_next` and then any object which can implement those supports iteration via foreach:

    #define foreach(x, xs) \
      for(var x = iter_start(xs); x != iter_end(xs); x = iter_next(xs))

### With

The idea behind `with` is almost identical to `foreach`. We have `enter_with` and `exit_with` functions implemented by the `With` typeclass then use a single iteration of a `for` loop to use them.

    #define with(x, y) \
      for(var x = enter_for(y); x isnt Undefined; x = exit_for(x))

The `enter_for` function calls `enter_with` and returns `y`, while the `exit_for` function calls `exit_with` and returns `Undefined`. Using a `for` loop for declaring variables scoped to a single block is a pretty nice hack that lets you create a whole bunch of blocks with custom behaviours.


### Lambda

GNU99 C has a great feature that lets you define functions inside functions. These are true lambdas that obey the expected scoping rules and let you reference variables used in that function's stack frame. Obviously without reference counting or other management calling a lambda like that can cause a segfault if the stack frame has been taken apart - but really they are fully functional.

If we assume the same type for all lambda statements, with arguments rolled into a list, we can create macro that declares a function inside the current function and wraps it in a rich object.

    #define lambda(name, args) \
      auto var __LambdaCello_##name(var); \
      var name = $(Function, __LambdaCello_##name); \
      var __LambdaCello_##name(var args)

      
GNU99 C also allows for use of the `auto` keyword to do forward declaration. Again not a win for portability but a powerful addition to the language.

While this hack is limited to `gcc` we can make use of [clang blocks](http://clang.llvm.org/docs/BlockLanguageSpec.html) when using the clang compiler on OSX. The functionality is the same, only requiring a small change in syntax.


### Exceptions

Anyone who has looked will know there are a rather large number of implementations of Exceptions in C. They have many different flavours and ways of working based around `setjmp` and `longjmp`. One of my requirements was no `try_end` macro to put after a try block. I thought it would be too easy for the programmer to forget to add. Secondly I wanted some kind of support for nested Exceptions and the ability to catch only certain types.

In the end I forumulated something that worked.

    #define try \
      Exception_Inc(); \ 
      Exception_Deactivate(); \
      if (!setjmp(Exception_Buffer()))

    #define catch(x, ...) \
      else { Exception_Activate(); } \
      Exception_Dec(); \
      for (var x = Exception_Catch(var_list_new(__VA_ARGS__)); x != Undefined; x = Undefined)

    #define throw(e, fmt, ...) \ 
      Exception_Throw(e, fmt, __FILE__, __func__, __LINE__, var_list_new(__VA_ARGS__))


Where `Exception_Throw` essentially just calls `longjmp` on the topmost jump location and `Exception_Catch` deals with the catching logic or returns `Undefined` when an exception is not active.


### True/False

One annoying thing about the rich object system is that it is not easy to make a _rich_ version of True or False. Any rich object must be a pointer to some memory so will always be evaluated as true.

Therefore we can hardcode True and False into our system. When we look for the _metadata_ information assigned to a structure we can test for pointers to address 0 and address 1 and if so return the type information for a `Bool` type.

In this way we've made the native `true` and `false` values _rich_ such that they can be used in the rest of our system without conflict.

    var type_of(var self) {
      
      /* Test against Builtins */
      if (self is True) return Bool;
      if (self is False) return Bool;

      /* Use first entry in struct */
      return ((ObjectData*)self)->type;

    }


  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
