  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__call__

    #define call(self, ...)
    var call_with(var self, var args);

Call the object `self` with arguments `args`.

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
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
