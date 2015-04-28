  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__reserve__

    void reserve(var self, var amount);

Reserve some `amount` of resource for object `self`.

### Examples

__Usage__

    var x = new(Array, Int);
    reserve(x, $I(10000)); /* Reserve space in Array */ 
    for (size_t i = 0; i < 10000; i++) {
      push(x, $I(i));
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# Reserve
__Resources can be Preallocated__

The `Reserve` class can be implemented by objects which allow for some resource or other to be preallocated or reserved. For example this class is implemented by `Array` and `Table` to preallocate memory space if it is known that many items are going to be added at a later date.

### Definition

    struct Reserve {
      void (*reserve)(var, var);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
