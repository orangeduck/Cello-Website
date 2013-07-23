File
----

File is a wrapper of the native C file object. It supports the standard `read` and `write` commands as well as formatted printing which resembles the c command `sprintf`. Files also support serialization of objects via the [Dict](reference/dict) functions `get` and `put`.

The position of the cursor in the file stream is stored internally and as such the `pos` argument in formatted printing commands is unused.

### Implements



* <span style="width:75px; float:left;">[New](reference/new)</span> `new`, `delete`, `construct`, `destruct`
* <span style="width:75px; float:left;">[With](reference/with)</span> `with_enter`, `with_exit`
* <span style="width:75px; float:left;">[Stream](reference/stream)</span> `open`, `close`, `seek`, `tell`, `flush`, `eof`, `read`, `write`
* <span style="width:75px; float:left;">[Dict](reference/dict)</span> `get`, `put`
* <span style="width:75px; float:left;">[Format](reference/format)</span> `format_to`, `format_from`

### See Also

* <span style="width:75px; float:left;">[String](reference/string)</span> _Cello String Object_

### Examples

__Opening & Closing__
    
    var x = new(File, "test.bin", "wb");
  
    char* binary = "\0\1\1\1\1\1\0\0\0\0"
    write(x, binary, 10);
    
    delete(x);
    
__Formatted Printing__
    
    var x = $(File, None);
    open(x, "details.txt", "w");
    
    print_to(x, 0, "%$ is %$", $(String, "Dan"),   $(Int, 23));
    print_to(x, 0, "%$ is %$", $(String, "Chess"), $(Int, 24));
    
    close(x);
    
__Automatic Closing__
    
    with(f in open($(File, None), "details.txt", "r")) {
      
      var x = new(Int, 0);
      
      for (int i = 0; i < 100; i++) {
        scan_from(f, 0, "%i", x);
        show(x);
      }
      
      delete(x);
      
    }
    
    

