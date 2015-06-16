  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__filter__

    #define filter(I, F)

Construct a `Filter` object on the stack over iterable `I` with filter function `F`.

### Examples

__Usage__

    var greater_than_two(var x) {
      return c_int(x) > 2 ? x : NULL;
    }
    
    var x = new(Array, Int, $I(0), $I(5), $I(2), $I(9));
    
    foreach (n in filter(x, $(Function, greater_than_two))) {
      show(n); /* 5, 9 */
    }
    

__Usage 2__

    var mem_hello(var x) {
      return mem(x, $S("Hello")) ? x : NULL;
    }
    
    var x = new(Tuple, 
      $S("Hello World"), $S("Hello Dan"), 
      $S("Bonjour"));
    
    var y = new(Tuple);
    assign(y, filter(x, $(Function, mem_hello)));
    show(y); /* tuple("Hello World", "Hello Dan") */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Filter
__Filtered Iterable__

The `Filter` type can be used to filter the results of some iterable. Given a callable object `Filter` iterable returns only those items in the original iterable for where calling the function returns a non-`NULL` value.

### Definition

    struct Filter {
      var iter;
      var func;
    };
    

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
* <span style="width:50px; float:left;">[Swap](/learn/swap)</span>`swap` 
### Implements

* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` `key_type` `val_type` 
* <span style="width:50px; float:left;">[Iter](/learn/iter)</span>`foreach` `iter_init` `iter_next` `iter_type` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
