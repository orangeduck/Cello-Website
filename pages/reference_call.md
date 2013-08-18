Call
----
__Callable like a Function__

Class for types which are _callable_ such as a function. That it some object that can be passed a number of arguments and return an object back.

Use the `call` macro to call in uncurried form, passing the arguments directly to the function. Use `call_with` to call in curried form, passing in a single List.


### Methods

-------------------------------

    #define call(x, ...) call_with_ptr(x, (var[]){ __VA_ARGS__, (var)-1 })
    var call_with_ptr(var self, var* args);
    var call_with(var self, var args);

Call a function with some arguments

* __Parameters__
    * `self` Object to call
    * `args` List of arguments to call with
* __Returns__ Returned value of Callable

------------------------------- 


### Signature


    class {
      var (*call_with)(var,var);
    } Call;
    

### Implementers

* <span style="width:75px; float:left;">[Function](function)</span> _High Level Function_
* <span style="width:75px; float:left;">[Thread](thread)</span> _Concurrent Processes_


### See Also

* <span style="width:75px; float:left;">[Process](process)</span> _Program Like_


### Examples

__Construction__

    lambda(hello_person, args) {
        var name = cast(pop(args), String);
        print("Hello %s!", name);
        return None;
    };
    
    call(hello_person, $(String, "Dan"));
    
__Multiple Arguments__

    lambda(add_print, args) {
        int fst = as_long(cast(at(args, 0), Int));
        int snd = as_long(cast(at(args, 1), Int));
        println("%i + %i = %i", $(Int, fst), $(Int, snd), $(Int, fst+snd));
        return None;
    };

    call(add_print, $(Int, 10), $(Int, 21));
    
    var args = new(List, 2, $(Int, 10), $(Int, 21));
    call_with(add_print, args);
    delete(args);
    
__Threads__

    lambda(f, args) {
        println("Hello from thread %$!", current(Thread));
        return None;
    };
    
    var t = new(Thread, f);    
    call(t, None);
    join(t);
    
    delete(t);

[Back](/documentation)
