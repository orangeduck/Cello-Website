  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Construction & Deletion__

    var x = new(Array, Int);
    push(x, $I(32));
    push(x, $I(6));
    
    /* <'Array' At 0x0000000000414603 [32, 6]> */
    show(x);
    

__Element Access__

    var x = new(Array, Float, $F(0.01), $F(5.12));
    
    show(get(x, $I(0))); /* 0.01 */
    show(get(x, $I(1))); /* 5.12 */
    
    set(x, $I(0), $F(500.1));
    show(get(x, $I(0))); /* 500.1 */
    

__Membership__

    var x = new(Array, Int, $I(1), $I(2), $I(3), $I(4));
    
    show($I(mem(x, $I(1)))); /* 1 */
    show($I(len(x)));        /* 4 */
    
    rem(x, $I(3));
    
    show($I(mem(x, $I(3)))); /* 0 */
    show($I(len(x)));        /* 3 */
    show($I(empty(x)));      /* 0 */
    
    clear(x);
    
    show($I(empty(x)));      /* 1 */
    

__Iteration__

    var greetings = new(Array, String, 
      $S("Hello"), $S("Bonjour"), $S("Hej"));
    
    foreach(greet in greetings) {
      show(greet);
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# Array
__Sequential Container__

Array is data structure containing a sequence of a single type of object. It can dynamically grow and shrink in size depending on how many elements it contains. It allocates storage for the type specified. It also deallocates and destroys the objects inside upon destruction.

Elements are copied into an Array using `assign` and will initially have zero'd memory.

Elements are ordered linearly. Elements are accessed by their position in this sequence directly. Addition and removal of elements at the end of the sequence is fast, with memory movement required for elements in the middle of the sequence.

This is largely equivalent to the C++ construct [std::vector](http://www.cplusplus.com/reference/vector/vector/)

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Clear](/learn/clear)</span>`clear` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Concat](/learn/concat)</span>`append` `concat` 
* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Iter](/learn/iter)</span>`iter_init` `iter_next` 
* <span style="width:75px; float:left;">[Len](/learn/len)</span>`len` 
* <span style="width:75px; float:left;">[Mark](/learn/mark)</span>`mark` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Push](/learn/push)</span>`push` `pop` `push_at` `pop_at` 
* <span style="width:75px; float:left;">[Reserve](/learn/reserve)</span>`reserve` 
* <span style="width:75px; float:left;">[Reverse](/learn/reverse)</span>`reverse` 
* <span style="width:75px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 
* <span style="width:75px; float:left;">[Sort](/learn/sort)</span>`sort` `sort_by` 
* <span style="width:75px; float:left;">[Subtype](/learn/subtype)</span>`subtype` `key_subtype` `val_subtype` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
