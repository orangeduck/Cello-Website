  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Starting & Stopping__

    var gc = current(GC);
    stop(gc);
    var x = new(Int, $I(10)); /* Not added to GC */
    show($I(running(gc))); /* 0 */
    del(x); /* Must be deleted when done */
    start(gc);
    



  </div>
  <div class="col-xs-6 col-md-6">

# GC
__Garbage Collector__

The `GC` type provides an interface to the Cello Garbage Collector. One instance of this class is created for each thread and can be retrieved using the `current` function. The Garbage Collector can be stopped and started using `start` and `stop` and objects can be added or removed from the Garbage Collector using `set` and `rem`.

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Current](/learn/current)</span>`current` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 
* <span style="width:75px; float:left;">[Start](/learn/start)</span>`with` `start` `stop` `wait` `running` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
