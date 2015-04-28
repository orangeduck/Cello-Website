  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__reverse__

    void reverse(var self);

The order of the object `self` is reversed.

### Examples

__Usage__

    var x = new(Array, Float, 
      $F(5.2), $F(7.1), $F(2.2), $F(1.1));
    
    show(x); /* <'Array' At 0x0000000000414603 [5.2, 7.1, 2.2, 1.1]> */
    reverse(x);
    show(x); /* <'Array' At 0x0000000000414603 [1.1, 2.2, 7.1, 5.2]> */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Reverse
__Order can be reversed__

The `Reverse` class can be implemented by types which are reversible in some way such as `Array`.

### Definition

    struct Reverse {
      void (*reverse)(var);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Stack Based Collection_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
