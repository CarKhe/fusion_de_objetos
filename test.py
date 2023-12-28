import clases.bd as bd
import clases.personaje as pj
import clases.menu as mn

menu = 1

while menu !=4:
    menu = mn.Menu.menu()
    if menu == 1:
        n,f,v = mn.Menu.crear_personaje()
        pj.Personaje(n,f,v)
        bd.Bd.agegar_personaje(n,f,v)
    if menu == 2:
        pjn = mn.Menu.preguntar_personaje_fusionar()
        pj1=bd.Bd.buscar_personaje(pjn)
        print(pj1)
        p,f,v = bd.Bd.enviar_caracteristicas(pjn)
        print(p,f,v)
        
        
            
    if menu == 3:
       bd.Bd.ver_personajes()
   
    if menu == 4:
        exit()
    