  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Benchmarks

Unfortunately there is no easy answer to _How Fast is Cello?_ Cello is 
a superset of standard C, which makes it very difficult to benchmark in an 
objective way. If you really want a single answer I can tell you that Cello is 
_somewhere between C and Java_, but before we go into the 
numbers, here are some broad statements about Cello's performance:

* __Cello works well in conjunction with standard C.__

Using standard C for tight loops and numerical computations is going to give 
you very fast performance. This is both natural and easy due to how simple the 
Cello/C interop is. Similarly, just using Cello as a high level wrapper for the 
main objects or components in your program is going to incur practically no 
performance penalty over standard C at all. It is also worth remembering that 
all of the benchmarked C programs are still valid Cello programs.

* __Generic Functions have some fixed overhead.__

Each time you call a Cello function such as `new` or `get` there is some 
small overhead associated with it. The overhead associated with a Cello 
function call is roughly 5-10 times that of a standard C function call - which 
may sound bad but is actually pretty good if you consider
[C++ virtual functions can be 2-7 times slower than standard C function calls](http://eli.thegreenplace.net/2013/12/05/the-cost-of-dynamic-virtual-calls-vs-static-crtp-dispatch-in-c).
The main issue, as with virtual function calls, is that Cello function calls 
cannot be inlined by the compiler and so when calling Cello functions in a 
tight loop this overhead can add up.

* __Cello's data structures are runtime polymorphic.__

Because Cello's data structures are runtime polymorphic rather than compile 
time polymorphic, in general they will never be as fast as C++ `stl` 
structures, data structures from a C macro library such as 
[klib](https://github.com/attractivechaos/klib), or even some unityped 
language's data structures. Even so, their performance is still pretty decent.


  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>

  <div class="row">
  <div class="col-xs-6 col-md-6">
  
<p style="text-align:center;">
  <img src="/static/img/benchmark_sudoku.png"/>
</p>

  </div>
  <div class="col-xs-6 col-md-6">

### Sudoku

In this benchmark Cello is used as a simple wrapper around the main objects 
used in the benchmarking program I.E the sudoku grid. Because all the heavy 
lifting is done in C the use of Cello incurs essentially no overhead and 
performance is the same as in C.
  
  </div>
  </div><hr/>
  <div class="row">
  <div class="col-xs-6 col-md-6">
  
<p style="text-align:center;">
  <img src="/static/img/benchmark_matrix.png"/>
</p>
  
  </div>
  <div class="col-xs-6 col-md-6">
  
### Matrix Multiplication
  
Similarly to the Sudoku benchmark, Cello is only used here as a basic wrapper 
around the main objects such as the matrices. The actual multiplication is done 
in normal C and so is very fast. Scripting languages like Ruby and Python 
perform particularly badly here due to their slowness with arithmetic.
  
  </div>
  </div><hr/>
  <div class="row">
  <div class="col-xs-6 col-md-6">
  
<p style="text-align:center;">
  <img src="/static/img/benchmark_nbodies.png"/>
</p>
  
  </div>
  <div class="col-xs-6 col-md-6">

### N-Body Simulation
  
This benchmark is written in _idomatic_ Cello. For example 
`foreach(b in bodies)` is used instead of 
`for(int i = 0; i < num_bodies; i++)` and Cello code is used where possible 
without concern for performance. In this case because using Cello functions 
blocks the compiler from unrolling loops and inlining functions it is 
somewhat slower than standard C. This benchmark shows the overhead of using 
_idomatic_ Cello even for performance critical sections of the code.
  
  </div>
  </div><hr/>
  <div class="row">
  <div class="col-xs-6 col-md-6">

<p style="text-align:center;">
  <img src="/static/img/benchmark_dictionary.png"/>
</p>
  
  </div>
  <div class="col-xs-6 col-md-6">

### Dictionary

This benchmark shows the use of the `Table` structure in Cello as compared to
other language's hashtable implementations. In C the `klib` library is used and 
in C++ `std::unordered_map` is used. Even unityped scripting languages tend to 
use optimised C implementations of hashtables and so everyone performs fairly 
evenly. Cello is slightly slower than you might expect due to using runtime 
polymorphism.

  </div>
  </div><hr/>
  <div class="row">
  <div class="col-xs-6 col-md-6">

<p style="text-align:center;">
  <img src="/static/img/benchmark_map.png"/>
</p>
  
  </div>
  <div class="col-xs-6 col-md-6">
  
### Map

This benchmark shows the use of the `Map` structure in Cello as compared to
other language's balance binary tree implementations (typically red-black 
trees). In C the `klib` library is used and in C++ `std::map` is used. Python 
is particularly slow in this benchmark because a pure-python implementation is 
used. Otherwise Cello achieves performance similar to Java or C 
implementations wrapped for scripting language such as the one used for Ruby.

  </div>
  </div><hr/>
  <div class="row">
  <div class="col-xs-6 col-md-6">

<p style="text-align:center;">
  <img src="/static/img/benchmark_array.png"/>
</p>
  
  </div>
  <div class="col-xs-6 col-md-6">
  
### Array

This benchmark shows the use of the `Array` structure in Cello as compared to
other language's array. In C++ `std::vector` is used. Cello's array 
implementation here is fairly slow due to being polymorphic and the overhead 
of storing type meta-data for each entry.

Lua performs very poorly because it's array type is implemented as a hash-table 
so many operations are much slower on it.

  </div>
  </div>

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
