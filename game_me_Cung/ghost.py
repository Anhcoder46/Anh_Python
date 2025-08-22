import pygame
import random

class Ghost:
    def __init__(self, tile, cols, rows, used_positions):
        self.tile = tile
        while True:
            self.x = random.randint(1, cols-2)
            self.y = random.randint(1, rows-2)
            if (self.x, self.y) not in used_positions:
                used_positions.add((self.x, self.y))
                break
        self.image = pygame.image.load('img/ghost.png')
        self.image = pygame.transform.scale(self.image, (tile, tile))
        self.rect = pygame.Rect(self.x * tile, self.y * tile, tile, tile)
        self.move_cooldown = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x * self.tile, self.y * self.tile))

    def move_towards(self, player, grid_cells):
        if self.move_cooldown > 0:
            self.move_cooldown -= 1
            return
        self.move_cooldown = 30

        def get_cell(x, y):
            for cell in grid_cells:
                if cell.x == x and cell.y == y:
                    return cell
            return None

        gx, gy = self.x, self.y
        px, py = int(player.x // self.tile), int(player.y // self.tile)

        if abs(px - gx) + abs(py - gy) > 2:
            return

        cell = get_cell(gx, gy)
        if cell is None:
            return

        options = []
        if px > gx and not cell.walls['right']:
            options.append((1, 0))
        if px < gx and not cell.walls['left']:
            options.append((-1, 0))
        if py > gy and not cell.walls['bottom']:
            options.append((0, 1))
        if py < gy and not cell.walls['top']:
            options.append((0, -1))

        if options:
            dx, dy = random.choice(options)
            self.x += dx
            self.y += dy
            self.rect = pygame.Rect(self.x * self.tile, self.y * self.tile, self.tile, self.tile)