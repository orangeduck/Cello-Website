  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__show__

    int show(var self);
    int show_to(var self, var out, int pos);

Show the object `self` either to `stdout` or to the object `output`.

__look__

    int look(var self);
        int look_from(var self, var input, int pos);

Read the object `self` either from `stdout` or from the object `input`.

__print__

    #define print(fmt, ...)
    #define println(fmt, ...)
    #define print_to(out, pos, fmt, ...)
    int print_with(const char* fmt, var args);
    int println_with(const char* fmt, var args);
    int print_to_with(var out, int pos, const char* fmt, var args);

Print the format string `fmt` either to `stdout` or to the object `out` at positions `pos`.

__scan__

    #define scan(fmt, ...)
    #define scanln(fmt, ...)
    #define scan_from(input, pos, fmt, ...)
    int scan_with(const char* fmt, var args);
    int scanln_with(const char* fmt, var args);
    int scan_from_with(var input, int pos, const char* fmt, var args);

Scan the format string `fmt` either from `stdout` or from the object `input` at position `pos`.

### Examples

__Hello World__

    println("Hello %s!", $S("World"));
    

__File Writing__

    with(f in sopen($(File, NULL), $S("prices.txt"), $S("wb"))) {
      print_to(f, 0, "%$ :: %$\n", $S("Banana"), $I(57));
      print_to(f, 0, "%$ :: %$\n", $S("Apple"),  $I(22));
      print_to(f, 0, "%$ :: %$\n", $S("Pear"),   $I(16));
    }
    

__String Scanning__

    var input = $S("1 and 52 then 78");
    
    var i0 = $I(0), i1 = $I(0), i2 = $I(0);
    scan_from(input, 0, "%i and %i then %i", i0, i1, i2);
    
    /* i0: 1, i1: 52, i2: 78 */
    println("i0: %$, i1: %$, i2: %$", i0, i1, i2);
    

__String Printing__

    var greeting = new(String);
    print_to(greeting, 0, "Hello %s %s, %s?", 
      $S("Mr"), $S("Johnson"), $S("how are you?"));
    
    /* Hello Mr Johnson, how are you? */
    show(greeting);
    



  </div>
  <div class="col-xs-6 col-md-6">

# Show
__Convert To or From String__

The `Show` class is used to convert objects to, and from, a `String` representation. Objects which implement `Show` should expect the input/output object to be one that support the `Format` class, such as `File` or `String`.

The `print`, `println` and `print_to` functions provide a mechanism for writing formatted strings with Cello objects. To do this they provide a new format specifier `%$` which uses an object's `Show` functionality to write that part of the string. All objects which don't support `Show` can still be shown via a default implementation.

All the Show methods which are variable arguments only take `var` objects as input. To print native C types wrap them in Cello types using `$`.

Standard format specifiers such as `%f` and `%d` will call functions such as `c_float` and `c_int` on their passed arguments to convert objects to C types before performing the standard C formatting behaviour.

See `printf` for more information on format specifiers.

### Definition

    struct Show {
      int (*show)(var, var, int);
      int (*look)(var, var, int);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Float Point Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Stack Based Collection_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
