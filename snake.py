import pygame, sys, random
pygame.init()
CELL=20; WIDTH=30; HEIGHT=20
HARD_MODE = True
screen=pygame.display.set_mode((WIDTH*CELL, HEIGHT*CELL))
clock=pygame.time.Clock()

snake=[(WIDTH//2, HEIGHT//2)]
direction=(1,0)
food=(random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1))

def move(snake, direction):
    x = snake[0][0] + direction[0]
    y = snake[0][1] + direction[1]
    if HARD_MODE:
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return None
    else:
        x %= WIDTH
        y %= HEIGHT
    head = (x, y)
    snake.insert(0, head)
    return snake[:-1]

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP   and direction != (0, 1):  direction = (0, -1)
            if e.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
            if e.key == pygame.K_LEFT and direction != (1, 0):  direction = (-1, 0)
            if e.key == pygame.K_RIGHT and direction != (-1, 0):direction = (1, 0)

    new_snake = move(snake, direction)
    if new_snake is None: break
    snake = new_snake

    if snake[0] == food:
        snake.append(snake[-1])
        food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))

    if snake[0] in snake[1:]: break

    screen.fill("black")
    for x, y in snake:
        pygame.draw.rect(screen, "green", (x*CELL, y*CELL, CELL, CELL))
    fx, fy = food
    pygame.draw.rect(screen, "red", (fx*CELL, fy*CELL, CELL, CELL))
    pygame.display.flip(); clock.tick(10)
