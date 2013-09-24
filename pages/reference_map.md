Map
---
__Binary Tree Collection__

Map is a binary tree data structure mapping keys to values. It is a [Collection](/documentation/containers) meaning it does not allocate storage for either the keys or the values places into it and it is not responsible for their destruction.

Key objects must implement `Ord` and `Eq` and as with `List` this implementation must be meaningful across all key types added to the map.

Maps provide O(log n) operation speeds for deletion, insertion and retrival making them a balanced overall data structure.

The equivalent C++ construct to this type is a [std::map](http://www.cplusplus.com/reference/map/map/) of pointers.


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

* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_


### Examples

__Creation__

    var prices = new(Map);
    var k0 = new(String, $(String, "Apple"));
    var k1 = new(String, $(String, "Banana"));
    var v0 = new(Int, $(Int, 10));
    var v1 = new(Int, $(Int, 20));
    
    put(prices, k0, v0);
    put(prices, k1, v1);
    
    foreach(k in prices) {
        println("The Price of %s is %i", k, get(prices, k));
    }
    
    delete(prices);
    delete(k0); delete(k1);
    delete(v0); delete(v1);

[Back](/documentation)
