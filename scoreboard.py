from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.updateScoreboard()
        
    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER" , align= ALIGNMENT, font= FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()
