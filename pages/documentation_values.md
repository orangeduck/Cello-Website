Values
------

Values are an experimental addition to Cello that allows for the creation and passing of object by _Value_. Value objects are stored on the stack and passed by copying the contents. As it is experimental value objects are not used anywhere in the standard library, but this isn't to say they shouldn't be used.

In Cello they look something like this.

    /* A function returning a Int (by value) and taking two Ints (by value) */
    val(Int) add_integers(val(Int) x, val(Int) y) {
      
      /* Declare a new variable to store the result */
      var res = $(Int, 0);
      
      /* Use `&` to get reference (var) from a value (val) type */
      add(res, &(x));
      add(res, &(y));
      
      /* Use `*` to get a value (val) from a reference (var) type */
      return *(res);
    }

    
The main advantage of value types is that they can be returned from functions without having to deal with memory management. The result will be allocated on the stack of the calling function. The disadvantage is that they must be typed and so cannot be used for generic functions to some extent.

It is also important to note that when value types are copied the memory is simply copied rather than using the `copy` function. This means if the object contains internal pointers these will not be deep copies.

[Back](/documentation)
