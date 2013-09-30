Parents
-------

Parent types are another experimental addition to Cello which are not made use of in the standard library, but may prove useful to users.

The strength of _Type Classes_ is that they allow users to define new _Data Types_ which will work 'out of the box' with standard library _Type Classes_.

Their weakness is that they don't allow users to extend standard library _Data Types_ to work with newly defined _Type Classes_.

The order of declaration, and the way in which you build up and compose a type system from smaller parts is somewhat one-directional.

The ability to build up some type system in a bi-directional way is supported in some lanaguages and sometimes called _mixins_. In Cello we can somewhat emulate this behaviour by using what we call _Parent Types_. These allow the user to extend some existing data type to implement a number of new classes.

For example say we want the type `Int` to implement our new class `be_awesome`.

    class {
      void (*be_awesome)(var);
    } BeAwesome;

    void be_awesome(var self) {
      return type_class_method(self, BeAwesome, be_awesome, self);
    }

First we create a new minimal type that implements `BeAwesome`.

    global var IntParent;

    void IntParent_BeAwesome(var self) {
      println("I am being awesome with value %i", self);
    }

    instance(IntParent, BeAwesome) = { IntParent_BeAwesome };

    var IntParent = type_data {
      type_begin(IntParent),
      type_entry(IntParent, BeAwesome),
      type_end(IntParent),
    };

Then we register this type as the _Parent Type_ of `Int`.
    
    int main(int argc, char** argv) {
      
      Type_Inherit(Int, IntParent);
      var x = $(Int, 52);
      
      be_awesome(x); /* 'I am being awesome with value 52' */
      
      return 0;
    }
  

In this way we can extend existing types to work with new functions. The solution isn't ideal because it requires registration at runtime, but it can still prove both useful and powerful in a number of applications.


[Back](/documentation)
