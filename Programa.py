import random


class Cuestionador:

    def __init__(self) :

        self.questions=[
            "¿Qué es el ALMICANTARAT?",
            "¿Donde se encuentr el Zenit?"
            "¿Cuantos orednes existen en la taxonomia de suelos?"
        
        
        ]

        self.answer=[
            "Circulo imaginario en esfera celeste",
            "90 grados respecto al horizonte",
            "12"
        
        ]


    def jugar(self):
        #Generar un numero aleatorio entre 0 y n-1 siendo n el tamaño de la lista de preguntas

        n=len(self.questions)
        number=random.randint(0, n-1)
        print(self.questions[number])

        #Solicitar la respuesta al usuario

        respuesta=input("¿Cual es tu respuesta?")

        #Verificar si la respuesta es correcta

        if respuesta==self.answer[number]:
            print("Eres genial!!")
        else:
            print("Deje de pensar que sus papás siempre lo van a mantener!!")


