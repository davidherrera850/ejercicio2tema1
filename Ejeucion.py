
import os
import time
from Vocal1 import Vocal1
from Vocal2 import Vocal2
if __name__ == "__main__":
    direccionarchivo=input("Diga ruta")
    if os.path.exists(direccionarchivo):
        if os.path.isfile(direccionarchivo):
            inicioEjecucionS = time.perf_counter()
            vocaluno=Vocal1(direccionarchivo)
            print("a= "+str(vocaluno.vocala()))
            print("e= " + str(vocaluno.vocale()))
            print("i= " + str(vocaluno.vocali()))
            print("o= " + str(vocaluno.vocalo()))
            print("u= " + str(vocaluno.vocalu()))

            finalEjecucionS = time.perf_counter() - inicioEjecucionS
            print("Tiempo de ejection vocal1 es:" + str(round(finalEjecucionS, 2)))
        inicioEjecucion = time.perf_counter()
        vocala = Vocal2(direccionarchivo,"a")
        vocale = Vocal2(direccionarchivo,"e")
        vocali = Vocal2(direccionarchivo,"i")
        vocalo = Vocal2(direccionarchivo,"o")
        vocalu = Vocal2(direccionarchivo,"u")
        vocala.start()
        vocale.start()
        vocali.start()
        vocalo.start()
        vocalu.start()
        vocala.join()
        vocale.join()
        vocali.join()
        vocalo.join()
        vocalu.join()
        finalEjecucion = time.perf_counter() - inicioEjecucion
        print("El tiempo de ejecucion del proceso contar vocales en paralelo es:" + str(round(finalEjecucion, 2)))
    else:
        print("No es archivo")