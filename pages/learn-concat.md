  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__append__

    void append(var self, var obj);

Append the object `obj` to the object `self`.

__concat__

    void concat(var self, var obj);

Concatenate the object `obj` to the object `self`.

### Examples

__Usage__

    var x = new(Array, Float, $F(9.9), $F(2.8));
    var y = new(Array, Float, $F(1.1), $F(6.5));
    
    show(x); /* <'Array' At 0x00414603 [9.9, 2.8]> */
    show(y); /* <'Array' At 0x00414603 [1.1, 6.5]> */
    append(x, $F(2.5));
    show(x); /* <'Array' At 0x00414603 [9.9, 2.8, 2.5]> */
    concat(x, y);
    show(x); /* <'Array' At 0x00414603 [9.9, 2.8, 2.5, 1.1, 6.5]> */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Concat
__Concatenate Objects__

The `Concat` class is implemented by objects that can have other objects either _appended_ to their, on _concatenated_ to them. For example collections or strings.

### Definition

    struct Concat {
      void (*concat)(var, var);
      void (*append)(var, var);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
