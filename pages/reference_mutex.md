Mutex
-----
__Mutual Exclusion Lock__

A basic Mutual Exclusion Primative. Used to lock around resources such that no two threads can enter the same block of code. Either `lock` and `unlock` can be used or `with`.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Lock](lock)</span> `lock` `unlock` `lock_try`
* <span style="width:75px; float:left;">[With](with)</span> `with` `enter_with` `exit_with`


### See Also

* <span style="width:75px; float:left;">[Thread](thread)</span> _Concurrent Processes_
* <span style="width:75px; float:left;">[Function](function)</span> _High Level Function_


### Examples

__Usage__

    var mutex = new(Mutex);
    var total = $(Int, 0);
    
    lambda(f, args) {
        with(m in mutex) {
            add(total, $(Int, 1));
        }
        return None;
    };
    
    var threads = new(List, 5,
        new(Thread, f), new(Thread, f),
        new(Thread, f), new(Thread, f),
        new(Thread, f));
        
    foreach(t in threads) {
        call(t, None);
    }
    
    foreach(t in threads) {
        join(t);
        delete(t);
    }
    
    show(total); /* 5 */
    
    delete(threads);
    delete(mutex);

[Back](/documentation)
