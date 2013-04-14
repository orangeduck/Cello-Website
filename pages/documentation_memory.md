Memory Management
-----------------

Memory management is hard. Very hard when combined with a lack of rich stack types. Very very hard when combined with a whole load of high level concepts. Cello gives you a few options, which where possible, the standard library is agnostic too. You can use what you think is best.

__Destructive Operations__ - Most of the standard library uses destructive operations and expects the user to make a copy if they exlicity want one.

__Output Parameters__ - In some places it is more appropriate to use output parameters and in which case `assign` is used to move the data around. 

__Reference Objects__ - References wrap standard objects, where `with` can be used to declare their lifetime. And `at` can be used to dereference.


    local void object_lifetime_example(void) {
      
      with(liferef in $(Reference, new(String, "Life is long"))) {
        print("This string is alive: %$\n", at(liferef,0));
      }

      print("Now it has been cleared up!\n");
      
    }

    /* They can also be stacked */

    local void many_object_lifetimes(void) {
      
      with(liferef0 in $(Reference, new(String, "Life is long")))
      with(liferef1 in $(Reference, new(String, "Life is Beautiful")))
      with(liferef2 in $(Reference, new(String, "Life is Grand"))) {
        print("%s :: %s :: %s\n", at(liferef0,0), at(liferef1,0), at(liferef2,0));
      }

    }
    
__Reference Pools__ - Reference pools are also avaliable which use `retain` and `release` to providing a reference counting mechanism.

    #include "Cello.h"

    local var g_pool;

    local void table_fill(var x) {
      put(x, $(String, "First"),  $(Real, 0.0));
      put(x, $(String, "Second"), $(Real, 0.1));
      put(x, $(String, "Third"),  $(Real, 5.7));
      release(g_pool, x);
    }

    local void table_process(var x) {
      put(x, $(String, "First"), $(Real, -0.65));
      release(g_pool, x);
    }

    int main(int argc, char** argv) {
      
      g_pool = new(Pool);
      
      var x = retain(g_pool, new(Table, String, Real));
      
      table_fill(retain(g_pool, x));
      table_process(retain(g_pool, x));
      
      release(g_pool, x);
      
      delete(g_pool);
      
    }

    
[Back](/documentation)

    