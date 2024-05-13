import random
import time
tablero=8
class reina():
    def __init__(self):
        self.poblacion=[]
        self.distancia=[]
    def genera_elementos(self,nelem):
        self.poblacion=[]
        b=''
        for i in range(nelem):
            if i==0:
                b=str(i)+''
            else:
                b=b+''+str(i)
        opciones=list(b)
        for i in range(nelem):
            r=random.choice(opciones)
            self.poblacion.append(int(r))
            opciones.remove(r)
        return self.poblacion


    def valora_errores_posicion(self,posicion):
        distancia = 0

        for i in range(len(posicion)):
            for j in range(i + 1, len(posicion)):
                if (
                    posicion[i] == posicion[j] or
                    abs(i - j) == abs(posicion[i] - posicion[j])
                ):
                    distancia += 1
        return distancia


r=reina()
tiempo_inicio = time.time()
a=0
poblacion=r.poblacion
listarReinas=[]
num=round(tablero/2)
while True and a<150:
    if a<150:
        reinasgeneradas=r.genera_elementos(tablero)
        dist=r.valora_errores_posicion(reinasgeneradas)
        listarReinas.append(reinasgeneradas)
        a+=1
    if dist==0:
        break
while True:
    listarReinas.sort(key=r.valora_errores_posicion)
    listarReinas=listarReinas[:100]  
    mezclareinas = []  # Lista para almacenar la mezcla final
    a=0
    valoracion=False
    # Iterar sobre las listas de listarReinas 
    for i in range(len(listarReinas)):
        if i % 2 == 0:

            parte2 = listarReinas[i][:num] 
            
        else:
            parte1 = listarReinas[i][:num]
            nuevo = (parte1 + parte2)
            nuevo2=(parte2+parte1)
            if random.randint(0,10) > 9:
                nuevo[random.randint(0, tablero-1)] = random.randint(0, tablero)
                nuevo2[random.randint(0, tablero-1)] = random.randint(0, tablero)
            mezclareinas.append(nuevo)
            mezclareinas.append(nuevo2)
            dist1=r.valora_errores_posicion(mezclareinas[i])
            dist2=r.valora_errores_posicion(mezclareinas[i-1])
            if dist2==0 or dist1==0:
                if dist1==0:
                    resultado=mezclareinas[i]
                else:
                    resultado=mezclareinas[i-1]
                a=1
                break
    listarReinas=mezclareinas
    listarReinas.sort(key=r.valora_errores_posicion)
    poblacion=listarReinas
    if a==1:
        print('Solucion de las nreinas',poblacion[0])
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio
        print('El tiempo de ejecucion es de:',tiempo_ejecucion,'segundos')
        break
solucion=poblacion[0]
