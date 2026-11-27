
import random
import pygame

# ==============================
# 1. GAME SETTINGS
# ==============================

GAME_TITLE = "Snake Game"

CELL_SIZE = 25
GRID_WIDTH = 24
GRID_HEIGHT = 18

SPEED = 10
SPEED_INCREMENT = 1
MAX_SPEED = 25

START_LENGTH = 3
POINTS_PER_FOOD = 1
GROW_PER_FOOD = 1
OBSTACLE_COUNT = 8

WALLS_KILL = True

BACKGROUND_COLOR = (20, 24, 38)
GRID_COLOR = (32, 38, 56)
SNAKE_COLOR = (90, 200, 120)
HEAD_COLOR = (50, 150, 80)
FOOD_COLOR = (235, 80, 80)
OBSTACLE_COLOR = (150, 150, 150)
TEXT_COLOR = (240, 240, 240)

# ==============================
# 2. GAME SETUP
# ==============================

pygame.init()

WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


# ==============================
# 3. GAME FUNCTIONS
# ==============================

def place_food(occupied):
    while True:
        spot = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )

        if spot not in occupied:
            return spot


def place_obstacles(snake):
    obstacles = []

    while len(obstacles) < OBSTACLE_COUNT:
        spot = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )

        if spot not in snake and spot not in obstacles:
            obstacles.append(spot)

    return obstacles


def new_game():
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2

    snake = []

    for i in range(START_LENGTH):
        snake.append((start_x - i, start_y))

    direction = (1, 0)

    obstacles = place_obstacles(snake)
    food = place_food(snake + obstacles)

    score = 0
    grow = 0
    current_speed = SPEED

    return snake, direction, food, score, grow, obstacles, current_speed


def draw_square(position, color):
    x, y = position

    rect = pygame.Rect(
        x * CELL_SIZE,
        y * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )

    pygame.draw.rect(screen, color, rect, border_radius=5)


def draw_text(text, y):
    image = font.render(text, True, TEXT_COLOR)

    screen.blit(
        image,
        (WIDTH // 2 - image.get_width() // 2, y)
    )


def draw_game(snake, food, score, obstacles, current_speed):

    screen.fill(BACKGROUND_COLOR)

    # Draw grid
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

    # Draw food
    draw_square(food, FOOD_COLOR)

    # Draw obstacles
    for obstacle in obstacles:
        draw_square(obstacle, OBSTACLE_COLOR)

    # Draw snake body
    for part in snake[1:]:
        draw_square(part, SNAKE_COLOR)

    # Draw snake head
    draw_square(snake[0], HEAD_COLOR)

    # Draw score and speed
    draw_text(
        "Score: " + str(score) + "  Speed: " + str(current_speed),
        10
    )


# ==============================
# 4. START GAME
# ==============================

snake, direction, food, score, grow, obstacles, current_speed = new_game()

game_over = False
paused = False
running = True


# ==============================
# 5. MAIN GAME LOOP
# ==============================

while running:

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if game_over:

                if event.key == pygame.K_r:
                    snake, direction, food, score, grow, obstacles, current_speed = new_game()
                    game_over = False
                    paused = False

                elif event.key == pygame.K_q:
                    running = False

            else:

                # Pause and resume
                if event.key == pygame.K_SPACE:
                    paused = not paused

                elif not paused:

                    # Movement controls
                    if event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)

                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)

                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)

                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)

    # UPDATE
    if not game_over and not paused:

        head_x, head_y = snake[0]

        new_head = (
            head_x + direction[0],
            head_y + direction[1]
        )

        # Wall collision
        if WALLS_KILL:

            if (
                new_head[0] < 0 or
                new_head[0] >= GRID_WIDTH or
                new_head[1] < 0 or
                new_head[1] >= GRID_HEIGHT
            ):
                game_over = True

        else:

            new_head = (
                new_head[0] % GRID_WIDTH,
                new_head[1] % GRID_HEIGHT
            )

        # Check if food is eaten
        eating = new_head == food

        # Self collision
        body_to_check = snake if eating else snake[:-1]

        if new_head in body_to_check:
            game_over = True

        # Obstacle collision
        if new_head in obstacles:
            game_over = True

        if not game_over:

            snake.insert(0, new_head)

            # Food collision
            if eating:

                score = score + POINTS_PER_FOOD
                grow = grow + GROW_PER_FOOD

                # Increase speed
                current_speed = min(
                    current_speed + SPEED_INCREMENT,
                    MAX_SPEED
                )

                food = place_food(snake + obstacles)

            # Snake growth
            if grow > 0:
                grow = grow - 1

            else:
                snake.pop()

    # DRAW
    draw_game(snake, food, score, obstacles, current_speed)

    if paused and not game_over:
        draw_text("PAUSED", HEIGHT // 2 - 20)
        draw_text("Press SPACE to resume", HEIGHT // 2 + 20)

    if game_over:
        draw_text("GAME OVER", HEIGHT // 2 - 40)
        draw_text("R = Restart   Q = Quit", HEIGHT // 2)

    pygame.display.flip()

    clock.tick(current_speed)

pygame.quit()
