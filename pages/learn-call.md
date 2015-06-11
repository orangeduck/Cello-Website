  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__call__

    #define call(self, ...)
    var call_with(var self, var args);

Call the object `self` with arguments `args`.

### Examples

__Usage__

    var increment(var args) {
      struct Int* i = get(args, $I(0));
      i->val++;
      return NULL;
    }
    
    var x = $I(0);
    show(x); /* 0 */
    call($(Function, increment), x);
    show(x); /* 1 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Call
__Callable__

The `Call` class is used by types which can be called as functions.

### Definition

    struct Call {
      var (*call_with)(var, var);
    };
    

### Implementers

* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Apply Function to Iterable_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
