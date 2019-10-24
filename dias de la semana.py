def dias_de_la_semana():
    i=input(str("inserta un numero del 1 al 7: "))
                
    if i is 1:
        print("Lunes")
    if i is 2:
        print("Martes")
    if i is 3:
        print("Miercoles")
    if i is 4:
        print("Jueves")
    if i is 5:
        print("Viernes")
    if i is 6:
        print("Sabado")
    if i is 7:
        print("Domingo")
    else:
        print("No existe\n")
        return dias_de_la_semana()

dias_de_la_semana()
