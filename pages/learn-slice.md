  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__slice__

    #define slice(I, ...)

Construct a `Slice` object on the stack over iterable `I`.

__reverse__

    #define reversed(I)Construct a `Slice` object that iterates over iterable `I` in reverse order.

(null)

### Examples

__Usage__

    var x = tuple(
      $S("Hello"), $S("There"), $S("World"), $S("!"));
    
    /* Iterate over elements 0 to 2 */
    foreach (s in slice(x, $I(2))) {
      print("%s\n", s);
    }
    
    /* Iterate over elements 1 to 2 */
    foreach (s in slice(x, $I(1), $I(2))) {
      print("%s\n", s);
    }
    
    /* Iterate over every other element */
    foreach (s in slice(x, _, _, $I(2))) {
      print("%s\n", s);
    }
    
    /* Iterate backwards, starting from element 3 */
    foreach (s in slice(x, _, $I(2), $I(-1))) {
      print("%s\n", s);
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# Slice
__Partial Iterable__

The `Slice` type is an iterable that allows one to only iterate over part of another iterable. Given some start, stop and step, only those entries described by the `Slice` are returned in the iteration.

Under the hood the `Slice` object still iterates over the whole iterable but it only returns those values in the range given.

### Definition

    struct Slice {
      var iter;
      var range;
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
