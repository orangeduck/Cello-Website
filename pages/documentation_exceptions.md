
Exceptions
----------

Cello provides a kind of exception handling to deal with errors.

    local var DivideByZeroError = Singleton(DivideByZeroError);

    local int try_divide(int x, int y) {
      if (y == 0) {
        throw(DivideByZeroError, "Division By Zero (%i / %i)", x, y);
      } else {
        return x / y;
      }
    }

    int main(int argc, char** argv) {

      try {
        int result = try_divide(2, 0);
      } catch (e in DivideByZeroError) {
        // Panic!
        return 1;
      }
      
      return 0;
    }

One can also catch multiple objects and then write conditional code based on each. Or one can catch all exceptions or any thown object by leaving the specifer list empty.

    try {
      do_some_work();
    } catch (e in TypeError, ClassError) {
      if (e is TypeError) { print("Got TypeError!\n"); }
      if (e is ClassError) { print("Got ClassError!\n"); }
    }

    try {
      do_some_other_word();
    } catch (e) {
      print("Got Exception: %$\n", e);
    }

Throwing an exception will jump the program control to the innermost `catch` block. If it is not handled here it is passed on to an outer block. To catch an exception one must put a reference to the thrown object. Any object can be thrown and caught as an Exception in Cello so users can create their own Exception types or find other applications for the semantics. The thrown message will be preserved internally, but be careful of throwing stack memory which may become invalidated when jumping to the new location.

[Back](/documentation)