Pool
----
__Reference Counting Pool__

Pool provides a method for reference counting of Cello objects via `retain` and `release`. It stores a reference count for any objects included in it and will perform destruction on those objects when their reference count reaches zero.

This is designed to aid in memory management.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Retain](retain)</span> `retain` `release`
* <span style="width:75px; float:left;">[Collection](collection)</span> `len` `clear` `contains` `discard`
* <span style="width:75px; float:left;">[Dict](dict)</span> `get` `put`


### See Also

* <span style="width:75px; float:left;">[Reference](reference)</span> _Basic Reference Type_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_


### Examples

__Usage__

    var p = new(Pool);
    
    lambda(table_fill, args) {
        var t = at(args, 0);
        put(t, $(String, "First"),  $(Real, 0.0));
        put(t, $(String, "Second"), $(Real, 0.1));
        put(t, $(String, "Third"),  $(Real, 5.7));
        release(p, t);
        return None
    };
    
    lambda(table_process, args) {
        var t = at(args, 0);
        put(t, $(String, "First"), $(Real, -0.65));
        release(p, t);
        return None;
    };

    var x = retain(p, new(Table, String, Real));

    call(table_fill, retain(p, x));
    call(table_process, retain(p, x));

    release(p, x);

[Back](/documentation)
