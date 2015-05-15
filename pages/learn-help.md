  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__help__

    void help(var self);
    int help_to(var out, int pos, var self);

Print help information about the object `self` either to `stdout` or to the object `out` at some position `pos`.

### Examples

__Usage__

    help(Int);
    



  </div>
  <div class="col-xs-6 col-md-6">

# Help
__Usage information__

The `Help` class can be implemented to let an object provide helpful information about itself. In the standard library this class is implemented by `Type` and it prints out the documentation provided by the `Doc` class in a friendly way.

### Definition

    struct Help {
      int (*help_to)(var, int);
    };
    

### Implementers

* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
