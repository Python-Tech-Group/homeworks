# Encapsulation and Polymorphism in Python

## Encapsulation
It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

### Protected members
Protected members are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
```python
class Base:
    def __init__(self):
         
        # Protected member
        self._a = 2
```
### Private members
Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class. However, to define a private member prefix the member name with double underscore “__”.
```python
class Base:
    def __init__(self):
        
        # Private member
        self.__c = "This variable can be accessed only in this class"
```
## Polymorphism
Polymorphism is the ability of an object to take on many forms. It means  same function name (but different signatures) being uses for different types.

#### Example of inbuilt polymorphic functions
```python
# len() being used for a string 
print(len("geeks")) 

# len() being used for a list 
print(len([10, 20, 30])) 
```
##### Output
```bash
5
3
```
#### Example of user defined polymorphic functions
```python
def add(x, y, z = 0):  
    return x + y+z 
  
print(add(2, 3)) 
print(add(2, 3, 4)) 
```
##### Output
```bash
5
9
```
#### Polymorphism with class methods
```python
class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
  
    def language(self): 
        print("Hindi is the most widely spoken language of India.") 
  
    def type(self): 
        print("India is a developing country.") 
  
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
        print("English is the primary language of USA.") 
  
    def type(self): 
        print("USA is a developed country.") 
  
obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type() 
```
##### Output
```bash
New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
```
#### Polymorphism and Inheritance
```python
class Bird: 
  def intro(self): 
    print("There are many types of birds.") 
      
  def flight(self): 
    print("Most of the birds can fly but some cannot.") 
    
class sparrow(Bird): 
  def flight(self): 
    print("Sparrows can fly.") 
      
class ostrich(Bird): 
  def flight(self): 
    print("Ostriches cannot fly.") 
      
obj_bird = Bird() 
obj_spr = sparrow() 
obj_ost = ostrich() 
  
obj_bird.intro() 
obj_bird.flight() 
  
obj_spr.intro() 
obj_spr.flight() 
  
obj_ost.intro() 
obj_ost.flight() 
```
##### Output
```bash
There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.
```
#### Polymorphism with a Function and objects
```python
class India(): 
	def capital(self): 
		print("New Delhi is the capital of India.") 

	def language(self): 
		print("Hindi is the most widely spoken language of India.") 

	def type(self): 
		print("India is a developing country.") 

class USA(): 
	def capital(self): 
		print("Washington, D.C. is the capital of USA.") 

	def language(self): 
		print("English is the primary language of USA.") 

	def type(self): 
		print("USA is a developed country.") 

def func(obj): 
	obj.capital() 
	obj.language() 
	obj.type() 

obj_ind = India() 
obj_usa = USA() 

func(obj_ind) 
func(obj_usa)
```
##### Output
```bash
New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
```
