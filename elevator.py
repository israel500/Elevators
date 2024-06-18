from seting import *
from bilding import *
import pygame
import time
ten =10

class Elevator:
    def __init__(self, num, num_of_floors, screen_height, elevator_image, ding_sound, speed):
        self.speed = speed # pixels per second
        self.num = num  # מספר המעלית
        self.num_of_floors = num_of_floors  # מספר הקומות
        self.screen_height = screen_height  # גודל המסך
        self.elevator_image = elevator_image  # תמונה של המעלית
        self.ding_sound = ding_sound  # צליל עצירה
        self.on_floor = 0  # הקומה הנוכחית בה נמצאת המעלית.
        self.target = []  # None    רשימת הקומות שהמעלית תבקר בהן.
        self.current_target = None # הזמן שנותר עד שהמעלית תסיים את הנסיעה הנוכחית.
        self.time_to_finish = 0
        self.whatch = None  # הזמן שבו התחילה הנסיעה הנוכחית.
        self.free = True
        self.y = self.floor_to_y(0)
        self.stop_time = ARRIVAL_DELAY  # זמן עצירה בקומה
        self.timer_text = None
        self.new_target = None
        self.sum_of_elvator = 0
        self.sum_time = 0
        self.departure_time = 0  # את זמן היציאה שומר
        self.current_source_y = self.y  # שומר מיקום היציאה
        self.current_dest_y = 0
        self.floor_dest = None
        self.arrival_time = 0
        self.waiting = False


    def floor_to_y(self, floor):  
        if floor is None:
            floor = zero
        floor_height = self.screen_height // self.num_of_floors
        return self.screen_height - (floor + 1) * floor_height
    

    def wait(self):
        current_time = time.time()
        if current_time - self.arrival_time >= ARRIVAL_DELAY:
            self.free = True
            self.waiting = False
        if not self.target:
            self.time_to_finish = zero


   
    def new_move(self):
        if not self.free:
            if self.y != self.current_dest_y:
                current_time = time.time()
                time_since_departure = current_time - self.departure_time
                direction = 1 if self.current_dest_y > self.y else -1
                new_y = self.current_source_y + direction * time_since_departure * self.speed
                if (self.y < self.current_dest_y and new_y > self.current_dest_y) or (self.y > self.current_dest_y and new_y < self.current_dest_y):
                    self.y = self.current_dest_y
                else:
                    self.y = new_y
            else:
                self.on_floor = self.floor_dest
                self.wait()


    def update(self):
        # free
        # in movement
        # waiting
        if self.free and len(self.target) > zero:# free
            self.departure_time = time.time()
            floor = self.target.pop(0)
            self.current_source_y = self.y
            self.current_dest_y = self.floor_to_y(floor)
            self.floor_dest = floor
            self.free = False
        if self.y == self.current_dest_y and not self.waiting:# waiting
            self.arrival_time = time.time()
            self.ding_sound.play()
            self.waiting = True
        self.new_move()
    

    def time_to_floor(self, floor):  
        if self.time_to_finish:
            time_elapsed = time.time() - self.whatch
            total_time = self.time_to_finish - time_elapsed
        else:
            time_elapsed = zero
            total_time = max(ARRIVAL_DELAY - (time.time() - self.arrival_time), zero)
        last_floor = self.target[-1] if self.target else self.on_floor
        distance = abs(floor - last_floor)
        result = total_time + distance * ELEVATOR_SPEED + ARRIVAL_DELAY
        print(result)
        return result


    def new_call(self, floor): 
        self.time_to_finish = self.time_to_floor(floor)
        self.whatch = time.time()
        for n in self.num  
        self.target.append(floor) 
        assert self.time_to_finish >= zero
        return self.time_to_finish - ARRIVAL_DELAY

    def draw(self, screen):
        screen.blit(self.elevator_image, (400 + self.num * (self.elevator_image.get_width() + ten), self.y))

