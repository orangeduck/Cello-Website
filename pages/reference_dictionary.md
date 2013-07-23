Dictionary
----------

Dictionary is hashtable data structure mapping hashable keys to objects. It is a [Collection](/documentation/collection) meaning it does not allocate storage for the objects inside of it. Instead it only stored references to the objects. This means both keys and values inside must be stored and managed by the programmer for the duration of the Dictionary's life.

### Implements

* <span style="width:75px; float:left;">[New](reference/new)</span> `new`, `delete`, `construct`, `destruct`
* <span style="width:75px; float:left;">[Assign](reference/assign)</span> `assign`
* <span style="width:75px; float:left;">[Copy](reference/copy)</span> `copy`
* <span style="width:75px; float:left;">[Eq](reference/eq)</span> `eq`, `neq`
* <span style="width:75px; float:left;">[Collection](reference/collection)</span> `len`, `clear`. `contains`, `discard`, `is_empty`
* <span style="width:75px; float:left;">[Dict](reference/dict)</span> `get`, `put`
* <span style="width:75px; float:left;">[Push](reference/push)</span> `push`, `push_at`, `pop`, `pop_at`
* <span style="width:75px; float:left;">[Iter](reference/iter)</span> `iter_start`, `iter_next`, `iter_end`
* <span style="width:75px; float:left;">[Show](reference/show)</span> `show`, `look`, `print`, `scan`


### See Also

### Examples


[Back](/documentation)