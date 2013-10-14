Num
---
__Can perform arithmetic__

The `Num` class provides an interface for doing arithematic on objects.

The most important thing to note is that these operations don't return a value. They are destructive on the first argument. This is in the name of speed and memory management. If every operation returned a new object there would be lots of objects to clean up and a lot of overhead in memory allocation.

If users require new objects they are encouraged to make copies of existing objects and then modify them using these methods.


### Methods

-------------------------------

    void add(var self, var obj);

Add one object to another

* __Parameters__
    * `self` Object to change
    * `obj` Object value to add
* __Returns__ None

------------------------------- 

    void sub(var self, var obj);

Subtract one object from another

* __Parameters__
    * `self` Object to change
    * `obj` Object value to subtract
* __Returns__ None

------------------------------- 

    void mul(var self, var obj);

Multiply one object by another

* __Parameters__
    * `self` Object to change
    * `obj` Object value to multiply
* __Returns__ None

------------------------------- 

    void divide(var self, var obj);

Divide one object by another

* __Parameters__
    * `self` Object to change
    * `obj` Object value to divide
* __Returns__ None

------------------------------- 

    void negate(var self);

Negate an object

* __Parameters__
    * `self` Object to negate
* __Returns__ None

------------------------------- 

    void absolute(var self);

Make an object absolute

* __Parameters__
    * `self` Object to make absolute
* __Returns__ None

------------------------------- 


### Signature


    class {
      void (*add)(var, var);
      void (*sub)(var, var);
      void (*mul)(var, var);
      void (*div)(var, var);
      void (*negate)(var);
      void (*absolute)(var);
    } Num;
    

### Implementers

* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_


### See Also

* <span style="width:75px; float:left;">[AsLong](aslong)</span> _Representable as C long_
* <span style="width:75px; float:left;">[AsDouble](asdouble)</span> _Representable as C double_


### Examples

__Usage__
        
    var x = $(Int, 0);
    
    show(x); /* 0 */
    
    add(x, $(Int, 10)); show(x);   /* 10 */
    sub(x, $(Int, 4));  show(x);   /*  6 */
    mul(x, $(Int, 10)); show(x);   /* 60 */
    
    divide(x, $(Int, 3)); show(x); /* 20 */
    
    negate(x);   show(x); /* -20 */
    absolute(x); show(x); /* 20 */
    absolute(x); show(x); /* 20 */ 
    

[Back](/documentation)
