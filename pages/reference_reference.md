Reference
---------
__Basic Reference Type__

Reference is a basic type providing a level of indirection to an object. It can be used like a pointer to store only references in contains such as Array or Table.

It can also be used in conjunction with `With` to declare object lifetimes. Or a number of other tricks. A reference is _dereferenced_ using `at(r, 0)` and assigned using `set(r, 0, x)`.


### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[Assign](assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](eq)</span> `eq` `neq` `if_eq` `if_neq`
* <span style="width:75px; float:left;">[Hash](hash)</span> `hash`
* <span style="width:75px; float:left;">[At](at)</span> `at` `set`
* <span style="width:75px; float:left;">[With](with)</span> `with` `enter_with` `exit_with`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also

* <span style="width:75px; float:left;">[Pool](pool)</span> _Reference Counting Pool_


### Examples

__Single Lifetime__

    with(liferef in $(Reference, new(String, "Life is long"))) {
        println("This reference is: %$", liferef);
        println("This string is alive: '%s'", at(liferef,0));
    }

    print("Now it has been cleared up!
");

__Many Lifetimes__

    with(liferef0 in $(Reference, new(String, "Life is long")))
    with(liferef1 in $(Reference, new(String, "Life is Beautiful")))
    with(liferef2 in $(Reference, new(String, "Life is Grand"))) {
        println("%s :: %s :: %s", at(liferef0,0), at(liferef1,0), at(liferef2,0));
    }

__Lambda Indirection__

    /*
    ** Reference can be used to set 
    ** an otherwise read-only variable 
    ** inside a closure.
    */
    var in_func = $(Reference, False);
    
    lambda(f, args) {
      set(in_func, 0, True);
      return None;
    };

[Back](/documentation)
