AsChar
------
__Representable as C char__

The `AsChar` class allows a user to represent an object as a C `char`. It is used by the native type wrapper `Char`.


### Methods

-------------------------------

    char as_char(var self);

represent object as C `char`

* __Parameters__
    * `self` object to represent
* __Returns__ C `char` representation of object

------------------------------- 


### Signature


    class {
      char (*as_char)(var);
    } AsChar;
    

### Implementers

* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_


### See Also

* <span style="width:75px; float:left;">[AsStr](asstr)</span> _Representable as C char*_


### Examples

__Usage__

    putc(as_char($(Char, 'a'))); /* a */
    putc(as_char($(Char, 'b'))); /* b */
    

[Back](/documentation)
