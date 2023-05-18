from turtle import Turtle
import random
from scoreboard import ScoreBoard

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        food_x = random.randint(-250,250)
        food_y = random.randint(-250,250)
        self.goto(food_x,food_y)