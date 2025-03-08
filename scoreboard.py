from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_high_score())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(220)
        self.speed(0)
        self.blit_score()

    def blit_score(self):
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, "center", ("Courier", 15, "bold"))

    def update_score(self):
        self.clear()
        self.blit_score()

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def read_high_score(self):
        with open("high_score.txt", "r") as f:
            high_score = f.read()
        return high_score