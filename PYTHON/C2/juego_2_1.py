import time
####MATEMAGIA

def pensar():
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5) 
    print("...")
    time.sleep(0.5) 



# IMPRIMIR UN MENSAJE QUE ANIME AL JUGADOR PENSAR EN UN NÚMERO:


print("Bienvenido al juego de Matemagia. \nPiense en un número al azar.")
time.sleep(1)

# INPRIMIR UN MENSAJE QUE ORDENE AL JUGADOR REALIZAR ESTAS OPERACIONES
# doblar el número secreto
# multiplicar por 5 el número secreto


print("Suma ese número por si mismo")
time.sleep(1)


print("A continuación, multiplica el resultado por 5")
time.sleep(1)
num=input("Escribe el resultado final: ")
pensar()
# Le quitamos al número el ultimo valor ya que lo hemos multiplicado por 10
num=num[:-1]
print("el resultado es: "+num)