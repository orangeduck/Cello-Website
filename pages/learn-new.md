  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__new__

    #define new(T, ...)
    #define new_raw(T, ...)
    #define new_root(T, ...)
    var new_with(var type, var args);
    var new_raw_with(var type, var args);
    var new_root_with(var type, var args);

Construct a new object of a given `type`. Use `new_raw` to avoid the Garbage Collector completely, and `new_root` to register the allocation as a Garbage Collection root. In the case of raw and root allocations they must be destructed with the corresponding deletion functions.

__del__

    void del(var self);
    void del_raw(var self);
    void del_root(var self);

Destruct the object `self` manually. If registered with the Garbage Collector then entry will be removed. If `del_raw` is used thenthe destruction will be done without going via the Garbage Collector.

__construct__

    #define construct(self, ...)
    var construct_with(var self, var args);

Call the constructor on object `self` which has already been allocated.

__destruct__

    var destruct(var self);

Call the destructor on object `self` without deallocating the memory for it.

### Examples

__Usage__

    var x = new(Int, $I(1));
    show(x); /* 1 */
    show(type_of(x)); /* Int */
    
    var y = alloc(Float);
    construct(y, $F(1.0));
    show(y); /* 1.0 */
    destruct(y);
    



  </div>
  <div class="col-xs-6 col-md-6">

# New
__Construction and Destruction__

The `New` class allows the user to define constructors and destructors for a type, accessible via `new` and `del`. Objects allocated with `new` are allocated on the heap and also registered with the Garbage Collector this means technically it isn't required to call `del` on them as they will be cleaned up at a later date.

The `new_root` function can be called to register a variable with the Garbage Collector but to indicate that it will be manually destructed with `del_root` by the user. This should be used for variables that wont be reachable by the Garbage Collector such as those in the data segment or only accessible via vanilla C structures.

The `new_raw` and `del_raw` functions can be called to construct and destruct objects without going via the Garbage Collector.

It is also possible to simply call the `construct` and `destruct` functions if you wish to construct an already allocated object.

Constructors should assume that memory is zero'd for an object but nothing else.

### Definition

    struct New {
      void (*construct_with)(var, var);
      void (*destruct)(var);
    };
    

### Derivers

* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Floating Point Object_
* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[Exception](/learn/exception)</span> | &nbsp; &nbsp;   _Exception Object_
* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Filter](/learn/filter)</span> | &nbsp; &nbsp;   _Filtered Iterable_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Apply Function to Iterable_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _Integer Sequence_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tree](/learn/tree)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_
* <span class="docitem">[Zip](/learn/zip)</span> | &nbsp; &nbsp;   _Multiple Iterator_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
