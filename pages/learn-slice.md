  <div class="row">
  <div class="col-xs-6 col-md-6">

  </div>
  <div class="col-xs-6 col-md-6">

# Slice
__Partial Iterable__

The `Slice` type is an iterable that allows one to only iterate over certain items of another iterable. Given some start, stop and step only those entries described by the slice are returned in the iteration.

Under the hood the `Slice` object still iterates over the whole iterable but it only returns those values in the range. For this reason there is no performance benefit to slicing.

### Definition

    struct Slice { var iter; var range; };

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
