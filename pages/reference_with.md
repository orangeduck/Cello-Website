With
----
__Can be entered and exited__

The `With` class provides an interface to provide 'entry' and 'exit' functions to be performed on an object within some scope. This allows for the use of the `with` keyword to specify the scope of an object or operation.


### Methods

-------------------------------

    void enter_with(var self);

Perform entry code for an object

* __Parameters__
    * `self` object to enter with
* __Returns__ None

------------------------------- 

    void exit_with(var self);

Perform exit code for an object

* __Parameters__
    * `self` object to exit with
* __Returns__ None

------------------------------- 


### Signature


    class {
      void (*enter)(var);
      void (*exit)(var);
    } With;
    

### Implementers

* <span style="width:75px; float:left;">[Reference](reference)</span> _Basic Reference Type_
* <span style="width:75px; float:left;">[Mutex](mutex)</span> _Mutual Exclusion Lock_
* <span style="width:75px; float:left;">[File](file)</span> _Operating System File_


### See Also

* <span style="width:75px; float:left;">[Stream](stream)</span> _File-like_
* <span style="width:75px; float:left;">[Lock](lock)</span> _Exclusive Resource_


### Examples

__Usage__

    with(file in stream_open($(File, NULL), "prices.bin", "wb")) {
      
        lambda(write_pair, args) {
            var key = cast(at(args, 0), String);
            var val = cast(get(prices, key), Int);
          
            print_to(file, 0, "%$ :: %$\n", key, val);      
            return None;
        };
        
        map(prices, write_pair);
      
    }
      
__Locks__

    var mut = new(Mutex);

    lambda(thread_function, args) {
        with(m in mut) {
            println("Hello from %$! with Arguments %$", current(Thread), args);
        }
        return None;
    };

    var threads = new(List, 5,
    new(Thread, thread_function),
    new(Thread, thread_function),
    new(Thread, thread_function),
    new(Thread, thread_function),
    new(Thread, thread_function));

    foreach(t in threads) {
        call(t, None);
    }

    foreach(t in threads) {
        join(t);
        delete(t);
    }

    delete(threads);
    delete(mut);

[Back](/documentation)
