Real
----
__Basic Float Point Type__

Basic wrapper of standard C `double`.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](eq)</span> `eq` `neq` `if_eq` `if_neq`
* <span style="width:75px; float:left;">[Ord](ord)</span> `gt` `lt` `ge` `le`
* <span style="width:75px; float:left;">[Hash](hash)</span> `hash`
* <span style="width:75px; float:left;">[AsDouble](asdouble)</span> `as_double`
* <span style="width:75px; float:left;">[AsLong](aslong)</span> `as_long`
* <span style="width:75px; float:left;">[Num](num)</span> `add` `sub` `mul` `div` `negate` `absolute`
* <span style="width:75px; float:left;">[Serialize](serialize)</span> `serial_read` `serial_write`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also

* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_


### Examples

__Usage__

    var r0 = $(Real, 1.0);
    var r1 = new(Real, 24.313);
    var r2 = copy(r0);
    
    show(r0); /* 1.0 */
    show(r1); /* 24.313 */
    show(r2); /* 1.0 */
    
    delete(r1);
    delete(r2);
    
__Maths__
    
    var r0 = $(Real, 0.0);
    
    show(r0); /* 0 */
    
    add(r0, $(Real, 10.1)); /* 10.1 */
    mul(r0, $(Real, 3.5));  /* 35.35 */
    div(r0, $(Real, 2.0));  /* 17.675 */
    
    if_gt(r0, $(Real, 11.1)) {
        print("%f is greater than 11.1!", i0);
    }
    

[Back](/documentation)
