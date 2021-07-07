import pygame as pg
import time
import random

pg.init()

yellow = (255, 255, 102)
red = (255, 0 , 0)
blue = (0, 0, 255)
green = (34, 139, 34)
cornsilk = (255, 248, 220)
black = (0, 0, 0)

dis_width = 600
dis_height = 400
dis = pg.display.set_mode((dis_width, dis_height))
pg.display.set_caption("Snake Game by Edureka")

clock = pg.time.Clock()

snake_block = 10
snake_speed = 30

font_style = pg.font.SysFont("bahnschrift", 25)
score_font = pg.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(1, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(1, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(cornsilk)
            Your_score(Length_of_snake - 1)
            message("You LOST! Press 'Q':quit or 'C' to play again", red)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_c:
                        game_loop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pg.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pg.K_UP:
                    x1_change = 0
                    y1_change = -snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(cornsilk)
        pg.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pg.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(1, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(1, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pg.quit()
    quit()

game_loop()
