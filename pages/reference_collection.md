Collection
----------
__Treatable as several objects__

The `Collection` class provides an interface for treating data structures as a container or collection of other objects. It provides methods to check the number of items in a collection. It also provides methods to check if a container has an object inside and to discard this object if it does.

Note that the `contains` method uses the `Eq` type class to test for containment. Therefore it does not test for actual exact objects but any two objects that are equal.


### Methods

-------------------------------

    int len(var self);

Give the length of a collection.

* __Parameters__
    * `self` Collection
* __Returns__ Length of Collection

------------------------------- 

    void clear(var self);

Remove all items from a Collection.

* __Parameters__
    * `self` Collection
* __Returns__ None

------------------------------- 

    var contains(var col, val obj);

Check if a Collection contains an Object.

* __Parameters__
    * `self` Collection
    * `obj` Object
* __Returns__ Containment truth value

------------------------------- 

    void discard(var self, var obj);

Remove an object from a Collection.

* __Parameters__
    * `self` Collection
    * `obj` Object
* __Returns__ None

------------------------------- 

    var is_empty(var self);

Check if a collection is empty.

* __Parameters__
    * `self` Collection
* __Returns__ Empty truth value

------------------------------- 

    var maximum(var self);

Return the largest item in a collection.

* __Parameters__
    * `self` Collection
* __Returns__ Largest Item

------------------------------- 

    var minimum(var self);

Return the smallest item in a collection.

* __Parameters__
    * `self` Collection
* __Returns__ Smallest Item

------------------------------- 


### Signature


    class {
      int (*len)(var);
      void (*clear)(var);
      var (*contains)(var, var);
      void (*discard)(var, var);
    } Collection;
    

### Implementers

* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Pool](pool)</span> _Reference Counting Pool_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Sort](sort)</span> _Elements can be sorted_
* <span style="width:75px; float:left;">[Append](append)</span> _Elements can be added to end_
* <span style="width:75px; float:left;">[Push](push)</span> _Elements can be Pushed and Popped_
* <span style="width:75px; float:left;">[At](at)</span> _Elements can be directly accessed and set_
* <span style="width:75px; float:left;">[Reverse](reverse)</span> _Order can be reversed_
* <span style="width:75px; float:left;">[Dict](dict)</span> _Key-Value access to object_
* <span style="width:75px; float:left;">[Iter](iter)</span> _Can be looped over_


### Examples

__Usage__
    var x = new(List, $(Int, 1), $(Real, 2.0), $(String, "Hello"));

    show(len(x)); /* 3 */
    show(contains(x, $(Int, 1)));          /* True */
    show(contains(x, $(Real, 2.0)));       /* True */
    show(contains(x, $(String, "Hello"))); /* True */

    discard(x, $(Real, 2.0));

    show(len(x)); /* 2 */
    show(contains(x, $(Int, 1)));          /* True */
    show(contains(x, $(String, "Hello"))); /* True */
    show(contains(x, $(Real, 2.0)));       /* False */

    clear(x);

    show(len(x));      /* 0 */
    show(is_empty(x)); /* True */

    delete(x);

[Back](/documentation)
