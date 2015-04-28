  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__cast__

    var cast(var self, var type);

Ensures the object `self` is of the given `type` and returns it if it is.

### Examples

__Usage__

    var x = $I(100);
    struct Int* y = cast(x, Int);
    show(y);
    



  </div>
  <div class="col-xs-6 col-md-6">

# Cast
__Runtime type checking__

The `Cast` class provides a rudimentary run-time type checking. By default it simply checks that the passed in object is of a given type but it can be overridden by types which have to do more complex checking to ensure the types are correct.

### Definition

    struct Cast {
      var (*cast)(var, var);
    };
    

### Derivers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Float Point Object_
* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _A Sequence of Numbers_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Stack Based Collection_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_
### Implementers


* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
