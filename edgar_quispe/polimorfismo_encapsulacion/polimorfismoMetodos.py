class Bolivia:
    def capital(self):
        print('Sucre')
    def idioma(self):
        print('en Bolivia se habla espanol')


class Francia:
    def capital(self):
        print('Paris')

    def idioma(self):
        print('en Francia se habla frances')

boliviano = Bolivia()
frances = Francia()

for pais in (boliviano, frances):
    pais.capital()
    pais.idioma()