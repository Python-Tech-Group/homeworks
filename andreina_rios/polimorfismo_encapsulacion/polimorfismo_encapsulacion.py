class Person(object):

    def __init__(self, name, last):
        self.name = name
        self.last = last

    def getName(self): #Polimorfismo
        return self.name


class Student(Person):

    def __init__(self, name, last, code):
        Person.__init__(self, name, last)
        self.code = code

    def __str__(self):
        return "Fullname: %s %s - Code: %s " % (self.name, self.last, self.code)

    def getName(self): #Polimorfismo
        return "I'm a student and my name is %s" % (self.name)


class Teacher(Person):
    __gen = 'F' #Encapsulamiento

    def __init__(self, name, last, ci, gen):
        Person.__init__(self, name, last)
        self.ci = ci
        if (gen == "Masculino"):
            self.__gen = 'M'

    def __str__(self):
        return "Fullname: %s %s - Number CI: %s" % (self.name, self.last, self.ci)

    def getName(self): #Polimorfismo
        if (self.__gen == 'F'):
            return "Teacher, I'm a women and my name is %s" % (self.name)
        else:
            return "Teacher, I'm a man and my name is %s" % (self.name)


alumno = Student("Boris", "Coronel", "344785")
profesor = Teacher("Angela", "Teran", "8541236","Femenino")
print(alumno.getName())
print(profesor.getName())
print(profesor.__gen) #Trata de llamar al atributo privado
