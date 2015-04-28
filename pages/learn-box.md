  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var obj0 = $F(1.0), obj1 = $F(2.0);
    var r = $(Box, obj0);
    show(r);
    show(deref(r)); /* 1.0 */
    ref(r, obj1);
    show(deref(r)); /* 2.0 */
    assign(r, obj0);
    show(deref(r)); /* 1.0 */
    

__Lifetimes__

    var quote = $S("Life is long");
    
    with(r in $B(new(String, quote))) {
      println("This reference is: %$", r);
      println("This string is alive: '%s'", deref(r));
    }
    
    print("Now it has been cleared up!\n");
    

__Collection__

    /* Multiple Types in one Collection */
    var x = new(Array, Box, 
      new(String, $S("Hello")), 
      new(String, $S("There")), 
      new(Int, $I(10)));
    
    print(deref(get(x, $I(0)))); /* Hello */ 
    
    del(x); /* Contents of `x` deleted with it */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Box
__Unique Pointer__

The `Box` type is another wrapper around a C pointer with one additional behaviour as compared to `Ref`. When a `Box` object is deleted it will also call `del` on the object it points to. The means a `Box` is considered a pointer type that _owns_ the object it points to, and so is responsible for it's destruction. 

While this might not seem that useful when there is Garbage Collection this can be very useful when Garbage Collection is turned off, and when used in conjunction with collections.

### Definition

    struct Box { var val; };

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Pointer](/learn/pointer)</span>`ref` `deref` 
* <span style="width:75px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
