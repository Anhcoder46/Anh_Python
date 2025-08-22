import pygame, sys
from maze import Maze
from player import Player
from game import Game
from clock import Clock
from ghost import Ghost
import random

pygame.init()
pygame.font.init()

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("impact", 30)
        self.message_color = pygame.Color("cyan")
        self.running = True
        self.game_over = False
        self.FPS = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
        self.ghosts_can_move = False
        self.game_win = False
        self.game_loss = False
        self.state = "playing"

    def instructions(self):
        instructions1 = self.font.render('Use', True, self.message_color)
        instructions2 = self.font.render('Arrow Keys', True, self.message_color)
        instructions3 = self.font.render('to Move', True, self.message_color)
        self.screen.blit(instructions1,(655,300))
        self.screen.blit(instructions2,(610,331))
        self.screen.blit(instructions3,(630,362))

    def _draw(self, maze, tile, player, game, clock):
        [cell.draw(self.screen, tile) for cell in maze.grid_cells]
        game.add_goal_point(self.screen)
        player.draw(self.screen)
        player.update()
        self.instructions()
        if self.game_over:
            clock.stop_timer()
            self.screen.blit(game.message(),(610,120))
        else:
            clock.update_timer()
        self.screen.blit(clock.display_timer(), (625,200))
        for ghost in game.ghosts:
            ghost.draw(self.screen)
        pygame.display.flip()

    def draw_gameover_screen(self, win):
        self.screen.fill((0,0,0))
        msg = "You Win!" if win else "You Lose!"
        text = self.font.render(msg, True, pygame.Color("orange"))
        continue_btn = self.font.render("Continue (C)", True, pygame.Color("white"))
        quit_btn = self.font.render("Exit (Q)", True, pygame.Color("white"))
        self.screen.blit(text, (self.screen.get_width()//2-70, 200))
        self.screen.blit(continue_btn, (self.screen.get_width()//2-90, 300))
        self.screen.blit(quit_btn, (self.screen.get_width()//2-60, 350))
        pygame.display.flip()

    def main(self, frame_size, tile):
        cols, rows = frame_size[0] // tile, frame_size[-1] // tile
        maze = Maze(cols, rows)
        game = Game(maze.grid_cells[-1], tile)
        player = Player(tile // 3, tile // 3)
        clock = Clock()
        maze.generate_maze()
        clock.start_timer()

        used_positions = set()
        used_positions.add((player.x // tile, player.y // tile))
        used_positions.add((maze.grid_cells[-1].x, maze.grid_cells[-1].y))
        n_ghosts = random.randint(2, 3)

        possible_cells = [
            cell for cell in maze.grid_cells
            if (cell.x, cell.y) not in used_positions
            and sum(cell.walls.values()) >= 2
        ]

        ghosts = []
        for _ in range(n_ghosts):
            if not possible_cells:
                break
            cell = random.choice(possible_cells)
            ghosts.append(Ghost(tile, cols, rows, used_positions={(cell.x, cell.y)}))
            possible_cells.remove(cell)

        game.ghosts = ghosts

        while self.running:
            self.screen.fill("gray")
            self.screen.fill( pygame.Color("darkslategray"), (603, 0, 752, 752))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if not self.game_over:
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = True
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = True
                    if event.key == pygame.K_UP:
                        player.up_pressed = True
                    if event.key == pygame.K_DOWN:
                        player.down_pressed = True
                    player.check_move(tile, maze.grid_cells, maze.thickness)

            if event.type == pygame.KEYUP:
                if not self.game_over:
                    if event.key == pygame.K_LEFT:
                        player.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        player.right_pressed = False
                    if event.key == pygame.K_UP:
                        player.up_pressed = False
                    if event.key == pygame.K_DOWN:
                        player.down_pressed = False
                    player.check_move(tile, maze.grid_cells, maze.thickness)

            if not self.ghosts_can_move and pygame.time.get_ticks() - self.start_time > 5000:
                self.ghosts_can_move = True

            if self.ghosts_can_move:
                for ghost in game.ghosts:
                    ghost.move_towards(player, maze.grid_cells)
            for ghost in game.ghosts:
                ghost.draw(self.screen)

            for ghost in game.ghosts:
                if player.rect.colliderect(ghost.rect):
                    self.game_loss = True
                    self.state = "gameover"

            if game.is_game_over(player):
                self.game_win = True
                self.state = "gameover"

            if self.state == "gameover":
                self.draw_gameover_screen(self.game_win)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            cols, rows = frame_size[0] // tile, frame_size[-1] // tile
                            maze = Maze(cols, rows)
                            game = Game(maze.grid_cells[-1], tile)
                            player = Player(tile // 3, tile // 3)
                            clock = Clock()
                            maze.generate_maze()
                            clock.start_timer()
                            used_positions = set()
                            used_positions.add((player.x // tile, player.y // tile))
                            used_positions.add((maze.grid_cells[-1].x, maze.grid_cells[-1].y))
                            n_ghosts = random.randint(8, 15)
                            ghosts = [Ghost(tile, cols, rows, used_positions) for _ in range(n_ghosts)]
                            game.ghosts = ghosts
                            self.game_over = False
                            self.ghosts_can_move = False
                            self.start_time = pygame.time.get_ticks()
                            self.state = "playing"
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                continue

            self._draw(maze, tile, player, game, clock)
            self.FPS.tick(60)

if __name__ == "__main__":
    window_size = (602, 602)
    screen = (window_size[0] + 150, window_size[-1])
    tile_size = 30
    screen = pygame.display.set_mode(screen)
    pygame.display.set_caption("Maze")

    game = Main(screen)
    game.main(window_size, tile_size)