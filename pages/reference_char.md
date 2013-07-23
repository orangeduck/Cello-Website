Char
----

Char is a wrapper for the native C char type. 

### Implements

* <span style="width:75px; float:left;">[New](reference/new)</span> `new`, `delete`, `construct`, `destruct`
* <span style="width:75px; float:left;">[Assign](reference/assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](reference/copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](reference/eq)</span> `eq`, `neq`
* <span style="width:75px; float:left;">[Ord](reference/ord)</span> `gt`, `lt`, `ge`, `le`
* <span style="width:75px; float:left;">[Hash](reference/hash)</span> `hash`
* <span style="width:75px; float:left;">[AsChar](reference/aschar)</span> `as_char`
* <span style="width:75px; float:left;">[Serialize](reference/serialize)</span> `serial_read`, `serial_write`
* <span style="width:75px; float:left;">[Show](reference/show)</span> `show`, `look`, `print`, `scan`

### See Also

* <span style="width:75px; float:left;">[String](reference/string)</span> _String Wrapper_

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