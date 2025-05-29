while True:    
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es:", edad)
        break
    except:
        print("Ingresaste un valor erróneo")
    finally:
        print("La ejecución ha terminado")