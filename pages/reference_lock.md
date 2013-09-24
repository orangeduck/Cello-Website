Lock
----
__Exclusive Resource__

The `Lock` class provides an interface for gaining exclusive access to resources.


### Methods

-------------------------------

    void lock(var self);

lock an object. If lock is unavaliable wait until it is avaliable.

* __Parameters__
    * `self` object to lock
* __Returns__ None

------------------------------- 

    void unlock(var self);

unlock an object

* __Parameters__
    * `self` object to unlock
* __Returns__ None

------------------------------- 

    var lock_try(var self);

lock an object. If lock is unavaliable continue.

* __Parameters__
    * `self` object to lock
* __Returns__ None

------------------------------- 


### Signature


    class {
      void (*lock)(var);
      void (*unlock)(var);
      var  (*lock_try)(var);
    } Lock;
    

### Implementers

* <span style="width:75px; float:left;">[Mutex](mutex)</span> _Mutual Exclusion Lock_


### See Also

* <span style="width:75px; float:left;">[Process](process)</span> _Program Like_
* <span style="width:75px; float:left;">[With](with)</span> _Can be entered and exited_


### Examples

__Usage__

    var mutex = new(Mutex);
    var total = $(Int, 0);
    
    lambda(f, args) {
      lock(mutex);
      add(total, $(Int, 1));
      unlock(mutex);
      return None;
    };
    
    var threads = new(List,
      new(Thread, f), new(Thread, f),
      new(Thread, f), new(Thread, f),
      new(Thread, f));
    
    foreach(t in threads) {
      call(t);
    }
    
    foreach(t in threads) {
      join(t);
      delete(t);
    }
    
    delete(threads);
    delete(mutex);

[Back](/documentation)
