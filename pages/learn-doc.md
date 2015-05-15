  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__name__

    const char* name(var type);

Return the name of a given `type`.

__brief__

    const char* brief(var type);

Return a brief description of a given `type`.

__description__

    const char* description(var type);

Return a longer description of a given `type`.

__definition__

    const char* definition(var type);

Return the C definition of a given `type`.

### Examples

__Usage__

    show($S(name(Int))); /* Int */
    show($S(brief(Int))); /* Integer Object */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Doc
__Has Documentation__

The `Doc` class can be used to give documentation to a certain class or type. This documentation can then be accessed using the `help` function or by other tools used to generate documentation such as for the Cello website. Documentation can be written in Markdown.

The `examples` and `methods` entries should be provided as `NULL` terminated arrays allocated statically.

### Definition

    struct Example {
      const char* name;
      const char* body;
    };
    
    struct Method {
      const char* name;
      const char* definition;
      const char* description;
    };
    
    struct Doc {
      const char* (*name)(void);
      const char* (*brief)(void);
      const char* (*description)(void);
      const char* (*definition)(void);
      struct Example* (*examples)(void);
      struct Method* (*methods)(void);
    };
    

### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Floating Point Object_
* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _Integer Sequence_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
