AsDouble
--------
__Representable as C double__

The `AsDouble` class allows a user to represent an object as a C `double`. It is used by the native type wrapper `Real`.


### Methods

-------------------------------

    double as_double(var self);

represent object as C `double`

* __Parameters__
    * `self` object to represent
* __Returns__ C `double` representation of object

------------------------------- 


### Signature


    class {
      double (*as_double)(var);
    } AsDouble;
    

### Implementers

* <span style="width:75px; float:left;">[None](none)</span> _Empty Value_
* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Bool](bool)</span> _Boolean Truth Value_


### See Also

* <span style="width:75px; float:left;">[AsLong](aslong)</span> _Representable as C long_


### Examples

__Usage__

    printf("%f", as_double($(Real, 5.1))); /* 5.1 */
    printf("%f", as_double($(Real, 5.2))); /* 5.2 */
    printf("%f", as_double($(Real, 9.8))); /* 9.8 */
    printf("%f", as_double($(Int, 5)));    /* 5.0 */
    printf("%f", as_double($(Int, 7)));    /* 7.0 */
    

[Back](/documentation)
