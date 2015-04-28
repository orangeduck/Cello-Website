  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__eq__

    bool eq(var self, var obj);

Returns true if the object `self` is equal to the object `obj`.

__neq__

    bool neq(var self, var obj);

Returns false if the object `self` is equal to the object `obj`.

### Examples

__Usage__

    show($I( eq($I(1), $I( 1)))); /* 1 */
    show($I(neq($I(2), $I(20)))); /* 1 */
    show($I(neq($S("Hello"), $S("Hello")))); /* 0 */
    show($I( eq($S("Hello"), $S("There")))); /* 0 */
    
    var a = $I(1); var b = $I(1);
    
    show($I(eq(a, b))); /* 1 */
    show($I(a is b));   /* 0 */
    show($I(a isnt b)); /* 1 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Eq
__Value Equality__

The `Eq` class is used to define equality between two object values. This class is important as it is used by many data structures to test for duplicate items or equality between two items.

By default, if passed two objects of the same type, the `Eq` class will simply compare the raw memory of both objects, using the `Size` class. If passed two objects of different types it will return `false`.

For objects that manage their own data this class may need to be overridden to ensure that objects of the same _value_ are still treated as equal. E.G. for string types.

This class to used to test for _value_ equality between objects, I.E. if they represent the same thing. For _object_ equality the `is` keyword can be used, which will return `true` only if two variables are pointing to the same object in memory.

### Derivers

* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _A Sequence of Numbers_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Stack Based Collection_
### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Float Point Object_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
