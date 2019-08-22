import sys

class Ahorcado(object):
     def init (self, no_fallas, palabra):
         self.no_fallas = no_fallas
         self.palabra = palabra
         self.adivinar = []
         self.ya_gane = False
         self.falle = 0
         self.ya_perdi = False
         
     def jugar(self, letra):
         if letra in self.palabra:
             self.adivinar.append(letra)
             gane = True
             for letra in self.palabra:
                 if letra not in self.adivinar:
                     gane = False
                 if gane:
                     self.ya_gane = True
         else:
             self.falle += 1
         if self.falle >= self.no_fallas:
             self.ya_perdi = True
         self.estado()
         
     def estado(self):
         temp_palabra = " "
         for letra in self.palabra:
             if letra in self.adivinar:
                 temp_palabra += letra
             else:
                 temp_palabra += "_"
         print(temp_palabra)
         print("Has cometido %d errores"%(self.falle))
         
         entero = int(input("Escribe un entero: "))
         palabra = input("Escribe una palabra: ")
