  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__push__

    void push(var self, var obj);

Push the object `obj` onto the top of object `self`.

__pop__

    void pop(var self);

Pop the top item from the object `self`.

__push_at__

    void push_at(var self, var obj, var key);

Push the object `obj` onto the object `self` at a given `key`.

__pop_at__

    void pop_at(var self, var key);

Pop the object from the object `self` at a given `key`.

### Examples

__Usage__

    var x = new(Array, Int);
    
    push(x, $I( 0));
    push(x, $I( 5));
    push(x, $I(10));
    
    show(get(x, $I(0))); /*  0 */
    show(get(x, $I(1))); /*  5 */
    show(get(x, $I(2))); /* 10 */
    
    pop_at(x, $I(1));
    
    show(get(x, $I(0))); /*  0 */
    show(get(x, $I(1))); /* 10 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Push
__Pushable and Popable object__

The `Push` class provides an interface for the addition and removal of objects from another in a positional sense.

`push` can be used to add new objects to a collection and `pop` to remove them. Usage of `push` can require `assign` to be defined on the argument.

### Definition

    struct Push {
      void (*push)(var, var);
      void (*pop)(var);
      void (*push_at)(var, var, var);
      void (*pop_at)(var, var);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
