Sort
----
__Elements can be sorted__

The `Sort` class provides an interface for sorting an object, typically a collection. Note that in general this means `Ord` needs to be defined across the items in the collection.


### Methods

-------------------------------

    void sort(var self);

Sort an object

* __Parameters__
    * `self` object to be sorted
* __Returns__ None

------------------------------- 


### Signature


    class {
      void (*sort)(var);
    } Sort;
    

### Implementers

* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_


### See Also

* <span style="width:75px; float:left;">[Ord](ord)</span> _Comparable for Ordering_
* <span style="width:75px; float:left;">[Collection](collection)</span> _Treatable as several objects_
* <span style="width:75px; float:left;">[At](at)</span> _Elements can be directly accessed and set_


### Examples

__Usage__

    var x = new(Array, Real, 4, $(Real, 5.2), $(Real, 7.1), $(Real, 2.2), $(Real, 1.1));
    
    show(x); /* <'Array' At 0x0000000000414603 [5.2, 7.1, 2.2, 1.1]> */
    sort(x);
    show(x); /* <'Array' At 0x0000000000414603 [1.1, 2.2, 5.2, 7.1]> */
    
    delete(x);

[Back](/documentation)
