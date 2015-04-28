  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__gt__

    bool gt(var self, var obj);

Returns true if the object `self` is greater than the object `obj`.

__lt__

    bool lt(var self, var obj);

Returns false if the object `self` is less than the object `obj`.

__ge__

    bool ge(var self, var obj);

Returns false if the object `self` is greater than or equal to the object `obj`.

__le__

    bool le(var self, var obj);

Returns false if the object `self` is less than or equal to the object `obj`.

__cmp__

    int cmp(var self, var obj);

The return value of `cmp` is `< 0` if `self` is less than `obj`, `> 0` if `self` is greater than `obj` and `0` if they are equal.

### Examples

__Usage__

    show($I(gt($I(15), $I(3 )))); /* 1 */
    show($I(lt($I(70), $I(81)))); /* 1 */
    show($I(lt($I(71), $I(71)))); /* 0 */
    show($I(ge($I(78), $I(71)))); /* 1 */
    show($I(gt($I(32), $I(32)))); /* 0 */
    show($I(le($I(21), $I(32)))); /* 1 */
    
    show($I(cmp($I(20), $I(20)))); /*  0 */
    show($I(cmp($I(21), $I(20)))); /*  1 */
    show($I(cmp($I(20), $I(21)))); /* -1 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Ord
__Comparable by Order__

The `Ord` class can be implemented to provide an ordering relationship between objects. In other words, to test if one object is _less than_ or _greater than_ another.

By default the `Ord` class will simply compare the raw memory of two objects using `memcmp` and the `Size` class, but for objects where ordering is more meaningful (such as Strings or Integers) this should be overridden.

### Derivers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _A Sequence of Numbers_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Stack Based Collection_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_
### Implementers

* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Float Point Object_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
