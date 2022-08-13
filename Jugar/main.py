from random import randint

respuesta = "s"
puntajeJugador = 0
puntajeCompu = 0
while respuesta == "s":
    print("*" * 55)
    print("              Piedra, papel o tijera")
    print("*" * 55)
    jugador = input("Escribir tu jugada: piedra, papel o tijera: ")

    eleccion = ["piedra", "papel", "tijera"]
    computadora = eleccion[randint(0, 2)]
    print("La computadora elige: ", computadora)

    if computadora == jugador:
        print("Hay un empate")
    elif computadora == "piedra" and jugador == "tijera":
        print("La computadora gana. La pidra le gana a tijera")
        puntajeCompu += 1
    elif computadora == "papel" and jugador == "tijera":
        print("El jugador gana. La tijera le gana al papel")
        puntajeJugador += 1
    elif computadora == "tijera" and jugador == "piedra":
        print("El jugador gana. La piedra le gana a tijera")
        puntajeJugador += 1
    elif computadora == "papel" and jugador == "piedra":
        print("La computadora gana. El papel le gana a la piedra")
        puntajeCompu += 1
    elif computadora == "piedra" and jugador == "papel":
        print("El jugador gana. El papel le gana a la piedra")
        puntajeJugador += 1
    elif computadora == "tijera" and jugador == "papel":
        print("La computadora gana. La tijera le gana al papel")
        puntajeCompu += 1
    print("El puntaje del jugador es: ", puntajeJugador)
    print("El puntaje de la computadora es: ", puntajeCompu)
    print("Desea continuar? si(s) No(n)")
    respuesta = input()
