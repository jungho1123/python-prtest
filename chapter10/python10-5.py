import random
import pygame

rgbs = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)] #바뀔 배경색
colors = ['black', 'red', 'green', 'blue', 'yellow']  #출력할 문자열

pygame.init()

screen = pygame.display.set_mode([400, 300])
font = pygame.font.SysFont('Arial', 30)

clock=pygame.time.Clock()

i=0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if i<=3:
       screen.fill(rgbs[i])
       text = font.render(colors[i], True, rgbs[i+1])
       screen.blit(text, [100, 80])
       i+=1

    elif i==4:
        screen.fill(rgbs[i])
        text = font.render(colors[i], True, rgbs[0])
        screen.blit(text, [100, 80])

    pygame.display.update()
    clock.tick(1)
pygame.quit()
