import  pygame 

ventana.fill(BLANCO)
    ls=[[posx,posy],[posx+50,posy],[posx+50,posy+110]]
    plantilla.triangulo(ls)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                posx-=velocidad
            elif event.key == K_RIGHT:
                posx+=velocidad
            elif event.key == K_UP:
                posy-=velocidad
            elif event.key == K_DOWN:
                posy+=velocidad
        elif event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                print "Tecla izquierda liberada."
            elif event.key == K_RIGHT:
                print "Tecla derecha liberada."
            elif event.key == K_UP:
                print "Tecla arriba liberada."
            elif event.key == K_DOWN:
                print "Tecla abajo liberada."
        
        posx,posy = pygame.mouse.get_pos()
        pygame.display.update()