  <div class="row">
  <div class="col-xs-6 col-md-6">

    #include "Cello.h"

    int main(int argc, char** argv) {

      /* Stack objects are created using "$" */
      var i0 = $(Int, 5);
      var i2 = $(Int, 3);
      var i2 = $(Int, 4);

      /* Heap objects are created using "new" */
      var items = new(Array, Int, i0, i1, i2);
      
      /* Collections can be looped over */
      foreach (item in items) {
        print("Object %$ is of type %$\n",
          item, type_of(item));
      }
      
      /* Heap objects destructed via Garbage Collection */
      return 0;
    }

  </div>
  <div class="col-xs-6 col-md-6">

__Cello__ is a _library_ that brings higher level programming to C.

By acting as a _modern_, _powerful_ runtime system Cello makes many things easy 
that were previously impractical or awkward in C such as:

* __Generic Data Structures__
* __Polymorphic Functions__
* __Interfaces / Type Classes__
* __Constructors / Destructors__
* __Garbage Collection__
* __Exceptions__
* __Reflection__

And because Cello works seamlessly alongside standard C you get all the other 
benefits such as great performance, powerful tooling, and extensive 
libraries.

  </div>
  </div><hr/>
  <div class="row">
  <div class="col-xs-6 col-md-6">

    #include "Cello.h"

    int main(int argc, char** argv) {
      
      /* Shorthand $ can be used for basic types */
      var prices = new(Table, String, Int);
      set(prices, $S("Apple"),  $I(12)); 
      set(prices, $S("Banana"), $I( 6)); 
      set(prices, $S("Pear"),   $I(55)); 

      /* Tables also support iteration */
      foreach (key in prices) {
        var val = get(prices, key);
        print("Price of %$ is %$\n", key, val);
      }
      
      return 0;
    }
    
  </div>
  <div class="col-xs-6 col-md-6">
    
### Articles

Learning Resources.

* [Installation](/learn/installation)
* [Cello World](/learn/cello-world)
* [Quickstart](/learn/quickstart)
* [Common Queries / Pitfalls](/learn/pitfalls)

Articles about its creation and internal workings.

* [A Fat Pointer Library](/learn/a-fat-pointer-library)
* [Hacking C to its Limits](/learn/hacking-c-to-its-limits)
* [Cello vs C++ vs ObjC](/learn/cello-vs-cpp-vs-objc)
* [Benchmarking Cello](/learn/benchmarks)
* [Garbage Collection](/learn/garbage-collection)
    
  </div>
  </div><hr/>
  <div class="row">
  <div class="col-xs-6 col-md-6">
    

    #include "Cello.h"

    int main(int argc, char** argv) {
      
      /* First class function declaration */
      fun (print_safe, args) {
        
        /* Exceptions */
        try {
          println("%$", get(args, $I(0)));
        } catch (e in IOError) {
          println("IOError: %$", e);
        }

        return None;
      };
      
      /* Tuple is a simple stack based collection */
      var t = tuple($F(51.25), $I(21), $S("Hello"));
      
      /* Higher Order Functions */
      map(t, print_safe);
      
      return 0;
    }


  </div>
  <div class="col-md-6">
  

### F.A.Q

* __Why does this exist?__

I made Cello as a fun experiment to see what C looks like hacked to its limits. 
As well as being a powerful library and toolkit, it should be interesting to 
those who want to explore what is possible in C.

* __How does it work?__

I recommend reading 
[A Fat Pointer Library](/learn/fatpointer) and 
[Hacking C to its Limits](/learn/hacking) to get an overview of how Cello works.
You can also peek at the source code, which I'm told is fairly readable, or 
ask me any questions you like via e-mail.

* __Can it be used in Production?__

It might be better to try Cello out on a hobby project first. Cello does aim to 
be _production ready_, but because it is a hack it has its fair share of 
oddities and pitfalls, and if you are working in a team, or to a deadline, 
there is much better tooling, support and community for languages such as C++.

* __Is anyone using Cello?__

People have exerimented with it, but there is no high profile project I know of
that uses it. Cello is too big and scary a dependancy for new C projects if 
they want to be portable and easy to maintain. Even so there are some smaller 
projects growing out of it. Why not check out [Chords](/chords).


  </div>
  </div>

