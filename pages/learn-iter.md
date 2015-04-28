  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__iter_init__

    var iter_init(var self);
    var iter_last(var self);

Return the initial item (or final item) in the iteration over `self`.

__iter_next__

    var iter_next(var self, var curr);
    var iter_prev(var self, var curr);

Given the current item `curr`, return the next (or previous) item in the iteration over `self`.

### Examples

__Usage__

    var x = new(Array, Int, $I(1), $I(2), $I(5));
    
    foreach(o in x) {
      show(o); /* 1, 2, 5 */
    }
    

__Table__

    var prices = new(Table, String, Int);
    set(prices, $S("Apple"),  $I(12));
    set(prices, $S("Banana"), $I( 6));
    set(prices, $S("Pear"),   $I(55));
    
    foreach(key in prices) {
      var price = get(prices, key);
      print("Price of %$ is %$\n", key, price);
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# Iter
__Can be looped over__

The `Iter` class is implemented by types which can be looped over. This allows them to be used in conjunction with the `foreach` macro as well as various other components of Cello.

### Definition

    struct Iter {
      var (*iter_init)(var);
      var (*iter_next)(var, var);
      var (*iter_prev)(var, var);
      var (*iter_last)(var);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _A Sequence of Numbers_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Stack Based Collection_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
