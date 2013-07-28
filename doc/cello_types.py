
cello_type = dict

def type_set(**types):

    types["None"] = types["NoneType"]
    types.pop("NoneType")

    for k in types.keys():
        
        types[k]["name"] = k
        types[k]["link"] = k.lower()
        types[k]["filename"] = "reference_" + k.lower() + ".md"
        
        for x in ["description", "examples"]:
            if not (x in types[k]): types[k][x] = "\nComing Soon...\n"
        
    return types
     
cello_types = type_set(

    Array = cello_type(
        tag  = "Sequential Container",
        implements="New Assign Copy Eq Collection Push At Iter Reverse Sort Append Show",
        related="List Table Tree Dictionary Map",
        description = 
"""
Array is data structure containing a sequence of a single type of object. It can dynamically grow and shrink in size depending on how many elements it contains. It is a [Container](/documentation/containers) meaning it allocates storage for the type specified. It also deallocates and destroys the objects inside upon destruction.

Elements are copied in an Array using `assign` which means the type much implement the [Assign](reference/assign) class.

Elements are ordered linearly. Elements are accessed by their position in this sequence directly. Addition and removal of elements at the end of the sequence is fast, with memory movement required for elements in the middle of the sequence. 

The equivalent C++ construct to this type is [std::vector](http://www.cplusplus.com/reference/vector/vector/)
""",
        examples=
"""
__Construction & Deletion__

    var x = new(Array, Int, 0);
    push(x, $(Int, 32));
    push(x, $(Int, 6));
    
    /* <'Array' At 0x0000000000414603 [32, 6]> */
    show(x);
    delete(x);
    
__Element Access__

    var x = new(Array, Real, 2, $(Real, 0.01), $(Real, 5.12));
    
    show(at(x, 0)); /* 0.01 */
    show(at(x, 1)); /* 5.12 */
    
    set(x, 0, $(Real, 500.1));
    show(at(x, 0)); /* 500.1 */
    
    delete(x);

__Collection Queries__

    var x = new(Array, Char, 4, $(Char, 'a'), $(Char, 'b'), $(Char, 'c'), $(Char, 'd'));
    
    show(contains(x, $(Char, 'a'))); /* True */
    show($(Int, len(x)));            /* 4 */
    
    discard(x, $(Char, 'c'));
    
    show(contains(x, $(Char, 'c'))); /* False */
    show($(Int, len(x)));            /* 3 */
    show(is_empty(x));               /* False */
    
    clear(x);
    
    show(is_empty(x));               /* True */
  
    delete(x);
    
__Iteration__

    var greetings = new(Array, String, 3, $(String, "Hello"), $(String, "Bonjour"), $(String, "Hej"));
    
    foreach(greet in greetings) {
      show(greet);
    }
    
    delete(x);
"""
    ),

    Bool = cello_type(
        tag  = "Boolean Truth Value",
        implements = "Eq Ord Hash AsChar AsLong AsDouble AsStr Show",
        related = "None Int",
        description =
"""
Bool is a Cello wrapper of a standard C bool. It is defined as follows.

    local var True  = (var)1;
    local var False = (var)0;
    
These evaluate to true and false correctly in `if` statements and can be returned, passed around, and manipulated using the standard logical operators. Bools can be cast to c `bool` and back again without issue.

There is no data object for Bool. This is because they are hard coded into `type_of`.
""",
        examples =
"""
__Logic__

    var x = True;
    var y = False;
    
    show(x and y); /* False */
    show(x or y);  /* True */
    show(x or y);  /* True */
    show(x and not y);  /* True */
    show(x or not y);   /* True */
    show(not (x or y)); /* False */
    
__Properties__
    
    var x = True;
    var y = False;
    
    show(gt(x, y));   /* True */
    show($(Int, as_long(x)));   /* 1 */
    show($(String, as_str(x))); /* "True" */
"""
    ),

    Char = cello_type(
        tag  = "Basic Character Type",
        implements = "New Assign Copy Eq Ord Hash AsChar Serialize Show",
        related = "String Int",
        description =
"""
Char is a wrapper for the native C char type.
""",
        examples = 
"""
__Properties__

    var x = $(Char, 'a');
    var y = new(Char, 'b');
    var z = copy(x);
    
    show(eq(x, z)); /* True */
    show(gt(y, x)); /* True */
    
    assign(y, x);
    
    show(y) /* a */
    
    delete(y)
    delete(z);
    
"""
    ),

    Dictionary = cello_type(
        tag  = "Hashtable Collection",
        implements = "New Assign Copy Eq Collection Dict Iter Show",
        related = "Table Map Tree",
        description = 
"""
Dictionary is hashtable data structure mapping hashable keys to values. It is a [Collection](/documentation/containers) meaning it does not allocate storage for the keys or values inside of it. Instead it only stored references to these objects. This means both keys and values inside must be stored and managed by the programmer for the duration of the Dictionary's life.

As it is a Hashtable Dictionary provides O(1) performance for element access in the best case and O(n) in the worst.

""",
        examples =
"""
__Usage__
    
    var prices = new(Dictionary);
    var k0 = new(String, "Apple");
    var k1 = new(String, "Banana");
    var v0 = new(Int, 10);
    var v1 = new(Int, 20);
    
    put(prices, k0, v0);
    put(prices, k1, v1);
    
    foreach(k in prices) {
        println("The Price of %s is %i", k, get(prices, k));
    }
    
    delete(prices);
    delete(k0); delete(k1);
    delete(v0); delete(v1);
"""
    ),

    File = cello_type(
        tag  = "Operating System File",
        implements = "New With Stream Dict Format",
        related = "",
        description =
"""
File is a wrapper of the native C file object. It supports the standard `read` and `write` commands as well as formatted printing which resembles the c command `sprintf`. Files also support serialization of objects via the [Dict](reference/dict) functions `get` and `put`.

The position of the cursor in the file stream is stored internally and as such the `pos` argument in formatted printing commands is unused.
""",
        examples = 
"""
__Opening & Closing__
    
    var x = new(File, "test.bin", "wb");
  
    char* binary = "\0\1\1\1\1\1\0\0\0\0"
    write(x, binary, 10);
    
    delete(x);
    
__Formatted Printing__
    
    var x = $(File, None);
    open(x, "details.txt", "w");
    
    print_to(x, 0, "%$ is %$", $(String, "Dan"),   $(Int, 23));
    print_to(x, 0, "%$ is %$", $(String, "Chess"), $(Int, 24));
    
    close(x);
    
__Automatic Closing__
    
    with(f in open($(File, None), "details.txt", "r")) {
      
      var x = new(Int, 0);
      
      for (int i = 0; i < 100; i++) {
        scan_from(f, 0, "%i", x);
        show(x);
      }
      
      delete(x);
      
    }
"""
    ),

    Function = cello_type(
        tag  = "High Level Function",
        implements = "New Copy Assign Call",
        related = "Thread",
        description =
"""
Function provides an interface to treating functions as full Cello objects. This allows them to be passed around, stored and manipulated.

Functions are constructed using `lambda` at the statement level. This creates a function object with the given name taking arguments rolled into a list. Functions must return a value.

To call a Function the function `call` can be used. Functions can also be called with `call_with` when arguments are already in a list. 
""",
        examples = 
"""
__Construction__

    lambda(hello_person, args) {
        var name = cast(pop(args), String);
        print("Hello %s!", name);
        return None;
    };
    
    call(hello_person, $(String, "Dan"));
    
__Mapping__

    lambda(hello_person, args) {
        var name = cast(pop(args), String);
        print("Hello %s!", name);
        return None;
    };

    var names = new(Array, 3, 
    $(String, "Dan"), 
    $(String, "Robert"), 
    $(String, "Chris"));

    map(names, hello_name);
    delete(names);
    
__Multiple Arguments__

    lambda(add_print, args) {
        int fst = as_long(cast(at(args, 0), Int));
        int snd = as_long(cast(at(args, 1), Int));
        println("%i + %i = %i", $(Int, fst), $(Int, snd), $(Int, fst+snd));
        return None;
    };

    /*
    ** Notice arguments to "call" in curried form.
    ** Use "call_with" for uncurried calling.
    */
    call(add_print, $(Int, 10), $(Int, 21));
    
__C-Functions__
    
    /*
    ** We can use normal c-functions too.
    ** If they have all argument types as "var".
    ** Then they can be uncurried.
    */
    var Welcome_Pair(var fst, var snd) {
        print("Hello %s and %s!\\n", fst, snd);
        return None;
    };

    lambda_uncurry(welcome_uncurried, Welcome_Pair, 2);

    call(welcome_uncurried, $(String, "John"), $(String, "David"));
    
"""
    ),

    List = cello_type(
        tag  = "Sequential Collection",
        implements = "New Assign Copy Eq Collection Push At Iter Reverse Sort Append Show",
        related = "Array",
        description = 
"""
List is data structure containing a sequence of pointers to Cello objects. It can dynamically grow and shrink in size depending on how many elements it contains. It is a [Collection](/documentation/containers) meaning it does not allocate storage for the objects inside and is not responsible for their destruction.

As it only contains pointers a List can contain several different types of objects, but if this is the case the user must ensure operations remain valid against all the contained types. For example to check if a list of `String` and `Int` contains a specific `Int`, the equality operation must be valid when comparing a `String` and an `Int`.

Elements are ordered linearly. They can be accessed by their position in this sequence directly. Addition and removal of elements at the end of the sequence is fast, with memory movement required for elements in the middle of the sequence. 

The equivalent C++ construct to this type is a [std::vector](http://www.cplusplus.com/reference/vector/vector/) of pointers.
""",
        examples = 
"""
__Construction & Deletion__

    var i0 = new(String, "Test");
    var i1 = new(Int, 6);
    
    var x = new(List, 2, i0, i1);
    show(x); /* <'List' At 0x0000000000414603 ["Test", 6]> */
    delete(x);
    
    delete(i0);
    delete(i1);
    
__Element Access__

    var i0 = new(String, "Test");
    var i1 = new(Int, 6);
    var i2 = new(Real, 5.2);
    
    var x = new(List, 2, i0, i1);
    show(at(x, 0)); /* "Test" */
    show(at(x, 1)); /* 6 */
    
    set(x, 0, i2);
    show(at(x, 0)); /* 5.2 */
    
    delete(x);
    
    delete(i0);
    delete(i1);
    delete(i2);

__Collection Queries__

    var i0 = new(Int, 2);
    var i1 = new(Int, 6);
    var i2 = new(Real, 5.2);

    var x = new(List, 3, i0, i1, i2);
    
    show(contains(x, $(Int, 6)));    /* True */
    show($(Int, len(x)));            /* 3 */
    
    discard(x, $(Int, 6));
    
    show(contains(x, $(Int, 6)));    /* False */
    show($(Int, len(x)));            /* 2 */
    show(is_empty(x));               /* False */
    
    clear(x);
    
    show(is_empty(x));               /* True */
  
    delete(x);
    
    delete(i0);
    delete(i1);
    delete(i2);
    
__Iteration__

    var i0 = new(String, "Test");
    var i1 = new(Int, 6);
    var i2 = new(Real, 5.2);
    
    var x = new(List, 3, i0, i1, i1);
    
    foreach(i in x) {
      show(i);
    }
    
    delete(x);
    
    delete(i0);
    delete(i1);
    delete(i2);
"""     
    ),

    Map = cello_type(
        tag  = "Binary Tree Collection",
        implements = "New Assign Copy Eq Collection Dict Iter Show",
        related = "Tree Dictionary Table",
        description = 
"""
Map is a binary tree data structure mapping keys to values. It is a [Collection](/documentation/containers) meaning it does not allocate storage for either the keys or the values places into it and it is not responsible for their destruction.

Key objects must implement `Ord` and `Eq` and as with `List` this implementation must be meaningful across all key types added to the map.

Maps provide O(log n) operation speeds for deletion, insertion and retrival making them a balanced overall data structure.

The equivalent C++ construct to this type is a [std::map](http://www.cplusplus.com/reference/map/map/) of pointers.
""",
        examples = 
"""
__Creation__

    var prices = new(Map);
    var k0 = new(String, "Apple");
    var k1 = new(String, "Banana");
    var v0 = new(Int, 10);
    var v1 = new(Int, 20);
    
    put(prices, k0, v0);
    put(prices, k1, v1);
    
    foreach(k in prices) {
        println("The Price of %s is %i", k, get(prices, k));
    }
    
    delete(prices);
    delete(k0); delete(k1);
    delete(v0); delete(v1);
"""
    ),

    NoneType = cello_type(
        tag  = "Empty Value",
        implements = "Eq Ord Hash AsChar AsLong AsDouble AsStr Show",
        related = "Bool Int",
        description = 
"""
`None` is a direct alias of `False` and is used idomatically in Cello code to represent a NULL, Empty or Non-Value. As None is just an alias of `False` it will evaluate to false in `if` blocks.

`None` shouldn't be confused with `Undefined` - which is used instead to represent an Errorous or Unspecified value. For example putting `None` into a `List` is perfectly valid but `Undefined` is not.

Also provided is `Some`, an alias to `True`. This can be used idomatically to indicate a single unspecified value.
""",
        examples = 
"""
__Usage__
    
    if (len(self) == 0) return None;

    var best = at(self, 0);
    foreach(item in self) {
        if_lt(item, best) {
            best = item;
        }
    }

    return best;
"""
    ),

    Int = cello_type(
        tag  = "Basic Integer Type",
        implements = "New Assign Copy Eq Ord Hash AsLong AsDouble Num Serialize Show",
        related = "Real Bool Char",
        description =
"""
Basic wrapper of standard C `long`.
""",
        examples = 
"""
__Usage__

    var i0 = $(Int, 1);
    var i1 = new(Int, 24313);
    var i2 = copy(i0);
    
    show(i0); /* 1 */
    show(i1); /* 24313 */
    show(i2); /* 1 */
    
    delete(i1);
    delete(i2);
    
__Maths__
    
    var i0 = $(Int, 0);
    
    show(i0); /* 0 */
    
    add(i0, $(Int, 10)); /* 10 */
    mul(i0, $(Int, 3));  /* 30 */
    div(i0, $(Int, 2));  /* 15 */
    
    if_gt(i0, $(Int, 10)) {
        print("%i is greater than 10!", i0);
    }
    
"""
    ),

    Real = cello_type(
        tag  = "Basic Float Point Type",
        implements = "New Assign Copy Eq Ord Hash AsDouble AsLong Num Serialize Show",
        related = "Int",
        description = 
"""
Basic wrapper of standard C `double`.
""",
        examples = 
"""
__Usage__

    var r0 = $(Real, 1.0);
    var r1 = new(Real, 24.313);
    var r2 = copy(r0);
    
    show(r0); /* 1.0 */
    show(r1); /* 24.313 */
    show(r2); /* 1.0 */
    
    delete(r1);
    delete(r2);
    
__Maths__
    
    var r0 = $(Real, 0.0);
    
    show(r0); /* 0 */
    
    add(r0, $(Real, 10.1)); /* 10.1 */
    mul(r0, $(Real, 3.5));  /* 35.35 */
    div(r0, $(Real, 2.0));  /* 17.675 */
    
    if_gt(r0, $(Real, 11.1)) {
        print("%f is greater than 11.1!", i0);
    }
    
"""
    ),

    Pool = cello_type(
        tag  = "Reference Counting Pool",
        implements = "New Retain Collection Dict",
        related = "Reference Dictionary",
        description = 
"""
Pool provides a method for reference counting of Cello objects via `retain` and `release`. It stores a reference count for any objects included in it and will perform destruction on those objects when their reference count reaches zero.

This is designed to aid in memory management.
""",
        examples = 
"""
__Usage__

    var p = new(Pool);
    
    lambda(table_fill, args) {
        var t = at(args, 0);
        put(t, $(String, "First"),  $(Real, 0.0));
        put(t, $(String, "Second"), $(Real, 0.1));
        put(t, $(String, "Third"),  $(Real, 5.7));
        release(p, t);
        return None
    };
    
    lambda(table_process, args) {
        var t = at(args, 0);
        put(t, $(String, "First"), $(Real, -0.65));
        release(p, t);
        return None;
    };

    var x = retain(p, new(Table, String, Real));

    call(table_fill, retain(p, x));
    call(table_process, retain(p, x));

    release(p, x);

"""        
    ),

    Reference = cello_type(
        tag  = "Basic Reference Type",
        implements = "New Assign Copy Eq Hash At With Show",
        related = "Pool",
        description = 
"""
Reference is a basic type providing a level of indirection to an object. It can be used like a pointer to store only references in contains such as Array or Table.

It can also be used in conjunction with `With` to declare object lifetimes. Or a number of other tricks. A reference is _dereferenced_ using `at(r, 0)` and assigned using `set(r, 0, x)`.
""",
        examples = 
"""
__Single Lifetime__

    with(liferef in $(Reference, new(String, "Life is long"))) {
        println("This reference is: %$", liferef);
        println("This string is alive: '%s'", at(liferef,0));
    }

    print("Now it has been cleared up!\n");

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
"""
    ),

    String = cello_type(
        tag  = "Basic String Type",
        implements = "New Assign Copy Eq Ord Collection Hash Reverse AsStr Append Format Show",
        related = "Char",
        description = 
"""
String provides a basic wrapper for the C `char*` type.

As well as wrapping the C string type it can also provide a number of other operations such as concatination and reversal for strings allocated on the heap. For these it will dynamically reallocate more memory if required making it significantly easier on mental overhead than C strings.

One must be careful when using strings not to attempt to modify strings allocated on the stack - as this will usually throw a bad error.
""",
        examples = 
"""
__Creation__
    
    /* Stack String must not be edited */
    var s0 = $(String, "Hello");
    
    /* Heap String can be freely edited */
    var s1 = new(String, "There");
    append(s1, $(String, " There"));
    
    delete(s1);
    
__Manipulation__

    var s0 = new(String, "Balloons");
    
    show($(Int, len(s0))); /* 8 */
    show(contains(s0, $(String, "Ball")));     /* True */
    show(contains(s0, $(String, "oon")));      /* True */
    show(contains(s0, $(String, "Balloons"))); /* True */
    show(contains(s0, $(Char, 'l')));          /* True */
    
    discard(s0, $(String, "oons"));
    
    show(eq(s0, $(String, "Ball"))); /* True */
    
    clear(s0);
    
    show($(Int, len(s0))); /* 0 */
    show(eq(s0, s0, $(String, ""))); /* True */
    
    delete(s0);
"""
    ),

    Table = cello_type(
        tag  = "Hashtable Container",
        implements = "New Assign Copy Eq Collection Dict Iter Show",
        related = "Dictionary Tree Map",
        description = 
"""
Table is a Hashtable container mapping a keys to values. The keys and values must each be a single type. `Hash` and `Eq` must be defined for the key types. It is a [Container](/documentation/containers) meaning it allocates storage for the keys and values specified. It also deallocates and destroys the objects inside upon destruction.

Data is copied into the container using `assign` meaning that must be defined for both key and value types.

As it is a Hashtable Dictionary provides O(1) performance for element access in the best case and O(n) in the worst.
""",
        examples =
"""
__Usage__

    var prices = new(Table, String, Int);
    put(prices, $(String, "Apple"),  $(Int, 12)); 
    put(prices, $(String, "Banana"), $(Int,  6)); 
    put(prices, $(String, "Pear"),   $(Int, 55));

    foreach (key in prices) {
        var price = get(prices, key);
        println("Price of %$ is %$", key, price);
    }
    
    delete(prices);
    
    
__Manipulation__

    var t = new(Table, String, Int);
    put(t, $(String, "Hello"), $(Int, 2));
    put(t, $(String, "There"), $(Int, 5));
    
    show($(Int, len(t))); /* 2 */
    show(contains(t, $(String, "Hello"))); /* True */
    
    discard(t, $(String, "Hello"));
    
    show($(Int, len(t))); /* 1 */
    show(contains(t, $(String, "Hello"))); /* False */
    show(contains(t, $(String, "There"))); /* True  */
    
    clear(t);
    
    show($(Int, len(t))); /* 0 */
    show(contains(t, $(String, "Hello"))); /* False */
    show(contains(t, $(String, "There"))); /* False */
    
    delete(t);
"""
    ),

    Tree = cello_type(
        tag  = "Binary Tree Container",
        implements = "New Assign Copy Eq Collection Dict Iter Show",
        related = "Map Table Dictionary",
        description = 
"""
Tree is a binary tree container mapping keys to values. It is a [Container](/documentation/containers) meaning allocates storage for the contained keys and values types and will destroy them upon destruction.

Key objects must implement `Ord` and `Eq`. Contents are copied into this container using `assign` which means both keys and values must also implement that.

Trees provide O(log n) operation speeds for deletion, insertion and retrival making them a balanced overall data structure.

The equivalent C++ construct to this type is a [std::map](http://www.cplusplus.com/reference/map/map/).
""",
        examples = 
"""
__Usage__

    var t0 = new(Tree, String, Int);
    put(t0, $(String, "Hello"), $(Int, 2));
    put(t0, $(String, "There"), $(Int, 5));
    
    var t1 = new(Tree, String, Int);
    put(t1, $(String, "Bonjour"), $(Int, 9));
    put(t1, $(String, "Where"), $(Int, 5));
    
    delete(t0);
    delete(t1);

    
__Manipulation__

    var t = new(Tree, String, Int);
    put(t, $(String, "Hello"), $(Int, 2));
    put(t, $(String, "There"), $(Int, 5));
    
    show($(Int, len(t))); /* 2 */
    show(contains(t, $(String, "Hello"))); /* True */
    
    discard(t, $(String, "Hello"));
    
    show($(Int, len(t))); /* 1 */
    show(contains(t, $(String, "Hello"))); /* False */
    show(contains(t, $(String, "There"))); /* True */
    
    clear(t);
    
    show($(Int, len(t))); /* 0 */
    show(contains(t, $(String, "Hello"))); /* False */
    show(contains(t, $(String, "There"))); /* False */
    
    delete(t);
"""
    ),

    Type = cello_type(
        tag  = "Metadata Type Object",
        implements = "New AsStr Show",
        related = "",
        description = 
"""
`Type` is one of the most important Types in Cello. It provides metadata about an object including which classes it implements. One can get the type of an object using the `type_of` function.

To see if a type implements a class `type_implements` can be used. To call a function of a class, implemented `type_class_method` can be used.

`cast` can be used to do runtime type checking. It checks a given object has a certain type and if so returns the given object.

""",
        examples = 
"""
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

"""
    ),
    
    Thread = cello_type(
        tag = "Concurrent Processes",
        implements = "New Assign Copy Call Process AsLong",
        related = "Mutex Function",
        description = 
"""
A basic Thread primative. These can be constructed with some `Function` type and then called with a number of arguments.
""",
        examples = 
"""
__Usage__

    lambda(f, args) {
        println("Hello from thread %$!", current(Thread));
        return None;
    };
    
    var t = new(Thread, f);    
    call(t, None);
    join(t);
    
    delete(t);
"""
    ),
    
    Mutex = cello_type(
        tag = "Mutual Exclusion Lock",
        implements = "New Assign Copy Lock With",
        related = "Thread Function",
        description =
"""
A basic Mutual Exclusion Primative. Used to lock around resources such that no two threads can enter the same block of code. Either `lock` and `unlock` can be used or `with`.
""",
        examples =
"""
__Usage__

    var mutex = new(Mutex);
    var total = $(Int, 0);
    
    lambda(f, args) {
        with(m in mutex) {
            add(total, $(Int, 1));
        }
        return None;
    };
    
    var threads = new(List, 5,
        new(Thread, f), new(Thread, f),
        new(Thread, f), new(Thread, f),
        new(Thread, f));
        
    foreach(t in threads) {
        call(t, None);
    }
    
    foreach(t in threads) {
        join(t);
        delete(t);
    }
    
    show(total); /* 5 */
    
    delete(threads);
    delete(mutex);
"""
    ),

)
