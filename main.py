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
        pj1=True
        pj2=True
        while pj1==True:
            pjn = mn.Menu.preguntar_personaje_fusionar()
            pj1=bd.Bd.buscar_personaje(pjn)

        p,f,v = bd.Bd.enviar_caracteristicas(pjn)
        personaje1 = pj.Personaje(p,f,v)
        
        while pj2==True:
            pjn2 = mn.Menu.preguntar_personaje_fusionar2()
            pj2=bd.Bd.buscar_personaje(pjn2)
  
        p2,f2,v2 = bd.Bd.enviar_caracteristicas(pjn2)
        personaje2 = pj.Personaje(p2,f2,v2)
        fusion = personaje1 + personaje2
        fn = fusion.get_nombre()
        ff = fusion.get_fuerza()
        fv = fusion.get_velocidad()
        bd.Bd.agegar_personaje(fn,ff,fv)
        print(fusion)
        
            
    if menu == 3:
       bd.Bd.ver_personajes()
   
    if menu == 4:
        exit()
    