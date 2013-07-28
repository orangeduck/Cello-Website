Type
----
__Metadata Type Object__

`Type` is one of the most important Types in Cello. It provides metadata about an object including which classes it implements. One can get the type of an object using the `type_of` function.

To see if a type implements a class `type_implements` can be used. To call a function of a class, implemented `type_class_method` can be used.

`cast` can be used to do runtime type checking. It checks a given object has a certain type and if so returns the given object.



### Implements

* <span style="width:75px; float:left;">[New](new)</span> `new` `delete` `construct` `destruct`
* <span style="width:75px; float:left;">[AsStr](asstr)</span> `as_str`
* <span style="width:75px; float:left;">[Show](show)</span> `show` `print` `look` `scan`


### See Also



### Examples

__Usage__
    
    var t = type_of($(Int, 5));
    show(t); /* Int */
    
    show(type_implements(t, New)); /* True */
    show(type_implements(t, Eq));  /* True */
    show(type_implements(t, Ord)); /* True */
    
    show(type_class_method(t, Eq, eq, $(Int, 5), $(Int, 6))); /* False */
    
    
__Casting__
    
    var x = $(Int, 10);
    
    var xs = cast(x, Int); /* Success */
    var xf = cast(x, Real); /* Throws Exception */


[Back](/documentation)
