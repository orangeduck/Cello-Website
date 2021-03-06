
Classes
-------

A __Class__ in Cello is a _typeclass_ - better known as an _interface_.

These are defined to allow for overloaded or generic functions which can work on multiple data types.

This is an abstract understanding, but they can be understood in real terms too. A __Class__ is simply a data structure consisting of a bunch of function pointers (or even other things) which a __Type__ must fill out when it _implements_. 

They are defined in header files as follows...

    /** Vector - vector operations */

    class {
      float (*dot)(var, var);
      float (*length)(var);
    } Vector;

    float dot(var self, var obj);
    float length(var self);

This shows a `Vector` class with two functions `dot` and `length`.

To access the implemented versions of these function pointers one must use `type_class` on an __Type__ object, specifying the __Class__. It is done in the source file as follows...

    float dot(var self, var obj) {
      return type_class_method(type_of(self), Vector, dot, self, obj);
    }

    float length(var self) {
      return type_class_method(type_of(self), Vector, length, self);
    }


Types
-----

A __Type__ is an object which _implements_ a number of __Classes__.

Typically __Types__ have an associated data object. This data object should be named `TypeData` and __must__ start with a `var` entry which specifies the __Type__.

The practical realisation of a __Type__ is that it is a list of pointers to __Classes__ which `type_class` can then look up.

In the header a __Type__  `Vec2` can be defined as follows...

    global var Vec2;

    data {
      var type;
      float x, y;
    } Vec2Data;
    
    var Vec2_New(var self, var_list vl);
    var Vec2_Delete(var self);
    size_t Vec2_Size(void);
    
    void Vec2_Assign(var self, var obj);
    var Vec2_Copy(var self);

    var Vec2_Eq(var self, var obj);

    float Vec2_Dot(var self, var obj);
    float Vec2_Length(var self);

    instance(Vec2, New) = { Vec2_New, Vec2_Delete, Vec2_Size };
    instance(Vec2, Assign) = { Vec2_Assign };
    instance(Vec2, Copy) = { Vec2_Copy };
    instance(Vec2, Eq) = { Vec2_Eq };
    instance(Vec2, Vector) = { Vec2_Dot, Vec2_Length };

In the source file we can use some macros to aid construction of the __Type__ object, and then define the rest of the functions.

    var Vec2 = type_data {
      type_begin(Vec2),
      type_entry(Vec2, New),
      type_entry(Vec2, Assign),
      type_entry(Vec2, Copy),
      type_entry(Vec2, Eq),
      type_entry(Vec2, Show),
      type_entry(Vec2, Vector),
      type_end(Vec2)
    };

    var Vec2_New(var self, var_list vl) {
      Vec2Data* v = cast(self, Vec2);
      v->x = as_double(var_list_get(vl));
      v->y = as_double(var_list_get(vl));
      return self;
    }

    var Vec2_Delete(var self) {
      return self;
    }
    
    size_t Vec2_Size(void) {
      return sizeof(Vec2Data);
    }

    void Vec2_Assign(var self, var obj) {
      Vec2Data* v1 = cast(self, Vec2);
      Vec2Data* v2 = cast(obj, Vec2);
      v1->x = v2->x;
      v1->y = v2->y;
    }
    
    var Vec2_Copy(var self) {
      Vec2Data* v = cast(self, Vec2);
      return new(Vec2, $(Real, v->x), $(Real, v->y));
    }

    var Vec2_Eq(var self, var obj) {
      Vec2Data* v1 = cast(self, Vec2);
      Vec2Data* v2 = cast(obj, Vec2);
      return bool_var(v1->x is v2->x and v1->y is v2->y);
    }

    float Vec2_Dot(var self, var obj) {
      Vec2Data* v1 = cast(self, Vec2);
      Vec2Data* v2 = cast(obj, Vec2);
      return (v1->x * v2->x + v2->y * v2->y);
    }

    float Vec2_Length(var self) {
      Vec2Data* v = cast(self, Vec2);
      return sqrt(v->x * v->x + v->y * v->y);
    }

    
And this is all it takes to program a __Class__ and a __Type__!
    
[Back](/documentation)
