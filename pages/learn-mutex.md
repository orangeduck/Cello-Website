  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var x = new(Mutex);
    with (mut in x) { /* Lock Mutex */ 
      print("Inside Mutex!\n");
    } /* Unlock Mutex */



  </div>
  <div class="col-xs-6 col-md-6">

# Mutex
__Mutual Exclusion Lock__

The `Mutex` type can be used to gain mutual exclusion across Threads for access to some resource.

### Derives

* <span style="width:75px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:75px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:75px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:75px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:75px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:75px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:75px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:75px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:75px; float:left;">[Lock](/learn/lock)</span>`lock` `lock_try` `unlock` 
* <span style="width:75px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:75px; float:left;">[Start](/learn/start)</span>`with` `start` `stop` `wait` `running` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
