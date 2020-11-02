# -*- coding: utf-8 -*-

class televisao:
     #Construtor , self e objeto em si
     def __init__(self, min, max):
         self.ligada = False
         self.canal = 2
         self.cmin = min
         self.cmax = max
    
    #metodos personalizados
     def muda_canal_para_baixo(self):
         if(self.canal-1 >= self.cmin):
               self.canal -= 1
     def muda_canal_para_cima(self):
         if(self.canal+1 <= self.cmax):
               self.canal += 1
     def muda_canal(self,valor):
               self.canal = valor
                              
