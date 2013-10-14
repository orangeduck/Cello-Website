Dict
----
__Key-Value access to object__

The `At` class provides an interface for key-value access and manipulation of objects (typically collections).


### Methods

-------------------------------

    var get(var self, var key);

Access an element of an object at a given key.

* __Parameters__
    * `self` object to be accessed
    * `key` key object to access at
* __Returns__ object at that key

------------------------------- 

    void put(var self, var key, var val);

Set an element of an object at a given key.

* __Parameters__
    * `self` object to be accessed
    * `key` key object to access at
    * `obj` object to set
* __Returns__ None

------------------------------- 


### Signature


    class {
      var (*get)(var, var);
      void (*put)(var, var, var);
    } Dict;
    

### Implementers

* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[Pool](pool)</span> _Reference Counting Pool_
* <span style="width:75px; float:left;">[File](file)</span> _Operating System File_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_


### See Also

* <span style="width:75px; float:left;">[Collection](collection)</span> _Treatable as several objects_
* <span style="width:75px; float:left;">[At](at)</span> _Elements can be directly accessed and set_


### Examples

__Usage__

    var prices = new(Table, String, Int);
    put(prices, $(String, "Apple"),  $(Int, 12)); 
    put(prices, $(String, "Banana"), $(Int,  6)); 
    put(prices, $(String, "Pear"),   $(Int, 55)); 
    
    var pear_price = get(prices, $(String, "Pear"));
    var banana_price = get(prices, $(String, "Banana"));
    var apple_price = get(prices, $(String, "Apple"));
    
    show(pear_price);   /* 55 */
    show(banana_price); /*  6 */
    show(apple_price);  /* 12 */

[Back](/documentation)
