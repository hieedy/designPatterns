# Singleton Pattern
* This belongs to creation design patterns.
* It solves the problem of sharing expensive resources such that it can be initialised once and can be used anywhere.

## Example:
* Logger, DatabaseConnection

## Pros:
* Better resource management.
* Avoid duplication of object creation that shared the same behaviour/

## Cons:
* Testing singleton classes are different as you cannot initialize the same object multiple time with different values.

## Ways to implement Singleton in Python
* import from module
* by overriding \_\_new__
* by using decorator
* by using metaclass
* Borg pattern (by sharing state - update \_\_dict__ attribute)
