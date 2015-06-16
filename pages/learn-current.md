  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__current__

    var current(var type);

Returns the current active object of the given `type`.

### Examples

__Usage__

    var gc = current(GC);
    show(gc);
    var thread = current(Thread);
    show(thread);
    



  </div>
  <div class="col-xs-6 col-md-6">

# Current
__Implicit Object__

The `Current` class can be implemented by types which have implicit instances associated with them. For example it can be used to retrieve the _current_ `Thread`, or it could be used to get the _current_ Garbage Collector.

This class may be implemented by types which express the [Singleton Design Pattern](http://en.wikipedia.org/wiki/Singleton_pattern)

### Definition

    struct Current {
      var (*current)(void);
    };
    

### Implementers

* <span class="docitem">[Exception](/learn/exception)</span> | &nbsp; &nbsp;   _Exception Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
