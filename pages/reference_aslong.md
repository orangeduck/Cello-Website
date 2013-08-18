AsLong
------
__Representable as C long__

The `AsLong` class allows a user to represent an object as a C `long`. It is used by the native type wrapper `Int`.


### Methods

-------------------------------

    long as_long(var self);

represent object as C `long`

* __Parameters__
    * `self` object to represent
* __Returns__ C `long` representation of object

------------------------------- 


### Signature


    class {
      long (*as_long)(var);
    } AsLong;
    

### Implementers

* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_
* <span style="width:75px; float:left;">[Thread](thread)</span> _Concurrent Processes_


### See Also

* <span style="width:75px; float:left;">[AsDouble](asdouble)</span> _Representable as C double_


### Examples

__Usage__

    printf("%li", as_long($(Int, 5)));    /* 5 */
    printf("%li", as_long($(Real, 5.6))); /* 5 */
    printf("%li", as_long($(Real, 5.5))); /* 5 */
    printf("%li", as_long($(Real, 5.4))); /* 5 */

[Back](/documentation)
