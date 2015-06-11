  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__clear__

    void clear(var self);

Clear the object `self`.

### Examples

__Usage__

    var x = new(Array, Int, $I(10), $I(20));
    show($I(len(x))); /* 2 */
    clear(x);
    show($I(len(x))); /* 0 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Clear
__Clearable__

The `Clear` class can be implemented when it makes sense to _clear_ an object, such as to remove all of the items from an `Array` or `Table`.

### Definition

    struct Clear {
      void (*clear)(var);
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
