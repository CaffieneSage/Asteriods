import pygame

def main():
    #Initialize the pygame module.
    pygame.init()
    #Define and load a logo.
    try:
        logo = pygame.image.load("enemy_UFO.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Asteroids")
    except:
        pass


    #Create a display surface and set the resolution.
    ds = pygame.display.set_mode((240, 180))

    #Define a bool to control the main loop.
    running = True

    #Python goes BRRRRRRRRRRRrrrRRRRRrrRRRrrrrr.
    while running:
        #Event handler, so we can handle events.
        for event in pygame.event.get():
            #If we quit, we quit. Or crash. All good.
            if event.type == pygame.QUIT:
                exit()
        #Time to blit something onto ous display surface.
        backdrop = pygame.image.load("C:\\Users\\CaffieneSage\\workspace_Python\\pygame_Asteroids\\backdrop_space.png")
        ds.blit(backdrop, (0, 0))
        asteroid = pygame.image.load("C:\\Users\\CaffieneSage\\workspace_Python\\pygame_Asteroids\\enemy_SpaceRock1.png")
        ds.blit(asteroid, (20, 20))
        pygame.display.flip()

main()
