from turtle import Turtle

TEXT = ("courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize scoreboard with score 0 and load high score from file."""
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 245)
        self.write_score()

    def write_score(self):
        """Display the current score and high score on screen."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=TEXT)

    def increase_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1
        self.write_score()

    def reset(self):
        """Checks if the session score is greater than the high score, and updates the high score accordingly."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.write_score()

    def clear_session_score(self):
        """Reset the session score to 0 and update the display."""
        self.score = 0
        self.write_score()




