  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__try__

    #define try

Start an exception `try` block.

__catch__

    #define catch(...)

Start an exception `catch` block, catching any objects listed in `...` as the first name given. To catch any exception object leave argument list empty other than caught variable name.

__#define throw__

    throw(E, F, ...)

Throw exception object `E` with format string `F` and arguments `...`.

__exception_signals__

    void exception_signals(void);

Register the standard C signals to throw corresponding exceptions.

__exception_object__

    void exception_object(void);
    

Retrieve the current exception object.

__exception_message__

    void exception_message(void);
    

Retrieve the current exception message.

### Examples

__Usage__

    var x = new(Table, String, Int);
    set(x, $S("Hello"), $I(1));
    set(x, $S("World"), $I(2));
    
    try {
      get(x, $S("Missing"));
    } catch (e in KeyError) {
      println("Got Exception: %$", e);
    }
    



  </div>
  <div class="col-xs-6 col-md-6">

# Exception
__Exception Object__

The `Exception` type provides an interface to the Cello Exception System. One instance of this type is created for each `Thread` and stores the various bits of data required for the exception system. It can be retrieved using the `current` function, although not much can be done with it.

Exceptions are available via the `try`, `catch` and `throw` macros. It is important that the `catch` part of the exception block is always evaluated otherwise the internal state of the exception system can go out of sync. For this reason please never use `return` inside a `try` block. 

The `exception_signals` method can be used to register some exception to be thrown for any of the [standard C signals](https://en.wikipedia.org/wiki/C_signal_handling).

To get the current exception object or message use the `exception_message` or `exception_object` methods.

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
* <span style="width:50px; float:left;">[Swap](/learn/swap)</span>`swap` 
### Implements

* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Current](/learn/current)</span>`current` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 
* <span style="width:50px; float:left;">[Len](/learn/len)</span>`len` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Show](/learn/show)</span>`show` `look` `print` `scan` 
* <span style="width:50px; float:left;">[Start](/learn/start)</span>`with` `start` `stop` `join` `running` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
