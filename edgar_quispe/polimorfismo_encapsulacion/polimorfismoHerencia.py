class Aves:
    def volar(self):
        print('la mayoria de las aves pueden volar pero algunas no')


class Aguila(Aves):
    def volar(self):
        print('las aguilas pueden volar')


class Gallina(Aves):
    def volar(self):
        print('la gallina no puede volar')


obj_ave = Aves()
obj_aguila = Aguila()
obj_ave.volar()
obj_aguila.volar()
obj_gallina = Gallina()
obj_gallina.volar()
