  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__len__

    size_t len(var self);

Returns the length of object `self`.

### Examples

__Usage__

    var x = new(Array, Int, $I(1), $I(2), $I(5));
    show($I(len(x))); /* 3 */
    var y = $S("Test");
    show($I(len(y))); /* 4 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Len
__Has a length__

The `Len` class can be implemented by any type that has a length associated with it. It is typically implemented by collections and is often used in conjunction with `Iter` or `Get`.

### Definition

    struct Len {
      size_t (*len)(var);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Exception](/learn/exception)</span> | &nbsp; &nbsp;   _Exception Object_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Apply Function to Iterable_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _Integer Sequence_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Tree](/learn/tree)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_
* <span class="docitem">[Zip](/learn/zip)</span> | &nbsp; &nbsp;   _Multiple Iterator_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
