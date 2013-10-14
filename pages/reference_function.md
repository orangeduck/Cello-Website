Function
--------
__High Level Function__

Function provides an interface to treating functions as full Cello objects. This allows them to be passed around, stored and manipulated.

Functions are constructed using `lambda` at the statement level. This creates a function object with the given name taking arguments rolled into a list. Functions must return a value.

To call a Function the function `call` can be used. Functions can also be called with `call_with` when arguments are already in a list. 


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Call](call)</span> `call`


### See Also

* <span style="width:75px; float:left;">[Thread](thread)</span> _Concurrent Processes_


### Examples

__Construction__

    lambda(hello_person, args) {
        var name = cast(pop(args), String);
        print("Hello %s!", name);
        return None;
    };
    
    call(hello_person, $(String, "Dan"));
    
__Mapping__

    lambda(hello_person, args) {
        var name = cast(pop(args), String);
        print("Hello %s!", name);
        return None;
    };

    var names = new(Array, 
    $(String, "Dan"), 
    $(String, "Robert"), 
    $(String, "Chris"));

    map(names, hello_name);
    delete(names);
    
__Multiple Arguments__

    lambda(add_print, args) {
        int fst = as_long(cast(at(args, 0), Int));
        int snd = as_long(cast(at(args, 1), Int));
        println("%i + %i = %i", $(Int, fst), $(Int, snd), $(Int, fst+snd));
        return None;
    };

    /*
    ** Notice arguments to "call" in curried form.
    ** Use "call_with" for uncurried calling.
    */
    call(add_print, $(Int, 10), $(Int, 21));
    
__C-Functions__
    
    /*
    ** We can use normal c-functions too.
    ** If they have all argument types as "var".
    ** Then they can be uncurried.
    */
    var Welcome_Pair(var fst, var snd) {
        print("Hello %s and %s!\n", fst, snd);
        return None;
    };

    lambda_uncurry(welcome_uncurried, Welcome_Pair, 2);

    call(welcome_uncurried, $(String, "John"), $(String, "David"));
    

[Back](/documentation)
