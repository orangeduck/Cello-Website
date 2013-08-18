Serialize
---------
__Convertible to Serial Form__

The `Serialize` class provides a way for objects to be serialized into and out of some stream. This functionality is pretty basic and for more important serialization tasks users are recommended to use more powerful libraries.

This class is used by the `put` and `get` methods on a `File` object.


### Methods

-------------------------------

    void serial_read(var self, var input);

serialize an object from a stream

* __Parameters__
    * `self` object to seralize into
    * `input` stream to read from
* __Returns__ None

------------------------------- 

    void serial_write(var self, var output);

serialize an object to a stream

* __Parameters__
    * `self` object to serialize from
    * `output` stream to write to
* __Returns__ None

------------------------------- 


### Signature


    class {
      void (*serial_read)(var,var);
      void (*serial_write)(var,var);
    } Serialize;
    

### Implementers

* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_


### See Also

* <span style="width:75px; float:left;">[Stream](stream)</span> _File-like_
* <span style="width:75px; float:left;">[Format](format)</span> _Read or Writable using a Format String_


### Examples

__Usage__

    var f = stream_open($(File, NULL), "test.bin", "w");
    
    serial_write(f, $(Int, 5));
    serial_write(f, $(Real, 2.0));
    
    stream_close(f);    

[Back](/documentation)
