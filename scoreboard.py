from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.l_score}", move=False, align='center', font=('Arial', 50, 'normal'))
        self.goto(100, 240)
        self.write(f"{self.r_score}", move=False, align='center', font=('Arial', 50, 'normal'))

    def l_increase_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_increase_score(self):
        self.r_score += 1
        self.update_scoreboard()