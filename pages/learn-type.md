  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__type_of__

    var type_of(var self);

Returns the `Type` of an object `self`.

__instance__

    var instance(var self, var cls);
    var type_instance(var type, var cls);

Returns the instance of class `cls` implemented by object `self` or type `type`. If class is not implemented then returns `NULL`.

__implements__

    bool implements(var self, var cls);
    bool type_implements(var type, var cls);

Returns if the object `self` or type `type` implements the class `cls`.

__method__

    #define method(X, C, M, ...)
    #define type_method(T, C, M, ...)

Returns the result of the call to method `M` of class `C` for object `X`or type `T`. If class is not implemented then an error is thrown.

__implements_method__

    #define implements_method(X, C, M)
    #define type_implements_method(T, C, M)

Returns if the type `T` or object `X` implements the method `M` of class C.

### Examples

__Usage__

    var t = type_of($I(5));
    show(t); /* Int */
    
    show($I(type_implements(t, New)));  /* 1 */
    show($I(type_implements(t, Cmp)));  /* 1 */
    show($I(type_implements(t, Hash))); /* 1 */
    
    show($I(type_method(t, Cmp, cmp, $I(5), $I(6))));
    



  </div>
  <div class="col-xs-6 col-md-6">

# Type
__Metadata Object__

The `Type` type is one of the most important types in Cello. It is the object which specifies the meta-data associated with a particular object. Most importantly this says what classes an object implements and what their instances are.

One can get the type of an object using the `type_of` function.

To see if an object implements a class `implements` can be used. To call a member of a class with an object `method` can be used.

To see if a type implements a class `type_implements` can be used. To call a member of a class, implemented `type_method` can be used.

### Derives

* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
* <span style="width:50px; float:left;">[Swap](/learn/swap)</span>`swap` 
### Implements

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[C_Str](/learn/c_str)</span>`c_str` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Help](/learn/help)</span>`help` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
