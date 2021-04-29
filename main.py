import pygame
import os


width, heigth = 900,500
janela = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Meu jogo')
white = (255,255,255)
space_width, space_heigth = 100,124
fps = 60
vel = 5

soldado1 = pygame.image.load(os.path.join('/home/karenrafael/Documentos/jogo-de-tiro-com-soldado/sordadin.jpg'))
sordado1 = pygame.transform.scale(soldado1, (space_width, space_heigth))
soldado2 = pygame.image.load(os.path.join('/home/karenrafael/Documentos/jogo-de-tiro-com-soldado/sordadin2.png'))
sordado2 = pygame.transform.scale(soldado2, (space_width,space_heigth))


def draw_display(sold1, sold2):
    janela.fill(white)
    janela.blit(sordado1, (sold1.x, sold1.y))
    janela.blit(sordado2, (sold2.x, sold2.y))        
    pygame.display.update()

def soldado1_movimento(keys_pressed, sold1):
    if keys_pressed[pygame.K_s]: #pra baixo 
        sold1.y += vel
    if keys_pressed[pygame.K_w]: #pra cima
        sold1.y -= vel
    if keys_pressed[pygame.K_a]: #pra esquerda 
        sold1.x -= vel 
    if keys_pressed[pygame.K_d]: #pra direita
        sold1.x += vel

def soldado2_movimento(keys_pressed, sold2):
    if keys_pressed[pygame.K_DOWN]: #pra baixo 
        sold2.y += vel
    if keys_pressed[pygame.K_UP]: #pra cima
        sold2.y -= vel
    if keys_pressed[pygame.K_LEFT]: #pra esquerda 
        sold2.x -= vel 
    if keys_pressed[pygame.K_RIGHT]: #pra direita
        sold2.x += vel 

def main():
    sold1 = pygame.Rect(0,0, space_width, space_heigth)
    sold2 = pygame.Rect(810,0, space_width, space_heigth)  
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        soldado1_movimento(keys_pressed, sold1)            
        soldado2_movimento(keys_pressed, sold2)
        draw_display(sold1, sold2)
        #draw_display()
    pygame.quit()


if __name__ == "__main__":
    main()
