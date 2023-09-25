import pygame

# Initialize Pygame
from collisions import check_collisions
from snake import Snake
from utils import draw_snake, FoodContainer, draw_food, draw_score, draw_endgame_message

pygame.init()

# Window dimensions
width = 800
height = 600

# Create a window
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Main game loop
running = True
snake = Snake()
end_game = False
food_container = FoodContainer(initial=5)
while running:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # Handle the left arrow key
        snake.change_direction("left")
    if keys[pygame.K_RIGHT]:
        # Handle the right arrow key
        snake.change_direction("right")
    if keys[pygame.K_UP]:
        # Handle the up arrow key
        snake.change_direction("up")
    if keys[pygame.K_DOWN]:
        # Handle the down arrow key
        snake.change_direction("down")
    if keys[pygame.K_ESCAPE]:
        running = False

    if keys[pygame.K_RETURN]:
        if end_game:
            snake = Snake()
            food_container = FoodContainer(initial=5)
            end_game = False

    window.fill(
        (
            0,
            0,
            0,
        )
    )
    if not end_game:
        snake.move()
        state = check_collisions(snake, food_container)
        if state.should_end_game():
            end_game = True

        if state.snake_eaten:
            snake.eat()
            food_container.add()
            
        draw_snake(window, snake)
        draw_food(window, food_container)
        draw_score(window, snake)
    else:
        draw_endgame_message(window, len(snake.body))

    # You can place your drawing and game logic code here

    # Force screen update
    pygame.display.flip()


# Quit Pygame
pygame.quit()
