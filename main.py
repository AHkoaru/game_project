from PIL import Image, ImageDraw, ImageFont
import time
import random
#import cv2 as cv
import numpy as np
from colorsys import hsv_to_rgb
from Enemy import *
from Bullet import Bullet
from Character import Character
from Joystick import Joystick

speed = 1
count = True
def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    # 잔상이 남지 않는 코드 & 대각선 이동 가능
    my_circle = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    enemy_1 = Enemy((50, 50),speed)
    enemy_2 = Enemy((200, 200),speed)
    enemy_3 = Enemy((150, 50),speed)


    enemys_list = (enemy_1, enemy_2, enemy_3)

    bullets = []

    cnt = True
    while cnt:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        if not joystick.button_A.value: # A pressed
            bullet = Bullet(my_circle.center, command)
            bullets.append(bullet)

        my_circle.move(command)
        enemy_1.move(my_circle.center)
        enemy_2.move(my_circle.center)
        enemy_3.move(my_circle.center)

        for bullet in bullets:
            bullet.collision_check(enemys_list)
            bullet.move()
            
        #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        my_draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = (0, 0, 0))

        #접촉시 종료
        for enemy in enemys_list:
            global count
            if my_circle.is_at_enemy(enemy.center):
                count = False
                cnt = False

        for enemy in enemys_list:
            if enemy.state != 'die':
                my_draw.ellipse(tuple(enemy.position), outline = enemy.outline, fill = (255, 0, 0))

        for bullet in bullets:
            if bullet.state != 'hit':
                my_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (0, 0, 255))

        all_enemies_dead = all(enemy.state == 'die' for enemy in enemys_list)
        if all_enemies_dead:
            cnt = False
            

        #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        joystick.disp.image(my_image)
        

if __name__ == '__main__':
    while count:
        main()
        speed += 0.5
    
