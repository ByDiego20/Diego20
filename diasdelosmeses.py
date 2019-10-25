def diasmeses():
    a=input("Introduzca numero del dia: ")
    b=input("Introduzca numero del mes: ")
    c=input("Introduzca numero del año: ")
    
    if b is 1:
        b = "Enero"
    elif b is 2:
        b = "Febrero"
    elif b is 3:
        b = "Marzo"
    elif b is 4:
        b = "Abril"
    elif b is 5:
        b = "Mayo"
    elif b is 6:
        b = "Junio"
    elif b is 7:
        b = "Julio"
    elif b is 8:
        b = "Agosto"
    elif b is 9:
        b = "Septiembre"
    elif b is 10:
        b = "Octubre"
    elif b is 11:
        b = "Noviembre"
    elif b is 12:
        b = "Diciembre"
    bb=str(b)
    aa=str(a)
    cc=str(c)

    print(aa + " / " + bb + " / " + cc)
    
diasmeses()
