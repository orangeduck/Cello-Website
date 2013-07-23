
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

    Array = dict(
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

    Bool = dict(
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

    Char = dict(
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

    Dictionary = dict(
        tag  = "Hashtable Collection",
        implements = "New Assign Copy Eq Collection Dict Iter Show",
        related = "Table Map Tree",
        description = 
"""
Dictionary is hashtable data structure mapping hashable keys to objects. It is a [Collection](/documentation/collection) meaning it does not allocate storage for the objects inside of it. Instead it only stored references to the objects. This means both keys and values inside must be stored and managed by the programmer for the duration of the Dictionary's life.
"""
    ),

    File = dict(
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

    Function = dict(
        tag  = "High Level Function",
        implements = "New Copy Assign Call",
        related = "Thread"
    ),

    List = dict(
        tag  = "Sequential Collection",
        implements = "New Assign Copy Eq Collection Push At Iter Reverse Sort Append Show",
        related = "Array"
    ),

    Map = dict(
        tag  = "Binary Tree Collection",
        implements = "New Assign Copy Eq Collection Dict Iter Show",
        related = "Tree Dictionary Table"
    ),

    NoneType = dict(
        tag  = "Empty Value",
        implements = "Eq Ord Hash AsChar AsLong AsDouble AsStr Show",
        related = "Bool Int"
    ),

    Int = dict(
        tag  = "Basic Integer Type",
        implements = "New Assign Copy Eq Ord Hash AsLong AsDouble Num Serialize Show",
        related = "Real Bool Char"
    ),

    Real = dict(
        tag  = "Basic Float Point Type",
        implements = "New Assign Copy Eq Ord Hash AsDouble AsLong Num Serialize Show",
        related = "Int"
    ),

    Pool = dict(
        tag  = "Reference Counting Pool",
        implements = "New Retain Collection Dict",
        related = "Reference Dictionary"
    ),

    Reference = dict(
        tag  = "Basic Reference Type",
        implements = "New Assign Copy Eq Hash At With Show",
        related = "Pool"
    ),

    String = dict(
        tag  = "Basic String Type",
        implements = "New Assign Copy Eq Ord Collection Hash Reverse AsStr Append Format Show",
        related = "Char"
    ),

    Table = dict(
        tag  = "Hashtable Container",
        implements = "New Assign Copy Eq Collection Dict Iter Show",
        related = "Dictionary Tree Map"
    ),

    Tree = dict(
        tag  = "Binary Tree Container",
        implements = "New Assign Copy Eq Collection Dict Iter Show",
        related = "Map Table Dictionary"
    ),

    Type = dict(
        tag  = "Metadata Type Object",
        implements = "New AsStr Show",
        related = ""
    ),
    
    Thread = dict(
        tag = "Concurrent Processes",
        implements = "New Assign Copy Call Process AsLong",
        related = "Mutex Function"
    ),
    
    Mutex = dict(
        tag = "Mutual Exclusion Lock",
        implements = "New Assign Copy Lock With",
        related = "Thread Function"
    ),

)
