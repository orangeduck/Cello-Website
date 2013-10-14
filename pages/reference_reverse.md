Reverse
-------
__Order can be reversed__

The `Reverse` class provides an interface for reversing an object, typically a collection.


### Methods

-------------------------------

    void reverse(var self);

Reverse an object

* __Parameters__
    * `self` object to be reversed
* __Returns__ None

------------------------------- 


### Signature


    class {
      void (*reverse)(var);
    } Reverse;
    

### Implementers

* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Collection](collection)</span> _Treatable as several objects_
* <span style="width:75px; float:left;">[At](at)</span> _Elements can be directly accessed and set_


### Examples

__Usage__

    var x = new(Array, Real, $(Real, 5.2), $(Real, 7.1), $(Real, 2.2), $(Real, 1.1));
    
    show(x); /* <'Array' At 0x0000000000414603 [5.2, 7.1, 2.2, 1.1]> */
    reverse(x);
    show(x); /* <'Array' At 0x0000000000414603 [1.1, 2.2, 7.1, 5.2]> */
    
    delete(x);

[Back](/documentation)
