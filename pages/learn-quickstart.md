  <div class="row">
  <div class="col-xs-2 col-md-2"></div>
  <div class="col-xs-8 col-md-8">
  
# Quickstart

## Overview

Cello adds a runtime layer on top of C. This is used to extend the C language 
in ways otherwise only possible by changing the compiler. Users declare runtime 
type variables linked to normal compile time types which contain information 
used to perform the new actions required.

Pointers in Cello are tagged with this extra information. It is stored in the 
memory just before the actual data which is pointed to. This means they are 
fully compatible with standard C pointers and can interoperate seamlessly.

The type information is mostly just a list of instances of _type classes_ or
_interfaces_. These prove to be an extremely powerful concept in Cello and are 
used for everything from Garbage Collection to Documentation. They allow you 
to use objects in terms of their _behaviours_. This is nice because it 
allows algorithms to be written in a generic way, only depending on inputs 
having specific behaviours or attributes, and not depending on their actual 
implementation.

Cello is pretty clever and it can automatically infer a whole bunch of these 
behaviours without the user having to provide them. Cello objects can be 
printed, compared, hashed, stored, garbage collected, ordered, copied and much 
more. In other words, Cello has batteries included.

## Installation

Please start by following the instructions on the 
[Installation](/learn/installation) page and then the instructions for making 
your first Cello program on the [Cello World](/learn/cello-world) page. This 
will get you ready for programming with Cello.

## Glitch Art

Let's make some glitch art using Cello. We're going to build some new Cello 
types to do this and see how they interact with standard C. Our glitch art is 
going to be inspired by the artwork of Reddit user 
[AMillionMonkeys](http://www.reddit.com/r/glitch_art/comments/20qgdi/old_man_in_a_suit_experimental_processing/). 
Who used 
[Langton's Ant](http://en.wikipedia.org/wiki/Langton%27s_ant) to generate the 
following images.

<p>
  <img src='/static/img/glitch0.png'
    style='float:left; margin-top:15px; margin-bottom:15px;' />
  <img src='/static/img/glitch1.png' 
    style='float:right; margin-top:15px; margin-bottom:15px;'/>
</p>

This is pretty cool - but we're going to use some different artwork as a base. 
How about [this](https://www.flickr.com/photos/lukepdq/116161887) beautiful 
image of a Cello player by flikr user 
[Luke G](https://www.flickr.com/photos/lukepdq/). For the purposes of this 
tutorial I've saved it as a `.tga` file and downsampled it.

<p style='text-align:center;'>
  <img src='/static/img/cello_glitch_start.png'
    style='margin-top:15px;' />
</p>

### [Download](/static/img/cello_original.tga)

## Image Object

Cello objects start as standard C structures which we then add our runtime 
information to. We must define our C structures without `typedef`'ing them. For 
example here is a `struct` we might use to represent some image data.

    struct Image {
      uint64_t width;
      uint64_t height;
      unsigned char *data;
    };
    
The C type is called `struct Image` and all it does is record a width, height, 
and pointer to some data. We can register this type with Cello using the 
`Cello` macro. We must call the Cello variable the same name as the C type, but 
without the `struct` prefix

    struct Image {
      uint64_t width;
      uint64_t height;
      unsigned char *data;
    };

    var Image = Cello(Image);

Now we have two things. We have the original C type called `struct Image` 
and a C variable representing our Cello runtime type called `Image`.

You'll notice the C type of the Cello runtime type object is `var`. In Cello 
`var` just means `void*` which is a _generic pointer_, but by convention we 
use it to mean _a pointer compatible with the Cello runtime_.

For basic types this is all that is required to interact with Cello. We can 
already allocate objects of this type either on the heap or on the 
stack, show them, compare them, put them in collections, and much more.
    
    /* Allocate on Stack or Heap */
    struct Image* x = $(Image, 0, 0, NULL);
    struct Image* y = new(Image);
    
    /* Print */
    print("This is an image: %$\n", x);

    /* Compare */
    print("Images %$ and %$ are equal? %s\n", 
      x, y, eq(x, y) ? $S("Yes") : $S("No"));
    
    /* Put in an Array */
    struct Array* a = new(Array, Image, x, y);
    print("Array of Images: %$\n", a);
    
In fact almost all of the main type classes in Cello provide default 
implementations - but the real power of Cello comes when we start to customize 
these type class implementations.

## Image Destructor

Our C structure `struct Image` has a pointer to some memory which might be 
allocated by some other function. If we want to avoid memory leaks we need to 
make sure we deallocate this memory when we are done with it. Here we can make 
use of Cello to define a custom destructor for the `Image` type.

    void Image_Del(var self) {
      struct Image* i = self;
      free(i->data);
    }

We can cast the input variable `self` to the C type `struct Image*`. This is 
possible because Cello `var` are fully compatible with 
standard C pointers. So if you have a Cello `var` pointer you know it is of a 
certain C type (such as in the destructor here), it is completely safe to cast 
it to that type and use the members directly. All we do then is call `free` on 
the data pointer.

To register this destructor with Cello we pass it to the `Cello` macro as an 
`Instance` of the `New` type class. Because we defined no custom constructor we 
just put `NULL` as that entry into the instance.

    var Image = Cello(Image, Instance(New, NULL, Image_Del));
      
Now when the Cello Garbage Collector comes to deallocate our `Image` objects it 
will call this destructor and free any memory that has been allocated by it.

## Reading Images

We want to write a `.tga` parser to read in data for the `Image` type. Rather 
than read from the C `FILE*` type we're going to read from a Cello `var` type 
that implements the `Stream` class. This will allow us to read not just from 
`FILE*` but anything that is _file-like_, which could include sockets, streams, 
processes, and a lot more. The Cello functions `sread` and `swrite` are used to 
read and write data from _file-like_ objects. 

Here are some functions I've prepared for reading and writing 3-channel TGA 
files.

    void Image_Load_TGA(struct Image* self, var stream) {

      uint16_t width, height;

      sseek(stream, 12, SEEK_SET);
      sread(stream, &width, sizeof(uint16_t));

      sseek(stream, 14, SEEK_SET);
      sread(stream, &height, sizeof(uint16_t));

      self->width  = width;
      self->height = height;
      self->data   = malloc(height * width * 3);

      sseek(stream, 18, SEEK_SET);
      sread(stream, self->data, height * width * 3);

    }
    
    void Image_Save_TGA(struct Image* self, var stream) {

      unsigned char xa= self->width % 256;
      unsigned char xb= (self->width-xa)/256;
      unsigned char ya= self->height % 256;
      unsigned char yb= (self->height-ya)/256;
      unsigned char header[18] = {
        0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, xa, xb, ya, yb, 24, 0};

      swrite(stream, header, sizeof(header));
      swrite(stream, self->data, self->width * self->height * 3);

    }
    
Now we can write a little C program that reads in a TGA file and then just 
saves it back out. We make use of the `File` object from the Cello standard 
library.

    int main(int argc, char** argv) {
      
      var f0 = new(File, $S("cello_original.tga"),  $S("rb"));
      var f1 = new(File, $S("cello_processed.tga"), $S("wb"));
      
      var img = new(Image);
        
      Image_Load_TGA(img, f0);
      Image_Save_TGA(img, f1);
    
      sclose(f0);
      sclose(f1);
    
    }

We can also use the `with` macro to get files that close automatically at 
scope exit just like in Python. The `with` macro can even be stacked nicely.
    
    int main(int argc, char** argv) {
      
      with (f0 in new(File, $S("cello_original.tga"),  $S("rb")))
      with (f1 in new(File, $S("cello_processed.tga"), $S("wb"))) {
      
        var img = new(Image);
        Image_Load_TGA(img, f0);
        Image_Save_TGA(img, f1);
        
      }
    
    }
    
Also notice that because of the Cello Garbage Collector we don't need to delete 
eother of the two file objects or `img` explicitly, and because the destructor 
for `img` will be called we don't have to clean up the memory it references 
either.

## Getting and Setting Pixels

Cello has something called Duck typing. This is the idea that an object is 
defined by it's behaviours and properties rather than it's type (if it walks 
like a duck and it quacks like a duck then it is a duck).

The `Get` type class is usually used by collections such as `Table` or `Array` 
to get and set entries, but we can also use it to `get` and `set` pixels in our 
`Image` type. The advantage of doing this is that if we change our 
representation of an `Image` (for example adding more channels), as long as it 
still provides a `get` and a `set` method our algorithm will still work.

First we need a key type. Let us define a basic 2D index type and register it 
with Cello like we did for `struct Image`.

    struct Point {
      uint64_t x, y;
    };

    var Point = Cello(Point);
    
And also let us define a color type we can return to the user.

    struct Color {
      char r, g, b;
    };
    
    var Color = Cello(Color);

To let us use `get` and `set` on our `Image` type we have to implement a type 
class called `Get`. Here are some functions that match the signature of the 
`Get` class. The `cast` function does runtime type checking to assert that the 
pointer passed in is of the given type. This allows us to safely cast to 
`struct Point*` and `struct Color*` for those arguments so we can use their
members directly.

    var Image_Get(var self, var key) {
      struct Image* i = self;
      struct Point* p = cast(key, Point);
      char r = i->data[0 + p->x*3 + p->y*i->width*3];
      char g = i->data[1 + p->x*3 + p->y*i->width*3];
      char b = i->data[2 + p->x*3 + p->y*i->width*3];
      return new(Color, $(Color, r, g, b));
    }

    var Image_Set(var self, var key, var val) {
      struct Image* i = self;
      struct Point* p = cast(key, Point);
      struct Color* c = cast(val, Color);
      i->data[0 + p->x*3 + p->y*i->width*3] = c->r;
      i->data[1 + p->x*3 + p->y*i->width*3] = c->g;
      i->data[2 + p->x*3 + p->y*i->width*3] = c->b;
    }

The reason we return `new(Color, $(Color, r, g, b))` instead of just 
`$(Color, r, g, b)` in the `Image_Get` function is because the `$` macro does 
allocation on the stack of the called function and gets a pointer to it. When 
we return this value the memory it points to will already be deallocated as the 
function has returned. For more information see 
[this](http://127.0.0.1:5000/learn/queries-and-pitfalls#returning-stack-objects) 
part of the FAQ.

Like before we need to register these functions with the `Cello` macro for the 
`Image` type using the `Get` type class. This class also has the functions 
`mem` and `rem`, but we don't implement these so we'll just provide `NULL` 
pointers.

    var Image = Cello(Image,
      Instance(New, NULL, Image_Del),
      Instance(Get, Image_Get, Image_Set, NULL, NULL));

## Glitching the Image
      
Now we can get onto defining our actual glitching routine. The algorithm will 
be very simple. Starting from some pixel `p` with some color `c`, we first read 
in the color at our location, set the color at our location to our current 
color. We then decide on a direction to move (up, down, left, right). If the 
direction to move is the same as the last direction we moved we keep our 
current color, otherwise we swap it for the color we just read in. This means 
pixels get _dragged_ across the image.

To decide on our new direction we'll hash the current color as well as the 
iteration number divided by eight. This means the algorithm should change 
direction roughly every eight steps. By default the `hash` function returns the 
same number when used on an integer, so instead we will use the `hash_data` 
function which performs a [MurmurHash](http://en.wikipedia.org/wiki/MurmurHash) 
on the raw input. 

    void Image_Glitch(struct Image* self) {

      struct Point* point = $(Point,
        rand() % self->width,
        rand() % self->height);

      var color = get(self, point);

      uint64_t dir = 0;

      for (uint64_t i = 0; i < 20000; i++) {

        var temp = get(self, point);
        set(self, point, color);

        uint64_t next = (hash(color) ^ hash_data($I(i / 8), size(Int))) % 4;
        switch (next) {
          case 0: point->x++; break;
          case 1: point->y++; break;
          case 2: point->x--; break;
          case 3: point->y--; break;
        }

        if (point->x < 0 or point->x >= self->width)  {
          point->x = rand() % self->width;
        }
        
        if (point->y < 0 or point->y >= self->height) {
          point->y = rand() % self->height;
        }

        if (dir isnt next) { color = temp; dir = next; }
        
      }

    }

Now we just plug this into our main function and we're ready to go!

    int main(int argc, char** argv) {
      
      with (f0 in new(File, $S("cello_original.tga"),  $S("rb")))
      with (f1 in new(File, $S("cello_processed.tga"), $S("wb"))) {
      
        var img = new(Image);
        Image_Load_TGA(img, f0);
        Image_Glitch(img);
        Image_Save_TGA(img, f1);
        
      }
    
    }
    
## Results
    
We can upsample the result using [imagemagick](http://www.imagemagick.org/) 
from the terminal.

    convert cello_processed.tga -filter box -resize 250x280 cello_processed.png
    
As you can see changing the iteration count can give different interesting 
results.

<p>
  <img src='/static/img/cello_glitch_quarter.png'
    style='float:left; margin-top:15px; margin-bottom:15px;' />
  <img src='/static/img/cello_glitch_half.png' 
    style='float:right; margin-top:15px; margin-bottom:15px;'/>
</p>

We can also try it on some different images. Here is the same process applied 
to some other images from flikr users 
[Lee Summers](https://www.flickr.com/photos/thisisawakeupcall/125391481),
[David](https://www.flickr.com/photos/qed_net/2769776676),
[Kristopher Chandroo](https://www.flickr.com/photos/lnoyl/4560438851),
[Tarheelcoxn](https://www.flickr.com/photos/tarheelcoxn/6409625479).

<p>
  <img src='/static/img/glitch_other0.png'
    style='float:left; margin-top:15px;' />
  <img src='/static/img/glitch_other1.png' 
    style='float:right; margin-top:15px;'/>
</p>

<p>
  <img src='/static/img/glitch_other2.png'
    style='float:left; margin-top:2px; margin-bottom:15px;' />
  <img src='/static/img/glitch_other3.png' 
    style='float:right; margin-top:2px; margin-bottom:15px;'/>
</p>

Our process is iterative, so we can also generate a gifs. Let's save out 
every 100th frame. All we need to do for this is put the following code inside 
our `for` loop.

    if (i % 100 is 0) {
      var filename = new(String);
      print_to(filename, 0, "./frames_cello/%04d.tga", $I(i / 100));
      with (f in new(File, filename, $S("wb")) {
        Image_Save_TGA(self, f);
      }
    }

What we do is generate a filename for each frame using the `print_to` function. 
This function is a lot like `sprintf` but works for any type of object that 
implements the `Format` class, so you can use it to also print to `stdout` or 
any other file object.
    
Once all of these are saved out we can make use of imagemagick to generate a 
gif.

    convert ./frames/*.tga -filter box -resize 250x280 cello_processed.gif
    
<p style='text-align:center;'>
  <img src='/static/img/cello_processed.gif' 
    style='margin-top:15px; margin-bottom:15px;'/>
</p>

And there you have it, some glitch art made with Cello!

## Conclusion

In this short introduction to Cello we made use of various features of Cello to 
easily create some glitch art. We created some new Cello objects, defined some 
type classes for them, made use of the Garbage Collector to clean up our 
resources once they were done, and used a couple of constructs from the Cello 
standard library.

I hope this guide has shown some of the potential for the high level things in 
Cello, how it easily interoperates with standard C, and that Cello programming 
can be fun.

If you're interested in learning more please check out the rest of the 
[learning resources](/learn).

## Full Source Code

Here is the final program in all its glory.

    #include "Cello.h"

    struct Point {
      int64_t x, y;
    };

    var Point = Cello(Point);

    struct Color {
      float r, g, b;
    };

    var Color = Cello(Color);

    struct Image {
      size_t width;
      size_t height;
      char* data;
    };

    var Image_Get(var self, var key) {
      struct Image* i = self;
      struct Point* p = cast(key, Point);
      char r = i->data[0 + p->x*3 + p->y*i->width*3];
      char g = i->data[1 + p->x*3 + p->y*i->width*3];
      char b = i->data[2 + p->x*3 + p->y*i->width*3];
      return new(Color, $(Color, r, g, b));
    }

    void Image_Set(var self, var key, var val) {
      struct Image* i = self;
      struct Point* p = cast(key, Point);
      struct Color* c = cast(val, Color);
      i->data[0 + p->x*3 + p->y*i->width*3] = c->r;
      i->data[1 + p->x*3 + p->y*i->width*3] = c->g;
      i->data[2 + p->x*3 + p->y*i->width*3] = c->b;
    }

    void Image_Del(var self) {
      struct Image* i = self;
      free(i->data);
    }

    void Image_Load_TGA(struct Image* self, var stream) {
      
      uint16_t width, height;
      
      sseek(stream, 12, SEEK_SET);
      sread(stream, &width, sizeof(uint16_t));

      sseek(stream, 14, SEEK_SET);
      sread(stream, &height, sizeof(uint16_t));
      
      self->width  = width;
      self->height = height;
      self->data   = malloc(height * width * 3);

      sseek(stream, 18, SEEK_SET);
      sread(stream, self->data, height * width * 3);
      
    }

    void Image_Save_TGA(struct Image* self, var stream) {
      
      unsigned char xa= self->width % 256;
      unsigned char xb= (self->width-xa)/256;
      unsigned char ya= self->height % 256;
      unsigned char yb= (self->height-ya)/256;
      unsigned char header[18] = {
        0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, xa, xb, ya, yb, 24, 0};
      
      swrite(stream, header, sizeof(header));
      swrite(stream, self->data, self->width * self->height * 3);
      
    }

    var Image = Cello(Image,
      Instance(New, NULL, Image_Del),
      Instance(Get, Image_Get, Image_Set, NULL, NULL));
      
    void Image_Glitch(struct Image* self) {

      struct Point* point = $(Point,
        rand() % self->width,
        rand() % self->height);

      var color = get(self, point);

      uint64_t dir = 0;

      for (uint64_t i = 0; i < 20000; i++) {

        var temp = get(self, point);
        set(self, point, color);

        uint64_t next = (hash(color) ^ hash_data($I(i / 8), size(Int))) % 4;
        switch (next) {
          case 0: point->x++; break;
          case 1: point->y++; break;
          case 2: point->x--; break;
          case 3: point->y--; break;
        }

        if (point->x < 0 or point->x >= self->width)  {
          point->x = rand() % self->width;
        }
        
        if (point->y < 0 or point->y >= self->height) {
          point->y = rand() % self->height;
        }

        if (dir isnt next) { color = temp; dir = next; }
        
        if (i % 100 is 0) {
          var filename = new(String);
          print_to(filename, 0, "./frames_cello/%04d.tga", $I(i / 100));
          with (f in new(File, filename, $S("wb")) {
            Image_Save_TGA(self, f);
          }
        }
        
      }

    }
      
    int main(int argc, char** argv) {
      
      system("mkdir -p frames_cello");
      system("rm -f frames_cello/*.tga");
      
      with (f0 in new(File, $S("./images/cello_original.tga"),  $S("rb")))
      with (f1 in new(File, $S("./images/cello_processed.tga"), $S("wb"))) {

        var img = new(Image);
        Image_Load_TGA(img, f0);
        Image_Glitch(img);
        Image_Save_TGA(img, f1);

      }
      
      system(
        "convert ./frames_cello/*.tga -filter box -resize 250x280 "
        "./images/cello_processed.gif");
      
      return 0;
    }




* * *


  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  <div class="col-xs-2 col-md-2"></div>
  </div>