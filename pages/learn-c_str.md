  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__c_str__

    char* c_str(var self);

Returns the object `self` represented as a `char*`.

### Examples

__Usage__

    puts(c_str($S("Hello"))); /* Hello */
    puts(c_str($S("There"))); /* There */
    



  </div>
  <div class="col-xs-6 col-md-6">

# C_Str
__Interpret as C String__

The `C_Str` class should be overridden by types which are representable as a C style String.

### Definition

    struct C_Str {
      char* (*c_str)(var);
    };
    

### Implementers

* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
