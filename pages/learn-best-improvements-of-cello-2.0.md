  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Best Improvements of Cello 2.0

## Fat Pointers

The complete internal workings of Cello have been rewritten and now it uses the 
concept of [fat pointers](/learn/a-fat-pointer-library) to ensure Cello 
Pointers are fully compatible with standard C pointers. This is a massive win 
for interoperation with standard C because it means you can use Cello objects 
with standard C functions and types. No longer are you forced to use typeless 
pointers when you don't want to and Cello really does work _on top_ of normal 
C, not orthogonal to it.

## Type Definitions

The overhead of declaring a structure Cello compatible has been reduced from 20 
or 30 lines of code to just one. Not only this but there are a huge number of 
operations Cello has defaults for now. In one line of code you can suddenly 
make it so that an object is usable across the whole Cello infrastructure 
including garbage collection, data structures, IO, and much more. Combined with 
C compatibility now you there is really nothing to lose by making your C 
structures Cello compatible. One line and you're ready to go.


## Performance

It is fair to say that Cello 1.0 was insanely slow. It had some pretty terrible 
data structures and the overhead of calling Cello functions inside a tight loop 
was massive.

In Cello 2.0 all the data structures have been updated to be modern, fast, and 
efficient. Cello has also been heavily optimised and 
[benchmarked](/learn/benchmarks) to ensure it doesn't have too much of a 
performance penalty. Currently it sits between C and Java on most operations. 
The better interop with C has also helped in this regard, making it easy to 
drop down to C for numerical calculations and other performance intensive 
areas. And if you still need that extra performance remember that all C 
programs are also valid Cello programs!


## Portability

Cello 2.0 only relies on a couple of fairly standard C language extensions. 
Namely the 
[dollars in identifiers](https://gcc.gnu.org/onlinedocs/gcc/Dollar-Signs.html) 
extension and the
[gnu variadic macros](https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html) 
extension.

Unfortunately this does mean that closures were been dropped from the features 
list since 1.0, but it seems like a sensible omission as now Cello can be 
compiled easily with all of the major compilers including `gcc`, `clang`, 
`cl.exe`, and `tcc` (on the development branch).

Several of the defines Cello 1.0 made such as `local` and `global` have also 
been dropped. While these are certainly more readable than `static` and 
`extern` the potential for shadowing issues, and the fact that I wanted 
Cello to play nicely with C in this release, outweighed the benefits.

In general programming in Cello feels a lot less like a different language and 
more like an augmented C.


## Debugging

Having a runtime layer isn't just good for high level programming - it also 
provides an easy way to insert all of the runtime checks that are missing from 
standard C programming. These are everywhere in Cello. It performs out of 
bounds checks, out of memory checks, IO checks, and much more. If there is a 
runtime error an exception will be thrown with a nice error message and a 
stack trace.

Of course once you're program is running correctly all of these checks can be 
disabled using `-DCELLO_NDEBUG` to get C style performance.

All of the documentation is now built into Cello and can be accessed via 
the `help` function. Even the website documentation is generated using a simple 
C script.

## Documentation

Cello Documentation is now built into the language. In fact - the website 
documentation is just generated using a simple Cello script. Having the 
documentation available from the library is nice (you can just call `help` on 
some type), but more importantly because the code and documentation is in the 
same place there is less chance of it getting out of sync - all pull requests 
go to the main repo.

## Iterables

The new version of Cello has python3 style iterables. Although the syntax isn't 
as nice as python this does mean you can do neat things like use slices, 
filters, and maps on any iterable type. Special care has also been taken to 
ensure these types can be constructed on the stack so the overhead should be as 
small as possible.

## Garbage Collection

One of the things I really wanted to try to add to Cello was optional Garbage 
Collection. Previously I had sworn that it would be impossible, but I started 
to get a few inklings about how it might be done (in some form or other) and 
after following on from those I managed to find a compromise that adds a kind 
of Garbage Collection for Cello objects and is both simple, and portable. 
Having [Garbage Collection](/learn/garbage-collection) is a big win for 
usability. And the fact that the Garbage Collection is optional means it can 
be turned off for performance critical sections or ignored where it isn't 
useful.

More generally it means you can choose to program more like you are using a 
scripting language than a systems language with the worry of memory leaks.



  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
