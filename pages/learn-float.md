  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var f0 = $(Float, 1.0);
    var f1 = new(Float, $F(24.313));
    var f2 = copy(f0);
    
    show(f0); /*  1.000 */
    show(f1); /* 24.313 */
    show(f2); /*  1.000 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Float
__Floating Point Object__

64-bit double precision float point Object.

### Definition

    struct Float {
      double val;
    };
    

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[C_Float](/learn/c_float)</span>`c_float` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
