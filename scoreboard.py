from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.color("white")
    self.score_update()
    
  def score_add(self):
    self.score += 1
    self.clear()
    self.score_update()
    
  def score_update(self):
    self.write(f"Score: {self.score}", align = "center", font = ("Arial", 18, "normal"))

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align="center", font=("Arial", 18, "normal"))