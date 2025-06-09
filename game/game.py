import pgzrun
import pygame
from pgzero.animation import animate
from pgzero.actor import Actor
import os
from pgzero.clock import clock

WIDTH = 900
HEIGHT = 1000
TITLE = "Alien Shooter"
os.environ['SDL_VIDEO_CENTERED'] = '1'

ship = Actor("ship", (WIDTH / 2, HEIGHT), anchor=('center', 'bottom'))
bullet = Actor("bullet", (ship.x, ship.y - 50))
bullet_2 = Actor("bullet", (ship.x, ship.y - 50))
bullet_3 = Actor("bullet", (ship.x, ship.y - 50))
bullet.visible = False
bullet_2.visible = False
bullet_3.visible = False
timer = 0

def draw():
    screen.fill((255, 255, 255))
    ship.draw()
    if bullet.visible:
        bullet.draw()
    if bullet_2.visible:
        bullet_2.draw()
    if bullet_3.visible:
        bullet_3.draw()

def update():
    if keyboard.left and ship.x > ship.width / 2:
        ship.x -= 5
    if keyboard.right and ship.x < (WIDTH - ship.width / 2):
        ship.x += 5
    if keyboard.up and ship.y > ship.height:
        ship.y -= 5
    if keyboard.down and ship.y < HEIGHT:
        ship.y += 5

    if not bullet.visible:
        bullet.pos = (ship.x, ship.y - 50)
        bullet.visible = True
        animate(bullet, tween='linear', duration=1, y=-50, on_finished=lambda: reset_bullet(bullet))
    if not bullet_2.visible and timer > 1/3:
        bullet_2.pos = (ship.x, ship.y - 50)
        bullet_2.visible = True
        animate(bullet_2, tween='linear', duration=1, y=-50, on_finished=lambda: reset_bullet(bullet_2))
    if not bullet_3.visible and timer > 2/3:
        bullet_3.pos = (ship.x, ship.y - 50)
        bullet_3.visible = True
        animate(bullet_3, tween='linear', duration=1, y=-50, on_finished=lambda: reset_bullet(bullet_3))

def reset_bullet(bullet_obj):
    bullet_obj.visible = False

def timer_value():
    global timer
    timer += 1/60

def update_timer():
    clock.schedule_interval(timer_value, 1/60)

update_timer()

pgzrun.go()