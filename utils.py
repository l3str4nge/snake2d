import pygame
import random


class Rect:
    width = None
    height = None

    color = (0, 0, 255)

    def __init__(self, x, y):
        self.x = x
        self.y = y


class SnakeHead(Rect):
    width = 10
    height = 10

    def __str__(self):
        return f"Head x: {self.x} y: {self.y}"


class SnakeElement(Rect):
    width = 10
    height = 10
    color = (255, 255, 255)

    def __str__(self):
        return f"Body x: {self.x} y: {self.y}"


class Food(Rect):
    width = 10
    height = 10
    color = (255, 0, 0)


class FoodContainer:
    def __init__(self, initial=0):
        self.container: list[Food] = []
        self.__index = 0

        for _ in range(initial):
            self.add()

    def add(self):
        x, y = random.randint(10, 790), random.randint(10, 590)
        self.container.append(Food(x, y))

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        try:
            item = self.container[self.__index]
        except IndexError:
            raise StopIteration

        self.__index += 1
        return item


def draw_snake(surface, snake):
    draw(surface, snake.head)
    for element in snake.body:
        draw(surface, element)


def draw_food(surface, food_container: FoodContainer):
    for food in food_container.container:
        draw(surface, food)


def draw(surface, rect: Rect):
    pygame.draw.rect(surface, rect.color, (rect.x, rect.y, rect.width, rect.height))


def draw_score(surface, game):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {len(game.snake.body)}", True, (0, 0, 255))
    surface.blit(score_text, (10, 10))

    highscore_text = font.render(f"Highscore: {game.highscore}", True, (0, 0, 255))
    surface.blit(highscore_text, (200, 10))


def draw_endgame_message(surface, score):
    font = pygame.font.Font(None, 30)
    msg = f"End game your score: {score}. Enter -> reset |  Escape -> Escape."
    message_text = font.render(msg, True, (0, 0, 255))
    text_rect = message_text.get_rect(center=(800 // 2, 600 // 2))
    surface.blit(message_text, text_rect)
