  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Cello vs C++ vs ObjC

A common question that gets asked about this project is "What are the 
advantages of using Cello over C++ or Objective C?". The short answer is 
_personal preference_. The features of each are fairly similar, but they all do 
differ in other areas.

The first Major difference between Cello, C++, and Objective C is that Cello is 
just a C library. The others are whole new languages. 

* When using __Cello__ you are programming in C. It requires a __C compiler__. 
* When using __C++__ you are programming C++. It requires a __C++ compiler__.
* When using __ObjC__ you are programming Objective C. It requires a 
  __ObjC compiler__.

Many people prefer programming in C to C++ or ObjC and many people prefer the 
opposite. This preference is something that may influence your decision before 
thinking about anything else. You may only have access to one compiler type or 
are required to use one language.


### Cello vs C++

There are two major difference between Cello and C++. The first is that Cello 
must rely on void pointers and runtime polymorphism to achieve its high 
level features, and the second is in the design and structure of the standard 
library of each.

The standard C++ library is well known for being large, complex and spanning 
paradigms. It supports many many things out of the box using different methods 
and techniques. Much of it is Object Oriented (such as IO), while other parts 
are Template based (such as STL). The C++ standard library is like a huge messy 
toolbox.

The Cello standard library has been desgined from scratch. It is much smaller 
and modern, with consistent ideas and design. It is designed using Composition 
rather than Inheritence. It much closer resembles the design of the Go or 
Haskell standard libraries.

Cello also comes with a basic form of Garbage Collection.

__Cello Cons__

* No Support for Smart Pointers
* No Support for Rich Stack Types
* Much Smaller Standard Library
* More Relaxed Type System
* Fewer Developers, Less Support
* No Templates

__Cello Pros__

* Consistent & Clean Syntax
* Consistent & Clean Standard Library
* Powerful Runtime with Reflection
* More Simple Extension to C


### Cello vs ObjC

I don't have nearly as much experience in ObjC but I can tell you that it is 
fairly similar to Cello when it comes to internals. The major difference is in 
the syntax and type checking ability.

Objective C, like Cello, has a runtime system built over the top of the normal 
workings. It also does dynamic function calling via a message passing type 
interface. The ObjC type system is both runtime and compile time giving it the 
advantage of being able to do compile time type checking to ensure objects 
recieve valid messages. This adds valuable type checking but can sometimes make 
some task laborious. I find Objective C often requires lots of boilerplate and 
that the Apple libraries are full of Object Oriented style design patterns. 
Objective C's syntax is generally regarded ugly and complicated but overall it 
is an interesting and powerful language which I like a lot.

If you prefer OO style design, with patterns and boxes, and like to have types 
checked at compile time, then Objective C definitely offers you more. But if 
you primarily like the dynamic nature of Objective C but wished it was more 
flexible then Cello may appeal.

__Cello Cons__

* No Compile Time Type Checking
* No Apple / OS X Libraries

__Cello Pros__

* Nicer Syntax
* Simple, Modern Standard Library
* Composition based design
* Exceptions instead of Error Codes

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
