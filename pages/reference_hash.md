Hash
----
__Hashable to a long__

The `Hash` class provides a way to convert an object into a long integer value. This value must remain the same for objects which are equal but should be evenly distributed for objects which are not equal.

A default implementation of `Hash` is provided for all type using the memory location cast to a long integer.

This is used by the Hashtable like objects such as `Table` and `Dictionary`.


### Methods

-------------------------------

    long hash(var obj);

Hash an object to a long integer value.

* __Parameters__
    * `self` Object
* __Returns__ Object Hash

------------------------------- 


### Signature


    class {
      long (*hash)(var);
    } Hash;    
    

### Implementers

* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Reference](reference)</span> _Basic Reference Type_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[AsLong](aslong)</span> _Representable as C long_


### Examples

__Usage__

    long x = hash($(Int, 1  )); /* 1   */
    long y = hash($(Int, 123)); /* 123 */
    long z = hash($(Int, 123)); /* 123 */
    
    long a = hash($(String, "Hello"));  /* 511 */
    long b = hash($(String, "There"));  /* 515 */
    long c = hash($(String, "People")); /* 629 */

[Back](/documentation)
