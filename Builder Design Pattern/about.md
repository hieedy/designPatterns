Builder pattern
# 🏗️ Python Builder Pattern & Immutability – Go-To Sheet

## 🔹 What Builder Pattern Solves
- Separates **construction** of an object from its **representation**.  
- Allows **step-by-step creation** of complex objects.  
- Useful when:
  - Object is **immutable**  
  - Object has **many optional/complex attributes**  
  - Different “recipes” for the same product exist  

---

## 🔹 Why Builder is Less Common in Python
- Python has **kwargs, default values, dataclasses** → constructors are already flexible.  
- Many Builder use cases in Java are solved naturally in Python.  
- Builder is still relevant for **immutability** or **complex stepwise creation**.  

---

## 🔹 When Builder Makes Sense in Python
- ✅ Product must be **immutable** (`frozen dataclass`, custom `__setattr__`).  
- ✅ You want **separate builders** for different configurations (LuxuryHouse, EcoHouse).  
- ✅ Construction requires **validation or intermediate steps**.  
- ❌ Not required if product is **mutable** and simple.  

---

## 🔹 Director in Python
- Defines “recipes” for building objects.  
- Rarely used in Python → replaced by **functions, helpers, kwargs**.  

**Example (without Director):**
```python
def make_luxury_house():
    return HouseBuilder().set_rooms(5).set_pool(True).build()
````

---

## 🔹 Immutability in Python

* `dataclass(frozen=True)` → prevents modification after creation.
* `__setattr__` override → raise `AttributeError` if object is frozen.
* Immutable objects = safer for configs, domain models, caches, multithreading.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class UserConfig:
    username: str
    timeout: int
```

---

## 🔹 Builder + Frozen Object

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

class PersonBuilder:
    def __init__(self):
        self._name = None
        self._age = None
    def set_name(self, name): self._name = name; return self
    def set_age(self, age): self._age = age; return self
    def build(self): return Person(name=self._name, age=self._age)

person = PersonBuilder().set_name("Sourabh").set_age(30).build()
```

---

## 🔹 Properties & Validation in Python

### Why `@property`?

* Replaces Java-style getters/setters with **natural attribute access**.
* Supports **validation, logging, side-effects**.

```python
class Person:
    def __init__(self, name):
        self._name = None
        self.name = name  # goes through setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
```

---

### Why `_attr` vs `attr`

* `self._name` = private storage.
* `self.name = ...` → triggers property setter.
* Prevents **infinite recursion**.

---

### When `_attr = None` is needed

* If the setter **reads current value** (logging, age cannot decrease, etc.).
* If setter only validates `value`, direct assignment is fine.

---

## 🔹 Advanced: Reusable Validated Property

```python
def validated_property(name, validator):
    storage_name = f"_{name}"
    def getter(self): return getattr(self, storage_name)
    def setter(self, value): validator(value); setattr(self, storage_name, value)
    return property(getter, setter)

def non_empty(v): 
    if not v: raise ValueError("Cannot be empty")

def non_negative(v):
    if v < 0: raise ValueError("Cannot be negative")

class Person:
    name = validated_property("name", non_empty)
    age = validated_property("age", non_negative)
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## 🔹 Rule of Thumb

* **Immutable product** → Builder recommended.
* **Mutable + simple** → Just use kwargs, dataclasses.
* **Validations** → Use `@property` or reusable property decorators.
* **Recipes (Director)** → Usually just helper functions in Python.

