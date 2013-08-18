Copy
----
__Copyable__

The `Copy` class allows for a user to make a copy of an object. This copy must be deleted by the user.

By convention `copy` means a deep copy. That is a copy that also copies all inner components of the object.


### Methods

-------------------------------

    var copy(var obj);

Make a copy of an object.

* __Parameters__
    * `obj` Object to copy
* __Returns__ Copy of Object

------------------------------- 


### Signature


    class {
      var (*copy)(var);
    } Copy;
    

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

* <span style="width:75px; float:left;">[New](new)</span> _Constructable on the Heap_
* <span style="width:75px; float:left;">[Assign](assign)</span> _Assignable to_


### Examples

__Usage__
    
    var x = new(String, "Hello");
    var y = copy(x);
    
    show(x); /* Hello */
    show(y); /* Hello */
    show(x is y); /* False */
    
    delete(x);
    delete(y);

[Back](/documentation)
