from seting import *
from bilding import *
from elevator import *
from systemelevater import *
ten =10
class FloorButton:
    def __init__(self, floor_number, x, y, width, height):
        self.floor_number = floor_number
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BUTTON_COLOR
        self.arrival_time = zero
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.floor_number), True, TEXT_COLOR)
        screen.blit(text, (self.rect.x + ten, self.rect.y + ten))
        if self.color == BUTTON_ACTIVE_COLOR and self.arrival_time:
            time_text = font.render(f'{self.arrival_time:.1f}s', True, TEXT_COLOR)
            screen.blit(time_text, (self.rect.x - 100, self.rect.y +20))

    def click(self):
        self.color = BUTTON_ACTIVE_COLOR

    def reset(self):
        self.color = BUTTON_COLOR

