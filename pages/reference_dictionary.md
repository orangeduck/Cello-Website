Dictionary
----------
__Hashtable Collection__

Dictionary is hashtable data structure mapping hashable keys to values. It is a [Collection](/documentation/containers) meaning it does not allocate storage for the keys or values inside of it. Instead it only stored references to these objects. This means both keys and values inside must be stored and managed by the programmer for the duration of the Dictionary's life.

As it is a Hashtable Dictionary provides O(1) performance for element access in the best case and O(n) in the worst.



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

* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_


### Examples

__Usage__
    
    var prices = new(Dictionary);
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
