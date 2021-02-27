import pygame
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
ncolor=(68,81,80)
gd = pygame.display.set_mode((360,400))
pygame.display.update()

#                                               **************Functions
# GAME_LOOP///////////////11111111111111
def game_loop():  
    b_w = 100
    b_h = 100 
    game_over = False
    while game_over == False:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    b_h = b_h + 10
                if event.key == pygame.K_UP:
                   b_h = b_h - 10

                if event.key == pygame.K_RIGHT:
                    b_w = b_w + 10
                if event.key == pygame.K_LEFT:
                    b_w = b_w - 10


       
        gd.fill(ncolor)
        pygame.draw.rect(gd,red, [b_w, b_h, 50, 50])
        Message(50, "Welcome!", 0, 350)
        pygame.display.update()


# MESSAGE   ////////////////2222222222222222222222222
def Message(size, mess, x_pos, y_pos):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess, True, red)
    gd.blit(render, (x_pos, y_pos))
    pygame.display.update()


Message(50, "Loding................", 0, 350)
pygame.time.wait(4000)
game_loop()

pygame.quit()
quit()