  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Benchmarking

Unfortunately there is no easy answer to _How Fast is Cello?_ The fact is, 
because Cello is a superset of standard C, it is very difficult to benchmark in 
an objective way. But before we go into the numbers here are some broad 
statements about Cello's performance:

Cello incurs no overhead if you don't use it. Using standard C for tight 
loops and numerical computations is going to give you very fast performance.
This is both natural and easy due to how simple the Cello/C interop is.

Similarly, just using Cello as a high level wrapper for the main objects or 
components in your program is going to incur practiclly no performance penalty
over standard C.

Each time you use a generic function such as `new` or `get` there is some 
small overhead associated with it. For one-off operations this is tiny, but it 
can add up to be quite significant if you call these functions hundreds of 
thousands of times in a tight loop.

Because Cello's data structures are runtime polymorphic rather than compile 
time polymorphic, in general they can't be made to be as fast as C++ data 
structures, data structures from a C macro library such as 
[klib](https://github.com/attractivechaos/klib), or even some scripting 
language's data structures.




  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
