  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var x = new(File, $S("test.bin"), $S("wb"));
    char* data = "hello";
    swrite(x, data, strlen(data));
    sclose(x);
    

__Formatted Printing__

    var x = $(File, NULL);
    sopen(x, $S("test.txt"), $S("w"));
    print_to(x, 0, "%$ is %$ ", $S("Dan"), $I(23));
    print_to(x, 0, "%$ is %$ ", $S("Chess"), $I(24));
    sclose(x);
    

__Automatic Closing__

    with(f in new(File, $S("test.txt"), $S("r"))) {
      var k = new(String); resize(k, 100);
      var v = new(Int, $I(0));
      foreach (i in range($I(2))) {
        scan_from(f, 0, "%$ is %$ ", k, v);
        show(k); show(v);
      }
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# File
__Operating System File__

The `File` type is a wrapper of the native C `FILE` type representing a file in the operating system.

### Definition

    struct File {
      FILE* file;
    };
    

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Format](/learn/format)</span>`format_to` `format_from` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Start](/learn/start)</span>`with` `start` `stop` `wait` `running` 
* <span style="width:50px; float:left;">[Stream](/learn/stream)</span>`sopen` `sclose` `sseek` `stell` `sflush` `seof` `sread` `swrite` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
