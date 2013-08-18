AsStr
-----
__Representable as C char*__

The `AsStr` class allows a user to represent an object as a C `char*`. It is used by the native type wrapper `String`.


### Methods

-------------------------------

    const char* as_str(var self);

represent object as C `char*`

* __Parameters__
    * `self` object to represent
* __Returns__ C `char*` representation of object

------------------------------- 


### Signature


    class {
      const char* (*as_str)(var);
    } AsStr;
    

### Implementers

* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_
* <span style="width:75px; float:left;">[Type](type)</span> _Metadata Type Object_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[AsChar](aschar)</span> _Representable as C char_


### Examples

__Usage__

    puts(as_str($(String, "Hello"))); /* Hello */
    puts(as_str($(String, "There"))); /* There */
    

[Back](/documentation)
