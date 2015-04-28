  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__lock__

    void lock(var self);

Wait until a lock can be aquired on object `self`.

__lock_try__

    bool lock_try(var self);

Try to acquire a lock on object `self`. Returns `true` on success and `false` if the resource is busy.

__unlock__

    void unlock(var self);

Release lock on object `self`.

  </div>
  <div class="col-xs-6 col-md-6">

# Lock
__Exclusive Resource__

The `Lock` class can be implemented by types to limit the access to them. For example this class is implemented by the `Mutex` type to provide mutual exclusion across Threads.

### Definition

    struct Lock {
      void (*lock)(var);
      void (*unlock)(var);
      bool (*lock_try)(var);
    };
    

### Implementers

* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
