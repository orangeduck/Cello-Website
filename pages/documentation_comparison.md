Cello vs C++ vs ObjC
--------------------

A common question that gets asked about this project is "What are the advantages of using _Cello_ over _C++_ or _Objective C_?"

The short answer is _personal preference_. As far as features are concerned all these projects are fairly similar. But they also all differ by a large amount in other areas.

The first Major difference between Cello C++ Objective C is that Cello is _just a C library_. The others are _whole new languages_. 

* When using __Cello__ you are programming in C. It requires a __C compiler__ (such as GCC or Clang which support the GNU99 standard). 
* When using __C++__ you are programming C++. It requires a __C++ compiler__.
* When using __ObjC__ you are programming Objective C. It requires a __ObjC compiler__.

Many people prefer programming in C to C++ or ObjC and many people prefer it the opposite way around. This preference is something that may influence your decision before thinking about anything else. You may only have access to one compiler type or are required to use one language.


### Cello vs C++

The major difference between Cello and C++ is in the structure of the _standard library_. The standard C++ library is well known for being large, complex and spanning paradigms. It supports many many things out of the box using different methods and techniques. Much of it is Object Oriented (such as IO), while other parts are Template based (such as STL). The C++ standard library is like a huge messy toolbox.

The Cello standard library has been desgined from scratch. It is much smaller and very modern, with consistent ideas and design. There are no OO sections and it is designed using Composition rather than Inheritence. It much closer resembles the design of the Go or Haskell standard libraries.


__Cello Pros__

* Consistent & Clean Syntax
* Consistent & Clean Standard Library
* Powerful Runtime
* Real Duck Typing
* Easier to Learn


__Cello Cons__

* No Support for Smart Pointers
* No Real Rich Stack Types
* Much Smaller Standard Library
* No Compile Time Type Checking
* Fewer Developers, Less Support
* No Templates


### Cello vs ObjC

I don't have nearly as much experience in ObjC but I can tell you that it is fairly similar to Cello when it comes to internals. The major difference is in the syntax and type checking ability.

Objective C, like Cello, has a runtime system built over the top of the normal workings. It also does dynamic function calling via a message passing type interface. The ObjC type system is both runtime and compile time giving it the advantage of being able to do compile time type checking to ensure objects recieve valid messages. This adds valuable type checking but can sometimes make some task laborious. I find Objective C often requires some boilerplate and that the Apple libraries are full of Object Oriented style design patterns. Objective C's syntax is generally regarded ugly and complicated but overall it is an interesting and powerful language.

If you prefer OO style design, with patterns and boxes, and like to have types checked at compile time, then Objective C definitely offers you more. But if you primarily like the dynamic nature of Objective C but wished it was more flexible then Cello may appeal.


__Cello Pros__

* Nicer Syntax
* Modern Standard Library
* Composition based design
* Exceptions instead of Error Codes
* Functions instead of Delegates


__Cello Cons__

* No Compile Time Type Checking
* No Apple / OS X Libraries
* More difficult memory management

[Back](/documentation)
