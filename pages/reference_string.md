String
------
__Basic String Type__

String provides a basic wrapper for the C `char*` type.

As well as wrapping the C string type it can also provide a number of other operations such as concatination and reversal for strings allocated on the heap. For these it will dynamically reallocate more memory if required making it significantly easier on mental overhead than C strings.

One must be careful when using strings not to attempt to modify strings allocated on the stack - as this will usually throw a bad error.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](eq)</span> `eq` `neq` `if_eq` `if_neq`
* <span style="width:75px; float:left;">[Ord](ord)</span> `gt` `lt` `ge` `le`
* <span style="width:75px; float:left;">[Collection](collection)</span> `len` `clear` `contains` `discard`
* <span style="width:75px; float:left;">[Hash](hash)</span> `hash`
* <span style="width:75px; float:left;">[Reverse](reverse)</span> `reverse`
* <span style="width:75px; float:left;">[AsStr](asstr)</span> `as_str`
* <span style="width:75px; float:left;">[Append](append)</span> `append`
* <span style="width:75px; float:left;">[Format](format)</span> `format_to` `format_from`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also

* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_


### Examples

__Creation__
    
    /* Stack String must not be edited */
    var s0 = $(String, "Hello");
    
    /* Heap String can be freely edited */
    var s1 = new(String, "There");
    append(s1, $(String, " There"));
    
    delete(s1);
    
__Manipulation__

    var s0 = new(String, "Balloons");
    
    show($(Int, len(s0))); /* 8 */
    show(contains(s0, $(String, "Ball")));     /* True */
    show(contains(s0, $(String, "oon")));      /* True */
    show(contains(s0, $(String, "Balloons"))); /* True */
    show(contains(s0, $(Char, 'l')));          /* True */
    
    discard(s0, $(String, "oons"));
    
    show(eq(s0, $(String, "Ball"))); /* True */
    
    clear(s0);
    
    show($(Int, len(s0))); /* 0 */
    show(eq(s0, s0, $(String, ""))); /* True */
    
    delete(s0);

[Back](/documentation)
