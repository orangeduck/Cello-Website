Char
----
__Basic Character Type__

Char is a wrapper for the native C char type.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](eq)</span> `eq` `neq` `if_eq` `if_neq`
* <span style="width:75px; float:left;">[Ord](ord)</span> `gt` `lt` `ge` `le`
* <span style="width:75px; float:left;">[Hash](hash)</span> `hash`
* <span style="width:75px; float:left;">[AsChar](aschar)</span> `as_char`
* <span style="width:75px; float:left;">[Serialize](serialize)</span> `serial_read` `serial_write`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also

* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_


### Examples

__Properties__

    var x = $(Char, 'a');
    var y = new(Char, 'b');
    var z = copy(x);
    
    show(eq(x, z)); /* True */
    show(gt(y, x)); /* True */
    
    assign(y, x);
    
    show(y) /* a */
    
    delete(y)
    delete(z);
    

[Back](/documentation)
