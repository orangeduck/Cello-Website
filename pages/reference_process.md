Process
-------
__Program Like__

The `Process` class provides an abstraction on functions related to multiple processes such as Threading.


### Methods

-------------------------------

    var current(var type);

return the current process.

* __Parameters__
    * `type` type implementing Progress of which to get the current
* __Returns__ None

------------------------------- 

    void join(var self);

join another process.

* __Parameters__
    * `self` process to join with
* __Returns__ None

------------------------------- 

    void terminate(var self);

terminate another process.

* __Parameters__
    * `self` process to terminate
* __Returns__ None

------------------------------- 


### Signature


    class {
      var  (*current)(void);
      void (*join)(var);
      void (*terminate)(var);
    } Process;
    

### Implementers

* <span style="width:75px; float:left;">[Thread](thread)</span> _Concurrent Processes_


### See Also

* <span style="width:75px; float:left;">[Lock](lock)</span> _Exclusive Resource_
* <span style="width:75px; float:left;">[Call](call)</span> _Callable like a Function_


### Examples

__Usage__
    
    lambda(thread_hello, args) {
        println("Hello from %$!", current(Thread));
    };
    
    var t = new(Thread, thread_hello);
    call(t);
    
    println("Waiting for %$...", t);
    join(t);
    
    println("And Hello from %$!", current(Thread));
    
    delete(t);

[Back](/documentation)
