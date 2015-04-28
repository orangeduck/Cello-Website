  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__join__

    void join(var self);

Wait for the object `self` to enter some state.

  </div>
  <div class="col-xs-6 col-md-6">

# Join
__Wait for object__

The `Join` class can be implemented by types which provide a mechanism for waiting for them to enter some same state. Primarily it is implemented by `Thread`.

### Definition

    struct Join {
      void (*join)(var);
    };
    

### Implementers

* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
