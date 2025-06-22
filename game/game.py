import os
import pgzrun
from pgzero.actor import Actor
from pgzero.animation import animate

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
bullet_timer = 0
bullet_org_y = 0
bullet_2_org_y = 0
bullet_2_org_y = 0
bullet_speed = 20
pause = False

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
    global bullet_timer, bullet_org_y, bullet_2_org_y, bullet_3_org_y, bullet_speed, pause
    if not pause:
        if keyboard.left and ship.x > ship.width / 2:
            ship.x -= 5
        if keyboard.right and ship.x < (WIDTH - ship.width / 2):
            ship.x += 5
        if keyboard.up and ship.y > ship.height:
            ship.y -= 5
        if keyboard.down and ship.y < HEIGHT:
            ship.y += 5
    
    if bullet_timer == 0:
        bullet.visible = True
        bullet.pos = ship.pos
        bullet_org_y = bullet.y = ship.y - 50
    if bullet.visible:
        if bullet.y > bullet_org_y - HEIGHT:
            bullet.y -= bullet_speed
        else:
            bullet.visible = False
            bullet_timer = -1
    
    if bullet.y <= bullet_org_y - HEIGHT / 3 + bullet_speed / 2 and bullet.y >= bullet_org_y - HEIGHT / 3 - bullet_speed / 2:
        bullet_2.visible = True
        bullet_2.pos = ship.pos
        bullet_2_org_y = bullet_2.y = ship.y - 50
    if bullet_2.visible:
        if bullet_2.y > bullet_2_org_y - HEIGHT:
            bullet_2.y -= bullet_speed
        else:
            bullet_2.visible = False
    
    if bullet.y <= bullet_org_y - ((HEIGHT * 2) / 3) + bullet_speed / 2 and bullet.y >= bullet_org_y - ((HEIGHT * 2) / 3) - bullet_speed / 2:
        bullet_3.visible = True
        bullet_3.pos = ship.pos
        bullet_3_org_y = bullet_3.y = ship.y - 50
    if bullet_3.visible:
        if bullet_3.y > bullet_3_org_y - HEIGHT:
            bullet_3.y -= bullet_speed
        else:
            bullet_3.visible = False
    if not pause:
        bullet_timer += 0.5
        bullet_speed = 100
    else:
        bullet_speed = 0

def animate_ship(pos):
    global ship, pause
    distance = ship.distance_to(pos)
    speed = 500
    animation = animate(ship, duration=distance/speed, pos=(pos[0], pos[1]+ship.height))
    if not pause:
        if pos[0] > ship.width/2 and pos[1] > 0 and pos[0] < WIDTH-ship.width/2 and pos[1] < HEIGHT - ship.height:
            animation.running = True
        else:
            animation.stop()
            animation.running = False
    else:
        animation.stop()
        animation.running = False

def on_mouse_move(pos):
    global ship
    animate_ship(pos)

def on_key_down(key):
    global pause
    if key == keys.P:
        if not pause:
            pause = True
        else:
            pause = False

pgzrun.go()