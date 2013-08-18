Ord
---
__Comparable for Ordering__

The `Ord` class provides an ordering relationship between objects of a certain type. This allows for one to test if some object is considered _Greater Than_ or _Less Than_ another.

The compliments of these are also provided in `le` and `ge`.

Similarly to the `Eq` class macros are provided to allow for testing like an `if` statement

    #define if_lt(X,Y) if(lt(X,Y))
    #define if_gt(X,Y) if(gt(X,Y))
    #define if_le(X,Y) if(le(X,Y))
    #define if_ge(X,Y) if(ge(X,Y))

Ordering is required for some standard containers and collections.

Strings are ordered in alphabetical order.


### Methods

-------------------------------

    var gt(var self, var obj);

Test if one object is greater than other.

* __Parameters__
    * `self` First Object
    * `obj` Second Object
* __Returns__ Equality Truth Value

------------------------------- 

    var lt(var self, var obj);

Test if one object is less than other.

* __Parameters__
    * `self` First Object
    * `obj` Second Object
* __Returns__ Equality Truth Value

------------------------------- 

    var ge(var self, var obj);

Test if one object is not less than other.

* __Parameters__
    * `self` First Object
    * `obj` Second Object
* __Returns__ Equality Truth Value

------------------------------- 

    var le(var self, var obj);

Test if one object is not greater than other.

* __Parameters__
    * `self` First Object
    * `obj` Second Object
* __Returns__ Equality Truth Value

------------------------------- 


### Signature


    class {
      var (*gt)(var,var);
      var (*lt)(var,var);
    } Ord;
    

### Implementers

* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Eq](eq)</span> _Comparable for Equality_


### Examples

__Usage__

    show(  gt($(Int, 15), $(Int, 3 )) ); /* True */
    show(  lt($(Int, 70), $(Int, 81)) ); /* True */
    show(  lt($(Int, 71), $(Int, 71)) ); /* False */
    show(  ge($(Int, 78), $(Int, 71)) ); /* True */
    show(  gt($(Int, 32), $(Int, 32)) ); /* False */
    show(  le($(Int, 21), $(Int, 32)) ); /* True */
    
__Macros__

    var x = $(String, "Daniel");
    var y = $(String, "Holden");
    
    if_gt(x, y) {
        println("Last Name First");
    } else {
        println("First Name First");
    }


[Back](/documentation)
