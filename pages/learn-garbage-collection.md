  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Garbage Collection

Cello provides a basic garbage collector which can be used to avoid having to 
manually deallocate memory.

Garbage collectable objects are allocated via the `new` function and can be 
(optionally) deleted via `del`. The Garbage Collector in Cello can also be 
disabled at compile time using the flag `-DCELLO_NGC` without affecting the 
standard library, which uses `del` either way to manage its memory. When 
disabled, memory must be manually managed with `new` and `del`. To allocate 
memory while avoiding the Garbage Collector without completely disabling it the 
`new_raw` and `del_raw` functions can be used.

There are a few things to be aware of when using the Cello Garbage Collector:

* __Reachability__

Garbage Collectable objects must be reachable via local variables on the 
stack, or via some chain of other GC allocated Cello objects that are 
themselves reachable. They __must not__ be stored in global/static variables, 
or in locations only reachable via non-Cello structures. Additionally each 
thread in Cello has its own Garbage Collector which runs locally, so objects 
should not be allocated in one thread, and only reachable from another. To 
store Cello objects in global/static locations or inside non-Cello structures 
the `new_root` function should be used, and the corresponding objects deleted 
manually with `del`. Due to these limitations it can be better to think of the 
Cello Garbage Collector as a kind of lazy 
[RAII](http://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization) 
which calls object destructors _some time_ after the object goes out of scope.

* __The Mark Class__

By default the Cello Garbage collector just scans the memory of an object to 
find pointers to other Cello objects it has allocated, but this behaviour can 
be overridden by implementing the `Mark` class. If you create a Cello type that 
does it's own memory allocation and stores Cello Objects inside of that memory  
you can define this class to allow it to interact correctly with the GC.

* __Real Time Collection__

Garbage Collection in Cello is still somewhat new and experimental. It uses 
a naive stop-the-world mark and sweep algorithm. This can result in quite 
long pauses so it is not appropriate for real-time applications.
  
* __Uninitialised Values__

The Garbage Collector scans the stack memory, and this naturally contains 
uninitialised values. Although it does this safely, if you are running a 
Cello program through Valgrind these accesses will be reported as errors. 
Other than this Cello, shouldn't have any memory errors in Valgrind, so the 
easiest way to disable these to examine any real problems is to run Valgrind 
with the option `--undef-value-errors=no`.
  
* __Portability__

There there is simply no way to create a _completely_ portable garbage 
collector in C. But unlike the [Boehm Garbage Collector](http://en.wikipedia.org/wiki/Boehm_garbage_collector), 
the Cello Garbage Collector doesn't need to use any platform specific 
tricks. All it relies on is the assumption that the architecture uses a call 
stack to implement function frames. This means it should be safe to use for 
more or less all architectures found in the wild.
  
# How it works  

So how can garbage collection be done in C?

For a basic mark and sweep garbage collector you need two things. The first 
thing you need is a list of all of the objects that have been allocated. The 
second is a list of all the objects that are still in scope - all the objects 
that are _reachable_ by program/programmer.

The mark and sweep garbage collector then just compares these two lists. If 
an object has been allocated, but is unreachable by the program/programmer, 
then it can be deleted. It really is as simple as that.

The list of allocated objects is usually pretty easy to obtain. You just make 
it so that your memory allocation function records all the allocations it 
makes. As long as all allocations go via this function you'll be fine. In Cello 
all allocations of garbage collectable objects have to go via `new` so there is 
no trouble recording whenever a new object is allocated.

The list of reachable objects is usually much harder to obtain. In languages 
such as Java, which run on a virtual machine, this can be made by traversing 
the data structures that represent the program running on the virtual machine, 
finding all references to objects and following any more references those 
objects contain.

In this case the list of reachable objects is not explicitly computed. Instead 
the comparison is done implicitly by _marking_ and then _sweeping_. First all 
of the reachable objects are _marked_, starting from local and global 
variables and recursively following references in the program all objects are 
marked, until there are no longer any unmarked objects to be found. Then the 
list of allocated objects is _swept_ by going over and deleting any that are 
remaining unmarked.

But C works at a lower level of abstraction than these languages. There is no 
convenient list of "objects" or "references" to follow. In C we are dealing 
with raw memory and all of this structure doesn't exist. Luckily, because Cello 
acts as a runtime system on top of native C, we can use it alongside a few 
crafty tricks to try and rebuild much of this structure - and in doing so 
create a basic Garbage Collector limited to Cello objects.

We can start with the observation that, in general, memory in C exists in three 
locations - the heap, the stack, and the data segment. This means if an object 
is _reachable_ by the program there must exist a pointer to it in one of these 
areas.

Given a list of all of the allocations made by our GC we should be able to 
search these memory locations (excluding the list of allocations itself) and if 
we find a pointer to any memory allocated by the GC we know it is still 
reachable by the program and so should not be deleted. If we find no pointers 
to an allocation it must no longer be used by the program and so it can be 
deleted. Now the question is how to search these memory locations. Where are 
they? And what are their bounds?

For the data segment unfortunately there is no portable way to find out, so in 
the case of the Cello Garbage Collector we simply ignore it and tell users not 
to allocate global variables with the garbage collector!

Similarly for the heap - it is reasonable to ask our users to only reference 
garbage collectable Cello objects from other Cello objects. This means we limit 
our search to heap objects created via Cello. Our Cello runtime knowns the 
allocation size for each heap object allocated, so we can scan the memory at 
each object for pointers to other Cello objects. If the object does some custom 
memory allocation we can get it to implement the `Mark` type class to tell 
us directly what objects it points to.

With the data segment ignored, and the heap easily scanned, this leaves the 
final, and arguably most important location for pointers to Cello objects, the 
stack. Now in almost all reasonable implementations of C the stack is a 
continuous area of memory that grows down (or sometimes up, although that 
doesn't make much difference) for each function call. It contains all the local 
variables used by functions as well as various other housekeeping data. By 
getting the memory address of the top of the stack, and of the bottom, we can 
scan over all the memory in-between and check it for pointers to Cello objects.

Assuming the stack grows from top to bottom we can get a conservative 
approximation of the bottom of the stack by just taking the address of some 
local variable:

    void* Cello_GC_Stack_Bot() {
      void* p = NULL;
      return &p;
    }
   
But before we do this we need to ensure two things. First we want to make sure 
we flush all of the values in the registers onto the stack so that 
we don't miss a pointer hiding in a register, and secondly we want to make sure 
the `Cello_GC_Stack_Bot` function isn't inlined by the compiler. We can spill 
the registers into stack memory in a somewhat portable way with `setjmp` - 
which puts the registers into a `jmp_buf` variable. And we can ensure that the 
function is not inlined by only calling the marking function via a function 
pointer, who's value is decided using a volatile variable (volatile variables 
are immune to optimisations). Then we know that the `Cello_GC_Stack_Bot` 
function will return an address that will definitely cover the spilled 
registers and everything else on the stack above our call.
    
    void Cello_GC_Mark_Prelude() {
      jmp_buf env;
      setjmp(env);
      
      volatile int noinline = 1;
      void (*mark_stack)(void) = noinline
        ? Cello_GC_Mark_Stack
        : (var(*)(void))(NULL);

      mark_stack();
    }

Getting the top of the stack is a little more difficult, but assuming user 
programs start from `main` we can use a very cheeky macro to wrap it in a 
custom function that first registers the address of some local variable with 
the Cello GC, and then calls the user program:
    
    int Cello_Main(int argc, char** argv);
    
    #define main(...) \
      main(int argc, char** argv) { \
        var stk = None; Cello_GC_Init(&stk); \
        return Cello_Main(argc, argv); \
      }; \
      int Cello_Main(int argc, char** argv)
    
Using these techniques we can get a safe approximate upper and lower bound to 
the area of stack memory that should contain all the relevant pointers to 
garbage collectable objects. Now all we need to do is scan this memory range 
and mark any pointers we find referenced. 

    void Cello_Mark(void) {

      var top = Cello_GC_Stack_Top();
      var bot = Cello_GC_Stack_Bot();

      for (var p = top; p <= bot; p += sizeof(var)) {
        Cello_GC_Mark_Item(*((var*)p));
      }
    
    }

But how can we tell if some block of memory is actually a pointer? We don't 
want to be following pointers recklessly or else we might cause a segfault. 
Now in general there is no way to distinguish between some memory that looks 
like a pointer, and an actual pointer itself - but there are a couple of 
heuristics that we can use to disregard lots of potential addresses.

First - pointers must be memory aligned - which means for 64-bit machines they 
can only be located every 8-byte boundary, and must only point to some value on
an 8-byte boundary. This means the pointer value must be a multiple of the 
pointer size, and the _address_ of the pointer must be a multiple of the 
pointer size. We can also keep track of the maximum and minimum 
pointer addresses we've allocated and quickly disregard anything outside of 
these bounds.

These simple measures will stop us following _bad_ or _invalid_ pointers in 
almost all cases, but we need to narrow it down even further because a bad 
memory access could crash the program. For this purpose a hash table is 
maintained which stores all the pointers which have been allocated by Cello. It 
can be used to quickly check if a pointer is to an allocated Cello object.

Here is what the function `Cello_GC_Mark_Item` roughly looks like. It does 
these brief checks and then on success does the actual marking and recursion. 
    
    void Cello_GC_Mark_Item(var a) {

      if (a % sizeof(var) is 0
      and a >= minptr
      and a <= maxptr
      and     Cello_GC_Allocated(a)
      and not Cello_GC_Marked(a)) {
          Cello_GC_Mark(a);
          Cello_GC_Recurse(a);
      }
    
    }

The recursion function is also simple. It either calls the `mark` function 
on the Cello object, or scans the memory at that location and tries to mark 
each segment of memory as if it were a pointer - just like the stack data.
    
    static void Cello_GC_Recurse(struct GC* gc, var ptr) {
      
      var type = type_of(ptr);
      
      struct Mark* m = type_instance(type, Mark);
      if (m and m->mark) {
        m->mark(ptr, gc, (void(*)(var,void*))GC_Mark_Item);
        return;
      }
      
      struct Size* s = type_instance(type, Size);
      if (s and s->size) {
        for (size_t i = 0; i < s->size(); i += sizeof(var)) {
          var p = ((char*)ptr) + i;
          GC_Mark_Item(gc, *((var*)p));
        }
        return;
      }
      
    }

This completes all that is required for the marking stage. The sweeping stage 
is equally simple. It just deletes all Cello Objects not marked! Again roughly
it looks like this:


    void Cello_Sweep(void) {
      
      for (size_t i = 0; i < Cello_GC_NumItems(); i++) {
        var ptr = Cello_GC_Item(i);
        if (Cello_GC_Marked(ptr)) {
          Cello_GC_Unmark(ptr);
        } else {
          Cello_GC_Delete(ptr);
        }
      }
    
    }

Now when a user asks for a new allocation via `new` and memory usage has 
exceeded some bound we simply call `Cello_Mark` and `Cello_Sweep` to free 
any avaliable memory.
    
As you probably suspected, in reality there is a little more going on, with 
various optimisations and tweaks to what is shown in the code snippits here, 
but the Cello Garbage Collector is still very simple, safe and portable - if a 
little slow!

Overall I hope I've shown that simple Garbage Collection for limited 
environments is not only possible in C - it is fairly simple to implement and 
understand.

### References / Resources

* [Boehm GC](http://www.hboehm.info/gc/)
* [Babies First Garbage Collector](http://journal.stuffwithstuff.com/2013/12/08/babys-first-garbage-collector/)

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
