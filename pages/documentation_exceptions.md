Exceptions
----------

Cello provides exception handling to deal with errors. The semantics and syntax are essentially as you would expect.

    local var DivideByZeroError = Singleton(DivideByZeroError);

    local int try_divide(int x, int y) {
      if (y == 0) {
        throw(DivideByZeroError, "%i / %i", $(Int, x), $(Int, y));
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
      do_some_other_work();
    } catch (e) {
      print("Got Exception: %$\n", e);
    }

Throwing an exception will jump the program control to the innermost `catch` block. If it is not handled here it is passed on to an outer block. To catch an exception one must put the thrown object. Any object can be thrown and caught as an Exception in Cello so users can create their own Exception types or find other applications for the semantics. The thrown message will be preserved internally, but be careful of throwing stack memory which may become invalidated when jumping to the new location.

[Back](/documentation)