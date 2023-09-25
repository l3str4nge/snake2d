from snake import Snake
from utils import FoodContainer


class CollisionState:
    def __init__(self, wall_hit = False, eaten_yourself = False, snake_eaten = False):
        self.wall_hit = wall_hit
        self.eaten_yourself = eaten_yourself
        self.snake_eaten = snake_eaten

    def should_end_game(self):
        return self.wall_hit or self.eaten_yourself

def check_collisions(snake: Snake, food_container: FoodContainer):
    if snake.head.x > 800 or snake.head.x < 0:
        return CollisionState(wall_hit=True)

    if snake.head.y > 600 or snake.head.y < 0:
        return CollisionState(wall_hit=True)

    for element in snake.body:
        if snake.head.x == element.x and snake.head.y == element.y:
            return CollisionState(eaten_yourself=True)
    to_eaten = []
    for food in food_container.container:
        if (snake.head.x - 10 <= food.x <= snake.head.x + 10) and (
            snake.head.y - 10 <= food.y <= snake.head.y + 10
        ):
            to_eaten.append(food)

    food_container.container = [
        x for x in food_container.container if x not in to_eaten
    ]
    if to_eaten:
        return CollisionState(snake_eaten=True)

    return CollisionState()
