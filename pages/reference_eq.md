Eq
--
__Comparable for Equality__

The `Eq` class provides a generic way to test for equality between two objects.

As well as `eq` and `neq` two macros are provided to test like an `if` statement. `#define if_eq(X,Y) if(eq(X,Y))` and `#define if_neq(X,Y) if(neq(X,Y))`.

A default implementation is provided by all types which compares memory location.

This default implementation is the same as `is` and `isnt`. While an implementation of Equality tests for equal values, `is` and `isnt` only test to see if two objects _are the same object_ in respect to their memory location.


### Methods

-------------------------------

    var eq(var self, var obj);

Test if two objects are considered equal.

* __Parameters__
    * `self` First Object
    * `obj` Second Object
* __Returns__ Equality Truth Value

------------------------------- 

    var neq(var self, var obj);

Test if two objects are considered not equal.

* __Parameters__
    * `self` First Object
    * `obj` Second Object
* __Returns__ Equality Truth Value

------------------------------- 


### Signature


    class {
      var (*eq)(var,var);
    } Eq;
    

### Implementers

* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Reference](reference)</span> _Basic Reference Type_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Ord](ord)</span> _Comparable for Ordering_


### Examples

__Usage__
    
    show(  eq($(Int, 1 ), $(Int, 1 )) ); /* True */
    show( neq($(Int, 2 ), $(Int, 20)) ); /* True */
    show( neq($(String, "Hello"), $(String, "Hello")) ); /* False */
    show(  eq($(String, "Hello"), $(String, "There")) ); /* False */

    var a = $(Int, 1);
    var b = $(Int, 1);
    
    show( eq(a, b) ); /* True */
    show( a is b );  /* False */
    show( a isnt b ); /* True */
    
__Macros__
    
    var x = $(String, "Foo");
    var y = $(String, "Foo");
    
    if_eq(x, y) {
        println("Foo!");
    } else {
        println("Foo! ????");
    }
    

[Back](/documentation)
