Thread
------
__Concurrent Processes__

A basic Thread primative. These can be constructed with some `Function` type and then called with a number of arguments.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Call](call)</span> `call`
* <span style="width:75px; float:left;">[Process](process)</span> `current` `join` `terminate`
* <span style="width:75px; float:left;">[AsLong](aslong)</span> `as_long`


### See Also

* <span style="width:75px; float:left;">[Mutex](mutex)</span> _Mutual Exclusion Lock_
* <span style="width:75px; float:left;">[Function](function)</span> _High Level Function_


### Examples

__Usage__

    lambda(f, args) {
        println("Hello from thread %$!", current(Thread));
        return None;
    };
    
    var t = new(Thread, f);    
    call(t);
    join(t);
    
    delete(t);

[Back](/documentation)
