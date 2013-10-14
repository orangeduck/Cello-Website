Append
------
__Elements can be added to end__

The `Append` class provides an interface for appending an object to another, this is typically a collection.


### Methods

-------------------------------

    void append(var self, var obj);

Append an object to another

* __Parameters__
    * `self` object to be appended to
    * `obj` object to be append
* __Returns__ None

------------------------------- 


### Signature


    class {
      void (*append)(var, var);
    } Append;
    

### Implementers

* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Collection](collection)</span> _Treatable as several objects_
* <span style="width:75px; float:left;">[Push](push)</span> _Elements can be Pushed and Popped_
* <span style="width:75px; float:left;">[At](at)</span> _Elements can be directly accessed and set_


### Examples

    var x = new(Array, Real, $(Real, 9.9), $(Real, 2.8));
    
    show(x); /* <'Array' At 0x0000000000414603 [9.9, 2.8]> */
    append(x, $(Real, 2.5));
    show(x); /* <'Array' At 0x0000000000414603 [9.9, 2.8, 2.5]> */
    
    delete(x);

[Back](/documentation)
