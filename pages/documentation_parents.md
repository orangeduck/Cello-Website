Parents
-------

Parent types are another experimental addition to Cello which are not made use of in the standard library, but may prove useful to users. They are designed to overcome a problem with the _Type Class_ system.

The strength of _Type Classes_ is that they allow users to define new _Data Types_ which will work 'out of the box' with standard library _Type Classes_. For example I can create a new _Data Type_ and use it with the standard library `Eq` _Type Class_ without any problems.

Their weakness is that they don't allow users to extend standard library _Data Types_ to work with newly defined _Type Classes_. For example I cannot define a new data manipulation _Type Class_ and have it work on `String`.

Because of this, the order of declaration, and the way in which you build up and compose a type system from smaller parts is somewhat one-directional. Functions always take priority over Data.

Building a type system in a bi-directional way is possible, and supported in some lanaguages. It is often called _mixins_. In Cello we can emulate this behaviour by using what we call _Parent Types_. These allow the user to extend some existing data type to implement a number of new classes. They aren't as elegant as normal _Type Classes_ but their end functionality is the same.

For example say we want the type `Int` to implement our new class `be_awesome`. Defined as follows...

    class {
      void (*be_awesome)(var);
    } BeAwesome;

    void be_awesome(var self) {
      return type_class_method(self, BeAwesome, be_awesome, self);
    }

First we create a new minimal type that implements `BeAwesome`...

    void IntParent_BeAwesome(var self) {
      println("I am being awesome with value %i", self);
    }

    instance(IntParent, BeAwesome) = { IntParent_BeAwesome };

    var IntParent = type_data {
      type_begin(IntParent),
      type_entry(IntParent, BeAwesome),
      type_end(IntParent),
    };

Then we register this type as the _Parent Type_ of `Int`. This means that if `Int` does not implement a type class we can look to it's parent type to perform the specified functionality. 
    
    int main(int argc, char** argv) {
      
      Type_Inherit(Int, IntParent);

      var x = $(Int, 52);
      be_awesome(x); /* 'I am being awesome with value 52' */
      
      return 0;
    }
  

In this way we can extend existing types to work with new functions. The solution isn't ideal because it requires registration at runtime, but it can still prove both useful and powerful in a number of applications.


[Back](/documentation)
