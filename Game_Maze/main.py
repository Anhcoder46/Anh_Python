import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Mê Cung")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Kích thước ô
CELL_SIZE = 20

# Load hình ảnh
player_img = pygame.image.load("player.png")
gate_img = pygame.image.load("gate.png")

# Resize hình ảnh về đúng kích thước ô
player_img = pygame.transform.scale(player_img, (CELL_SIZE, CELL_SIZE))
gate_img = pygame.transform.scale(gate_img, (CELL_SIZE, CELL_SIZE))

# Lớp Maze
class Maze:
    def __init__(self, layout):
        self.grid = [list(row) for row in layout]
        self.start = (1, 1)
        for y in range(len(self.grid) - 2, 0, -1):
            for x in range(len(self.grid[0]) - 2, 0, -1):
                if self.grid[y][x] == '0':
                    self.end = (x, y)
                    return

    def draw(self, screen):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if (x, y) == self.start:
                    pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif (x, y) == self.end:
                    screen.blit(gate_img, (x * CELL_SIZE, y * CELL_SIZE))
                else:
                    color = WHITE if self.grid[y][x] == '0' else BLACK
                    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Lớp Player
class Player:
    def __init__(self, start):
        self.x, self.y = start

    def move(self, dx, dy, maze):
        nx, ny = self.x + dx, self.y + dy
        if 0 <= ny < len(maze.grid) and 0 <= nx < len(maze.grid[0]):
            if maze.grid[ny][nx] == '0':
                self.x = nx
                self.y = ny

    def draw(self, screen):
        screen.blit(player_img, (self.x * CELL_SIZE, self.y * CELL_SIZE))

# Tạo mê cung theo cấp độ
def create_maze(level):
    if level == 1:
        return [
            "111111111111111111111111",
            "100000000000000000000001",
            "101111111111111111110101",
            "101000000000000001010101",
            "101011111111110101010101",
            "101010000001010101010101",
            "101010111101010101010101",
            "101010100101010101010101",
            "101010101101010101010101",
            "101010101001010101010101",
            "101010101111010101010101",
            "101010100000010101010101",
            "101011111111110101010101",
            "101000000000000101010101",
            "101111111111111101010101",
            "100000000000000000000001",
            "111111111111111111111111"
        ]
    elif level == 2:
        return [
            "111111111111111111111111",
            "100000000000000000000001",
            "101111111111111111110101",
            "101000000000000001010001",
            "101011111111110101011111",
            "101010000001010100000001",
            "101010111101011111111101",
            "101010100101000000000001",
            "101010101101111111111101",
            "101010101000000000000001",
            "101010101111111111110101",
            "101010100000000000010101",
            "101011111111111110010101",
            "100000000000000000010001",
            "111111111111111111111111"
        ]
    elif level == 3:
        return [
            "111111111111111111111111",
            "100000000000000000000001",
            "101111111111111111110101",
            "101000000000000000010101",
            "101011111111111111010101",
            "101010000000000001010101",
            "101010111111111101010101",
            "101010100000001101010101",
            "101010101111101101010101",
            "101010100100001101010101",
            "101011101111101101010101",
            "101000001000001100010101",
            "101111111111111111110101",
            "100000000000000000000001",
            "111111111111111111111111"
        ]
    elif level == 4:
        return [
            "111111111111111111111111",
            "100000000000000000000001",
            "101111111111111111110101",
            "101000000000000000010101",
            "101011111111111111010101",
            "101010000000000001010101",
            "101011111111111101010101",
            "101000000000001101010101",
            "101111111101101101010101",
            "100000001101001101000001",
            "101111101101101111111101",
            "100000101100001000000001",
            "101111101111111111110101",
            "100000000000000000000001",
            "111111111111111111111111"
        ]
    else:
        return create_maze(1)

# Vẽ thông điệp
def draw_message(screen, message, sub_message=""):
    font = pygame.font.Font(None, 48)
    text = font.render(message, True, YELLOW)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height()))
    if sub_message:
        font2 = pygame.font.Font(None, 32)
        sub_text = font2.render(sub_message, True, WHITE)
        screen.blit(sub_text, (WIDTH // 2 - sub_text.get_width() // 2, HEIGHT // 2 + 20))

# Hàm chính
def main():
    clock = pygame.time.Clock()
    running = True
    level = 1
    maze_layout = create_maze(level)
    maze = Maze(maze_layout)
    player = Player(maze.start)
    rounds_completed = 0
    game_started = False
    win_screen = False

    move_delay = 150  # ms
    last_move = 0

    start_time = 0
    elapsed_time = 0

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_started:
            draw_message(screen, "Bấm SPACE để bắt đầu")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game_started = True
                start_time = pygame.time.get_ticks()
        elif win_screen:
            draw_message(screen, "Bạn đã đến đích!", "SPACE: Tiếp tục | ESC: Thoát")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                level += 1
                rounds_completed += 1
                maze_layout = create_maze(level)
                maze = Maze(maze_layout)
                player = Player(maze.start)
                win_screen = False
                start_time = pygame.time.get_ticks()
            elif keys[pygame.K_ESCAPE]:
                running = False
        else:
            maze.draw(screen)
            player.draw(screen)

            # Hiển thị số vòng
            font = pygame.font.Font(None, 36)
            rounds_text = font.render(f"Vòng: {rounds_completed}", True, WHITE)
            screen.blit(rounds_text, (WIDTH - 200, 10))

            # Hiển thị thời gian
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            time_text = font.render(f"Time: {elapsed_time}s", True, YELLOW)
            screen.blit(time_text, (WIDTH - 200, 40))

            keys = pygame.key.get_pressed()
            now = pygame.time.get_ticks()
            if now - last_move > move_delay:
                if keys[pygame.K_UP]:
                    player.move(0, -1, maze)
                    last_move = now
                elif keys[pygame.K_DOWN]:
                    player.move(0, 1, maze)
                    last_move = now
                elif keys[pygame.K_LEFT]:
                    player.move(-1, 0, maze)
                    last_move = now
                elif keys[pygame.K_RIGHT]:
                    player.move(1, 0, maze)
                    last_move = now

            if (player.x, player.y) == maze.end:
                win_screen = True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
