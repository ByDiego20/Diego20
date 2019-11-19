def pajarita ():
    filas = int(input("Filas: \n"))
    filasm = filas/2
    for i in range (1,filas+1):
        if i <=filasm:
            print ("*"*(i)+" "*((filas-2*i))+"*"*((i)))
        elif i>filasm:
            print("*"*((filas-i))+" "*((filas-2*(filas-i)))+"*"*((filas-i)))

pajarita()
