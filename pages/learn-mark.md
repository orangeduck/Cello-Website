  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__mark__

    void mark(var self, var gc, void(*f)(var,void*));

Mark the object `self` with the Garbage Collector `gc` and the callback function `f`.

  </div>
  <div class="col-xs-6 col-md-6">

# Mark
__Markable by GC__

The `Mark` class can be overridden to customize the behaviour of the Cello Garbage Collector on encountering a given type. By default the allocated memory for a structure is scanned for pointers to other Cello objects, but if a type does its own memory allocation it may store pointers to Cello objects in other locations.

If this is the case the `Mark` class can be overridden and the callback function `f` must be called on all pointers which might be Cello objects which are managed by the class. Alternately the `mark` function can be called on any sub object to start a chain of recursive marking.

### Definition

    struct Mark {
      void (*mark)(var, var, void(*)(var,void*));
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tree](/learn/tree)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
