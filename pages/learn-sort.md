  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__sort__

    void sort(var self);

Sorts the object `self`.

__sort_by__

    void sort_by(var self, bool(*f)(var,var));

Sorts the object `self` using the function `f`.

### Examples

__Usage__

    var x = new(Array, Float, 
      $F(5.2), $F(7.1), $F(2.2));
    
    show(x); /* <'Array' At 0x00414603 [5.2, 7.1, 2.2]> */
    sort(x);
    show(x); /* <'Array' At 0x00414603 [2.2, 5.2, 7.1]> */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Sort
__Sortable__

The `Sort` class can be implemented by types which can be sorted in some way such as `Array`. By default the sorting function uses the `lt` method to compare elements, but a custom function can also be provided.

### Definition

    struct Sort {
      void (*sort_by)(var,bool(*f)(var,var));
    };

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
