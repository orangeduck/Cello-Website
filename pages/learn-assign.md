  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__assign__

    var assign(var self, var obj);

Assign the object `obj` to the object `self`. The assigned object `self` is returned.

### Examples

__Usage__

    var x = new(Int, $I(10));
    var y = new(Int, $I(20));
    
    show(x); /* 10 */
    show(y); /* 20 */
    
    assign(x, y);
    
    show(x); /* 20 */
    show(y); /* 20 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Assign
__Assignment__

`Assign` is potentially the most important class in Cello. It is used throughout Cello to initialise objects using other objects. In C++ this is called the _copy constructor_ and it is used to assign the value of one object to another.

By default the `Assign` class uses the `Size` class to copy the memory from one object to another. But for more complex objects which maintain their own behaviours and state this may need to be overridden.

The most important thing about the `Assign` class is that it must work on the assumption that the target object may not have had it's constructor called and could be uninitialised with just zero'd memory. This is often the case when copying contents into containers.

### Definition

    struct Assign {
      void (*assign)(var, var);
    };
    

### Derivers

* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _Integer Sequence_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Floating Point Object_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
