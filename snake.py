from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ORIGIN_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake:
   
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.shape('triangle')
        # self.snake_x=0
        # self.snake_y=0

    def create_snake(self):
        
        for i in ORIGIN_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        
        new_snake_body_piece = Turtle(shape = 'square')
        new_snake_body_piece.color('white')
        new_snake_body_piece.penup() 
        new_snake_body_piece.goto(position)
        self.snake_body.append(new_snake_body_piece)
        # snake_x = new_snake_body_piece.xcor()
        # snake_x -= 20

    def grow_snake(self):
        self.add_segment(self.snake_body[-1].position())


         
        
    def snake_move(self):
        for segment_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[segment_num -1].xcor()
            new_y = self.snake_body[segment_num -1].ycor()
            self.snake_body[segment_num].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)
    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)
    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)