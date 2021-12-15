from multiprocessing import Process
import os
import time

class Vocal2(Process):
    def __init__(self,direccion,voca):
        Process.__init__(self)
        self.direccion=direccion
        self.voca=voca

    def run(self):
        print("El numero de vocales " + self.voca + " es:" + str(self.contarvocal()))

    def contarvocal(self):
        vocal=0
        archivo=open(self.direccion, "r", encoding='utf-8')
        while archivo:
                char=archivo.read(1)
                if char.lower()==self.voca:
                    vocal=vocal+1
                else:
                    if not char:
                        break
        archivo.close()
        return vocal