List
----
__Sequential Collection__

List is data structure containing a sequence of pointers to Cello objects. It can dynamically grow and shrink in size depending on how many elements it contains. It is a [Collection](/documentation/containers) meaning it does not allocate storage for the objects inside and is not responsible for their destruction.

As it only contains pointers a List can contain several different types of objects, but if this is the case the user must ensure operations remain valid against all the contained types. For example to check if a list of `String` and `Int` contains a specific `Int`, the equality operation must be valid when comparing a `String` and an `Int`.

Elements are ordered linearly. They can be accessed by their position in this sequence directly. Addition and removal of elements at the end of the sequence is fast, with memory movement required for elements in the middle of the sequence. 

The equivalent C++ construct to this type is a [std::vector](http://www.cplusplus.com/reference/vector/vector/) of pointers.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](eq)</span> `eq` `neq` `if_eq` `if_neq`
* <span style="width:75px; float:left;">[Collection](collection)</span> `len` `clear` `contains` `discard`
* <span style="width:75px; float:left;">[Push](push)</span> `push` `pop` `push_at` `pop_at`
* <span style="width:75px; float:left;">[At](at)</span> `at` `set`
* <span style="width:75px; float:left;">[Iter](iter)</span> `foreach` `iter_start` `iter_end` `iter_next`
* <span style="width:75px; float:left;">[Reverse](reverse)</span> `reverse`
* <span style="width:75px; float:left;">[Sort](sort)</span> `sort`
* <span style="width:75px; float:left;">[Append](append)</span> `append`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also

* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_


### Examples

__Construction & Deletion__

    var i0 = new(String, $(String, "Test"));
    var i1 = new(Int, $(Int, 6));
    
    var x = new(List, i0, i1);
    show(x); /* <'List' At 0x0000000000414603 ["Test", 6]> */
    delete(x);
    
    delete(i0);
    delete(i1);
    
__Element Access__

    var i0 = new(String, $(String, "Test"));
    var i1 = new(Int, $(Int, 6));
    var i2 = new(Real, $(Real, 5.2));
    
    var x = new(List, i0, i1);
    show(at(x, 0)); /* "Test" */
    show(at(x, 1)); /* 6 */
    
    set(x, 0, i2);
    show(at(x, 0)); /* 5.2 */
    
    delete(x);
    
    delete(i0);
    delete(i1);
    delete(i2);

__Collection Queries__

    var i0 = new(Int, $(Int, 2));
    var i1 = new(Int, $(Int, 6));
    var i2 = new(Real, $(Real, 5.2));

    var x = new(List, i0, i1, i2);
    
    show(contains(x, $(Int, 6)));    /* True */
    show($(Int, len(x)));            /* 3 */
    
    discard(x, $(Int, 6));
    
    show(contains(x, $(Int, 6)));    /* False */
    show($(Int, len(x)));            /* 2 */
    show(is_empty(x));               /* False */
    
    clear(x);
    
    show(is_empty(x));               /* True */
  
    delete(x);
    
    delete(i0);
    delete(i1);
    delete(i2);
    
__Iteration__

    var i0 = new(String, $(String, "Test"));
    var i1 = new(Int, $(Int, 6));
    var i2 = new(Real, $(Real, 5.2));
    
    var x = new(List, i0, i1, i1);
    
    foreach(i in x) {
      show(i);
    }
    
    delete(x);
    
    delete(i0);
    delete(i1);
    delete(i2);

[Back](/documentation)
