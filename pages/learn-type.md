  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var t = type_of($I(5));
    show(t); /* Int */
    
    show($I(type_implements(t, New))); /* 1 */
    show($I(type_implements(t, Cmp)));  /* 1 */
    show($I(type_implements(t, Hash))); /* 1 */
    
    show($I(type_method(t, Cmp, cmp, $I(5), $I(6)))); /* -1 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Type
__Metadata Object__

The `Type` type is one of the most important types in Cello. It is the object which specifies the meta-data associated with a particular object most importantly this says what classes an object implements and what their instances are.

One can get the type of an object using the `type_of` function.

To see if an object implements a class `implements` can be used. To call a member of a class with an object `method` can be used.

To see if a type implements a class `type_implements` can be used. To call a member of a class, implemented `type_method` can be used.

### Derives

* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[C_Str](/learn/c_str)</span>`c_str` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Help](/learn/help)</span>`help` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
