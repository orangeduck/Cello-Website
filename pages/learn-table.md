  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var prices = new(Table, String, Int);
    set(prices, $S("Apple"),  $I(12));
    set(prices, $S("Banana"), $I( 6));
    set(prices, $S("Pear"),   $I(55));
    
    foreach (key in prices) {
      var price = get(prices, key);
      println("Price of %$ is %$", key, price);
    }
    

__Manipulation__

    var t = new(Table, String, Int);
    set(t, $S("Hello"), $I(2));
    set(t, $S("There"), $I(5));
    
    show($I(len(t))); /* 2 */
    show($I(mem(t, $S("Hello")))); /* 1 */
    
    rem(t, $S("Hello"));
    
    show($I(len(t))); /* 1 */
    show($I(mem(t, $S("Hello")))); /* 0 */
    show($I(mem(t, $S("There")))); /* 1 */
    
    clear(t);
    
    show($I(len(t))); /* 0 */
    show($I(mem(t, $S("Hello")))); /* 0 */
    show($I(mem(t, $S("There")))); /* 0 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Table
__Hash table__

The `Table` type is a hash table data structure that maps keys to values. It uses an open-addressing robin-hood hashing scheme which requires `Hash` and `Cmp` to be defined on the key type. Keys and values are copied into the collection using the `Assign` class and intially have zero'd memory.

Hash tables provide `O(1)` lookup, insertion and removal can but require long pauses when the table must be _rehashed_ and all entries processed.

This is largely equivalent to the C++ construct [std::unordered_map](http://www.cplusplus.com/reference/unordered_map/unordered_map/)

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Clear](/learn/clear)</span>`clear` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Iter](/learn/iter)</span>`foreach` `iter_init` `iter_next` 
* <span style="width:75px; float:left;">[Len](/learn/len)</span>`len` 
* <span style="width:75px; float:left;">[Mark](/learn/mark)</span>`mark` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Reserve](/learn/reserve)</span>`reserve` 
* <span style="width:75px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 
* <span style="width:75px; float:left;">[Subtype](/learn/subtype)</span>`subtype` `key_subtype` `val_subtype` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
