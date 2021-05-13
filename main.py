from os import path
import pygame

'''configurações do game, janela, fps, cor de fundo, velocidade'''
WIDTH, HEIGHT = 900,500
janela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Meu jogo')
WHITE = (255,255,255)
BLACK = (255,255,255)
SPACE_WIDTH, SPACE_HEIGTH = 100,124
BORDA = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)
FPS = 60
bala_vel = 8
max_balas = 3
VEL = 5

PASTA_LOCAL = path.dirname(__file__)
PASTA_IMAGENS = path.join(PASTA_LOCAL, "imagens/")

soldado1 = pygame.image.load(PASTA_IMAGENS + "sordadin.jpg")
sordado1 = pygame.transform.scale(soldado1, (SPACE_WIDTH, SPACE_HEIGTH))

soldado2 = pygame.image.load(PASTA_IMAGENS + "sordadin.jpg")
sordado2 = pygame.transform.scale(soldado2, (SPACE_WIDTH, SPACE_HEIGTH))
sordado2 = pygame.transform.flip(sordado2, True, False)


class Atirar(pygame.sprite.Sprite):
    """Classe que cria faz o tiro"""
    def __init__(self, posicao_x, posicao_y):
        super().__init__()
        self.image = pygame.image.load(PASTA_IMAGENS + "bala.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.x = posicao_x
        self.rect.y = posicao_y + 22
        self.disparo = False

    def update(self):
        if self.disparo:
            self.rect.x += bala_vel
            if self.rect.x > WIDTH:
                self.dirparo = False

balas = pygame.sprite.Group()


def draw_display(sold1, sold2):
    janela.fill(WHITE)
    pygame.draw.rect(janela, BLACK, BORDA)
    janela.blit(sordado1, (sold1.x, sold1.y))
    janela.blit(sordado2, (sold2.x, sold2.y))
    balas.draw(janela)
    balas.update()
    pygame.display.update()



def soldado1_movimento(keys_pressed, sold1):
    """
    Implementando a movimentação do sordado usando as propriedades do retangulo
    do sordado
    """

    if keys_pressed[pygame.K_s] and sold1.bottom <= HEIGHT:
        sold1.y += VEL
    if keys_pressed[pygame.K_w] and sold1.top >= 0:
        sold1.y -= VEL
    if keys_pressed[pygame.K_a] and sold1.left >= -20:
        sold1.x -= VEL
    if keys_pressed[pygame.K_d] and sold1.right <= WIDTH // 2:
        sold1.x += VEL


def soldado2_movimento(keys_pressed, sold2):
    if keys_pressed[pygame.K_DOWN] and sold2.y + VEL + sold2.height < HEIGHT: #pra baixo 
        sold2.y += VEL
    if keys_pressed[pygame.K_UP] and sold2.y - VEL > 0: #pra cima
        sold2.y -= VEL
    if keys_pressed[pygame.K_LEFT] and sold2.x - VEL > BORDA.x + BORDA.width: #pra esquerda 
        sold2.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and sold2.x + VEL + sold2.width < WIDTH: #pra direita
        sold2.x += VEL


def main():
    sold1 = pygame.Rect(0,0, SPACE_WIDTH, SPACE_HEIGTH)
    sold2 = pygame.Rect(805,2, SPACE_WIDTH, SPACE_HEIGTH)

    sold1_balas = []
    sold2_balas = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False

            if evento.type == pygame.KEYDOWN:
                if (evento.key == pygame.K_SPACE
                        and len(sold1_balas) < max_balas):
                    if len(balas) <= max_balas:
                        bala = Atirar(sold1.right, sold1.y)
                        bala.disparo = True
                        balas.add(bala)

                if evento.key == pygame.K_r:
                    if all(list(map(lambda x: x.rect.x > WIDTH, balas))):
                        balas.empty()


        keys_pressed = pygame.key.get_pressed()
        soldado1_movimento(keys_pressed, sold1)
        soldado2_movimento(keys_pressed, sold2)
        draw_display(sold1, sold2)

if __name__ == "__main__":
    main()
