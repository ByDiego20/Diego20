def piramide ():
    rango = input("Introduzca el numero de filas: ")
    for i in range (1, rango+1):
        print" "* (rango-(i-1))+"*"*((i)*2-1)
        
piramide()
