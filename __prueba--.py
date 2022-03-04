from enum import Enum
class Semana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7
# def __init__(self):
#     print(" ")
def main():
#creating 2 new objects from the Semana Enum
#    lunes = Semana(lunes)
    lunes=Semana.LUNES
    martes=Semana.MARTES
# printing an enum value
    print(lunes,martes)
# calling a mutator method
if __name__ == "__main__":
    main()
