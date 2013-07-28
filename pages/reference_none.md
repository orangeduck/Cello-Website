None
----
__Empty Value__

`None` is a direct alias of `False` and is used idomatically in Cello code to represent a NULL, Empty or Non-Value. As None is just an alias of `False` it will evaluate to false in `if` blocks.

`None` shouldn't be confused with `Undefined` - which is used instead to represent an Errorous or Unspecified value. For example putting `None` into a `List` is perfectly valid but `Undefined` is not.

Also provided is `Some`, an alias to `True`. This can be used idomatically to indicate a single unspecified value.


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

* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_


### Examples

__Usage__
    
    if (len(self) == 0) return None;

    var best = at(self, 0);
    foreach(item in self) {
        if_lt(item, best) {
            best = item;
        }
    }

    return best;

[Back](/documentation)
