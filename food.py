from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.4)
        self.color("blue")
        self.speed(0)
        self.goto(randint(-230, 230), randint(-230, 230))

    def refresh(self):
        self.goto(randint(-230, 230), randint(-230, 230))