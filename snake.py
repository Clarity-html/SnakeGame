from turtle import Turtle

STARTING_SEGMENTS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        """Initialize the snake by creating its body and setting the head as the first segment."""
        self.all_segments = []
        self.create_snake()
        self.SNAKE_HEAD = self.all_segments[0]

    def add_segment(self, position):
        """Creates a new segment and adds it to self.all_segments"""
        new_segment = Turtle("square")
        new_segment.color("forestgreen")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def create_snake(self):
        """Create the initial snake body using the positions in STARTING_SEGMENTS."""
        for pos in STARTING_SEGMENTS:
            self.add_segment(position=pos)

    def move_forward(self):
        """The main snake movement algorithm: it checks the position of the segment in front of it, and applies that segment's position to itself while continuously moving the snake head forward 20 units"""
        for seg in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg - 1].xcor()
            new_y = self.all_segments[seg - 1].ycor()
            self.all_segments[seg].goto(new_x, new_y)
        self.SNAKE_HEAD.forward(20)
        self.SNAKE_HEAD.color("chartreuse")

    def reset(self):
        """Moves the previous snake out of view and creates a new one by calling the self.create_snake function"""
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.create_snake()
        self.SNAKE_HEAD = self.all_segments[0]

    def extend_snake(self):
        self.add_segment(position=self.all_segments[-1].position())

    def up(self):
        if self.SNAKE_HEAD.heading() != 270:
            self.SNAKE_HEAD.setheading(90)

    def right(self):
        if self.SNAKE_HEAD.heading() != 180:
            self.SNAKE_HEAD.setheading(0)

    def down(self):
        if self.SNAKE_HEAD.heading() != 90:
            self.SNAKE_HEAD.setheading(270)

    def left(self):
        if self.SNAKE_HEAD.heading() != 0:
            self.SNAKE_HEAD.setheading(180)
