Stream
------
__File-like__

The `Stream` class provides a way to treat objects as File-Like such that they can be read from and written to.


### Methods

-------------------------------

    var stream_open(var self, const char* name, const char* access);

Open an object stream with a certain filename with given access rights

* __Parameters__
    * `self` object to open
    * `name` filename to open
    * `access` access rights
* __Returns__ opened object

------------------------------- 

    void stream_close(var self);

Close an object stream

* __Parameters__
    * `self` stream object to close
* __Returns__ None

------------------------------- 

    void stream_seek(var self, int pos, int origin);

Seek to a given position in a stream

* __Parameters__
    * `self` stream object to seek
    * `pos` Position to seek to
    * `origin` seek origin. Must be one of `SEEK_SET`, `SEEK_END`, `SEEK_CUR`
* __Returns__ None

------------------------------- 

    int stream_tell(var self);

return the current position in the stream

* __Parameters__
    * `self` stream object to tell
* __Returns__ position in stream

------------------------------- 

    void stream_flush(var self);

flush all queued reads and writes in a stream

* __Parameters__
    * `self` stream object to flush
* __Returns__ None

------------------------------- 

    bool stream_eof(var self);

returns if a stream is at the end

* __Parameters__
    * `self` stream object to check
* __Returns__ if a stream object is at the end

------------------------------- 

    int stream_read(var self, void* output, int size);

read a block of data from a stream

* __Parameters__
    * `self` stream object to read from
    * `output` pointer to output data block
    * `size` amount of data to read in bytes
* __Returns__ number of bytes read

------------------------------- 

    int stream_write(var self, void* input, int size);

write a block of data to a stream

* __Parameters__
    * `self` stream object to write to
    * `output` pointer to input data block
    * `size` amount of data to write in bytes
* __Returns__ number of bytes written

------------------------------- 


### Signature


    class {
      var (*stream_open)(var,const char*,const char*);
      void (*stream_close)(var);
      void (*stream_seek)(var,int,int);
      int (*stream_tell)(var);
      void (*stream_flush)(var);
      bool (*stream_eof)(var);
      int (*stream_read)(var,void*,int);
      int (*stream_write)(var,void*,int);
    } Stream;
    

### Implementers

* <span style="width:75px; float:left;">[File](file)</span> _Operating System File_


### See Also

* <span style="width:75px; float:left;">[Serialize](serialize)</span> _Convertible to Serial Form_
* <span style="width:75px; float:left;">[Format](format)</span> _Read or Writable using a Format String_
* <span style="width:75px; float:left;">[With](with)</span> _Can be entered and exited_


### Examples

__Usage__

    var f = $(File, NULL);
    
    stream_open(f, "test.bin", "w");
    
    char c;
    while (!stream_eof(f)) {
        stream_read(f, &c, 1);
        putc(c);
    }
    
    stream_close(f);


[Back](/documentation)
