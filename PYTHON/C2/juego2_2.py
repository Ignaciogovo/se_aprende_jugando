# Programa en el que el ordenador pregunte 3 preguntas al jugador, el programa tiene que ser capaz de sumar los puntos obtenidos con las respuestas. Si no responde con a b o c pierde todos los puntos
import time

def responder_preguntas(num_pregunta):
    preguntas=[
        {"pregunta":"¿Quién mandó construir el parque de El Capricho de Madrid?","respuestas":["a) La Duquesa de Osuna","b) Carlos III","c)José I de España (Conocido como Pepe Botella)"],"verdadera":"a"},
        {"pregunta":"¿Cuántos elementos forman la Tabla Periódica?","respuestas":["a) 110 elementos","b) 112 elementos","c) 118 elementos"],"verdadera":"c"},
        {"pregunta":"¿Quién inventó la bombilla?","respuestas":["a) Isaac Newtoon","b) Thomas Edison","c) René Lorin"],"verdadera":"b"}]
    pregunta=preguntas[num_pregunta]
    print(pregunta["pregunta"])
    time.sleep(0.5)
    for i in pregunta["respuestas"]:
        print(i)
        time.sleep(0.9)

    respuesta=input("¿Cual crees que es la respuesta? ").lower()

    if respuesta not in ("a","b","c"):
        suma=-1
        texto="No has seguido las reglas ya que esa respuesta no esta entre las posibles, pierdes todos los puntos que tengas."
    else:
        if respuesta == pregunta["verdadera"]:
            suma=1
            texto="Correcto!!\nTienes un punto más"
        else:
            suma=0
            texto="Respuesta incorrecta, la verdadera era la: "+pregunta["verdadera"]


    return(suma,texto)




print("Bienvenido al juego trivial.")
print("Tienes que conseguir la máxima puntuación posible, cada pregunta que respondas adecuadamente conseguiras un punto.")
print("Para responder adecuadamente debes contestar con la letra que tenga asignada cada pregunta.")


total=0
for i in range(0,3):
    time.sleep(2)
    suma,texto=responder_preguntas(i)
    if suma == -1:
        total=0
    else:
        total=total+suma
    time.sleep(1)
    print(texto)

if total>=2:
    print("Enhorabuena, has acertado %d preguntas" % total)
else:
    print("Lo siento, necesitas más culturilla, has acertado %d preguntas" % total)
