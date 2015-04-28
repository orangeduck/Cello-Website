  <div class="row">
  <div class="col-xs-6 col-md-6">

  </div>
  <div class="col-xs-6 col-md-6">

# Function
__Function Object__

The `Function` type allows C function pointers to be treated as Cello objects. They can be passed around, stored, and manipulated. Only C functions of the type `var(*)(var)` can be stored as a `Function` type and when called the arguments will be wrapped into an iterable and passed as the first argument, typically in the form of a `tuple`.

### Definition

    struct Function { var(*func)(var); };

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Call](/learn/call)</span>`call` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
