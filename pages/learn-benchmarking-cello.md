  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Benchmarking

Unfortunately there is no easy answer to _How Fast is Cello?_ Because Cello is 
a superset of standard C, it is very difficult to benchmark in an objective 
way. But before we go into the numbers here are some broad statements about 
Cello's performance:

* __Cello incurs no overhead if you don't use it.__

Using standard C for tight loops and numerical computations is going to give 
you very fast performance. This is both natural and easy due to how simple the 
Cello/C interop is. Similarly, just using Cello as a high level wrapper for the 
main objects or components in your program is going to incur practically no 
performance penalty over standard C.

* __Generic Functions have some fixed overhead cost.__

Each time you call a generic function such as `new` or `get` there is some 
small overhead associated with it. The overhead associated with a function call 
is roughly 10x that of a standard C function call - which is actually not bad 
if you consider C++ virtual functions can be 6x slower than standard C
function calls - but it still isn't ideal. If you are calling Cello functions 
in a tight loop this overhead can really add up and additionally these function 
calls can't be inlined by the compiler, so in this case consider reverting to 
standard C.

* __Cello's data structures are runtime polymorphic.__

Because Cello's data structures are runtime polymorphic rather than compile 
time polymorphic, in general they can't be made to be as fast as C++ data 
structures, data structures from a C macro library such as 
[klib](https://github.com/attractivechaos/klib), or even some JIT scripting 
language's data structures. Saying that they should still be competative with 
most programming language's data structures.

# Figures

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
