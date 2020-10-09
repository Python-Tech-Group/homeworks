

Herencia
La herencia es utilizada (como su nombre lo indica) para heredar: campos de datos, métodos de acceso de otra clase, ademas de poder añadir nuestros propios métodos y campos. Por lo tanto la herencia nos proporciona una manera de organizar el código para no tener que volver a repetir código.
En la terminología orientada a objetos, cuando la clase "X" es heredada por la clase "Y", "X" es llamada Super Clase o Clase Base e "Y" es llamada Subclase o Clase Derivada. Un dato más a tener en cuenta es que solo los campos y métodos que no son privados son accesibles por la Clase Derivada. Los campos y métodos privados solo son accesibles por la propia clase.

Métodos Overriding: 
Para sustituir un método proveniente de la Clase Base, en la Clase Derivada debemos definir un método con la misma firma (es decir, mismo nombre de método y mismo número de parámetros que como está definido en la Clase Base).

Polimorfismo:
La técnica de polimorfismo de la POO significa la capacidad de tomar más de una forma. Una operación puede presentar diferentes comportamientos en diferentes instancias. El comportamiento depende de los tipos de datos utilizados en la operación. El polimorfismo es ampliamente utilizado en la aplicación de la herencia.
La palabra polimorfismo viene del griego pilo que significa muchas y morfismo que significa formas, es decir, muchas formas. El polimorfismo en python es la capacidad que tienen los objetos de diferentes clases para usar un comportamiento o atributo del mismo nombre pero con diferente valor


Encapsulación:
La encapsulación consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior. En Python no existe, pero se puede simular precediendo atributos y métodos con dos barras bajas __ como indicando que son "especiales".
La encapsulación es una forma de darle uso exclusivo a los comportamientos o atributos que posee una clase, es decir, protege esos atributos y comportamientos para que no sean usados de manera externa.
En python para hacer que un atributo o comportamiento sea privado tenemos que colocar un par de guiones bajos antes del nombre del atributo o comportamiento “__nombre”

Python posee varias formas de mostrar contenido privado y una de ella en el name mangling, para aplicar el name mangling debemos hacerlos de esta manera:
print(objeto._Ejemplo__privado())
