Bool
----
__Boolean Truth Value__

Bool is a Cello wrapper of a standard C bool. It is defined as follows.

    local var True  = (var)1;
    local var False = (var)0;
    
These evaluate to true and false correctly in `if` statements and can be returned, passed around, and manipulated using the standard logical operators. Bools can be cast to c `bool` and back again without issue.

There is no data object for Bool. This is because they are hard coded into `type_of`.


### Implements

* <span style="width:75px; float:left;">[Eq](eq)</span> `eq` `neq` `if_eq` `if_neq`
* <span style="width:75px; float:left;">[Ord](ord)</span> `gt` `lt` `ge` `le`
* <span style="width:75px; float:left;">[Hash](hash)</span> `hash`
* <span style="width:75px; float:left;">[AsChar](aschar)</span> `as_char`
* <span style="width:75px; float:left;">[AsLong](aslong)</span> `as_long`
* <span style="width:75px; float:left;">[AsDouble](asdouble)</span> `as_double`
* <span style="width:75px; float:left;">[AsStr](asstr)</span> `as_str`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also

* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_


### Examples

__Logic__

    var x = True;
    var y = False;
    
    show(x and y); /* False */
    show(x or y);  /* True */
    show(x or y);  /* True */
    show(x and not y);  /* True */
    show(x or not y);   /* True */
    show(not (x or y)); /* False */
    
__Properties__
    
    var x = True;
    var y = False;
    
    show(gt(x, y));   /* True */
    show($(Int, as_long(x)));   /* 1 */
    show($(String, as_str(x))); /* "True" */

[Back](/documentation)
