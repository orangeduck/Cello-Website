Show
----
__Write To or Read From String__

Show is the standard class used to convert objects to, and from, a String representation. Objects which implement show should expect the input/output object to support the `Format` class.

The `print`, `println` and `print_to` functions provide a mechanism for writing formatted strings. To do this they provide a new format specifier `%$` which uses an object's `Show` functionality to write to String. All objects which don't support `Show` can still be shown via a default implementation. 

All the `Show` methods which are variable arguments should only be passed `var` type objects and should never be passed native C types. To print native C types wrap them in Cello types using `$` (see examples below).

Standard format specifiers such as `%f` and `%d` will call functions such as `as_double` and `as_long` on their passed in arguments to convert to a C type before performing the standard C formatting behaviour.

See [printf](http://www.cplusplus.com/reference/cstdio/printf/) for more information on format specifiers.


### Methods

-------------------------------

    int show(var self);
    int show_to(var self, var out, int pos);

Writes an Object

* __Parameters__
    * `self` Object to write as String
    * `out` Format object to write to. For `show` this is `stdout`
    * `pos` Position in output object
* __Returns__ Updated Position in output object

------------------------------- 

    int print(const char* fmt, ...);
    int println(const char* fmt, ...);
    int print_to(var out, int pos, const char* fmt, ...);
    int print_va(const char* fmt, va_list va);
    int print_to_va(var out, int pos, const char* fmt, va_list va);

Use a format string to write several objects

* __Parameters__
    * `out` Format object to write to. For `print`, `println` and `print_va` this is `stdout`
    * `fmt` Format string
    * `pos` Position in output object
    * `...` Objects used in format string
* __Returns__ Updated Position in output object

------------------------------- 

    int look(var self);
    int look_from(var self, var input, int pos);

Reads an Object

* __Parameters__
    * `self` Object to read into
    * `out` Format object to read from. For `look` this is `stdout`
    * `pos` Position in input object
* __Returns__ Updated Position in input object

------------------------------- 

    int scan(const char* fmt, ...);
    int scanln(const char* fmt, ...);
    int scan_from(var input, int pos, const char* fmt, ...);
    int scan_va(const char* fmt, va_list va);
    int scan_from_va(var input, int pos, const char* fmt, va_list va);

Use a format string to read several objects

* __Parameters__
    * `input` Format object to write to. For `scan`, scanln` and `scan_va` this is `stdout`
    * `fmt` Format string
    * `pos` Position in input object
    * `...` Objects read from format string
* __Returns__ Updated Position in input object

------------------------------- 


### Signature


    class {
      int (*show)(var,var,int);
      int (*look)(var,var,int);
    } Show;
    

### Implementers

* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Reference](reference)</span> _Basic Reference Type_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_
* <span style="width:75px; float:left;">[Type](type)</span> _Metadata Type Object_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Format](format)</span> _Read or Writable using a Format String_
* <span style="width:75px; float:left;">[Stream](stream)</span> _File-like_


### Examples

__Hello World__
    
    println("Hello %s!", $(String, "World"));
    
__File Writing__

    with(file in stream_open($(File, NULL), "prices.txt", "wb")) {
  
        print_to(file, 0, "%$ :: %$\n", $(String, "Banana"), $(Int, 57));
        print_to(file, 0, "%$ :: %$\n", $(String, "Apple"),  $(Int, 22));
        print_to(file, 0, "%$ :: %$\n", $(String, "Pear"),   $(Int, 16));
        
        return None;
    };

    
__String Scanning__
    
    var input = $(String, "1 and 52 then 78");
    
    var i0 = new(Int, 0);
    var i1 = new(Int, 0);
    var i2 = new(Int, 0);
    
    scan_from(input, 0, "%i and %i then %i", i0, i1, i2);
    
    /* i0: 1, i1: 52, i2: 78 */
    println("i0: %$, i1: %$, i2: %$", i0, i1, i2);
    
__String Writing__

    var greeting = new(String, "");
    print_to(greeting, 0, "Hello %s %s, %s?", $(String, "Mr"), $(String, "Johnson"), $(String, "how are you?"));
    
    /* Hello Mr Johnson, how are you? */
    show(greeting);
    

[Back](/documentation)
