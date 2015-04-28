  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var s0 = $(String, "Hello");
    var s1 = new(String, $S("Hello"));
    append(s1, $S(" There"));
    show(s0); /* Hello */
    show(s1); /* Hello There */
    

__Manipulation__

    var s0 = new(String, $S("Balloons"));
    
    show($I(len(s0))); /* 8 */
    show($I(mem(s0, $S("Ball"))));     /* 1 */
    show($I(mem(s0, $S("oon"))));      /* 1 */
    show($I(mem(s0, $S("Balloons")))); /* 1 */
    show($I(mem(s0, $S("l"))));        /* 1 */
    
    rem(s0, $S("oons"));
    
    show($I(eq(s0, $S("Ball")))); /* 1 */
    
    clear(s0);
    
    show($I(len(s0))); /* 0 */
    show($I(eq(s0, $S("")))); /* 1 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# String
__String Object__

The `String` type is a wrapper around the native C string type. This includes strings that are allocated on either the Stack or the Heap.

For strings allocated on the heap a number of extra operations are provided overs standard C strings such as concatenation.

### Definition

    struct String { char* val; };

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[C_Str](/learn/c_str)</span>`c_str` 
* <span style="width:75px; float:left;">[Clear](/learn/clear)</span>`clear` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Concat](/learn/concat)</span>`append` `concat` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Format](/learn/format)</span>`format_to` `format_from` 
* <span style="width:75px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Len](/learn/len)</span>`len` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Reserve](/learn/reserve)</span>`reserve` 
* <span style="width:75px; float:left;">[Reverse](/learn/reverse)</span>`reverse` 
* <span style="width:75px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
