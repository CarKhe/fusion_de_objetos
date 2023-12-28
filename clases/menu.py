class Menu:
    def menu():
        while True:
            print("Menú:")
            print(" 1.-Crear Personaje:")
            print(" 2.-Fusionar Personajes:")
            print(" 3.-Ver Todos los Personajes:")
            print(" 4.-Salir:")
            val=input("Selecciona la opción: ")
            try:
                val=int(val)+0 
            except ValueError as e:
                print(f"Error: {e}" )
            else:
                break
        return val
    def crear_personaje():
        nombre= input("Nombre del persoanje: ")
        fuerza = input("Fuerza del persoanje: ")
        velocidad =input("Velocidad del persoanje: ")
        nombre = nombre.lower()
        fuerza = fuerza.lower()
        velocidad = velocidad.lower()
        return nombre,fuerza,velocidad
    
    def preguntar_personaje_fusionar():
        psj=input("Selecciona al personaje: ")
        return psj
    
    def preguntar_personaje_fusionar2():
        psj=input("Selecciona al personaje 2: ")
        return psj