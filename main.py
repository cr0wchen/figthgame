import pygame

def main():
    pygame.init()
    screen=pygame.display.set_mode([768,446])
    pygame.display.set_caption('决战糖果街')
    background=pygame.image.load('src\\pic\\beijing.png')
    runing=True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing=False
        screen.blit(background,(0,0))
        pygame.display.update()

if __name__=='__main__':
    main()
