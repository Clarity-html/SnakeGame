from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Food(Turtle):
    def __init__(self):
        """Initializes the shape and size of the food item."""
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(0.5, 0.5)

    def spawn_food(self):
        """Spawn the food at a random position with a random color."""
        self.color(random.choice(COLORS))
        self.goto(random.randint(-285, 285), random.randint(-285, 230))
