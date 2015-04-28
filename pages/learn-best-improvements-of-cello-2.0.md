# Best Improvements of Cello 2.0

## 1. Better C Interop

The complete internal workings of Cello have been rewritten and now it uses the 
concept of fat pointers to ensure Cello Pointers are fully compatible with 
standard C pointers. This is a massive win for interop with C because it means 
you can happily write standard C functions with types and this or that when it 
makes things easier. No longer are you forced to use typeless pointers when you 
don't want to. Now Cello really does work _on top_ of normal C, not orthogonal 
to it.


    static void Body_Offset_Momentum(struct Body* self, 
      double px, double py, double pz) {
      self->vx = -px / solar_mass;
      self->vy = -py / solar_mass;
      self->vz = -pz / solar_mass;
    }
    
    static void Bodies_Offset(var bodies) {
    
      foreach (body in bodies) {
        struct Body* b = body;
        px += b->vx * b->mass;
        py += b->vy * b->mass;
        pz += b->vz * b->mass;
      }
      
      struct Body* first = get(bodies, $I(0));
      
      Body_Offset_Momentum(first, px, py, pz);
      
    }

    
Additionally the overhead of declaring a structure Cello compatible has been 
reduced from 20 or 30 lines of code to just one. Not only this but there are a
huge number of operations Cello has defaults for now. In one line of code you 
can suddenly make it so that an object is usable across the whole Cello 
infrastructure including garbage collection, data structures, IO, and much 
more.


    struct Body {
      double  x,  y,  z;
      double vx, vy, vz;
      double mass;
    };

    var Body = Cello(Body);

    
Before going down the path of declaring a Cello style object was pretty time 
consuming. Now you can't afford not to!


## 2. Performance

It is fair to say that Cello 1.0 was insanely slow. It had some pretty terrible 
data structures and the overhead of calling Cello functions inside a tight loop 
was massive.

In Cello 2.0 all the data structures have been updated to be modern, fast, and 
efficient. Cello has also been heavily optimised and benchmarked to ensure it 
doesn't have too much of a performance penalty. Currently it sits between C and 
Java on most operations. The better interop with C has also helped in this 
regard, making it easy to drop down to C for numerical calculations and other 
performance intensive areas. And if you still need that extra performance 
remember that all C programs are also valid Cello programs!


## 3. Portability

Cello 2.0 only relies on a couple of fairly standard C language extensions. 
Namely the _dollars in identifiers_ extension and the _gnu style variadic 
macros_ extension.

Unfortunately this does mean that closures have been dropped from the features 
list since 1.0, but it seems like a sensible omission as now Cello can be 
compiled easily with all of the major compilers including `gcc`, `clang`, 
`cl.exe`, and `tcc`.

Several of the defines Cello 1.0 made such as `local` and `global` have also 
been dropped. While these are certainly more readable than `static` and 
`extern` the potential for shadowing issues, and the fact that I wanted Cello 
to play nicely with C in this release outweighed the benefits.


## 4. Debugging



## 5. Garbage Collection
