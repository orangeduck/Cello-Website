Retain
------
__Can be used for reference counting__

The `Retain` class provides an interface to reference counting behaviour to objects using a reference pool or other structure. This can ease memory management as the number of code locations that still require an object to exist can be monitored.

Users call `retain` to increment the reference count of an object and `release` to decrement. Upon reaching a zero reference count typically an object will be destructed and deallocated.


### Methods

-------------------------------

    var retain(var p, var x);

Retain another reference to `x` in `p`

* __Parameters__
    * `p` Object which to retain a reference in
    * `x` Referenced Object
* __Returns__ Referenced Object

------------------------------- 

    void release(var p, var x);

Release a reference to `x` in `p`

* __Parameters__
    * `p` Object which to release a reference in
    * `x` Referenced Object
* __Returns__ Referenced Object

------------------------------- 


### Signature


    class {
      var (*retain)(var p, var x);
      void (*release)(var p, var x);
    } Retain;
    

### Implementers

* <span style="width:75px; float:left;">[Pool](pool)</span> _Reference Counting Pool_


### See Also

* <span style="width:75px; float:left;">[With](with)</span> _Can be entered and exited_


### Examples

__Usage__

    var p = new(Pool);
    
    lambda(table_fill, args) {
        var t = at(args, 0);
        put(t, $(String, "First"),  $(Real, 0.0));
        put(t, $(String, "Second"), $(Real, 0.1));
        put(t, $(String, "Third"),  $(Real, 5.7));
        release(p, t);
        return None
    };
    
    lambda(table_process, args) {
        var t = at(args, 0);
        put(t, $(String, "First"), $(Real, -0.65));
        release(p, t);
        return None;
    };

    var x = retain(p, new(Table, String, Real));

    call(table_fill, retain(p, x));
    call(table_process, retain(p, x));

    release(p, x);

[Back](/documentation)
