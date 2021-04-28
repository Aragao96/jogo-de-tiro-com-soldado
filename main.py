import pygame
import os


width, heigth = 900,500
janela = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Meu jogo')
white = (255,255,255)

fps = 60
soldado_direito, soldado_esquerdo = 100,124

space_width, space_heigth = 100,124

soldado1 = pygame.image.load(os.path.join('/home/karenrafael/Documentos/jogo_labirinto/sordadin.jpg'))
sordado1 = pygame.transform.scale(soldado1, (space_width, space_heigth))
soldado2 = pygame.image.load(os.path.join('/home/karenrafael/Documentos/jogo_labirinto/sordadin2.png'))
sordado2 = pygame.transform.scale(soldado2, (space_width,space_heigth))


def draw_display():
    janela.fill(white)
    janela.blit(sordado1,(0,0))
    janela.blit(sordado2, (810,0))
            
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False 

        draw_display()
    pygame.quit()


if __name__ == "__main__":
    main()

