  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__ref__

    void ref(var self, var item);

Set the object `self` to reference the object `item`.

__deref__

    var deref(var self);

Get the object referenced by `self`.

### Examples

__Usage__

    var obj0 = $F(1.0), obj1 = $F(2.0);
    var r = $(Ref, obj0);
    show(r);
    show(deref(r)); /* 1.0 */
    ref(r, obj1);
    show(deref(r)); /* 2.0 */
    assign(r, obj0);
    show(deref(r)); /* 1.0 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Pointer
__Reference to other object__

The `Pointer` class is implemented by types which act as references to other objects. Primarily this class is implemented by `Ref` and `Box` which provide the two main pointer types in Cello.

### Definition

    struct Pointer {
      void (*ref)(var, var);
      var (*deref)(var);
    };
    

### Implementers

* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
