  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__map__

    #define map(I, F)

Construct a `Map` object on the stack over iterable `I` applying function `F`.

### Examples

__Usage__

    var convert_to_int(var x) {
      var y = new(Int);
      look_from(y, x, 0);
      return y;
    }
    
    var x = tuple($S("1"), $S("2"), $S("3"));
    
    foreach (y in map(x, $(Function, convert_to_int))) {
      show(y); /* 1, 2, 3 */
    };
    

__Usage 2__

    var print_object(var x) {
      println("Object %$ is of type %$", x, type_of(x));
      return NULL;
    }
    
    var x = tuple($I(0), $S("Hello!"), $F(2.4));
    
    call(map(x, $(Function, print_object)));
    



  </div>
  <div class="col-xs-6 col-md-6">

# Map
__Apply Function to Iterable__

The `Map` type is an iterable that applies some callable to each item in another iterable and returns the result. This can be useful to make more concise iteration when there are callback functions available.

If the mapping callable is a purely side-effect callable it is possible to use the `call` function on the `Map` object directly for a quick way to perform the iteration.

One downside of `Map` is that the `iter_type` becomes unknown (there is no way to know what type the callable will return so some objects such as `Array`s may revert to using `Ref` as the object type when assigned a `Map`.

### Definition

    struct Map {
      var iter;
      var curr;
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

* <span style="width:50px; float:left;">[Call](/learn/call)</span>`call` 
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
