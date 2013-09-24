Assign
------
__Assignable to__

The `Assign` class lets one assign a value from one object to another. This essentially means copying the contents of `obj` into `self`.

This class is important to implement as it is used extensively by contains to give allocated space values. Also for this reason one should not assume anything about the state of `self` (for example it may not have been constructed).


### Methods

-------------------------------

    void assign(var self, var obj);

Assign the value of one object to another.

* __Parameters__
    * `self` Object to get assigned to
    * `obj` Object to assign
* __Returns__ None

------------------------------- 


### Signature


    class {
      void (*assign)(var, var);
    } Assign;    
    

### Implementers

* <span style="width:75px; float:left;">[Function](function)</span> _High Level Function_
* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Reference](reference)</span> _Basic Reference Type_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Mutex](mutex)</span> _Mutual Exclusion Lock_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_
* <span style="width:75px; float:left;">[Thread](thread)</span> _Concurrent Processes_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Copy](copy)</span> _Copyable_
* <span style="width:75px; float:left;">[New](new)</span> _Constructable on the Heap_


### Examples

__Usage 1__

    var x = new(Int, $(Int, 10));
    var y = new(Int, $(Int, 20));
    
    show(x); /* 10 */
    show(y); /* 20 */

    assign(x, y);
    
    show(x); /* 20 */
    show(y); /* 20 */
    
    delete(x);
    delete(y);


__Usage 2__

    var x = new(String, $(String, "Hello"));
    var y = new(String, $(String, "There"));
    
    show(x); /* Hello */
    show(y); /* There */
    
    assign(x, y);
    
    show(x); /* There */
    show(y); /* There */
    
    delete(x);
    delete(y);

[Back](/documentation)
