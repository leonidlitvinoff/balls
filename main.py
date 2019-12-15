import pygame
pygame.init()
size = width, height = 600, 800
screen = pygame.display.set_mode(size)
running = True
r = 0
v = 100   # пикселей в секунду
clock = pygame.time.Clock()
pos = False
screen.fill((0, 0, 255))
circles = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            circles.append([event.pos, 1])
    screen.fill((0, 0, 255))
    for i in range(len(circles)):
        pygame.draw.circle(screen, (255, 255, 0), (circles[i][0][0], circles[i][0][1]), 10)
        if circles[i][-1] == 1:
            circles[i][0] = (circles[i][0][0] - 1, circles[i][0][1] - 1)
        elif circles[i][-1] == 2:
            circles[i][0] = (circles[i][0][0] - 1, circles[i][0][1] + 1)
        elif circles[i][-1] == 3:
            circles[i][0] = (circles[i][0][0] + 1, circles[i][0][1] + 1)
        elif circles[i][-1] == 4:
            circles[i][0] = (circles[i][0][0] + 1, circles[i][0][1] - 1)
        if circles[i][0][1] - 10 == 0:
            if circles[i][-1] == 1:
                circles[i][-1] = 2
            else:
                circles[i][-1] = 3
        if circles[i][0][1] + 10 == height - 1:
            if circles[i][-1] == 3:
                circles[i][-1] = 4
            else:
                circles[i][-1] = 1
        if circles[i][0][0] - 10 == 0:
            if circles[i][-1] == 2:
                circles[i][-1] = 3
            else:
                circles[i][-1] = 4
        if circles[i][0][0] + 10 == width - 1:
            if circles[i][-1] == 4:
                circles[i][-1] = 1
            else:
                circles[i][-1] = 2
    clock.tick(100)
    pygame.display.flip()