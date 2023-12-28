class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__velocidad = velocidad
        
    def __repr__(self) -> str:
        return f'{self.__nombre} (fuerza: {self.__fuerza}, velocidad: {self.__velocidad})'
    
    def __add__(self, other):
        nuevo_nombre = self.__nombre +"-"+other.__nombre
        nueva_fuerza = round(((self.__fuerza + other.__fuerza)/2)**1.2)
        nueva_velocidad = round(((self.__velocidad + other.__velocidad)/2)**1.2)
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    
    def get_nombre(self):
        return self.__nombre
    
    def get_fuerza(self):
        return self.__fuerza
    
    def get_velocidad(self):
        return self.__velocidad