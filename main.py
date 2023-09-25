import pygame

from collisions import check_collisions
from constants import HEIGHT, CLOCK, INITIAL_FOOD_NUMBER, WIDTH
from snake import Snake
from utils import draw_snake, FoodContainer, draw_food, draw_score, draw_endgame_message


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food_container = FoodContainer(initial=INITIAL_FOOD_NUMBER)

        self.game_over = False
        self.running = True

    def handle_key_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.snake.change_direction("left")
        if keys[pygame.K_RIGHT]:
            self.snake.change_direction("right")
        if keys[pygame.K_UP]:
            self.snake.change_direction("up")
        if keys[pygame.K_DOWN]:
            self.snake.change_direction("down")
        if keys[pygame.K_ESCAPE]:
            self.running = False

        if keys[pygame.K_RETURN]:
            if self.game_over:
                self.snake = Snake()
                self.food_container = FoodContainer(initial=INITIAL_FOOD_NUMBER)
                self.game_over = False


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    game = Game()

    while game.running:
        clock.tick(CLOCK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.handle_key_pressed()
        window.fill((0, 0, 0))
        if not game.game_over:
            game.snake.move()
            state = check_collisions(game.snake, game.food_container)
            if state.should_end_game():
                game.game_over = True

            if state.snake_eaten:
                game.snake.eat()
                game.food_container.add()

            draw_snake(window, game.snake)
            draw_food(window, game.food_container)
            draw_score(window, game.snake)
        else:
            draw_endgame_message(window, len(game.snake.body))

        pygame.display.flip()

    pygame.quit()
