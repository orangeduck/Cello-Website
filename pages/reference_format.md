Format
------
__Read or Writable using a Format String__

Format abstracts the class of operations such as `scanf`, `sprintf` and `fprintf` with matching semantics. It provides general `printf` and `scanf` functionality for several different types objects in a homogenius way. This class is used by the `Show` functions to write output.

It is important to note that the semantics of these options match `printf` and not the newly defined `Show` class. For example it is perfectly valid to pass a C `int` to these functions, while that would crash the `println` function from Show which must be passed only `var` objects. 


### Methods

-------------------------------

    int format_to(var self, int pos, const char* fmt, ...);
    int format_to_va(var self, int pos, const char* fmt, va_list va);

Write a formatted string to an object from some values

* __Parameters__
    * `self` Object to Format to
    * `pos` Position in Stream
    * `fmt` Format String
    * `...` List of values to be formatted
* __Returns__ number of characters written

------------------------------- 

    int format_from(var self, int pos, const char* fmt, ...);
    int format_from_va(var self, int pos, const char* fmt, va_list va);

Read a formatted string from an object into some values

* __Parameters__
    * `self` Object to Format From
    * `pos` Position in Stream
    * `fmt` Format String
    * `...` List of values to be formatted into
* __Returns__ number of arguments scanned

------------------------------- 


### Signature


    class {
      int (*format_to)(var,int,const char*,va_list);
      int (*format_from)(var,int,const char*,va_list);
    } Format;
    

### Implementers

* <span style="width:75px; float:left;">[File](file)</span> _Operating System File_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Show](show)</span> _Write To or Read From String_
* <span style="width:75px; float:left;">[Stream](stream)</span> _File-like_


### Examples

__Usage__
    
    /* printf("Hello my name is %s, I am %i\n", "Dan", 23); */
    format_to($(File, stdout), 0, "Hello my name is %s, I am %i\n", "Dan", 23);
    

[Back](/documentation)
