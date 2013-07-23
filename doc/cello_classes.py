
def class_set(**classes):
    
    for k in classes.keys():
        
        classes[k]["name"] = k
        classes[k]["link"] = k.lower()
        classes[k]["filename"] = "reference_" + k.lower() + ".md"
        
        for x in ["description", "examples"]:
            if not (x in classes[k]): classes[k][x] = "\nComing Soon...\n"
        
    return classes

cello_classes = class_set(

    Format = dict(
        tag     = "Read or Writable using a Format String",
        funcs   = "format_to format_from",
        related = "Show Stream"
    ),

    Show = dict(
        tag     = "Write To or Read From String",
        funcs   = "show print look scan",
        related = "Format Stream"
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