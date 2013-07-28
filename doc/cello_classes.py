
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
        related = ""
    ),

    Num = dict(
        tag     = "Can perform arithmetic",
        funcs   = "add sub mul div negate absolute",
        related = "AsLong AsDouble"
    ),

    Retain = dict(
        tag     = "Can be used for reference counting",
        funcs   = "retain release",
        related = "With"
    ),

    New = dict(
        tag     = "Constructable on the Heap",
        funcs   = "new delete construct destruct",
        related = "Assign Copy"
    ),

    Assign = dict(
        tag     = "Assignable to",
        funcs   = "assign",
        related = "Copy New"
    ),

    Copy = dict(
        tag     = "Copyable",
        funcs   = "copy",
        related = "New Assign"
    ),

    Eq = dict(
        tag     = "Comparable for Equality",
        funcs   = "eq neq if_eq if_neq",
        related = "Ord"
    ),

    Ord = dict(
        tag     = "Comparable for Ordering",
        funcs   = "gt lt ge le",
        related = "Eq"
    ),

    Hash = dict(
        tag     = "Hashable to a long",
        funcs   = "hash",
        related = "AsLong"
    ),

    Collection = dict(
        tag     = "Treatable as several objects",
        funcs   = "len clear contains discard",
        related = "Sort Append Push At Reverse Dict Iter"
    ),

    Sort = dict(
        tag     = "Elements can be sorted",
        funcs   = "sort",
        related = "Ord Collection At"
    ),

    Reverse = dict(
        tag     = "Order can be reversed",
        funcs   = "reverse",
        related = "Collection At"
    ),

    Append = dict(
        tag     = "Elements can be added to end",
        funcs   = "append",
        related = "Collection Push At"
    ),

    Iter = dict(
        tag     = "Can be looped over",
        funcs   = "foreach iter_start iter_end iter_next",
        related = "Collection At"
    ),

    Push = dict(
        tag     = "Elements can be Pushed and Popped",
        funcs   = "push pop push_at pop_at",
        related = "Collection At Append"
    ),

    At = dict(
        tag     = "Elements can be directly accessed and set",
        funcs   = "at set",
        related = "Push At Collection"
    ),

    Dict = dict(
        tag     = "Key-Value access to object",
        funcs   = "get put",
        related = "Collection At"
    ),

    AsChar = dict(
        tag     = "Representable as C char",
        funcs   = "as_char",
        related = "AsStr"
    ),

    AsStr = dict(
        tag     = "Representable as C char*",
        funcs   = "as_str",
        related = "AsChar"
    ),

    AsLong = dict(
        tag     = "Representable as C long",
        funcs   = "as_long",
        related = "AsDouble"
    ),

    AsDouble = dict(
        tag     = "Representable as C double",
        funcs   =  "as_double",
        related = "AsLong"
    ),

    With = dict(
        tag     = "Can be entered and exited",
        funcs   = "with enter_with exit_with",
        related = "Stream"
    ),

    Stream = dict(
        tag   = "File-like",
        funcs = "stream_open stream_close stream_seek stream_read stream_write",
        related = "Serialize Format With"
    ),

    Serialize = dict(
        tag     = "Convertible to Serial Form",
        funcs   = "serial_read serial_write",
        related = "Stream Format"
    ),
    
    Lock = dict(
        tag     = "Exclusive Resource",
        funcs   = "lock unlock lock_try",
        related = "Process With"
    ),
    
    Process = dict(
        tag     = "Program Like",
        funcs   = "current join terminate",
        related = "Lock Call"
    )

)