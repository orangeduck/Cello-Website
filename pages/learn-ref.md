  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var obj0 = $F(1.0), obj1 = $F(2.0);
    var r = $(Ref, obj0);
    show(r);
    show(deref(r)); /* 1.0 */
    ref(r, obj1);
    show(deref(r)); /* 2.0 */
    assign(r, obj0);
    show(deref(r)); /* 1.0 */
    

__Collections__

    var i0 = new(Int, $I(100));
    var i1 = new(Int, $I(200));
    var x = new(Array, Ref, i0, i1);
    
    print(deref(get(x, $I(0)))); /* 100 */
    del(x); /* Contents of `x` still alive */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Ref
__Shared Pointer__

The `Ref` type is a basic wrapper around a C pointer. It can be used as a type argument to collections to allow them to store generic types. It may also be useful in various circumstances where another level of indirection or mutability is required.

### Definition

    struct Ref { var val; };

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Pointer](/learn/pointer)</span>`ref` `deref` 
* <span style="width:75px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
