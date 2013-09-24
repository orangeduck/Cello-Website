
Containers and Collections
--------------------------

Using libCello it is possible to produce a number of generic data structures. These are included in the standard library as `Array`, `List`, `Table`, `Dictionary`, `Tree`, `Map`.

They are divided up into two types. _Containers_ and _Collections_.


Containers
----------

Containers are data structures which actually contain objects. They allocating memory for them and deallocating memory on destruction. The primary example of this is `Array`, a dynamically resizeable sequence of one type of Object.

Because these containers must allocate and deallocate space (calling deconstructors), they can only work on a single type which must be specified at creation. 

    var x = new(Array, Int);
    push(x, $(Int, 32));
    push(x, $(Int, 6));
    
    /* <'Array' At 0x0000000000414603 [32, 6]> */
    show(x);
    delete(x);

When new items are added to containers the contents of the argument are copied to the existing memory location using `assign`.

Examples of Containers are:

* `Array` - A dynamically sized sequence data structure.
* `Table` - A hashtable data structure mapping hashable keys to values.
* `Tree`  - A binary tree data structure mapping ordered keys to values.

Collections
-----------

Collections are data structures containing pointers to objects. They are not responsible for the allocation or deallocation of the objects pointed to inside and simply provide a way of grouping or associating certain existing objects.

Because they are not responsible for allocation they can contain several differing types but it is the user's responsibility to ensure operations remain valid across all types inside (for example to ensure `Eq` makes sense when comparing a `Int` and an `String`).
    
    var i0 = new(Int, $(Int, 21));
    var i1 = new(String, $(String, "Hello"));
    
    var x = new(List);
    push(x, i0);
    push(x, i1);
    
    /* <'List' At 0x0000000000414603 [21, "Hello"]> */
    show(x);
    delete(x);
    
    delete(i0);
    delete(i1);

Examples of Collections are:
    
* `List`       - A dynamically sized sequence data structure.
* `Dictionary` - A hashtable data structure mapping hashable keys to values.
* `Map`        - A binary tree data structure mapping ordered keys to values.

[Back](/documentation)
