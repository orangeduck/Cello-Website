Int
---
__Basic Integer Type__

Basic wrapper of standard C `long`.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](eq)</span> `eq` `neq` `if_eq` `if_neq`
* <span style="width:75px; float:left;">[Ord](ord)</span> `gt` `lt` `ge` `le`
* <span style="width:75px; float:left;">[Hash](hash)</span> `hash`
* <span style="width:75px; float:left;">[AsLong](aslong)</span> `as_long`
* <span style="width:75px; float:left;">[AsDouble](asdouble)</span> `as_double`
* <span style="width:75px; float:left;">[Num](num)</span> `add` `sub` `mul` `div` `negate` `absolute`
* <span style="width:75px; float:left;">[Serialize](serialize)</span> `serial_read` `serial_write`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also

* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_


### Examples

__Usage__

    var i0 = $(Int, 1);
    var i1 = new(Int, 24313);
    var i2 = copy(i0);
    
    show(i0); /* 1 */
    show(i1); /* 24313 */
    show(i2); /* 1 */
    
    delete(i1);
    delete(i2);
    
__Maths__
    
    var i0 = $(Int, 0);
    
    show(i0); /* 0 */
    
    add(i0, $(Int, 10)); /* 10 */
    mul(i0, $(Int, 3));  /* 30 */
    div(i0, $(Int, 2));  /* 15 */
    
    if_gt(i0, $(Int, 10)) {
        print("%i is greater than 10!", i0);
    }
    

[Back](/documentation)
