  <div class="row">
  <div class="col-xs-6 col-md-6">

### Examples

__Usage__

    var increment(var args) {
      struct Int* i = get(args, $I(0));
      i->val++;
      return NULL;
    }
    
    var x = $I(0);
    show(x); /* 0 */
    call($(Function, increment), x);
    show(x); /* 1 */
    

__Usage 2__

    var hello_person(var args) {
      print("Hello %$!", get(args, $I(0)));
      return NULL;
    }
    
    call($(Function, hello_person), $S("Dan"));
    

__Usage 3__

    var add_print(var args) {
      int64_t fst = c_int(get(args, $I(0)));
      int64_t snd = c_int(get(args, $I(1)));
      println("%i + %i = %i", $I(fst), $I(snd), $I(fst+snd));
      return NULL;
    }
    
    call($(Function, add_print), $I(10), $I(21));
    



  </div>
  <div class="col-xs-6 col-md-6">

# Function
__Function Object__

The `Function` type allows C function pointers to be treated as Cello objects. They can be passed around, stored, and manipulated. Only C functions of the type `var(*)(var)` can be stored as a `Function` type and when called the arguments will be wrapped into an iterable and passed as the first argument, typically in the form of a `tuple`.

### Definition

    struct Function {
      var (*func)(var);
    };
    

### Derives

* <span style="width:50px; float:left;">[Alloc](/learn/alloc)</span>`$` `alloc` `dealloc` 
* <span style="width:50px; float:left;">[Assign](/learn/assign)</span>`assign` 
* <span style="width:50px; float:left;">[Cast](/learn/cast)</span>`cast` 
* <span style="width:50px; float:left;">[Cmp](/learn/cmp)</span>`cmp` `eq` `neq` `gt` `lt` `ge` `le` 
* <span style="width:50px; float:left;">[Copy](/learn/copy)</span>`copy` 
* <span style="width:50px; float:left;">[Hash](/learn/hash)</span>`hash` `hash_data` 
* <span style="width:50px; float:left;">[New](/learn/new)</span>`new` `del` `construct` `destruct` 
* <span style="width:50px; float:left;">[Size](/learn/size)</span>`size` 
### Implements

* <span style="width:50px; float:left;">[Call](/learn/call)</span>`call` 
* <span style="width:50px; float:left;">[Doc](/learn/doc)</span>`name` `brief` `description` `definition` 

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
