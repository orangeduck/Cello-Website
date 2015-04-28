  <div class="row">
  <div class="col-xs-6 col-md-6">

### Methods

__sopen__

    var sopen(var self, var resource, var options);

Open the stream `self` with a given `resource` and `options`.

__sclose__

    void sclose(var self);

Close the stream `self`.

__sseek__

    void sseek(var self, int64_t pos, int origin);

Seek to the position `pos` from some `origin` in the stream `self`.

__stell__

    int64_t stell(var self);

Return the current position of the stream `stell`.

__sflush__

    void sflush(var self);

Flush the buffered contents of stream `self`.

__seof__

    bool seof(var self);

Returns true if there is no more information in the stream.

__sread__

    size_t sread(var self, void* output, size_t size);

Read `size` bytes from the stream `self` and write them to `output`.

__swrite__

    size_t swrite(var self, void* input, size_t size);

Write `size` bytes to the stream `self` and read them from `input`.

### Examples

__Usage__

    var f = sopen($(File, NULL), $S("test.bin"), $S("r"));
    
    char c;
    while (!seof(f)) {
      sread(f, &c, 1);
      putc(c, stdout);
    }
    
    sclose(f);
    



  </div>
  <div class="col-xs-6 col-md-6">

# Stream
__File-like__

The `Stream` class represents an abstract set of operations that can be performed on File-like objects.

### Definition

    struct Stream {
      var  (*sopen)(var,var,var);
      void (*sclose)(var);
      void (*sseek)(var,int64_t,int);
      int64_t (*stell)(var);
      void (*sflush)(var);
      bool (*seof)(var);
      size_t (*sread)(var,void*,size_t);
      size_t (*swrite)(var,void*,size_t);
    };
    

### Implementers

* <span class="docitem">[File](/learn/file)</span> | &nbsp; &nbsp;   _Operating System File_
* <span class="docitem">[Process](/learn/process)</span> | &nbsp; &nbsp;   _Operating System Process_

* * *

  <p style="text-align:center;">
[Back](/learn)
  </p>

  </div>
  </div>
