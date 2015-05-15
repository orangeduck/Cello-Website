  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__format_to__

    int format_to(var self, int pos, const char* fmt, ...);
    int format_to_va(var self, int pos, const char* fmt, va_list va);

Write a formatted string `fmt` to the object `self` at position `pos`.

__format_from__

    int format_from(var self, int pos, const char* fmt, ...);
    int format_from_va(var self, int pos, const char* fmt, va_list va);

Read a formatted string `fmt` from the object `self` at position `pos`.

### Examples

__Usage__

    /* printf("Hello my name is %s, I'm %i\n", "Dan", 23); */
    format_to($(File, stdout), 0, 
      "Hello my name is %s, I'm %i\n", "Dan", 23);
    



  </div>
  <div class="col-xs-6 col-md-6">

# Format
__Read or Write with Format String__

Format abstracts the class of operations such as `scanf`, `sprintf` and `fprintf` with matching semantics. It provides general `printf` and `scanf` functionality for several different types objects in a uniform way. This class is essentially an inbetween class, used by the `Show` class to read and write output.

It is important to note that the semantics of these operations match `printf` and not the newly defined `Show` class. For example it is perfectly valid to pass a C `int` to these functions, while the `println` function from `Show` must be passed only `var` objects.

### Definition

    struct Format {
      int (*format_to)(var,int,const char*,va_list);
      int (*format_from)(var,int,const char*,va_list);
    };
    

### Implementers

* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
