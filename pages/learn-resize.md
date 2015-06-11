  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__resize__

    void resize(var self, size_t n);

Resize to some size `n`, perhaps reserving some resource for object `self`.

### Examples

__Usage__

    var x = new(Array, Int);
    resize(x, 10000); /* Reserve space in Array */ 
    for (size_t i = 0; i < 10000; i++) {
      push(x, $I(i));
    }
    

__Usage 2__

    var x = new(Array, Int, $I(0), $I(1), $I(2));
    resize(x, 0); /* Clear Array of items */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Resize
__Object can be resized__

The `Resize` class can be implemented by objects which can be resized in some way. Resizing to a larger size than the current may allow for some resource or other to be preallocated or reserved. For example this class is implemented by `Array` and `Table` to either remove a number of items quickly or to preallocate memory space if it is known that many items are going to be added at a later date.

### Definition

    struct Resize {
      void (*resize)(var, size_t);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Tree](/learn/tree)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
