  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Cello World

Here is a quick tutorial in building your first Cello program. To start open up 
a text editor and create a new file called `cello_world.c`. Type in the 
following:

    #include "Cello.h"
    
    int main(int argc, char** argv) {
      println("Cello World!");
      return 1;
    }
    
You should be able to compile this with something like the following command 

    $ gcc -std=gnu99 cello_world.c -lCello -o cello_world
    
On __Linux__ you might need to link some additional libraries

    $ gcc -std=gnu99 cello_world.c -lCello -lm -lpthread -o cello_world

On __Windows__ you might need to link to the `DbgHelp` library.

    $ gcc -std=gnu99 cello_world.c -lCello -lDbgHelp -o cello_world

Or if the `DbgHelp` library can't be found then it's likely that Cello has 
compiled without stack trace support. In this case you should use the 
`-DCELLO_NSTRACE` flag instead.

    $ gcc -std=gnu99 cello_world.c -lCello -DCELLO_NSTRACE -o cello_world
    
This should create a program called `cello_world` you can then execute

    $ ./cello_world
      Cello World!

If you have errors:

* You should double check you have [installed](installation) the library 
correctly.
* You may need to run `ldconfig` to refresh your library cache.
* You must make sure the flags you compile with are the same as the ones used 
to compile Cello itself. If you are unsure what these were you can run 
`make examples` in the Cello source directory and see what flags it uses in 
that case.

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>
