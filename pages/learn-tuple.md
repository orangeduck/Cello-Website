  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__tuple__

    #define tuple(...)

Construct a `Tuple` object on the stack.

### Examples

__Usage__

    var x = tuple($I(100), $I(200), $S("Hello"));
    show(x);
    var y = tuple(Int, $I(10), $I(20));
    var z = new_with(Array, y);
    show(z);
    
    foreach (item in x) {
      println("%$", item);
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# Tuple
__Basic Collection__

The `Tuple` type provides a basic way to create a simple collection of objects. Its main use is the fact that it can be constructed on the stack using the `tuple` macro. This makes it suitable for a number of purposes such as use in functions that take a variable number of arguments.

Tuples can also be constructed on the heap and stored in collections. This makes them also useful as a simple _untyped_ list of objects.

Internally Tuples are just an array of pointers terminated with a pointer to the Cello `Terminal` object. This makes positional access fast, but many other operations slow including iteration and counting the number of elements. Due to this it is only recommended Tuples are used for small collections. 

Because Tuples are terminated with the Cello `Terminal` object this can't naturally be included within them. This object should therefore only be returned from iteration functions.

### Definition

    struct Tuple {
      var* items;
    };
    

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Concat](/learn/concat)</span>`append` `concat` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` `key_type` `val_type` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Iter](/learn/iter)</span>`foreach` `iter_init` `iter_next` `iter_type` 
* <span style="width:50px; float:left;">[Len](/learn/len)</span>`len` 
* <span style="width:50px; float:left;">[Mark](/learn/mark)</span>`mark` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Push](/learn/push)</span>`push` `pop` `push_at` `pop_at` 
* <span style="width:50px; float:left;">[Resize](/learn/resize)</span>`resize` 
* <span style="width:50px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 
* <span style="width:50px; float:left;">[Sort](/learn/sort)</span>`sort` `sort_by` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
