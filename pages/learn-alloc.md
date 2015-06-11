  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__$__

    #define $(T, ...)
    #define $I(X)
    #define $F(X)
    #define $S(X)
    #define $R(X)
    #define $B(X)

Allocate memory for the given type `T` on the stack and copy in the given arguments `...` as struct members. Shorthand constructors exist for native types:

* `$I -> Int` `$F -> Float` `$S -> String`
* `$R -> Ref` `$B -> Box`



__alloc__

    #define alloc_stack(T)
    var alloc(var type);
    var alloc_raw(var type);
    var alloc_root(var type);

Allocate memory for a given `type`. To avoid the Garbage Collector completely use `alloc_raw`, to register the allocation as a root use `alloc_root`. In the case of raw or root allocations the corresponding `dealloc` function should be used when done. Memory allocated with `alloc_stack` is not managed by the Garbage Collector.

__dealloc__

    void dealloc(var self);
    void dealloc_raw(var self);
    void dealloc_root(var self);

Deallocate memory for object `self` manually. If registered with the Garbage Collector then entry will be removed. If the `raw` variation is used memory will be deallocated without going via the Garbage Collector.

### Examples

__Usage__

    /* Allocation deallocated by Garbage Collector */
    var x = alloc(Int);
    construct(x, $I(10));
    

__Avoid Garbage Collection__

    /* Allocation must be manually deallocated */
    var x = alloc_raw(Int);
    construct(x, $I(10));
    destruct(x);
    dealloc_raw(x);
    



  </div>
  <div class="col-xs-6 col-md-6">

# Alloc
__Memory Allocation__

The `Alloc` class can be used to override how memory is allocated for a given data type. By default memory is allocated using `calloc` along with the `Size` class to determine the amount of memory to allocate.

A custom allocator should be careful to also initialise the header for the allocated memory using the function `header_init`. Cello objects without a header wont be recognised as such as so will throw errors when used with Cello functions.

Allocated memory is automatically registered with the garbage collector unless the functions `alloc_raw` and `dealloc_raw` are used.

### Definition

    struct Alloc {
      var (*alloc)(void);
      void (*dealloc)(var);
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
