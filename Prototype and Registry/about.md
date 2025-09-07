# Prototype and Resgistry Design Pattern

## Intent
**Prototype**  is a creational design patten that allows you to copy existing objects without making your code dependent on their class.

## Problem
Suppose you have an object, and you want to create a exact copy of it. How would you do it ?

- First you will create a new object of it and then have to go through all the fields of original object and copy all the fields one by one.
- But what if the fields are private and you cannot access them ? 
- This means your code becomes dependent on that class as you have to know object's class to create a duplicate (**Tight Coupling**).

![](images/Screenshot 2025-09-07 210300.png)

## Solution:
The Prototype pattern delegates te clonning process to **actual** object thar are being cloned. (i.e. the class itself will have clone object that handles cloning of respective object and will return the new one to the client code).

The implementation of clone object is very similar in all the classes it just create an object of our own class, carries over all of the field values of the object into the new one (this also solves the problem of accessing private variables as every class can access it's own private members.)

An object that supports clonning is called a *prototype*. 

*When your objects have dozens of fields and hundreds of possible configurations, clonning them serve as an alternative to subclassing.*

*Here is how it works: You create a set of objects, configured in various ways. When you need an object like the one you've configured, you just **clone a protoype** instead of constructing a new object from scratch*

In short:-
- classes and respective subclasses should have clone method to support clonning of fields and return anew copy.
- Client will get the clone of the prototype from registry ( ! important -- client will get the clone of the prototype not the prototyped object itself else it will change the prototype object itself which should not be the case. ) and make the attribute changes(if required) and use it.

## Registry
The **Prototype Registry** provides an easy way to access frequently-used prototypes. It acts like a storage of prebuilt objects that are available to be copied. i.e. it holds the dictionary that contains name --> prototype object. So registry class will simply returns you the prototype of the asked type (like a search/lookup of prebuilt - objects)


## When to use:

- Use this patten when client code should not depend on the concrete classes of objects that they need to copy. 
- Use this when you want to reduce the number of *subclasses* that only differ in the way they initialize their respective objects. Example: ClassMate notebooks of same size(height and width) and price are only different with their front page design and the design of the back page. So if we need to create a 1000 copies and we know only very few attributes are gonna change then creating a prototype and clonning it and modifying that few attributes(front and back in our case) would make more sense instead of *reinitializing an object every time OR creating different different classes with those default values*.
