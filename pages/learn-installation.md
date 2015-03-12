
  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">

# Installation
  
## About

Although Cello does not look like it - it is _just a C library_. That means 
that in general it can be installed and used like any other C library.

The reason I mention this is because if you get stuck, or become unsure of what 
to do, then looking for help in general about _using C_ or 
_installing C libraries_ will be a good way to start. If you are completely new 
to C it might be good to learn some very basics before diving into Cello. For 
this why not try my other project 
[Build Your Own Lisp](http://www.buildyourownlisp.com/), or if you don't fancy 
that, you can try 
[Learn C the Hard Way](http://c.learncodethehardway.org/book/), which is a 
pretty good resource for newcomers and beginners.

Saying all that, installing a C library is not always a trivial matter, so here 
are some general instructions as to how to get started.


## Download

First download the tarball from the download link at the top of this page. This 
is the _source code_ of the latest release of libCello.

In this form it is not ready to use but first needs to be __compiled__ and 
then __installed__.

## Compile

To compile Cello requires a gnu99 compatible C compiler.

__Linux:__ You can use `gcc`, which can be installed via the system package 
manager. For example if you are using Ubuntu enter `apt-get install gcc` into a 
terminal.

__Mac:__ XCode needs to be installed along with the command line tools. This 
will install a version of `gcc` using the `clang` compiler suite.

__Windows:__ I recommend [MinGW64](http://mingw-w64.sourceforge.net/) or 
[Cygwin](http://www.cygwin.com/). Either of these need to be downloaded and 
installed and they will provide a version of the `gcc` compiler. 

To check you have `gcc` installed open a terminal and type:

    $ gcc --version
      gcc (rubenvb-4.7.2-release) 4.7.2
      ...

You should see something similar to the above. Once this is the case, browse to 
the directory in which you unzipped the source distribution and run the 
following:
    
    $ ls
      INSTALL.md  Makefile   examples tests
      LICENSE.md  README.md  include  src   
    $ make
      ...
    
This will compile the library. If there are no errors it should create a file 
`libCello.a`. You can then run the following to make the tests and ensure 
everything is working correctly.

    $ make check
    
    
## Install

You should now have a `libCello.a` which you can potentially use directly in 
your projects. If you want to install it system wide you can run the following:

    $ make install

If this does not work the user is encourage to install the library and headers 
manually, or include them directly in their project.

If everything has gone correctly you should be 
[ready to play](/learn/cello-world).

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>

