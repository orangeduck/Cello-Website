Table
-----
__Hashtable Container__

Table is a Hashtable container mapping a keys to values. The keys and values must each be a single type. `Hash` and `Eq` must be defined for the key types. It is a [Container](/documentation/containers) meaning it allocates storage for the keys and values specified. It also deallocates and destroys the objects inside upon destruction.

Data is copied into the container using `assign` meaning that must be defined for both key and value types.

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

* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_


### Examples

__Usage__

    var prices = new(Table, String, Int);
    put(prices, $(String, "Apple"),  $(Int, 12)); 
    put(prices, $(String, "Banana"), $(Int,  6)); 
    put(prices, $(String, "Pear"),   $(Int, 55));

    foreach (key in prices) {
        var price = get(prices, key);
        println("Price of %$ is %$", key, price);
    }
    
    delete(prices);
    
    
__Manipulation__

    var t = new(Table, String, Int);
    put(t, $(String, "Hello"), $(Int, 2));
    put(t, $(String, "There"), $(Int, 5));
    
    show($(Int, len(t))); /* 2 */
    show(contains(t, $(String, "Hello"))); /* True */
    
    discard(t, $(String, "Hello"));
    
    show($(Int, len(t))); /* 1 */
    show(contains(t, $(String, "Hello"))); /* False */
    show(contains(t, $(String, "There"))); /* True  */
    
    clear(t);
    
    show($(Int, len(t))); /* 0 */
    show(contains(t, $(String, "Hello"))); /* False */
    show(contains(t, $(String, "There"))); /* False */
    
    delete(t);

[Back](/documentation)
