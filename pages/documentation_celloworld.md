First Notes
-----------

Here is a quick tutorial in building your first Cello program.

To start open up a text editor and create a new file called `cello_world.c`. Type in the following:

    #include "Cello.h"
    
    int main(int argc, char** argv) {
      println("Cello World!");
    }
    
You should be able to compile this with the following command 

    $ gcc -std=gnu99 cello_world.c -lCello -o cello_world

This should create a program called `cello_world` you can then execute

    $ ./cello_world
      Cello World!

If you have errors:

* You should double check you have [installed](installation) the library correctly.
* You may need to add some extra compile flags such as `-fblocks`
* You may need to add some extra linker flags such as `-lpthread -lm`
* You may need to run `ldconfig` to refresh your library cache.

[Back](/documentation)
