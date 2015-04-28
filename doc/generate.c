#include "Cello.h"

void to_lower(var s) {
  for (size_t i = 0; i < len(s); i++) {
    c_str(s)[i] = tolower(c_str(s)[i]);
    if (c_str(s)[i] is ' ') { c_str(s)[i] = '-'; }
    if (c_str(s)[i] is '&') { c_str(s)[i] = 'a'; }
  }
}

static bool type_name_cmp(var fst, var snd) {
  return strcmp(c_str(fst), c_str(snd)) < 0;
}

static void print_indent(var f, const char* str) {
  print_to(f, 0, "    ");
  while (*str) {
    if (*str is '\n') { print_to(f, 0, "\n    "); }
    else { print_to(f, 0, "%c", $I(*str)); }
    str++;
  }
}

static void test_example(var object, struct Example* example) {
  
  print("Testing %$ Example '%s'...\n", object, $S(example->name));
  
  var type = copy($S(c_str(object)));
  var name = copy($S(example->name));
  to_lower(type); to_lower(name);
  
  var filename = new(String);
  var command0 = new(String);
  var command1 = new(String);

  print_to(filename, 0, "examples\\%s-%s.c", type, name);
    
  with (f in new(File, filename, $S("w"))) {
    print_to(f, 0,
      "#include \"Cello.h\"\n\n"
      "int main(int argc, char** argv) {\n"
      "%s\n"
      "return 0;\n"
      "}", $S(example->body));
  }
  
  print_to(command0, 0,
    "gcc examples\\%s-%s.c -std=gnu99 "
    "-g -Wall -lCello -lDbgHelp -o examples\\%s-%s", 
    type, name, type, name);
  
  print_to(command1, 0,
    "examples\\%s-%s.exe > examples\\%s-%s.out",
    type, name, type, name);
     
  system(c_str(command0));
  system(c_str(command1));
  
}

int main(int argc, char** argv) {
  
  var types = tuple(
    Type,  Tuple, Ref,    Box,
    Int,   Float, String, Map,
    List,  Array, Table,  Range,
    Slice, File,  Mutex,  Thread,
    Process, Function, GC);

  var classes = tuple(
    Doc,     Help,    Cast,    Size,
    Alloc,   New,     Assign,  Copy,
    Subtype, Cmp,     Hash,    Len,
    Iter,    Push,    Concat,  Get,
    Reverse, Sort,    Clear,   Reserve, 
    C_Str,   C_Int,   C_Float, Stream, 
    Pointer, Call,    Format,  Show, 
    Current, Start,   Join,    Lock,
    Mark);
  
  var defaults = tuple(
    Cast, Size,   Alloc, 
    New,  Assign, Copy,
    Cmp,  Hash);

  sort_by(types,    type_name_cmp);
  sort_by(classes,  type_name_cmp);
  sort_by(defaults, type_name_cmp);
  
  with (f in new(File, $S("object-list.md"), $S("w"))) {
    foreach (type  in   types) { print_to(f, 0, "%s ",  type); }
    foreach (class in classes) { print_to(f, 0, "%s ", class); }
  }
  
  /* Create Reference for Types */
  
  foreach (type in types) {
    
    var filename = new(String);
    print_to(filename, 0, "../pages/learn-%s.md", type);
    to_lower(filename);
    
    struct Doc* doc = type_instance(type, Doc);
    
    with (f in new(File, filename, $S("w"))) {
      
      if (doc is NULL) {
        print_to(f, 0, "No Documentation Found");
      } else {
        
        print_to(f, 0,
          "  <div class=\"row\">\n"
          "  <div class=\"col-xs-6 col-md-6\">\n"
          "\n");
          
        if (doc->methods) {
          print_to(f, 0, "### Methods\n\n");
          struct Method* methods = doc->methods();
          while (methods[0].name) {
            print_to(f, 0, "__%s__\n\n", $S(methods[0].name));
            print_indent(f, methods[0].definition);
            print_to(f, 0, "\n\n%s\n\n", $S(methods[0].description));
            methods++;
          }
        }
          
        if (doc->examples) {
          print_to(f, 0, "### Examples\n\n");
          struct Example* examples = doc->examples();
          while (examples[0].name) {
            print_to(f, 0, "__%s__\n\n", $S(examples[0].name));
            print_indent(f, examples[0].body);
            print_to(f, 0, "\n\n");
            test_example(type, examples);
            examples++;
          }
          print_to(f, 0, "\n\n");
        }
        
        print_to(f, 0,
          "  </div>\n"
          "  <div class=\"col-xs-6 col-md-6\">\n"
          "\n");
      
        print_to(f, 0, "# %s\n", type);
        
        if (doc->brief) {
          print_to(f, 0, "__%s__\n\n", $S(doc->brief()));
        }
      
        if (doc->description) {
          print_to(f, 0, "%s\n\n", $S(doc->description()));
        }
        
        if (doc->definition) {
          print_to(f, 0, "### Definition\n\n");
          print_indent(f, doc->definition());
          print_to(f, 0, "\n\n");
        }
        
        print_to(f, 0, "### Derives\n\n");
        
        foreach (class in defaults) {
          if (not type_implements(type, class)) {
            var link = new(String);
            print_to(link, 0, "(/learn/%s)", class);
            to_lower(link);
            print_to(f, 0, 
              "* <span style=\"width:75px; float:left;\">"
              "[%s]%s</span>", class, link);
            struct Doc* cdoc = type_instance(class, Doc);
            if (cdoc->methods) {
              struct Method* methods = cdoc->methods();
              while (methods[0].name) {
                print_to(f, 0, "`%s` ", $S(methods[0].name));
                methods++;
              }
            }
            print_to(f, 0, "\n");
          }
        }
        
        print_to(f, 0, "### Implements\n\n");
        
        foreach (class in classes) {
          if (type_implements(type, class)) {
            var link = new(String);
            print_to(link, 0, "(/learn/%s)", class);
            to_lower(link);
            print_to(f, 0, 
              "* <span style=\"width:75px; float:left;\">"
              "[%s]%s</span>", class, link);
            struct Doc* cdoc = type_instance(class, Doc);
            if (cdoc->methods) {
              struct Method* methods = cdoc->methods();
              while (methods[0].name) {
                print_to(f, 0, "`%s` ", $S(methods[0].name));
                methods++;
              }
            }
            print_to(f, 0, "\n");
          }
        }
        
        print_to(f, 0,
          "\n"
          "* * *\n"
          "\n"
          "  <p style=\"text-align:center;\">\n"
          "[Back](/learn)\n"
          "  </p>\n"
          "\n"
          "  </div>\n"
          "  </div>\n");
      
      }
      
    }
    
  }
  
  /* Create Reference for Classes */
  
  foreach (class in classes) {
    
    var filename = new(String);
    print_to(filename, 0, "../pages/learn-%s.md", class);
    to_lower(filename);
    
    struct Doc* doc = type_instance(class, Doc);
    
    with (f in new(File, filename, $S("w"))) {
      
      if (doc is NULL) {
        print_to(f, 0, "No Documentation Found");
      } else {
        
        print_to(f, 0,
          "  <div class=\"row\">\n"
          "  <div class=\"col-xs-6 col-md-6\">\n"
          "\n");
          
        if (doc->methods) {
          print_to(f, 0, "### Methods\n\n");
          struct Method* methods = doc->methods();
          while (methods[0].name) {
            print_to(f, 0, "__%s__\n\n", $S(methods[0].name));
            print_indent(f, methods[0].definition);
            print_to(f, 0, "\n\n%s\n\n", $S(methods[0].description));
            methods++;
          }
        }
          
        if (doc->examples) {
          print_to(f, 0, "### Examples\n\n");
          struct Example* examples = doc->examples();
          while (examples[0].name) {
            print_to(f, 0, "__%s__\n\n", $S(examples[0].name));
            print_indent(f, examples[0].body);
            print_to(f, 0, "\n\n");
            test_example(class, examples);
            examples++;
          }
          print_to(f, 0, "\n\n");
        }
        
        print_to(f, 0,
          "  </div>\n"
          "  <div class=\"col-xs-6 col-md-6\">\n"
          "\n");
      
        print_to(f, 0, "# %s\n", class);
        
        if (doc->brief) {
          print_to(f, 0, "__%s__\n\n", $S(doc->brief()));
        }
      
        if (doc->description) {
          print_to(f, 0, "%s\n\n", $S(doc->description()));
        }
        
        if (doc->definition) {
          print_to(f, 0, "### Definition\n\n");
          print_indent(f, doc->definition());
          print_to(f, 0, "\n\n");
        }
        
        if (mem(defaults, class)) {
          
          print_to(f, 0, "### Derivers\n\n");
          
          foreach (type in types) {
            if (not type_implements(type, class)) {
              struct Doc* doc = type_instance(type, Doc);
              var link = new(String);
              print_to(link, 0, "(/learn/%s)", type);
              to_lower(link);
              print_to(f, 0,
                "* <span class=\"docitem\">[%s]%s</span>"
                " | &nbsp; &nbsp;   _%s_\n", type, link, 
                doc->brief ? $S(doc->brief()) : $S(""));
            }
          }
        }
        
        print_to(f, 0, "### Implementers\n\n");
        
        foreach (type in types) {
          if (type_implements(type, class)) {
            struct Doc* doc = type_instance(type, Doc);
            var link = new(String);
            print_to(link, 0, "(/learn/%s)", type);
            to_lower(link);
            print_to(f, 0,
              "* <span class=\"docitem\">[%s]%s</span>"
              " | &nbsp; &nbsp;   _%s_\n", type, link, 
              doc->brief ? $S(doc->brief()) : $S(""));
          }
        }
        
        print_to(f, 0,
          "\n"
          "* * *\n"
          "\n"
          "  <p style=\"text-align:center;\">\n"
          "[Back](/learn)\n"
          "  </p>\n"
          "\n"
          "  </div>\n"
          "  </div>\n");
      
      }
      
    }
     
  }
  
  /* Create Index Page */
  
  with (f in new(File, $S("../pages/learn.md"), $S("w"))) {

    print_to(f, 0,
      "\n"
      "  <div class=\"row\">\n"
      "  <div class=\"col-xs-6 col-md-6\">\n"
      "\n"
      "### Learning\n"
      "\n"
      "Here are several resources for getting started with Cello.\n"
      "\n"
      "* [Installation](/learn/installation)\n"
      "* [Cello World](/learn/cello-world)\n"
      "* [Quickstart](/learn/quickstart)\n"
      "* [Common Queries / Pitfalls](/learn/pitfalls)\n"
      "* [Type / Classes](/learn/types)\n"
      "* [Exceptions](/learn/exceptions)\n"
      "* [Closures](/learn/functions)\n"
      "* [Garbage Collection](/learn/memory)\n"
      "\n"
      "### Articles\n"
      "\n"
      "Here are several articles related to the creation and inner workings of Cello.\n"
      "\n"
      "* [A Fat Pointer Library](/learn/a-fat-pointer-library)\n"
      "* [Hacking C to it's limits](/learn/hacking-c-to-its-limits)\n"
      "* [Cello vs C++ vs ObjC](/learn/cello-vs-cpp-vs-objc)\n"
      "\n"
      "  </div>\n"
      "  <div class=\"col-xs-6 col-md-6\">\n"
      "\n"
      "### Reference\n"
      "\n"
      "Here is the full reference documentation for all the Types and Classes defined\n"
      "by Cello. All of this information is also avaliable via the Cello \n"
      "<code>help</code> function which can be called with any Type object.\n"
      "\n");
      
    print_to(f, 0, "\n__Types__\n\n");
    
    foreach (type in types) {
      struct Doc* doc = type_instance(type, Doc);
      var link = new(String);
      print_to(link, 0, "(/learn/%s)", type);
      to_lower(link);
      print_to(f, 0,
        "* <span class=\"docitem\">[%s]%s</span>"
        " | &nbsp; &nbsp;   _%s_\n", type, link, 
        doc->brief ? $S(doc->brief()) : $S(""));
    }
    
    print_to(f, 0, "\n__Classes__\n\n");

    foreach (class in classes) {
      struct Doc* doc = type_instance(class, Doc);
      var link = new(String);
      print_to(link, 0, "(/learn/%s)", class);
      to_lower(link);
      print_to(f, 0,
        "* <span class=\"docitem\">[%s]%s</span>"
        " | &nbsp; &nbsp;   _%s_\n", class, link, 
        doc->brief ? $S(doc->brief()) : $S(""));
    }
    
    print_to(f, 0, "\n\n  </div>\n  </div>\n\n");

  }
  
  return 0;
  
}