  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__subtype__

    var subtype(var self);

Returns the subtype of object `self`.

__key_subtype__

    var key_subtype(var self);

Returns the key subtype of object `self`.

__val_subtype__

    var val_subtype(var self);

Returns the value subtype of object `self`.

### Examples

__Usage__

    var x = new(Array, Int);
    show(subtype(x)); /* Int */
    var y = new(Table, String, Int);
    show(key_subtype(y)); /* String */
    show(val_subtype(y)); /* Int */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Subtype
__Contains elements of some Subtype__

The `Subtype` class can be used to find the type of elements contained within another class. For example if an `Array` of a particular type is created, this class can be used to find what type that was.

### Definition

    struct Subtype {
      var (*subtype)(var);
      var (*key_subtype)(var);
      var (*val_subtype)(var);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _Integer Sequence_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
