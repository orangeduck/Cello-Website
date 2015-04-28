  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var x = new(Process, $S("ls"), $S("r"));
    var o = new(String);
    scan_from(x, 0, "%s", o);
    show(o);
    sclose(x);
    



  </div>
  <div class="col-xs-6 col-md-6">

# Process
__Operating System Process__

The `Process` type is a wrapper for an operating system process as constructed by the unix-like call `popen`. In this sense it is much like a standard file in the operating system but that instead of writing data to a location you are writing it as input to a process.

### Definition

    struct Process { FILE* proc; };

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Format](/learn/format)</span>`format_to` `format_from` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Start](/learn/start)</span>`start` `stop` `running` 
* <span style="width:75px; float:left;">[Stream](/learn/stream)</span>`sopen` `sclose` `sseek` `stell` `sflush` `seof` `sread` `swrite` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
