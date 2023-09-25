from constants import VELOCITY
from utils import Rect, SnakeHead, SnakeElement


class Snake:
    def __init__(self):
        self.head = SnakeHead(50, 50)
        self.body: list[Rect] = []
        self.direction = "right"

    def change_direction(self, value):
        self.direction = value

    def move(self):
        head_x, head_y = self.head.x, self.head.y

        if self.direction == "left":
            self.head.x -= VELOCITY
        elif self.direction == "right":
            self.head.x += VELOCITY
        elif self.direction == "up":
            self.head.y -= VELOCITY
        elif self.direction == "down":
            self.head.y += VELOCITY

        for element in self.body:
            _x, _y = element.x, element.y

            element.x = head_x
            element.y = head_y

            head_x, head_y = _x, _y

    def eat(self):
        tail = self.body[-1] if self.body else self.head
        self.body.append(SnakeElement(tail.x - 10, tail.y))
