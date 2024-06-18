
from seting import *


# אתחול pygame
pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Elevator System')

# טעינת תמונת המעלית והקול
elevator_image = pygame.image.load('elv.png')
ding_sound = pygame.mixer.Sound('ding.mp3')
brick_texture = pygame.image.load('kir.jpg')

# מגדיר את הגודל החדש לתמונה
new_width = 40  # רוחב חדש בפיקסלים
new_height = 60  # גובה חדש בפיקסלים

# מקטין את התמונה לגודל החדש
elevator_image = pygame.transform.scale(elevator_image, (new_width, new_height))
# הגדרת צבעים
RED = (255, 0, 0)
BACKGROUND_COLOR = (200, 200, 200)
BRICK_COLOR = (150, 75, 0)
BUTTON_COLOR = (255, 255, 255)
BUTTON_ACTIVE_COLOR = (0, 255, 0)
TEXT_COLOR = (0, 0, 0)
FLOOR_BAR_COLOR = (0, 0, 0)
BUTTON_CLICKED_COLOR =(255,0,255)
zero = 0
hundred_fifty =150
# טען את התמונה פעם אחת בתחילת הקוד
floor_height = screen_height // NUM_OF_FLOORS
floor_texture = pygame.image.load('kir.jpg')
floor_texture = pygame.transform.scale(floor_texture, (hundred_fifty, floor_height))

def draw_building(screen):
    floor_height = screen_height // NUM_OF_FLOORS
    for floor in range(NUM_OF_FLOORS):
        screen.blit(floor_texture, (zero, screen_height - (floor + 1) * floor_height))
       