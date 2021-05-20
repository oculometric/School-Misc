import os, random, pygame

os.environ["SDL_VIDEO_CENTRED"] = "1"
pygame.init()


pygame.display.set_caption ("Hell")
screen = pygame.display.set_mode ((420,69))

fg_col = (250, 250, 250)
bg_col = (0, 0, 0)

def change_colour_scheme ():
    global fg_col
    global bg_col
    fg_col = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))
    bg_col = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))

up_press = False
down_press = False

running = True

box_offset = 69/2

attackers = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.dict['key'] == 1073741906:
                up_press = True
            if event.dict['key'] == 1073741905:
                down_press = True
        if event.type == pygame.KEYUP:
            if event.dict['key'] == 1073741906:
                up_press = False
            if event.dict['key'] == 1073741905:
                down_press = False
            
    if (up_press or down_press):
        change_colour_scheme()

    if (up_press): box_offset -= 0.5
    if (down_press): box_offset += 0.5

    if (box_offset < 0): box_offset = 0
    if (box_offset > 69-20): box_offset = 69-20

    screen.fill (bg_col)
    pygame.draw.rect (screen, fg_col, pygame.Rect(0,box_offset,10,20))
    pygame.display.flip()

pygame.exit()
