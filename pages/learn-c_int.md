  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__c_int__

    int64_t c_int(var self);

Returns the object `self` represented as a `int64_t`.

### Examples

__Usage__

    printf("%li", c_int($I(5))); /* 5 */
    printf("%li", c_int($I(6))); /* 6 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# C_Int
__Interpret as C Integer__

The `C_Int` class should be overridden by types which are representable as a C style Integer of the type `int64_t`.

### Definition

    struct C_Int {
      int64_t (*c_int)(var);
    };
    

### Implementers

* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
