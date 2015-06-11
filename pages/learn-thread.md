  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var set_value(var args) {
      assign(get(args, $I(0)), $I(1));
      return NULL;
    }
    
    var i = $I(0);
    
    var x = new(Thread, $(Function, set_value));
    call(x, i);
    wait(x);
    
    show(i); /* 1 */
    

__Exclusive Resource__

    var increment(var args) {
      var mut = get(args, $I(0));
      var tot = get(args, $I(1));
      lock(mut);
      assign(tot, $I(c_int(tot)+1));
      unlock(mut);
      return NULL;
    }
    
    var mutex = new(Mutex);
    var total = $I(0);
    
    var threads = new(Array, Box,
      new(Thread, $(Function, increment)),
      new(Thread, $(Function, increment)),
      new(Thread, $(Function, increment)));
    
    show(total); /* 0 */
    
    foreach (t in threads) {
      call(deref(t), mutex, total);
    }
    
    foreach (t in threads) {
      wait(deref(t));
    }
    
    show(total); /* 3 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Thread
__Concurrent Execution__

The `Thread` type provides a basic primitive for concurrent execution. It acts as a basic wrapper around operating system threads, using WinThreads on Windows and pthreads otherwise.

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:50px; float:left;">[C_Int](/learn/c_int)</span>`c_int` 
* <span style="width:50px; float:left;">[Call](/learn/call)</span>`call` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Current](/learn/current)</span>`current` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Get](/learn/get)</span>`get` `set` `mem` `rem` `key_type` `val_type` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Mark](/learn/mark)</span>`mark` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Start](/learn/start)</span>`with` `start` `stop` `wait` `running` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
