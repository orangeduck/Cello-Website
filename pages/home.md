__Cello__ is a _GNU99_ C _library_ which brings higher level programming to C.

<blockquote>

<ul>
<li> <strong>Interfaces</strong> allow for structured design </li>
<li> <strong>Duck Typing</strong> allows for simpler functions </li>
<li> <strong>Exceptions</strong> control error handling </li>
<li> <strong>Constructors/Destructors</strong> aid memory management </li>
<li> <strong>Syntactic Sugar</strong> increases readability </li>
<li> <strong>C Library</strong> means excellent performance and integration </li>
</ul>

</blockquote>


    /* Example libCello Program */

    #include "Cello.h"

    int main(int argc, char** argv) {

      /* Stack objects are created using "$" */
      var int_item = $(Int, 5);
      var float_item = $(Real, 2.4);
      var string_item = $(String, "Hello");

      /* Heap objects are created using "new" */
      var items = new(List, 3, int_item, float_item, string_item);
      
      /* Collections can be looped over */
      foreach (item in items) {
        /* Types are also objects */
        var type = type_of(item);
        print("Object %$ has type %$\n", item, type);
      }
      
      /* Heap objects destroyed with "delete" */
      delete(items); 
    }
      
Quickstart
----------

For more examples please take a look at the quickstart documentation section:

* [Containers and Collections](/documentation/containers)
* [Type and Classes](/documentation/types)
* [Exceptions](/documentation/exceptions)
* [First Class Functions](/documentation/functions)
* [Memory Management](/documentation/memory)

Or some articles about the creation:

* [Hacking C to it's limits](/documentation/hacking)

Or a longer example:

    /* Another Example Cello Program */

    #include "Cello.h"

    int main(int argc, char** argv) {
      
      /* Tables require "Eq" and "Hash" on key type */
      var prices = new(Table, String, Int);
      put(prices, $(String, "Apple"),  $(Int, 12)); 
      put(prices, $(String, "Banana"), $(Int,  6)); 
      put(prices, $(String, "Pear"),   $(Int, 55)); 

      /* Tables also supports iteration */
      foreach (key in prices) {
        var price = get(prices, key);
        print("Price of %$ is %$\n", key, price);
      }
      
      /* "with" automatically closes file at end of scope. */
      with (file in open($(File, NULL), "prices.bin", "wb"))) {
      
        /* First class function object */
        lambda(write_pair, args) {
          
          /* Run time type-checking with "cast" */
          var key = cast(at(args, 0), String);
          var val = cast(get(prices, key), Int);
          
          print_to(file, 0, "%$ :: %$\n", key, val);
          
          return None;
        };
        
        /* Higher order functions */
        map(prices, write_pair);
      }
      
      delete(prices);
    }

Inspiration
-----------

The high level stucture of Cello projects is inspired by _Haskell_, while the syntax and semantics are inspired by _Python_ and _Obj-C_. Cello isn't about _Object Orientation_ in C, but I hope that with Cello I've turned C into something of a _dynamic_ and _powerful_ functional language which it may have once been.

Although the syntax is pleasant, Cello _isn't_ a library for beginners. It is for C power users, as manual memory management doesn't play nicely with many higher-order concepts. Most of all Cello is just a fun experiment to see what C would look like when Hacked to it's limits.

Contributions
-------------

Cello is licensed under BSD3.

Contributions are welcomed via [github](https://github.com/orangeduck/libCello).

For queries please visit the IRC channel `#libcello` on Freenode. 

Or send them to `contact@theorangeduck.com`.

