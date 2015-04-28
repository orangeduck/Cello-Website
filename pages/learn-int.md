  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var i0 = $(Int, 1);
    var i1 = new(Int, $I(24313));
    var i2 = copy(i0);
    
    show(i0); /*     1 */
    show(i1); /* 24313 */
    show(i2); /*     1 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Int
__Integer Object__

64-bit signed integer Object.

### Definition

    struct Int { int64_t val; };

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[C_Int](/learn/c_int)</span>`c_int` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
