from turtle import Turtle

class ScoreBoard(Turtle):
    # global HS

    def __init__(self):
        super().__init__()
        self.score = 0
        # with open("./snake/snakehighscore.txt") as file:
        with open("snakehighscore.txt") as file:
            self.high_score = int(file.read())
        
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,250)
        self.write(f"SCORE: {self.score} | HIGH SCORE: {self.high_score}", move=False, align='center', font=('Arial', 24, 'normal'))
        

    def add_score(self):
       self.score+= 1
       self.clear()
       self.write(f"SCORE: {self.score} | HIGH SCORE: {self.high_score}", move=False, align='center', font=('Roboto', 24, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.reset_scores()
        self.write(f"GAME OVER | SCORE: {self.score}", move=False, align='center', font=('Roboto', 20, 'normal'))
        self.goto(0,-40)
        self.write(f"HIGH SCORE: {self.high_score}", move=False, align='center', font=('Roboto', 18, 'normal'))
        self.goto(0,-80)
        self.write("PRESS SPACE TO RESTART", move=False, align='center', font=('Roboto', 14, 'normal'))


    def reset_scores(self):
        # global HS
        if(self.score > self.high_score):
            self.high_score = self.score
            with open("snakehighscore.txt", mode = 'w') as file:
               
                file.write(str(self.score))
                
        score = 0


    