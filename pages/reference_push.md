Push
----
__Elements can be Pushed and Popped__

The `Push` class provides an interface for the addition and remove of objects from another  (typically a collection) in a positional sense.

`push` can be used to add new objects to a collection and `pop` to remove them.

In containers `push` uses `assign` to copy in new contents and the result of a `pop` is typically Undefined as it will have been removed from memory and cannot be returned to the user.


### Methods

-------------------------------

    void push(var self, var obj);
    void push_at(var self, var obj, int i);
    void push_back(var self, var obj);
    void push_front(var self, var obj);

Push an object onto another.

* __Parameters__
    * `self` object to get pushed onto
    * `obj` object to push
    * `i` position to push at
* __Returns__ None

------------------------------- 

    var pop(var self);
    var pop_at(var self, int i);
    var pop_back(var self);
    var pop_front(var self);

Pop an object from another.

* __Parameters__
    * `self` object to get popped frm onto
    * `i` position to pop from
* __Returns__ Popped Object

------------------------------- 


### Signature


    class {
      void (*push)(var, var);
      void (*push_at)(var, var, int);
      void (*push_back)(var, var);
      void (*push_front)(var, var);
      var (*pop)(var);
      var (*pop_at)(var, int);
      var (*pop_back)(var);
      var (*pop_front)(var);
    } Push;
    

### Implementers

* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_


### See Also

* <span style="width:75px; float:left;">[Collection](collection)</span> _Treatable as several objects_
* <span style="width:75px; float:left;">[At](at)</span> _Elements can be directly accessed and set_
* <span style="width:75px; float:left;">[Append](append)</span> _Elements can be added to end_


### Examples

__Usage__

    var x = new(Array, Int, 0);
    
    push(x, $(Int, 0));
    push(x, $(Int, 5));
    push(x, $(Int, 10));
    
    show(at(x, 0)); /* 0  */
    show(at(x, 1)); /* 5  */
    show(at(x, 2)); /* 10 */
    
    pop_at(x, 1);
    
    show(at(x, 0)); /* 0  */
    show(at(x, 1)); /* 10  */
    
    delete(x);

[Back](/documentation)
