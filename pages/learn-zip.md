  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__zip__

    #define zip(...)

Construct a `Zip` object on the stack.

__enumerate__

    #define enumerate(I)

Zip the iterable `I` with a `Range` object of the same length.

### Examples

__Usage__

    /* Iterate over two iterables at once */
    var x = new(Array, Int, $I(100), $I(200), $I(130));
    var y = new(Array, Float, $F(0.1), $F(0.2), $F(1.3));
    foreach (pair in zip(x, y)) {
      print("x: %$\n", get(pair, $I(0)));
      print("y: %$\n", get(pair, $I(1)));
    }
    
    /* Iterate over iterable with count */
    foreach (pair in enumerate(x)) {
      print("%i: %$\n", get(pair, $I(0)), get(pair, $I(1)));
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# Zip
__Multiple Iterator__

The `Zip` type can be used to combine multiple iterables into one which is then iterated over all at once and returned as a Tuple. The Zip object only iterates when all of it's sub iterators have valid items. More specifically the Zip iteration will terminate if _any_ of the sub iterators terminate.

### Definition

    struct Zip {
      var iters;
      var values;
    };
    

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
* <span style="width:50px; float:left;">[Swap](/learn/swap)</span>`swap` 
### Implements

* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` `key_type` `val_type` 
* <span style="width:50px; float:left;">[Iter](/learn/iter)</span>`foreach` `iter_init` `iter_next` `iter_type` 
* <span style="width:50px; float:left;">[Len](/learn/len)</span>`len` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
