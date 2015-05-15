  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__with__

    #define with(...)

Perform operations in between `start` and `stop`.

__start__

    void start(var self);

Start the object `self`.

__stop__

    void stop(var self);

Stop the object `self`.

__wait__

    void wait(var self);

Block and wait for the object `self` to stop.

__running__

    bool running(var self);

Check if the object `self` is running.

### Examples

__Usage__

    var x = new(Mutex);
    start(x); /* Lock Mutex */ 
    print("Inside Mutex!\n");
    stop(x); /* unlock Mutex */

__Scoped__

    var x = new(Mutex);
    with (mut in x) { /* Lock Mutex */ 
      print("Inside Mutex!\n");
    } /* unlock Mutex */



  </div>
  <div class="col-xs-6 col-md-6">

# Start
__Can be started or stopped__

The `Start` class can be implemented by types which provide an abstract notion of a started and stopped state. This can be real processes such as `Thread`, or something like `File` where the on/off correspond to if the file is open or not.

The main nicety of the `Start` class is that it allows use of the `with` macro which performs the `start` function at the opening of a scope block and the `stop` function at the end.

### Definition

    struct Start {
      void (*start)(var);
      void (*stop)(var);
      void (*wait)(var);
      bool (*running)(var);
    };
    

### Implementers

* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
