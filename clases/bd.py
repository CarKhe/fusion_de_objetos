import csv
import pandas as pd
ruta = "base_datos\\bd_personajes.csv"
class Bd:
    def agegar_personaje(nombre,fuerza,velocidad):
        with open(ruta,newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]
        with open(ruta,'w',newline='') as f:
            w = csv.writer(f)
            w.writerow([nombre,fuerza,velocidad])
            w.writerows(data)  
             
    def buscar_personaje(nombre):
        nombre= nombre.lower()
        archivo = pd.read_csv(ruta,names=["Personaje","Fuerza","Velocidad"])
        df = pd.DataFrame(archivo)
        resultado = df[df['Personaje'] == nombre]
        if resultado.empty: 
            return True
        else:
           return False
    
    def enviar_caracteristicas(nombre):
        nombre= nombre.lower()
        archivo = pd.read_csv(ruta,names=["Personaje","Fuerza","Velocidad"])
        df = pd.DataFrame(archivo)
        resultado = df[df['Personaje'] == nombre]
        p=resultado.values[0][0]
        f=resultado.values[0][1]
        v=resultado.values[0][2]
        return p,f,v
        
    
    def ver_personajes():
        archivo = pd.read_csv(ruta,names=["Personaje","Fuerza","Velocidad"])
        print(archivo)
                

