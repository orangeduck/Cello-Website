
from cello_classes import cello_classes
from cello_types import cello_types

f = open("output/documentation.md", "w")
f.write(
"""

Contents
--------

### Introduction

* [Installation](/documentation/installation)
* [Cello World](/documentation/celloworld)

### QuickStart

* [Containers and Collections](/documentation/containers)
* [Type and Classes](/documentation/types)
* [Exceptions](/documentation/exceptions)
* [First Class Functions](/documentation/functions)
* [Memory Management](/documentation/memory)
    
### Articles

* [Hacking C to it's limits](/documentation/hacking)
* [Cello vs C++ vs ObjC](/documentation/comparison)
    
### Reference

* __Types__
"""
+
"".join(["""    * <span style="width:100px; float:left;">[%s](reference/%s)</span> _%s_\n""" % (t["name"], t["link"], t["tag"]) for _, t in sorted(cello_types.iteritems())])
+
"""

* __Classes__
"""
+
"".join(["""    * <span style="width:100px; float:left;">[%s](reference/%s)</span> _%s_\n""" % (c["name"], c["link"], c["tag"]) for _, c in sorted(cello_classes.iteritems())])
+
"""
    
* __Other__
    * [Exception](reference/exception)
    * [Lambda](reference/lambda)
    * [Value](reference/value)
"""
)

f.close()
  
for _, t in sorted(cello_types.iteritems()):
    
    print("Processing %s" % t["name"])
    
    f = open("output/" + t["filename"], "w")
    
    title = t["name"]
    
    f.write(title + "\n")
    f.write("-" * len(title) + "\n")
    f.write("__" + t["tag"] + "__\n")
    f.write(t["description"])
    
    def funcs_list(funcs):
        return " ".join(["`"+fu+"`" for fu in filter(None, funcs.split(" "))])
    
    f.write("\n\n### Implements\n\n")
    implement = filter(None, t["implements"].split(" "))
    implement_links = ['* <span style="width:75px; float:left;">[%s](%s)</span> %s'
        % (cello_classes[c]["name"], 
           cello_classes[c]["link"], 
           funcs_list(cello_classes[c]["funcs"])) 
           for c in implement]
    for l in implement_links: f.write(l + "\n")
    
    def cello_thing(name):
        if name in cello_types: return cello_types[name]
        if name in cello_classes: return cello_classes[name]
        raise KeyError(name)
    
    f.write("\n\n### See Also\n\n")
    see_also = filter(None, t["related"].split(" "))
    see_also_links = ['* <span style="width:75px; float:left;">[%s](%s)</span> _%s_'
        % (cello_thing(r)["name"], cello_thing(r)["link"], cello_thing(r)["tag"]) for r in see_also]
    for s in see_also_links: f.write(s + "\n")
    
    f.write("\n\n### Examples\n")
    f.write(t["examples"] + "\n")
    f.write("[Back](/documentation)\n")
    
    f.close()
    
for _, c in sorted(cello_classes.iteritems()):

    print("Processing %s" % c["name"])
    
    f = open("output/" + c["filename"], "w")
    
    title = c["name"]
    
    f.write(title + "\n")
    f.write("-" * len(title) + "\n")
    f.write("__" + c["tag"] + "__\n")
    f.write(c["description"])
    
    def funcs_list(funcs):
        return " ".join(["`"+fu+"`" for fu in filter(None, funcs.split(" "))])
    
    f.write("\n\n### Implementers\n\n")
    implementers = [t for t in cello_types.values() if c["name"] in t["implements"].split(" ")]
    implementers_links = ['* <span style="width:75px; float:left;">[%s](%s)</span> _%s_'
        % (t["name"], t["link"], t["tag"]) 
           for t in implementers]
    for l in implementers_links: f.write(l + "\n")
    
    def cello_thing(name):
        if name in cello_types: return cello_types[name]
        if name in cello_classes: return cello_classes[name]
        raise KeyError(name)
    
    f.write("\n\n### See Also\n\n")
    see_also = filter(None, c["related"].split(" "))
    see_also_links = ['* <span style="width:75px; float:left;">[%s](%s)</span> _%s_'
        % (cello_thing(r)["name"], cello_thing(r)["link"], cello_thing(r)["tag"]) for r in see_also]
    for s in see_also_links: f.write(s + "\n")
    
    f.write("\n\n### Examples\n")
    f.write(c["examples"] + "\n")
    f.write("[Back](/documentation)\n")
    
    f.close()

    
