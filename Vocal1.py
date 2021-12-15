from multiprocessing import Process
import os
import time

class Vocal1():
    def __init__(self,direccion):
        self.direccion=direccion
    def vocala(self):
        a=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
            char=archivo.read(1)
            if char.lower()=="a":
                    a=a+1
            else:
                if not char:
                    break
        archivo.close()
        return a

    def vocale(self):
        e=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
                char=archivo.read(1)
                if char.lower()=="e":
                    e=e+1
                else:
                    if not char:
                        break
        archivo.close()
        return e

    def vocali(self):
        i=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
                char=archivo.read(1)
                if char.lower()=="i":
                    i=i+1
                else:
                    if not char:
                        break
        archivo.close()
        return i

    def vocalo(self):
        o=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
                char=archivo.read(1)
                if char.lower()=="o":
                    o=o+1
                else:
                    if not char:
                        break
        archivo.close()
        return o

    def vocalu(self):
        u=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
                char=archivo.read(1)
                if char.lower()=="u":
                    u=u+1
                else:
                    if not char:
                        break
        archivo.close()
        return u