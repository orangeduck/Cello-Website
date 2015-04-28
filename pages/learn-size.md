  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__size__

    size_t size(var type);

Returns the associated size of a given `type` in bytes.

### Examples

__Usage__

    show($I(size(Int)));
    show($I(size(Float)));
    show($I(size(Array)));
    



  </div>
  <div class="col-xs-6 col-md-6">

# Size
__Object has some Size__

The `Size` class is a very important class in Cello because it gives the size in bytes you can expect an object of a given type to be. This is used by many methods to allocate, assign, or compare various objects.

By default this size is automatically found and recorded by the `Cello` macro, but if the type does it's own allocation, or the size cannot be found naturally then it may be necessary to override this method.

### Definition

    struct Size {
      size_t (*size)(void);
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
