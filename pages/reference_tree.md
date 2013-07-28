Tree
----
__Binary Tree Container__

Tree is a binary tree container mapping keys to values. It is a [Container](/documentation/containers) meaning allocates storage for the contained keys and values types and will destroy them upon destruction.

Key objects must implement `Ord` and `Eq`. Contents are copied into this container using `assign` which means both keys and values must also implement that.

Trees provide O(log n) operation speeds for deletion, insertion and retrival making them a balanced overall data structure.

The equivalent C++ construct to this type is a [std::map](http://www.cplusplus.com/reference/map/map/).


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](eq)</span> `eq` `neq` `if_eq` `if_neq`
* <span style="width:75px; float:left;">[Collection](collection)</span> `len` `clear` `contains` `discard`
* <span style="width:75px; float:left;">[Dict](dict)</span> `get` `put`
* <span style="width:75px; float:left;">[Iter](iter)</span> `foreach` `iter_start` `iter_end` `iter_next`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also

* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_


### Examples

__Usage__

    var t0 = new(Tree, String, Int);
    put(t0, $(String, "Hello"), $(Int, 2));
    put(t0, $(String, "There"), $(Int, 5));
    
    var t1 = new(Tree, String, Int);
    put(t1, $(String, "Bonjour"), $(Int, 9));
    put(t1, $(String, "Where"), $(Int, 5));
    
    delete(t0);
    delete(t1);

    
__Manipulation__

    var t = new(Tree, String, Int);
    put(t, $(String, "Hello"), $(Int, 2));
    put(t, $(String, "There"), $(Int, 5));
    
    show($(Int, len(t))); /* 2 */
    show(contains(t, $(String, "Hello"))); /* True */
    
    discard(t, $(String, "Hello"));
    
    show($(Int, len(t))); /* 1 */
    show(contains(t, $(String, "Hello"))); /* False */
    show(contains(t, $(String, "There"))); /* True */
    
    clear(t);
    
    show($(Int, len(t))); /* 0 */
    show(contains(t, $(String, "Hello"))); /* False */
    show(contains(t, $(String, "There"))); /* False */
    
    delete(t);

[Back](/documentation)
