
def class_set(**classes):
    
    for k in classes.keys():
        
        classes[k]["name"] = k
        classes[k]["link"] = k.lower()
        classes[k]["filename"] = "reference_" + k.lower() + ".md"
        
        for x in ["description", "examples", "signature"]:
            if not (x in classes[k]): classes[k][x] = "\nComing Soon...\n"
        
        if not ("methods" in classes[k]): classes[k]["methods"] = []
        
    return classes

cello_classes = class_set(

    Format = dict(
        tag     = "Read or Writable using a Format String",
        funcs   = "format_to format_from",
        related = "Show Stream",
        signature = 
    """
    class {
      int (*format_to)(var,int,const char*,va_list);
      int (*format_from)(var,int,const char*,va_list);
    } Format;
    """,
        methods = [
             {
                "code" : ["int format_to(var self, int pos, const char* fmt, ...);", "int format_to_va(var self, int pos, const char* fmt, va_list va);"],
                "description" : "Write a formatted string to an object from some values",
                "parameters" :
                [
                    ("self" , "Object to Format to"),
                    ("pos"  , "Position in Stream"),
                    ("fmt"  , "Format String"),
                    ("..."  , "List of values to be formatted")
                ],
                "return" : "number of characters written"
            },
            {
                "code" : ["int format_from(var self, int pos, const char* fmt, ...);", "int format_from_va(var self, int pos, const char* fmt, va_list va);"],
                "description" : "Read a formatted string from an object into some values",
                "parameters" :
                [
                    ("self" , "Object to Format From"),
                    ("pos"  , "Position in Stream"),
                    ("fmt"  , "Format String"),
                    ("..."  , "List of values to be formatted into")
                ],
                "return" : "number of arguments scanned"
            },
            
        ],
        description =
"""
Format abstracts the class of operations such as `scanf`, `sprintf` and `fprintf` with matching semantics. It provides general `printf` and `scanf` functionality for several different types objects in a homogenius way. This class is used by the `Show` functions to write output.

It is important to note that the semantics of these options match `printf` and not the newly defined `Show` class. For example it is perfectly valid to pass a C `int` to these functions, while that would crash the `println` function from Show which must be passed only `var` objects. 
""",
        examples = 
"""
__Usage__
    
    /* printf("Hello my name is %s, I am %i\\n", "Dan", 23); */
    format_to($(File, stdout), 0, "Hello my name is %s, I am %i\\n", "Dan", 23);
    
"""
    ),

    Show = dict(
        tag     = "Write To or Read From String",
        funcs   = "show print look scan",
        related = "Format Stream",
        signature = 
    """
    class {
      int (*show)(var,var,int);
      int (*look)(var,var,int);
    } Show;
    """,
        methods = [
            {
                "code" : ["int show(var self);", "int show_to(var self, var out, int pos);"],
                "description" : "Writes an Object",
                "parameters" : [
                    ("self" , "Object to write as String"),
                    ("out"  , "Format object to write to. For `show` this is `stdout`"),
                    ("pos"  , "Position in output object")
                ],
                "return" : "Updated Position in output object"
            },
            {
                "code" : [
                    "int print(const char* fmt, ...);",
                    "int println(const char* fmt, ...);",
                    "int print_to(var out, int pos, const char* fmt, ...);",
                    "int print_va(const char* fmt, va_list va);",
                    "int print_to_va(var out, int pos, const char* fmt, va_list va);"],
            
                "description" : "Use a format string to write several objects",
                "parameters" : [
                    ("out" , "Format object to write to. For `print`, `println` and `print_va` this is `stdout`"),
                    ("fmt" , "Format string"),
                    ("pos" , "Position in output object"),
                    ("..." , "Objects used in format string")
                ],
                "return" : "Updated Position in output object"
            },
            {
                "code" : ["int look(var self);", "int look_from(var self, var input, int pos);"],
                "description" : "Reads an Object",
                "parameters" : [
                    ("self" , "Object to read into"),
                    ("out"  , "Format object to read from. For `look` this is `stdout`"),
                    ("pos"  , "Position in input object")
                ],
                "return" : "Updated Position in input object"
            },
            {
                "code" : [
                    "int scan(const char* fmt, ...);",
                    "int scanln(const char* fmt, ...);",
                    "int scan_from(var input, int pos, const char* fmt, ...);",
                    "int scan_va(const char* fmt, va_list va);",
                    "int scan_from_va(var input, int pos, const char* fmt, va_list va);"],
            
                "description" : "Use a format string to read several objects",
                "parameters" : [
                    ("input" , "Format object to write to. For `scan`, scanln` and `scan_va` this is `stdout`"),
                    ("fmt"   , "Format string"),
                    ("pos"   , "Position in input object"),
                    ("..."   , "Objects read from format string")
                ],
                "return" : "Updated Position in input object"
            },
        ],
        description = 
"""
Show is the standard class used to convert objects to, and from, a String representation. Objects which implement show should expect the input/output object to support the `Format` class.

The `print`, `println` and `print_to` functions provide a mechanism for writing formatted strings. To do this they provide a new format specifier `%$` which uses an object's `Show` functionality to write to String. All objects which don't support `Show` can still be shown via a default implementation. 

All the `Show` methods which are variable arguments should only be passed `var` type objects and should never be passed native C types. To print native C types wrap them in Cello types using `$` (see examples below).

Standard format specifiers such as `%f` and `%d` will call functions such as `as_double` and `as_long` on their passed in arguments to convert to a C type before performing the standard C formatting behaviour.

See [printf](http://www.cplusplus.com/reference/cstdio/printf/) for more information on format specifiers.
""",
        examples = 
"""
__Hello World__
    
    println("Hello %s!", $(String, "World"));
    
__File Writing__

    with(file in stream_open($(File, NULL), "prices.txt", "wb")) {
  
        print_to(file, 0, "%$ :: %$\\n", $(String, "Banana"), $(Int, 57));
        print_to(file, 0, "%$ :: %$\\n", $(String, "Apple"),  $(Int, 22));
        print_to(file, 0, "%$ :: %$\\n", $(String, "Pear"),   $(Int, 16));
        
        return None;
    };

    
__String Scanning__
    
    var input = $(String, "1 and 52 then 78");
    
    var i0 = new(Int, 0);
    var i1 = new(Int, 0);
    var i2 = new(Int, 0);
    
    scan_from(input, 0, "%i and %i then %i", i0, i1, i2);
    
    /* i0: 1, i1: 52, i2: 78 */
    println("i0: %$, i1: %$, i2: %$", i0, i1, i2);
    
__String Writing__

    var greeting = new(String, "");
    print_to(greeting, 0, "Hello %s %s, %s?", $(String, "Mr"), $(String, "Johnson"), $(String, "how are you?"));
    
    /* Hello Mr Johnson, how are you? */
    show(greeting);
    
"""
    ),

    Call = dict(
        tag     = "Callable like a Function",
        funcs   = "call",
        related = "Process",
        signature =
    """
    class {
      var (*call_with)(var,var);
    } Call;
    """,
        methods = 
        [
            {
                "code" : ["#define call(x, ...) call_with_ptr(x, (var[]){ __VA_ARGS__, (var)-1 })",
                          "var call_with_ptr(var self, var* args);",
                          "var call_with(var self, var args);"],
                "description" : "Call a function with some arguments",
                "parameters" : [
                    ("self", "Object to call"),
                    ("args", "List of arguments to call with")
                ],
                "return" : "Returned value of Callable"
            }
        ],
        description = 
"""
Class for types which are _callable_ such as a function. That it some object that can be passed a number of arguments and return an object back.

Use the `call` macro to call in uncurried form, passing the arguments directly to the function. Use `call_with` to call in curried form, passing in a single List.
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
    
__Multiple Arguments__

    lambda(add_print, args) {
        int fst = as_long(cast(at(args, 0), Int));
        int snd = as_long(cast(at(args, 1), Int));
        println("%i + %i = %i", $(Int, fst), $(Int, snd), $(Int, fst+snd));
        return None;
    };

    call(add_print, $(Int, 10), $(Int, 21));
    
    var args = new(List, 2, $(Int, 10), $(Int, 21));
    call_with(add_print, args);
    delete(args);
    
__Threads__

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

    Num = dict(
        tag     = "Can perform arithmetic",
        funcs   = "add sub mul div negate absolute",
        related = "AsLong AsDouble",
        signature = 
    """
    class {
      void (*add)(var, var);
      void (*sub)(var, var);
      void (*mul)(var, var);
      void (*div)(var, var);
      void (*negate)(var);
      void (*absolute)(var);
    } Num;
    """,
        methods = [
            {
                "code" : ["void add(var self, var obj);"],
                "description" : "Add one object to another",
                "parameters" : [
                    ("self", "Object to change"),
                    ("obj", "Object value to add")
                ],
                "return" : "None"
            },
            {
                "code" : ["void sub(var self, var obj);"],
                "description" : "Subtract one object from another",
                "parameters" : [
                    ("self", "Object to change"),
                    ("obj", "Object value to subtract")
                ],
                "return" : "None"
            },
            {
                "code" : ["void mul(var self, var obj);"],
                "description" : "Multiply one object by another",
                "parameters" : [
                    ("self", "Object to change"),
                    ("obj", "Object value to multiply")
                ],
                "return" : "None"
            },
            {
                "code" : ["void divide(var self, var obj);"],
                "description" : "Divide one object by another",
                "parameters" : [
                    ("self", "Object to change"),
                    ("obj", "Object value to divide")
                ],
                "return" : "None"
            },
            {
                "code" : ["void negate(var self);"],
                "description" : "Negate an object",
                "parameters" : [
                    ("self", "Object to negate"),
                ],
                "return" : "None"
            },
            {
                "code" : ["void absolute(var self);"],
                "description" : "Make an object absolute",
                "parameters" : [
                    ("self", "Object to make absolute"),
                ],
                "return" : "None"
            }       
        ],
        description =
"""
The `Num` class provides an interface for doing arithematic on objects.

The most important thing to note is that these operations don't return a value. They are destructive on the first argument. This is in the name of speed and memory management. If every operation returned a new object there would be lots of objects to clean up and a lot of overhead in memory allocation.

If users require new objects they are encouraged to make copies of existing objects and then modify them using these methods.
""",
        examples = 
"""
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
    
"""     
    ),

    Retain = dict(
        tag     = "Can be used for reference counting",
        funcs   = "retain release",
        related = "With",
        signature = 
    """
    class {
      var (*retain)(var p, var x);
      void (*release)(var p, var x);
    } Retain;
    """,
        methods = [
            {
                "code" : ["var retain(var p, var x);"],
                "description" : "Retain another reference to `x` in `p`",
                "parameters" : [
                    ("p", "Object which to retain a reference in"),
                    ("x", "Referenced Object"),
                ],
                "return" : "Referenced Object"
            },
            {
                "code" : ["void release(var p, var x);"],
                "description" : "Release a reference to `x` in `p`",
                "parameters" : [
                    ("p", "Object which to release a reference in"),
                    ("x", "Referenced Object"),
                ],
                "return" : "Referenced Object"
            }
        ],
    description =
"""
The `Retain` class provides an interface to reference counting behaviour to objects using a reference pool or other structure. This can ease memory management as the number of code locations that still require an object to exist can be monitored.

Users call `retain` to increment the reference count of an object and `release` to decrement. Upon reaching a zero reference count typically an object will be destructed and deallocated.
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

    New = dict(
        tag     = "Constructable on the Heap",
        funcs   = "new delete construct destruct",
        related = "Assign Copy",
        signature = 
    """
    class {
      size_t size;
      var (*construct)(var, va_list*);
      var (*destruct)(var);
    } New;
    """,
        methods = [
            {
                "code" : ["var new(var type, ...);"],
                "description" : "Create a new object of a certain type on the heap.",
                "parameters" : [
                    ("type", "Type to create"),
                    ("...", "Arguments to be passed to constructor"),
                ],
                "return" : "New Object"
            },
            {
                "code" : ["void delete(var obj);"],
                "description" : "Delete an object created on the heap.",
                "parameters" : [
                    ("obj", "Object to delete"),
                ],
                "return" : "None"
            },
            {
                "code" : ["var allocate(var type);"],
                "description" : "Allocate space for an object of a certain type.",
                "parameters" : [
                    ("type", "Type to allocate space for"),
                ],
                "return" : "Blank object of certain type"
            },
            {
                "code" : ["void deallocate(var obj);"],
                "description" : "Free the space allocated by a certain object.",
                "parameters" : [
                    ("obj", "Object to free the memory for"),
                ],
                "return" : "None"
            },
            {
                "code" : ["var construct(var obj, ...);"],
                "description" : "Call the constructor of an object.",
                "parameters" : [
                    ("obj", "Object to call constructor on"),
                    ("...", "Arguments to be passed to constructor")
                ],
                "return" : "Newly Constructed Object"
            },
            {
                "code" : ["var destruct(var obj);"],
                "description" : "Call the destructor of an object.",
                "parameters" : [
                    ("obj", "Object to call destructor on")
                ],
                "return" : "Newly Destructed Object"
            }
        ],
        description = 
"""
The `New` class provides a method to implement dynamic (heap) memory allocation for certain object types as well as _constructor_ and _destructor_ functions to be called just after an object's memory space has been allocated and just before it's memory allocation is freed. To implement this class you must also give the memory size of the data object to allocated.

The `new` function uses C variable arguments to provide a method of passing arguments to an object's constructor. Unfortunately the exact type and order of these arguments cannot be checked by the compiler so it is up to the users to refer to the documentation to see how a certain type of object is correctly constructed. Incorrect construction will simply crash the program.
""",
        examples =
"""
__Usage__

    var x = new(Int, 1);
    
    show(x); /* 1 */
    show(type_of(x)) /* Int */
    
    delete(x);
    
    var y = $(Real, 0.0);  
    
    show(y); /* 0.0 */
    construct(y, 1.0);
    show(y); /* 1.0 */
    
    var z = allocate(String);
    construct(z, "Hello");
    
    show(z); /* Hello */
    z = destruct(z);
    deallocate(z);
    
"""
    ),

    Assign = dict(
        tag     = "Assignable to",
        funcs   = "assign",
        related = "Copy New",
        signature = 
    """
    class {
      void (*assign)(var, var);
    } Assign;    
    """,
        methods = [
            {
                "code" : ["void assign(var self, var obj);"],
                "description" : "Assign the value of one object to another.",
                "parameters" : [
                    ("self", "Object to get assigned to"),
                    ("obj", "Object to assign"),
                ],
                "return" : "None"
            }
        ],
        description = 
"""
The `Assign` class lets one assign a value from one object to another. This essentially means copying the contents of `obj` into `self`.

This class is important to implement as it is used extensively by contains to give allocated space values. Also for this reason one should not assume anything about the state of `self` (for example it may not have been constructed).
""",
        examples = 
"""
__Usage 1__

    var x = new(Int, 10);
    var y = new(Int, 20);
    
    show(x); /* 10 */
    show(y); /* 20 */

    assign(x, y);
    
    show(x); /* 20 */
    show(y); /* 20 */
    
    delete(x);
    delete(y);


__Usage 2__

    var x = new(String, "Hello");
    var y = new(String, "There");
    
    show(x); /* Hello */
    show(y); /* There */
    
    assign(x, y);
    
    show(x); /* There */
    show(y); /* There */
    
    delete(x);
    delete(y);
"""
    ),

    Copy = dict(
        tag     = "Copyable",
        funcs   = "copy",
        related = "New Assign",
        signature = 
    """
    class {
      var (*copy)(var);
    } Copy;
    """,
        methods = [
            {
                "code" : ["var copy(var obj);"],
                "description" : "Make a copy of an object.",
                "parameters" : [
                    ("obj", "Object to copy"),
                ],
                "return" : "Copy of Object"
            }
        ],
        description = 
"""
The `Copy` class allows for a user to make a copy of an object. This copy must be deleted by the user.

By convention `copy` means a deep copy. That is a copy that also copies all inner components of the object.
""",
        examples =
"""
__Usage__
    
    var x = new(String, "Hello");
    var y = copy(x);
    
    show(x); /* Hello */
    show(y); /* Hello */
    show(x is y); /* False */
    
    delete(x);
    delete(y);
"""
    ),

    Eq = dict(
        tag     = "Comparable for Equality",
        funcs   = "eq neq if_eq if_neq",
        related = "Ord",
        signature =
    """
    class {
      var (*eq)(var,var);
    } Eq;
    """,
        methods = [
            {
                "code" : ["var eq(var self, var obj);"],
                "description" : "Test if two objects are considered equal.",
                "parameters" : [
                    ("self", "First Object"),
                    ("obj", "Second Object"),
                ],
                "return" : "Equality Truth Value"
            },
            {
                "code" : ["var neq(var self, var obj);"],
                "description" : "Test if two objects are considered not equal.",
                "parameters" : [
                    ("self", "First Object"),
                    ("obj", "Second Object"),
                ],
                "return" : "Equality Truth Value"
            }
        ],
        description =
"""
The `Eq` class provides a generic way to test for equality between two objects.

As well as `eq` and `neq` two macros are provided to test like an `if` statement. `#define if_eq(X,Y) if(eq(X,Y))` and `#define if_neq(X,Y) if(neq(X,Y))`.

A default implementation is provided by all types which compares memory location.

This default implementation is the same as `is` and `isnt`. While an implementation of Equality tests for equal values, `is` and `isnt` only test to see if two objects _are the same object_ in respect to their memory location.
""",
        examples = 
"""
__Usage__
    
    show(  eq($(Int, 1 ), $(Int, 1 )) ); /* True */
    show( neq($(Int, 2 ), $(Int, 20)) ); /* True */
    show( neq($(String, "Hello"), $(String, "Hello")) ); /* False */
    show(  eq($(String, "Hello"), $(String, "There")) ); /* False */

    var a = $(Int, 1);
    var b = $(Int, 1);
    
    show( eq(a, b) ); /* True */
    show( a is b );  /* False */
    show( a isnt b ); /* True */
    
__Macros__
    
    var x = $(String, "Foo");
    var y = $(String, "Foo");
    
    if_eq(x, y) {
        println("Foo!");
    } else {
        println("Foo! ????");
    }
    
"""
    ),

    Ord = dict(
        tag     = "Comparable for Ordering",
        funcs   = "gt lt ge le",
        related = "Eq",
        signature =
    """
    class {
      var (*gt)(var,var);
      var (*lt)(var,var);
    } Ord;
    """,
        methods = [
            {
                "code" : ["var gt(var self, var obj);"],
                "description" : "Test if one object is greater than other.",
                "parameters" : [
                    ("self", "First Object"),
                    ("obj", "Second Object"),
                ],
                "return" : "Equality Truth Value"
            },
            {
                "code" : ["var lt(var self, var obj);"],
                "description" : "Test if one object is less than other.",
                "parameters" : [
                    ("self", "First Object"),
                    ("obj", "Second Object"),
                ],
                "return" : "Equality Truth Value"
            },
            {
                "code" : ["var ge(var self, var obj);"],
                "description" : "Test if one object is not less than other.",
                "parameters" : [
                    ("self", "First Object"),
                    ("obj", "Second Object"),
                ],
                "return" : "Equality Truth Value"
            },
            {
                "code" : ["var le(var self, var obj);"],
                "description" : "Test if one object is not greater than other.",
                "parameters" : [
                    ("self", "First Object"),
                    ("obj", "Second Object"),
                ],
                "return" : "Equality Truth Value"
            }
        ],
        description = 
"""
The `Ord` class provides an ordering relationship between objects of a certain type. This allows for one to test if some object is considered _Greater Than_ or _Less Than_ another.

The compliments of these are also provided in `le` and `ge`.

Similarly to the `Eq` class macros are provided to allow for testing like an `if` statement

    #define if_lt(X,Y) if(lt(X,Y))
    #define if_gt(X,Y) if(gt(X,Y))
    #define if_le(X,Y) if(le(X,Y))
    #define if_ge(X,Y) if(ge(X,Y))

Ordering is required for some standard containers and collections.

Strings are ordered in alphabetical order.
""",
        examples = 
"""
__Usage__

    show(  gt($(Int, 15), $(Int, 3 )) ); /* True */
    show(  lt($(Int, 70), $(Int, 81)) ); /* True */
    show(  lt($(Int, 71), $(Int, 71)) ); /* False */
    show(  ge($(Int, 78), $(Int, 71)) ); /* True */
    show(  gt($(Int, 32), $(Int, 32)) ); /* False */
    show(  le($(Int, 21), $(Int, 32)) ); /* True */
    
__Macros__

    var x = $(String, "Daniel");
    var y = $(String, "Holden");
    
    if_gt(x, y) {
        println("Last Name First");
    } else {
        println("First Name First");
    }

"""
    ),

    Hash = dict(
        tag     = "Hashable to a long",
        funcs   = "hash",
        related = "AsLong",
        signature =
    """
    class {
      long (*hash)(var);
    } Hash;    
    """,
        methods = [
            {
                "code" : ["long hash(var obj);"],
                "description" : "Hash an object to a long integer value.",
                "parameters" : [
                    ("self", "Object"),
                ],
                "return" : "Object Hash"
            }
        ],
        description = 
"""
The `Hash` class provides a way to convert an object into a long integer value. This value must remain the same for objects which are equal but should be evenly distributed for objects which are not equal.

A default implementation of `Hash` is provided for all type using the memory location cast to a long integer.

This is used by the Hashtable like objects such as `Table` and `Dictionary`.
""",
        examples = 
"""
__Usage__

    long x = hash($(Int, 1  )); /* 1   */
    long y = hash($(Int, 123)); /* 123 */
    long z = hash($(Int, 123)); /* 123 */
    
    long a = hash($(String, "Hello"));  /* 511 */
    long b = hash($(String, "There"));  /* 515 */
    long c = hash($(String, "People")); /* 629 */
"""
    ),

    Collection = dict(
        tag     = "Treatable as several objects",
        funcs   = "len clear contains discard",
        related = "Sort Append Push At Reverse Dict Iter",
        signature = 
    """
    class {
      int (*len)(var);
      void (*clear)(var);
      var (*contains)(var, var);
      void (*discard)(var, var);
    } Collection;
    """,
        methods = [
            {
                "code" : ["int len(var self);"],
                "description" : "Give the length of a collection.",
                "parameters" : [
                    ("self", "Collection"),
                ],
                "return" : "Length of Collection"
            },
            {
                "code" : ["void clear(var self);"],
                "description" : "Remove all items from a Collection.",
                "parameters" : [
                    ("self", "Collection"),
                ],
                "return" : "None"
            },
            {
                "code" : ["var contains(var col, val obj);"],
                "description" : "Check if a Collection contains an Object.",
                "parameters" : [
                    ("self", "Collection"),
                    ("obj", "Object"),
                ],
                "return" : "Containment truth value"
            },
            {
                "code" : ["void discard(var self, var obj);"],
                "description" : "Remove an object from a Collection.",
                "parameters" : [
                    ("self", "Collection"),
                    ("obj", "Object"),
                ],
                "return" : "None"
            },
            {
                "code" : ["var is_empty(var self);"],
                "description" : "Check if a collection is empty.",
                "parameters" : [
                    ("self", "Collection"),
                ],
                "return" : "Empty truth value"
            },
            {
                "code" : ["var maximum(var self);"],
                "description" : "Return the largest item in a collection.",
                "parameters" : [
                    ("self", "Collection"),
                ],
                "return" : "Largest Item"
            },
            {
                "code" : ["var minimum(var self);"],
                "description" : "Return the smallest item in a collection.",
                "parameters" : [
                    ("self", "Collection"),
                ],
                "return" : "Smallest Item"
            },
        
        ],
        description = 
"""
The `Collection` class provides an interface for treating data structures as a container or collection of other objects. It provides methods to check the number of items in a collection. It also provides methods to check if a container has an object inside and to discard this object if it does.

Note that the `contains` method uses the `Eq` type class to test for containment. Therefore it does not test for actual exact objects but any two objects that are equal.
""",
        examples =
"""
__Usage__
    var x = new(List, 3, $(Int, 1), $(Real, 2.0), $(String, "Hello"));

    show(len(x)); /* 3 */
    show(contains(x, $(Int, 1)));          /* True */
    show(contains(x, $(Real, 2.0)));       /* True */
    show(contains(x, $(String, "Hello"))); /* True */

    discard(x, $(Real, 2.0));

    show(len(x)); /* 2 */
    show(contains(x, $(Int, 1)));          /* True */
    show(contains(x, $(String, "Hello"))); /* True */
    show(contains(x, $(Real, 2.0)));       /* False */

    clear(x);

    show(len(x));      /* 0 */
    show(is_empty(x)); /* True */

    delete(x);
"""
    ),

    Sort = dict(
        tag     = "Elements can be sorted",
        funcs   = "sort",
        related = "Ord Collection At",
        signature = 
    """
    class {
      void (*sort)(var);
    } Sort;
    """,
        methods = [
            {
                'code' : ['void sort(var self);'],
                'description' : 'Sort an object',
                'parameters' : [
                    ('self', 'object to be sorted'),
                ],
                'return' : 'None'
            }
        ],
        description = 
"""
The `Sort` class provides an interface for sorting an object, typically a collection. Note that in general this means `Ord` needs to be defined across the items in the collection.
""",
        examples =
"""
__Usage__

    var x = new(Array, Real, 4, $(Real, 5.2), $(Real, 7.1), $(Real, 2.2), $(Real, 1.1));
    
    show(x); /* <'Array' At 0x0000000000414603 [5.2, 7.1, 2.2, 1.1]> */
    sort(x);
    show(x); /* <'Array' At 0x0000000000414603 [1.1, 2.2, 5.2, 7.1]> */
    
    delete(x);
"""     
    ),

    Reverse = dict(
        tag     = "Order can be reversed",
        funcs   = "reverse",
        related = "Collection At",
        signature = 
    """
    class {
      void (*reverse)(var);
    } Reverse;
    """,
        methods = [
            {
                'code' : ['void reverse(var self);'],
                'description' : 'Reverse an object',
                'parameters' : [
                    ('self', 'object to be reversed'),
                ],
                'return' : 'None'
            }
        ],
        description = 
"""
The `Reverse` class provides an interface for reversing an object, typically a collection.
""",
        examples =
"""
__Usage__

    var x = new(Array, Real, 4, $(Real, 5.2), $(Real, 7.1), $(Real, 2.2), $(Real, 1.1));
    
    show(x); /* <'Array' At 0x0000000000414603 [5.2, 7.1, 2.2, 1.1]> */
    reverse(x);
    show(x); /* <'Array' At 0x0000000000414603 [1.1, 2.2, 7.1, 5.2]> */
    
    delete(x);
"""
    ),

    Append = dict(
        tag     = "Elements can be added to end",
        funcs   = "append",
        related = "Collection Push At",
        signature = 
    """
    class {
      void (*append)(var, var);
    } Append;
    """,
        methods = [
            {
                'code' : ['void append(var self, var obj);'],
                'description' : 'Append an object to another',
                'parameters' : [
                    ('self', 'object to be appended to'),
                    ('obj', 'object to be append'),
                ],
                'return' : 'None'
            }
        ],
        description = 
"""
The `Append` class provides an interface for appending an object to another, this is typically a collection.
""",
        examples = 
"""
    var x = new(Array, Real, 2, $(Real, 9.9), $(Real, 2.8));
    
    show(x); /* <'Array' At 0x0000000000414603 [9.9, 2.8]> */
    append(x, $(Real, 2.5));
    show(x); /* <'Array' At 0x0000000000414603 [9.9, 2.8, 2.5]> */
    
    delete(x);
"""
    ),

    Iter = dict(
        tag     = "Can be looped over",
        funcs   = "foreach iter_start iter_end iter_next",
        related = "Collection At",
        signature = 
    """
    class {
      var (*iter_start)(var);
      var (*iter_end)(var);
      var (*iter_next)(var, var);
    } Iter;
    """,
        methods = [
            {
                'code' : ['var iter_start(var self);'],
                'description' : 'Start iteration over an object, get the first element.',
                'parameters' : [
                    ('self', 'object to iterate over'),
                ],
                'return' : 'The first object in the iteration'
            },
            {
                'code' : ['var iter_end(var self);'],
                'description' : 'Return an iteration termination object (such as Undefined).',
                'parameters' : [
                    ('self', 'object being iterated over'),
                ],
                'return' : 'An iteration termination object.'
            },
            {
                'code' : ['var iter_next(var self, var curr);'],
                'description' : 'Given the current iteration object return the next. If there is no objects left return an iteration termination object (such as Undefined).',
                'parameters' : [
                    ('self', 'object being iterated over'),
                    ('curr', 'current iteration object'),
                ],
                'return' : 'The next object in the iteration or an iteration termination object.'
            }
        ],
        description = 
"""
The `Iter` class provides a global interface for iteration. It is what allows objects to be iterated over with `foreach` in a uniform way.

Using `iter_next` in a non incremental way is discouraged as it can occasionally cause problems or performance issues.

As iteration does not use an `iterator` object but actually the raw contents of the collection in most cases it should be very fast.

Key-Value mapping data structures will usually provide iteration only over their keys.
""",
        examples =
"""
__Usage__

    var x = new(Array, Int, 3, $(Int, 1), $(Int, 2), $(Int, 5));
    
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
        print("Price of %$ is %$\\n", key, price);
    }
"""
    ),

    Push = dict(
        tag     = "Elements can be Pushed and Popped",
        funcs   = "push pop push_at pop_at",
        related = "Collection At Append",
        signature = 
    """
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
    """,
        methods = [
            {
                'code' : [
                    'void push(var self, var obj);',
                    'void push_at(var self, var obj, int i);',
                    'void push_back(var self, var obj);',
                    'void push_front(var self, var obj);'
                ],
                'description' : 'Push an object onto another.',
                'parameters' : [
                    ('self', 'object to get pushed onto'),
                    ('obj', 'object to push'),
                    ('i', 'position to push at'),
                ],
                'return' : 'None'
            },
            {
                'code' : [
                    'var pop(var self);',
                    'var pop_at(var self, int i);',
                    'var pop_back(var self);',
                    'var pop_front(var self);'
                ],
                'description' : 'Pop an object from another.',
                'parameters' : [
                    ('self', 'object to get popped frm onto'),
                    ('i', 'position to pop from'),
                ],
                'return' : 'Popped Object'
            }
        ],
        description = 
"""
The `Push` class provides an interface for the addition and remove of objects from another  (typically a collection) in a positional sense.

`push` can be used to add new objects to a collection and `pop` to remove them.

In containers `push` uses `assign` to copy in new contents and the result of a `pop` is typically Undefined as it will have been removed from memory and cannot be returned to the user.
""",
        examples = 
"""
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
"""
    ),

    At = dict(
        tag     = "Elements can be directly accessed and set",
        funcs   = "at set",
        related = "Push At Collection",
        signature = 
    """
    class {
      var (*at)(var, int);
      void (*set)(var, int, var);
    } At;
    """,
        methods = [
            {
                'code' : ['var at(var self, int i);'],
                'description' : 'Access an element of an object at a position.',
                'parameters' : [
                    ('self', 'object to be accessed'),
                    ('i', 'position to access at'),
                ],
                'return' : 'Object at that position'
            },
            {
                'code' : ['void set(var self, int i, var obj);'],
                'description' : 'Set an element of an object at a position.',
                'parameters' : [
                    ('self', 'object to be accessed'),
                    ('i', 'position to access at'),
                    ('obj', 'Object to set'),
                ],
                'return' : 'None'
            }
        ],
        description = 
"""
The `At` class provides an interface for positional access and manipulation of objects (typically collections but not always).
""",
        examples =
"""
__Usage__

    var fst = $(Int, 1);
    var snd = $(Real, 2.0);
    var trd = $(String, "Hello");

    var x = new(List, 3, fst, snd, trd);

    show(at(x, 0)); /* 1 */
    show(at(x, 1)); /* 2.0 */
    show(at(x, 2)); /* Hello */
    
    set(x, 1, trd);
    
    show(at(x, 1)); /* Hello */
    
    delete(x);
"""
    ),

    Dict = dict(
        tag     = "Key-Value access to object",
        funcs   = "get put",
        related = "Collection At",
        signature = 
    """
    class {
      var (*get)(var, var);
      void (*put)(var, var, var);
    } Dict;
    """,
        methods = [
            {
                'code' : ['var get(var self, var key);'],
                'description' : 'Access an element of an object at a given key.',
                'parameters' : [
                    ('self', 'object to be accessed'),
                    ('key', 'key object to access at'),
                ],
                'return' : 'object at that key'
            },
            {
                'code' : ['void put(var self, var key, var val);'],
                'description' : 'Set an element of an object at a given key.',
                'parameters' : [
                    ('self', 'object to be accessed'),
                    ('key', 'key object to access at'),
                    ('obj', 'object to set'),
                ],
                'return' : 'None'
            }
        ],
        description = 
"""
The `At` class provides an interface for key-value access and manipulation of objects (typically collections).
""",
        examples = 
"""
__Usage__

    var prices = new(Table, String, Int);
    put(prices, $(String, "Apple"),  $(Int, 12)); 
    put(prices, $(String, "Banana"), $(Int,  6)); 
    put(prices, $(String, "Pear"),   $(Int, 55)); 
    
    var pear_price = get(prices, $(String, "Pear"));
    var banana_price = get(prices, $(String, "Banana"));
    var apple_price = get(prices, $(String, "Apple"));
    
    show(pear_price);   /* 55 */
    show(banana_price); /*  6 */
    show(apple_price);  /* 12 */
"""
    ),

    AsChar = dict(
        tag     = "Representable as C char",
        funcs   = "as_char",
        related = "AsStr",
        signature = 
    """
    class {
      char (*as_char)(var);
    } AsChar;
    """,
        methods = [
            {
                'code' : ['char as_char(var self);'],
                'description' : 'represent object as C `char`',
                'parameters' : [
                    ('self', 'object to represent'),
                ],
                'return' : 'C `char` representation of object'
            }
        ],
        description = 
"""
The `AsChar` class allows a user to represent an object as a C `char`. It is used by the native type wrapper `Char`.
""",
        examples = 
"""
__Usage__

    putc(as_char($(Char, 'a'))); /* a */
    putc(as_char($(Char, 'b'))); /* b */
    
"""
    ),

    AsStr = dict(
        tag     = "Representable as C char*",
        funcs   = "as_str",
        related = "AsChar",
        signature =
    """
    class {
      const char* (*as_str)(var);
    } AsStr;
    """,
        methods = [
            {
                'code' : ['const char* as_str(var self);'],
                'description' : 'represent object as C `char*`',
                'parameters' : [
                    ('self', 'object to represent'),
                ],
                'return' : 'C `char*` representation of object'
            }
        ],
        description = 
"""
The `AsStr` class allows a user to represent an object as a C `char*`. It is used by the native type wrapper `String`.
""",
        examples = 
"""
__Usage__

    puts(as_str($(String, "Hello"))); /* Hello */
    puts(as_str($(String, "There"))); /* There */
    
"""
    ),

    AsLong = dict(
        tag     = "Representable as C long",
        funcs   = "as_long",
        related = "AsDouble",
        signature = 
    """
    class {
      long (*as_long)(var);
    } AsLong;
    """,
        methods = [
            {
                'code' : ['long as_long(var self);'],
                'description' : 'represent object as C `long`',
                'parameters' : [
                    ('self', 'object to represent'),
                ],
                'return' : 'C `long` representation of object'
            }
        ],
        description =
"""
The `AsLong` class allows a user to represent an object as a C `long`. It is used by the native type wrapper `Int`.
""",
        examples = 
"""
__Usage__

    printf("%li", as_long($(Int, 5)));    /* 5 */
    printf("%li", as_long($(Real, 5.6))); /* 5 */
    printf("%li", as_long($(Real, 5.5))); /* 5 */
    printf("%li", as_long($(Real, 5.4))); /* 5 */
"""
    ),

    AsDouble = dict(
        tag     = "Representable as C double",
        funcs   =  "as_double",
        related = "AsLong",
        signature = 
    """
    class {
      double (*as_double)(var);
    } AsDouble;
    """,
        methods = [
            {
                'code' : ['double as_double(var self);'],
                'description' : 'represent object as C `double`',
                'parameters' : [
                    ('self', 'object to represent'),
                ],
                'return' : 'C `double` representation of object'
            }
        ],
        description =
"""
The `AsDouble` class allows a user to represent an object as a C `double`. It is used by the native type wrapper `Real`.
""",
        examples = 
"""
__Usage__

    printf("%f", as_double($(Real, 5.1))); /* 5.1 */
    printf("%f", as_double($(Real, 5.2))); /* 5.2 */
    printf("%f", as_double($(Real, 9.8))); /* 9.8 */
    printf("%f", as_double($(Int, 5)));    /* 5.0 */
    printf("%f", as_double($(Int, 7)));    /* 7.0 */
    
"""
    ),

    With = dict(
        tag     = "Can be entered and exited",
        funcs   = "with enter_with exit_with",
        related = "Stream Lock",
        signature = 
    """
    class {
      void (*enter)(var);
      void (*exit)(var);
    } With;
    """,
        methods = [
            {
                'code' : ['void enter_with(var self);'],
                'description' : 'Perform entry code for an object',
                'parameters' : [
                    ('self', 'object to enter with'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['void exit_with(var self);'],
                'description' : 'Perform exit code for an object',
                'parameters' : [
                    ('self', 'object to exit with'),
                ],
                'return' : 'None'
            },
        ],
        description = 
"""
The `With` class provides an interface to provide 'entry' and 'exit' functions to be performed on an object within some scope. This allows for the use of the `with` keyword to specify the scope of an object or operation.
""",
        examples =
"""
__Usage__

    with(file in stream_open($(File, NULL), "prices.bin", "wb")) {
      
        lambda(write_pair, args) {
            var key = cast(at(args, 0), String);
            var val = cast(get(prices, key), Int);
          
            print_to(file, 0, "%$ :: %$\\n", key, val);      
            return None;
        };
        
        map(prices, write_pair);
      
    }
      
__Locks__

    var mut = new(Mutex);

    lambda(thread_function, args) {
        with(m in mut) {
            println("Hello from %$! with Arguments %$", current(Thread), args);
        }
        return None;
    };

    var threads = new(List, 5,
    new(Thread, thread_function),
    new(Thread, thread_function),
    new(Thread, thread_function),
    new(Thread, thread_function),
    new(Thread, thread_function));

    foreach(t in threads) {
        call(t, None);
    }

    foreach(t in threads) {
        join(t);
        delete(t);
    }

    delete(threads);
    delete(mut);
"""
    ),

    Stream = dict(
        tag   = "File-like",
        funcs = "stream_open stream_close stream_seek stream_read stream_write",
        related = "Serialize Format With",
        signature = 
    """
    class {
      var (*stream_open)(var,const char*,const char*);
      void (*stream_close)(var);
      void (*stream_seek)(var,int,int);
      int (*stream_tell)(var);
      void (*stream_flush)(var);
      bool (*stream_eof)(var);
      int (*stream_read)(var,void*,int);
      int (*stream_write)(var,void*,int);
    } Stream;
    """,
        methods = [
            {
                'code' : ['var stream_open(var self, const char* name, const char* access);'],
                'description' : 'Open an object stream with a certain filename with given access rights',
                'parameters' : [
                    ('self', 'object to open'),
                    ('name', 'filename to open'),
                    ('access', 'access rights'),
                ],
                'return' : 'opened object'
            },
            {
                'code' : ['void stream_close(var self);'],
                'description' : 'Close an object stream',
                'parameters' : [
                    ('self', 'stream object to close'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['void stream_seek(var self, int pos, int origin);'],
                'description' : 'Seek to a given position in a stream',
                'parameters' : [
                    ('self', 'stream object to seek'),
                    ('pos', 'Position to seek to'),
                    ('origin', 'seek origin. Must be one of `SEEK_SET`, `SEEK_END`, `SEEK_CUR`'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['int stream_tell(var self);'],
                'description' : 'return the current position in the stream',
                'parameters' : [
                    ('self', 'stream object to tell'),
                ],
                'return' : 'position in stream'
            },
            {
                'code' : ['void stream_flush(var self);'],
                'description' : 'flush all queued reads and writes in a stream',
                'parameters' : [
                    ('self', 'stream object to flush'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['bool stream_eof(var self);'],
                'description' : 'returns if a stream is at the end',
                'parameters' : [
                    ('self', 'stream object to check'),
                ],
                'return' : 'if a stream object is at the end'
            },
            {
                'code' : ['int stream_read(var self, void* output, int size);'],
                'description' : 'read a block of data from a stream',
                'parameters' : [
                    ('self', 'stream object to read from'),
                    ('output', 'pointer to output data block'),
                    ('size', 'amount of data to read in bytes'),
                ],
                'return' : 'number of bytes read'
            },
            {
                'code' : ['int stream_write(var self, void* input, int size);'],
                'description' : 'write a block of data to a stream',
                'parameters' : [
                    ('self', 'stream object to write to'),
                    ('output', 'pointer to input data block'),
                    ('size', 'amount of data to write in bytes'),
                ],
                'return' : 'number of bytes written'
            },
        ],
        description = 
"""
The `Stream` class provides a way to treat objects as File-Like such that they can be read from and written to.
""",
        examples =
"""
__Usage__

    var f = $(File, NULL);
    
    stream_open(f, "test.bin", "w");
    
    char c;
    while (!stream_eof(f)) {
        stream_read(f, &c, 1);
        putc(c);
    }
    
    stream_close(f);

"""
    ),

    Serialize = dict(
        tag     = "Convertible to Serial Form",
        funcs   = "serial_read serial_write",
        related = "Stream Format",
        signature = 
    """
    class {
      void (*serial_read)(var,var);
      void (*serial_write)(var,var);
    } Serialize;
    """,
        methods = [
            {
                'code' : ['void serial_read(var self, var input);'],
                'description' : 'serialize an object from a stream',
                'parameters' : [
                    ('self', 'object to seralize into'),
                    ('input', 'stream to read from'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['void serial_write(var self, var output);'],
                'description' : 'serialize an object to a stream',
                'parameters' : [
                    ('self', 'object to serialize from'),
                    ('output', 'stream to write to'),
                ],
                'return' : 'None'
            },
        ],
        description = 
"""
The `Serialize` class provides a way for objects to be serialized into and out of some stream. This functionality is pretty basic and for more important serialization tasks users are recommended to use more powerful libraries.

This class is used by the `put` and `get` methods on a `File` object.
""",
        examples = 
"""
__Usage__

    var f = stream_open($(File, NULL), "test.bin", "w");
    
    serial_write(f, $(Int, 5));
    serial_write(f, $(Real, 2.0));
    
    stream_close(f);    
"""
    ),
    
    Lock = dict(
        tag     = "Exclusive Resource",
        funcs   = "lock unlock lock_try",
        related = "Process With",
        signature = 
    """
    class {
      void (*lock)(var);
      void (*unlock)(var);
      var  (*lock_try)(var);
    } Lock;
    """,
        methods = [
            {
                'code' : ['void lock(var self);'],
                'description' : 'lock an object. If lock is unavaliable wait until it is avaliable.',
                'parameters' : [
                    ('self', 'object to lock'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['void unlock(var self);'],
                'description' : 'unlock an object',
                'parameters' : [
                    ('self', 'object to unlock'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['var lock_try(var self);'],
                'description' : 'lock an object. If lock is unavaliable continue.',
                'parameters' : [
                    ('self', 'object to lock'),
                ],
                'return' : 'None'
            },
        ],
        description = 
"""
The `Lock` class provides an interface for gaining exclusive access to resources.
""",
        examples =
"""
__Usage__

    var mutex = new(Mutex);
    var total = $(Int, 0);
    
    lambda(f, args) {
      lock(mutex);
      add(total, $(Int, 1));
      unlock(mutex);
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
    
    delete(threads);
    delete(mutex);
"""
    ),
    
    Process = dict(
        tag     = "Program Like",
        funcs   = "current join terminate",
        related = "Lock Call",
        signature = 
    """
    class {
      var  (*current)(void);
      void (*join)(var);
      void (*terminate)(var);
    } Process;
    """,
        methods = [
            {
                'code' : ['var current(var type);'],
                'description' : 'return the current process.',
                'parameters' : [
                    ('type', 'type implementing Progress of which to get the current'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['void join(var self);'],
                'description' : 'join another process.',
                'parameters' : [
                    ('self', 'process to join with'),
                ],
                'return' : 'None'
            },
            {
                'code' : ['void terminate(var self);'],
                'description' : 'terminate another process.',
                'parameters' : [
                    ('self', 'process to terminate'),
                ],
                'return' : 'None'
            },
        ],
        description = 
"""
The `Process` class provides an abstraction on functions related to multiple processes such as Threading.
""",
        examples =
"""
__Usage__
    
    lambda(thread_hello, args) {
        println("Hello from %$!", current(Thread));
    };
    
    var t = new(Thread, thread_hello);
    call(t, None);
    
    println("Waiting for %$...", t);
    join(t);
    
    println("And Hello from %$!", current(Thread));
    
    delete(t);
"""
    )

)