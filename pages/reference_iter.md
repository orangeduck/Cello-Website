Iter
----
__Can be looped over__

The `Iter` class provides a global interface for iteration. It is what allows objects to be iterated over with `foreach` in a uniform way.

Using `iter_next` in a non incremental way is discouraged as it can occasionally cause problems or performance issues.

As iteration does not use an `iterator` object but actually the raw contents of the collection in most cases it should be very fast.

Key-Value mapping data structures will usually provide iteration only over their keys.


### Methods

-------------------------------

    var iter_start(var self);

Start iteration over an object, get the first element.

* __Parameters__
    * `self` object to iterate over
* __Returns__ The first object in the iteration

------------------------------- 

    var iter_end(var self);

Return an iteration termination object (such as Undefined).

* __Parameters__
    * `self` object being iterated over
* __Returns__ An iteration termination object.

------------------------------- 

    var iter_next(var self, var curr);

Given the current iteration object return the next. If there is no objects left return an iteration termination object (such as Undefined).

* __Parameters__
    * `self` object being iterated over
    * `curr` current iteration object
* __Returns__ The next object in the iteration or an iteration termination object.

------------------------------- 


### Signature


    class {
      var (*iter_start)(var);
      var (*iter_end)(var);
      var (*iter_next)(var, var);
    } Iter;
    

### Implementers

* <span style="width:75px; float:left;">[Map](map)</span> _Binary Tree Collection_
* <span style="width:75px; float:left;">[Dictionary](dictionary)</span> _Hashtable Collection_
* <span style="width:75px; float:left;">[Tree](tree)</span> _Binary Tree Container_
* <span style="width:75px; float:left;">[List](list)</span> _Sequential Collection_
* <span style="width:75px; float:left;">[Table](table)</span> _Hashtable Container_
* <span style="width:75px; float:left;">[Array](array)</span> _Sequential Container_


### See Also

* <span style="width:75px; float:left;">[Collection](collection)</span> _Treatable as several objects_
* <span style="width:75px; float:left;">[At](at)</span> _Elements can be directly accessed and set_


### Examples

__Usage__

    var x = new(Array, Int, $(Int, 1), $(Int, 2), $(Int, 5));
    
    foreach(o in x) {
        show(o); /* 1, 2, 5 */
    }
    
__Table__

    var prices = new(Table, String, Int);
    put(prices, $(String, "Apple"),  $(Int, 12)); 
    put(prices, $(String, "Banana"), $(Int,  6)); 
    put(prices, $(String, "Pear"),   $(Int, 55)); 

    foreach(key in prices) {
        var price = get(prices, key);
        print("Price of %$ is %$\n", key, price);
    }

[Back](/documentation)
