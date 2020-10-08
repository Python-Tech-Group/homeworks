class ejemplo:
    def __init__(self):
        self.__oculto = "me encuentro oculto en la clase"
    def publico(self):
        return "soy un metodo publico. a la vista de todos!"
    def __privado(self):
        # return "soy un metodo privado. Para ti no existo!"
        print("Dentro de la clase todos me puede ver")
    def get_oculto(self):
        return self.__oculto
    def set_oculto(self):
        self.__oculto = self.__privado()

objeto = ejemplo()
# intentanto acceder a metodo publico
print(objeto.publico())
# intentanto acceder a metodo privado
# print(objeto.__privado())
# name mangling
print(objeto._ejemplo__privado())
#accedemos al atributo __oculto del metodo __init__
# mediante el metodo get_oculto
# print(objeto.get_oculto())
objeto.set_oculto()