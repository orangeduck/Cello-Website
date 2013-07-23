Array
-----

Array is data structure containing a sequence of a single type of object. It can dynamically grow and shrink in size depending on how many elements it contains. It is a [Container](/documentation/containers) meaning it allocates storage for the type specified. It also deallocates and destroys the objects inside upon destruction.

Elements are copied in an Array using `assign` which means the type much implement the [Assign](reference/assign) class.

Elements are ordered linearly. Elements are accessed by their position in this sequence directly. Addition and removal of elements at the end of the sequence is fast, with memory movement required for elements in the middle of the sequence. 

The equivalent C++ construct to this type is [std::vector](http://www.cplusplus.com/reference/vector/vector/)

### Implements

* <span style="width:75px; float:left;">[New](reference/new)</span> `new`, `delete`, `construct`, `destruct`
* <span style="width:75px; float:left;">[Assign](reference/assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](reference/copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](reference/eq)</span> `eq`, `neq`
* <span style="width:75px; float:left;">[Collection](reference/collection)</span> `len`, `clear`. `contains`, `discard`, `is_empty`
* <span style="width:75px; float:left;">[Push](reference/push)</span> `push`, `push_at`, `pop`, `pop_at`
* <span style="width:75px; float:left;">[At](reference/at)</span> `at`, `set`
* <span style="width:75px; float:left;">[Iter](reference/iter)</span> `iter_start`, `iter_next`, `iter_end`
* <span style="width:75px; float:left;">[Reverse](reference/reverse)</span> `reverse`
* <span style="width:75px; float:left;">[Sort](reference/sort)</span> `sort`
* <span style="width:75px; float:left;">[Append](reference/append)</span> `append`
* <span style="width:75px; float:left;">[Show](reference/show)</span> `show`, `look`, `print`, `scan`

### See Also

* <span style="width:75px; float:left;">[List](reference/list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Table](reference/table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Tree](reference/tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[Dictionary](reference/dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Map](reference/map)</span> _Binary Tree Collection_

### Examples

__Construction & Deletion__

    var x = new(Array, Int, 0);
    push(x, $(Int, 32));
    push(x, $(Int, 6));
    
    /* <'Array' At 0x0000000000414603 [32, 6]> */
    show(x);
    delete(x);
    
__Element Access__

    var x = new(Array, Real, 2, $(Real, 0.01), $(Real, 5.12));
    
    show(at(x, 0)); /* 0.01 */
    show(at(x, 1)); /* 5.12 */
    
    set(x, 0, $(Real, 500.1));
    show(at(x, 0)); /* 500.1 */
    
    delete(x);

__Collection Queries__

    var x = new(Array, Char, 4, $(Char, 'a'), $(Char, 'b'), $(Char, 'c'), $(Char, 'd'));
    
    show(contains(x, $(Char, 'a'))); /* True */
    show($(Int, len(x)));            /* 4 */
    
    discard(x, $(Char, 'c'));
    
    show(contains(x, $(Char, 'c'))); /* False */
    show($(Int, len(x)));            /* 3 */
    show(is_empty(x));               /* False */
    
    clear(x);
    
    show(is_empty(x));               /* True */
  
    delete(x);
    
__Iteration__

    var greetings = new(Array, String, 3, $(String, "Hello"), $(String, "Bonjour"), $(String, "Hej"));
    
    foreach(greet in greetings) {
      show(greet);
    }
    
    delete(x);

[Back](/documentation)