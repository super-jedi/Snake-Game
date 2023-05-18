from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

def snake_main():
    print("START")
    game_is_on = True

    screen = Screen()
    screen.clear()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("SNAKE")
    
    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    screen.listen()
    screen.onkey(key="w",fun=snake.up)
    screen.onkey(key="s",fun=snake.down)
    screen.onkey(key="a",fun=snake.left)
    screen.onkey(key="d",fun=snake.right)
    screen.onkey(key="space",fun=snake_main)

    while(game_is_on):
        screen.update()
        time.sleep(0.1)
        snake.snake_move()
        if(snake.head.distance(food) < 15 ):
            print("YUM YUM")
            food.refresh_food()
            snake.grow_snake()
            scoreboard.add_score()
            
        # detect wall collision
        if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
            game_is_on = False
            print("HIT WALL DEAD")
            scoreboard.game_over()
            
            
            
        for body_part in snake.snake_body[3:]:
            
            if(snake.head.distance(body_part) < 10):
                
                game_is_on = False
                print("ATE SELF")
                scoreboard.game_over()
                

    screen.exitonclick()
    
snake_main()
