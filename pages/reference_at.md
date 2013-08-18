At
--
__Elements can be directly accessed and set__

The `At` class provides an interface for positional access and manipulation of objects (typically collections but not always).


### Methods

-------------------------------

    var at(var self, int i);

Access an element of an object at a position.

* __Parameters__
    * `self` object to be accessed
    * `i` position to access at
* __Returns__ Object at that position

------------------------------- 

    void set(var self, int i, var obj);

Set an element of an object at a position.

* __Parameters__
    * `self` object to be accessed
    * `i` position to access at
    * `obj` Object to set
* __Returns__ None

------------------------------- 


### Signature


    class {
      var (*at)(var, int);
      void (*set)(var, int, var);
    } At;
    

### Implementers

* <span style="width:75px; float:left;">[Reference](reference)</span> _Basic Reference Type_
* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_


### See Also

* <span style="width:75px; float:left;">[Push](push)</span> _Elements can be Pushed and Popped_
* <span style="width:75px; float:left;">[At](at)</span> _Elements can be directly accessed and set_
* <span style="width:75px; float:left;">[Collection](collection)</span> _Treatable as several objects_


### Examples

__Usage__

    var fst = $(Int, 1);
    var snd = $(Real, 2.0);
    var trd = $(String, "Hello");

    var x = new(List, 3, fst, snd, trd);

    show(at(x, 0)); /* 1 */
    show(at(x, 1)); /* 2.0 */
    show(at(x, 2)); /* Hello */
    
    set(x, 1, trd);
    
    show(at(x, 1)); /* Hello */
    
    delete(x);

[Back](/documentation)
