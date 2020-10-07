#Main Concepts

##Encapsulation
### 1) What is Encapsulation in Python?
Encapsulation in Python is the process of wrapping up variables and methods into a single entity. In programming, a class is an example that wraps all the variables and methods defined inside it.
### 2) How can we achieve Encapsulation in Python?
In Python, Encapsulation can be achieved using Private and Protected Access Members.
### 3) How can we define a variable as Private?
In Python, Private variables are preceded by using two underscores.
### 4) How can we define a variable as Protected?
In Python, Protected variables are preceded by using a single underscore.
```python
class Ejemplo():

    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"

    def publico(self):
        return "Soy un método público, a la vista de todo"
    def __privado(self):
        print ("Soy un metodo privado, para ti no existo")
    def get_oculto(self):
        return self.__oculto
    def set_oculto(self):
        self.__oculto = self.__privado()

objeto = Ejemplo()

print(objeto.publico())

print(objeto._Ejemplo__privado())

print(objeto.get_oculto())

objeto.set_oculto()

```

## Polimorfismo

Polimorfismo:
Esta propiedad permite implementar una misma operación pero con comportamiento distinto.

```python
class gato():
	def hablar(self):
		print("MIAU")	

class perro():
	def hablar(self):
		print("GUAU")

def escucharMascota(animal):
	animal.hablar()	

if __name__ == '__main__':
	g = gato()
	p = perro()
	escucharMascota(g)
	escucharMascota(p)
```