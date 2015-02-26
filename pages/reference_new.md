  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods


    var new(var type, ...);

Create a new object of a certain type on the heap.

__Parameters__
  
  * `type` Type to create
  * `...` Arguments to be passed to constructor

__Returns__ New Object


    void delete(var obj);


Delete an object created on the heap.

* __Parameters__
    * `obj` Object to delete
* __Returns__ None


    var allocate(var type);


Allocate space for an object of a certain type.

* __Parameters__
    * `type` Type to allocate space for
* __Returns__ Blank object of certain type


    void deallocate(var obj);


Free the space allocated by a certain object.

* __Parameters__
    * `obj` Object to free the memory for
* __Returns__ None


    var construct(var obj, ...);


Call the constructor of an object.

* __Parameters__
    * `obj` Object to call constructor on
    * `...` Arguments to be passed to constructor
* __Returns__ Newly Constructed Object


    var destruct(var obj);


Call the destructor of an object.

* __Parameters__
    * `obj` Object to call destructor on
* __Returns__ Newly Destructed Object



### Examples

__Usage__

    var x = new(Int, $(Int, 1));
    
    show(x); /* 1 */
    show(type_of(x)) /* Int */
    
    delete(x);
    
    var y = $(Real, 0.0);  
    
    show(y); /* 0.0 */
    construct(y, $(Int, 1.0));
    show(y); /* 1.0 */
    
    var z = allocate(String);
    construct(z, $(String, "Hello"));
    
    show(z); /* Hello */
    z = destruct(z);
    deallocate(z);

  </div>
  <div class="col-xs-6 col-md-6">


New
---
__Constructable on the Heap__

The `New` class provides a method to implement dynamic (heap) memory allocation for certain object types as well as _constructor_ and _destructor_ functions to be called just after an object's memory space has been allocated and just before it's memory allocation is freed. To implement this class you must also give a function returning the memory size of the data object to allocated.

The `new` function takes a list of `var` type arguments to provide a method of passing arguments to an object's constructor. native C types should never be passed into this list and should instead be wrapped using `$`. See examples for details.




### Signature


    class {
      var (*construct)(var, var_list);
      var (*destruct)(var);
      size_t (*size)(void);
    } New;
    

### Implementers

* <span style="width:75px; float:left;">[Function](function)</span> _High Level Function_
* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[Real](real)</span> _Basic Float Point Type_
* <span style="width:75px; float:left;">[Reference](reference)</span> _Basic Reference Type_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Mutex](mutex)</span> _Mutual Exclusion Lock_
* <span style="width:75px; float:left;">[Int](int)</span> _Basic Integer Type_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Char](char)</span> _Basic Character Type_
* <span style="width:75px; float:left;">[Pool](pool)</span> _Reference Counting Pool_
* <span style="width:75px; float:left;">[File](file)</span> _Operating System File_
* <span style="width:75px; float:left;">[Thread](thread)</span> _Concurrent Processes_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_
* <span style="width:75px; float:left;">[Type](type)</span> _Metadata Type Object_
* <span style="width:75px; float:left;">[String](string)</span> _Basic String Type_


### See Also

* <span style="width:75px; float:left;">[Assign](assign)</span> _Assignable to_
* <span style="width:75px; float:left;">[Copy](copy)</span> _Copyable_


  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
