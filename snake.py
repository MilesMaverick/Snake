import pygame, sys, random
pygame.init()
CELL=20; WIDTH=30; HEIGHT=20
screen=pygame.display.set_mode((WIDTH*CELL, HEIGHT*CELL))
clock=pygame.time.Clock()

snake=[(WIDTH//2, HEIGHT//2)]
direction=(1,0)
food=(random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1))

def move(snake, direction):
    head=((snake[0][0]+direction[0])%WIDTH,
          (snake[0][1]+direction[1])%HEIGHT)
    snake.insert(0, head)
    return snake[:-1]

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: pygame.quit(); sys.exit()
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_UP   and direction!=(0,1):  direction=(0,-1)
            if e.key==pygame.K_DOWN and direction!=(0,-1): direction=(0,1)
            if e.key==pygame.K_LEFT and direction!=(1,0):  direction=(-1,0)
            if e.key==pygame.K_RIGHT and direction!=(-1,0):direction=(1,0)
    snake=move(snake,direction)
    if snake[0]==food:
        snake.append(snake[-1])                 # grow
        food=(random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1))
    if snake[0] in snake[1:]: break            # collision -> game over
    screen.fill("black")
    for x,y in snake: pygame.draw.rect(screen,"green",(x*CELL,y*CELL,CELL,CELL))
    fx,fy=food; pygame.draw.rect(screen,"red",(fx*CELL,fy*CELL,CELL,CELL))
    pygame.display.flip(); clock.tick(10)
