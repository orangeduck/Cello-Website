  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var prices = new(Tree, String, Int);
    set(prices, $S("Apple"),  $I(12));
    set(prices, $S("Banana"), $I( 6));
    set(prices, $S("Pear"),   $I(55));
    
    foreach (key in prices) {
      var price = get(prices, key);
      println("Price of %$ is %$", key, price);
    }
    

__Manipulation__

    var t = new(Tree, String, Int);
    set(t, $S("Hello"), $I(2));
    set(t, $S("There"), $I(5));
    
    show($I(len(t))); /* 2 */
    show($I(mem(t, $S("Hello")))); /* 1 */
    
    rem(t, $S("Hello"));
    
    show($I(len(t))); /* 1 */
    show($I(mem(t, $S("Hello")))); /* 0 */
    show($I(mem(t, $S("There")))); /* 1 */
    
    resize(t, 0);
    
    show($I(len(t))); /* 0 */
    show($I(mem(t, $S("Hello")))); /* 0 */
    show($I(mem(t, $S("There")))); /* 0 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Tree
__Balanced Binary Tree__

The `Tree` type is a self balancing binary tree implemented as a red-black tree. It provides key-value access and requires the `Cmp` class to be defined on the key type.

Element lookup and insertion are provided as an `O(log(n))` operation. This means in general a `Tree` is slower than a `Table` but it has several other nice properties such as being able to iterate over the items in order and not having large pauses for rehashing on some insertions.

This is largely equivalent to the C++ construct [std::map](http://www.cplusplus.com/reference/map/map/)

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
* <span style="width:50px; float:left;">[Swap](/learn/swap)</span>`swap` 
### Implements

* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` `key_type` `val_type` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Iter](/learn/iter)</span>`foreach` `iter_init` `iter_next` `iter_type` 
* <span style="width:50px; float:left;">[Len](/learn/len)</span>`len` 
* <span style="width:50px; float:left;">[Mark](/learn/mark)</span>`mark` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Resize](/learn/resize)</span>`resize` 
* <span style="width:50px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
