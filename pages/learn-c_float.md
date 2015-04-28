  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__c_float__

    double c_float(var self);

Returns the object `self` represented as a `double`.

### Examples

__Usage__

    printf("%f", c_float($F(5.1))); /* 5.1 */
    printf("%f", c_float($F(6.2))); /* 6.2 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# C_Float
__Interpret as C Float__

The `C_Float` class should be overridden by types which are representable as a C style Float of the type `double`.

### Definition

    struct C_Float {
      double (*c_float)(var);
    };
    

### Implementers

* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Float Point Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
