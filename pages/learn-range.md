  <div class="row">
  <div class="col-xs-6 col-md-6">

  </div>
  <div class="col-xs-6 col-md-6">

# Range
__A Sequence of Numbers__

The `Range` type is a basic iterable type which acts as a virtual sequence of numbers, starting from some value, stopping at some value and incrementing by some step.

This can be a useful replacement for the standard C `for` loop with decent performance but returning a wrapped integer. To range backwards `iter_prev` must be defined on the iterable object.

### Definition

    struct Range {
      var iter;
      int64_t start;
      int64_t stop;
      int64_t step;
    };
    

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Iter](/learn/iter)</span>`iter_init` `iter_next` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
