  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__copy__

    var copy(var self);

Make a copy of the object `self`.

### Examples

__Usage__

    var x = new(String, $S("Hello"));
    var y = copy(x);
    show(x); /* Hello */
    show(y); /* Hello */
    show($I(eq(x, y))); /* 1 */
    show($I(x is y)); /* 0 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Copy
__Copyable__

The `Copy` class can be used to override the behaviour of an object when a copy is made of it. By default the `Copy` class allocates a new empty object of the same type and uses the `Assign` class to set the contents. The copy is then registered with the Garbage Collector as if it had been constructed with `new`. This means when using manual memory management a copy must be deleted manually.

If the `copy` class is overridden then the implementer may manually have to register the object with the Garbage Collector if they wish for it to be tracked.

By convention `copy` follows the semantics of `Assign`, which typically means a _deep copy_ should be made, and that an object will create a copy of all of the sub-objects it references or contains - although this could vary depending on the type's overridden behaviours.

### Definition

    struct Copy {
      var (*copy)(var);
    };
    

### Derivers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Filter](/learn/filter)</span> | &nbsp; &nbsp;   _Filtered Iterable_
* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Floating Point Object_
* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Apply Function to Iterable_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _Integer Sequence_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tree](/learn/tree)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_
* <span class="docitem">[Zip](/learn/zip)</span> | &nbsp; &nbsp;   _Multiple Iterator_
### Implementers

* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
