  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__range__

    #define range(...)

Construct a `Range` object on the stack.

### Examples

__Usage__

    /* Iterate 0 to 10 */
    foreach (i in range($I(10))) {
      print("%i\n", i);
    }
    
    /* Iterate 10 to 20 */
    foreach (i in range($I(10), $I(20))) {
      print("%i\n", i);
    }
    
    /* Iterate 10 to 20 with a step of 5 */
    foreach (i in range($I(10), $I(20), $I(5))) {
      print("%i\n", i);
    }
    
    /* Iterate 20 to 10 */
    foreach (i in range($I(10), $I(20), $I(-1))) {
      print("%i\n", i);
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# Range
__Integer Sequence__

The `Range` type is a basic iterable which acts as a virtual sequence of integers, starting from some value, stopping at some value and incrementing by some step.

This can be a useful replacement for the standard C `for` loop with decent performance but returning a Cello `Int`. It is constructable on the stack with the `range` macro which makes it practical and easy to use.

### Definition

    struct Range {
      var value;
      int64_t start;
      int64_t stop;
      int64_t step;
    };
    

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
* <span style="width:50px; float:left;">[Swap](/learn/swap)</span>`swap` 
### Implements

* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` `key_type` `val_type` 
* <span style="width:50px; float:left;">[Iter](/learn/iter)</span>`foreach` `iter_init` `iter_next` `iter_type` 
* <span style="width:50px; float:left;">[Len](/learn/len)</span>`len` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
