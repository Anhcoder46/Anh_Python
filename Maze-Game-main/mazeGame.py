import pygame
import sys
import maze as mz
import random

pygame.init()
clock = pygame.time.Clock()

if len(sys.argv) > 1:
    mazeFile = sys.argv[1]
else:
    mazeFile = "maze.txt"

maze = mz.Maze(mazeFile)
maze.print()

BLOCK_SIZE = 20
S_WIDTH = maze.width
S_HEIGHT = maze.height
screen = pygame.display.set_mode((BLOCK_SIZE*S_WIDTH, BLOCK_SIZE*S_HEIGHT))
pygame.display.set_caption('Maze Game')
icon = pygame.image.load('mazeGameIcon.ico')
pygame.display.set_icon(icon)

BLUE = pygame.Color("blue")
GREEN = pygame.Color("green")
RED = pygame.Color("red")
PURPLE = pygame.Color("purple")
WHITE = pygame.Color("white")
BLACK = pygame.Color("black")
FLASH_COLOR = pygame.Color("yellow")

player = pygame.Rect(BLOCK_SIZE*maze.start[1], BLOCK_SIZE*maze.start[0], BLOCK_SIZE, BLOCK_SIZE)
startBlock = pygame.Rect(BLOCK_SIZE*maze.start[1], BLOCK_SIZE*maze.start[0], BLOCK_SIZE, BLOCK_SIZE)
goalBlock = pygame.Rect(BLOCK_SIZE*maze.goal[1], BLOCK_SIZE*maze.goal[0], BLOCK_SIZE, BLOCK_SIZE)

lives = 3
font = pygame.font.SysFont(None, 30)

# Monster
monster = pygame.Rect(BLOCK_SIZE*random.randint(0, maze.width-1), BLOCK_SIZE*random.randint(0, maze.height-1), BLOCK_SIZE, BLOCK_SIZE)
while maze.walls[monster.y//BLOCK_SIZE][monster.x//BLOCK_SIZE] or (monster == player):
    monster.x = BLOCK_SIZE*random.randint(0, maze.width-1)
    monster.y = BLOCK_SIZE*random.randint(0, maze.height-1)

monster_direction = random.choice(["up", "down", "left", "right"])
flash_timer = 0
invincible_timer = 0

running = True
game_over = False
you_win = False

def move(rect, dx, dy):
    new_x = rect.x + dx * BLOCK_SIZE
    new_y = rect.y + dy * BLOCK_SIZE
    i, j = new_y // BLOCK_SIZE, new_x // BLOCK_SIZE
    if 0 <= i < maze.height and 0 <= j < maze.width and not maze.walls[i][j]:
        rect.x, rect.y = new_x, new_y

while running:
    screen.fill(WHITE)

    for i in range(maze.height):
        for j in range(maze.width):
            if maze.walls[i][j]:
                pygame.draw.rect(screen, BLUE, (j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(screen, PURPLE, startBlock)
    pygame.draw.rect(screen, RED, goalBlock)

    pygame.draw.rect(screen, BLACK, monster)

    if flash_timer > 0 and (pygame.time.get_ticks() // 100) % 2 == 0:
        pygame.draw.rect(screen, FLASH_COLOR, player)
        flash_timer -= 1
    else:
        pygame.draw.rect(screen, GREEN, player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over and not you_win:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            move(player, 0, -1)
        elif keys[pygame.K_DOWN]:
            move(player, 0, 1)
        elif keys[pygame.K_LEFT]:
            move(player, -1, 0)
        elif keys[pygame.K_RIGHT]:
            move(player, 1, 0)

        if random.randint(0, 10) == 0:
            dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
            move(monster, dx, dy)

        if player.colliderect(monster) and invincible_timer == 0:
            lives -= 1
            flash_timer = 10
            invincible_timer = 40
            if lives <= 0:
                game_over = True

        if invincible_timer > 0:
            invincible_timer -= 1

        if player.colliderect(goalBlock):
            you_win = True

    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(lives_text, (10, 5))

    if game_over:
        over_text = font.render("Game Over!", True, RED)
        screen.blit(over_text, (BLOCK_SIZE*S_WIDTH//2 - 50, BLOCK_SIZE*S_HEIGHT//2))

    if you_win:
        win_text = font.render("You Win!", True, GREEN)
        screen.blit(win_text, (BLOCK_SIZE*S_WIDTH//2 - 50, BLOCK_SIZE*S_HEIGHT//2))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
