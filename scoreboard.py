from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.pencolor("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"Score: {self.current_score}", move=False, align="center", font=("Arial", 14, "normal"))

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}", move = False, align = "center", font = ("Arial", 14, "normal"))
    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move = False, align = "center", font = ("Arial", 24, "normal"))