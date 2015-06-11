  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__hash__

    uint64_t hash(var self);

Get the hash value for the object `self`.

__hash_data__

    uint64_t hash_data(void* data, size_t num);

Hash `num` bytes pointed to by `data` using [Murmurhash](http://en.wikipedia.org/wiki/MurmurHash).

### Examples

__Usage__

    println("%li", $I(hash($I(  1)))); /*   1 */
    println("%li", $I(hash($I(123)))); /* 123 */
    
    /* 866003103 */
    println("%li", $I(hash_data($I(123), size(Int))));
    
    println("%li", $I(hash($S("Hello"))));  /* -1838682532 */
    println("%li", $I(hash($S("There"))));  /*   961387266 */
    println("%li", $I(hash($S("People")))); /*   697467069 */
    



  </div>
  <div class="col-xs-6 col-md-6">

# Hash
__Hashable__

The `Hash` class provides a mechanism for hashing an object. This hash value should remain the same across objects that are also considered equal by the `Cmp` class. For objects that are not considered equal this value should aim to be evenly distributed across integers.

This is not a cryptographic hash. It is used for various objects or data structures that require fast hashing such as the `Table` type. Due to this it should not be used for cryptography or security.

By default an object is hashed by using its raw memory with the [Murmurhash](http://en.wikipedia.org/wiki/MurmurHash) algorithm. Due to the link between them it is recommended to only override `Hash` and `Cmp` in conjunction.

### Definition

    struct Hash {
      uint64_t (*hash)(var);
    };
    

### Derivers

* <span class="docitem">[Box](/learn/box)</span> | &nbsp; &nbsp;   _Unique Pointer_
* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Filter](/learn/filter)</span> | &nbsp; &nbsp;   _Filtered Iterable_
* <span class="docitem">[Function](/learn/function)</span> | &nbsp; &nbsp;   _Function Object_
* <span class="docitem">[GC](/learn/gc)</span> | &nbsp; &nbsp;   _Garbage Collector_
* <span class="docitem">[Map](/learn/map)</span> | &nbsp; &nbsp;   _Apply Function to Iterable_
* <span class="docitem">[Mutex](/learn/mutex)</span> | &nbsp; &nbsp;   _Mutual Exclusion Lock_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_
* <span class="docitem">[Range](/learn/range)</span> | &nbsp; &nbsp;   _Integer Sequence_
* <span class="docitem">[Ref](/learn/ref)</span> | &nbsp; &nbsp;   _Shared Pointer_
* <span class="docitem">[Slice](/learn/slice)</span> | &nbsp; &nbsp;   _Partial Iterable_
* <span class="docitem">[Zip](/learn/zip)</span> | &nbsp; &nbsp;   _Multiple Iterator_
### Implementers

* <span class="docitem">[Array](/learn/array)</span> | &nbsp; &nbsp;   _Sequential Container_
* <span class="docitem">[Float](/learn/float)</span> | &nbsp; &nbsp;   _Floating Point Object_
* <span class="docitem">[Int](/learn/int)</span> | &nbsp; &nbsp;   _Integer Object_
* <span class="docitem">[List](/learn/list)</span> | &nbsp; &nbsp;   _Linked List_
* <span class="docitem">[String](/learn/string)</span> | &nbsp; &nbsp;   _String Object_
* <span class="docitem">[Table](/learn/table)</span> | &nbsp; &nbsp;   _Hash table_
* <span class="docitem">[Thread](/learn/thread)</span> | &nbsp; &nbsp;   _Concurrent Execution_
* <span class="docitem">[Tree](/learn/tree)</span> | &nbsp; &nbsp;   _Balanced Binary Tree_
* <span class="docitem">[Tuple](/learn/tuple)</span> | &nbsp; &nbsp;   _Basic Collection_
* <span class="docitem">[Type](/learn/type)</span> | &nbsp; &nbsp;   _Metadata Object_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
