  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__get__

    var get(var self, var key);

Get the value at a given `key` for object `self`.

__set__

    void set(var self, var key, var val);

Set the value at a given `key` for object `self`.

__mem__

    bool mem(var self, var key);

Returns true if `key` is a member of the object `self`.

__rem__

    void rem(var self, var key);

Removes the `key` from object `self`.

__key_type__

    var key_type(var self);

Returns the key type for the object `self`.

__val_type__

    var val_type(var self);

Returns the value type for the object `self`.

### Examples

__Usage 1__

    var x = new(Array, String, 
      $S("Hello"), $S("There"));
    
    show(get(x, $I(0))); /* Hello */
    show(get(x, $I(1))); /* There */
    set(x, $I(1), $S("Blah"));
    show(get(x, $I(1))); /* Blah */
    

__Usage 2__

    var prices = new(Table, String, Int, 
      $S("Apple"),  $I(12),
      $S("Banana"), $I( 6),
      $S("Pear"),   $I(55));
    
    var pear_price   = get(prices, $S("Pear"));
    var banana_price = get(prices, $S("Banana"));
    var apple_price  = get(prices, $S("Apple"));
    
    show(pear_price);   /* 55 */
    show(banana_price); /*  6 */
    show(apple_price);  /* 12 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Get
__Gettable or Settable__

The `Get` class provides a method to _get_ or _set_ certain properties of an object using keys and value. Typically it is implemented by data lookup structures such as `Table` or `Map` but it is also used more generally such as using indices to look up items in `Array`, or as thread local storage for the `Thread` object.

### Definition

    struct Get {
      var  (*get)(var, var);
      void (*set)(var, var, var);
      bool (*mem)(var, var);
      void (*rem)(var, var);
      var (*key_type)(var);
      var (*val_type)(var);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Filter](/learn/filter)</span> | &nbsp; &nbsp;   _Filtered Iterable_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Apply Function to Iterable_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _Integer Sequence_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tree](/learn/tree)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_
* <span class="docitem">[Zip](/learn/zip)</span> | &nbsp; &nbsp;   _Multiple Iterator_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
