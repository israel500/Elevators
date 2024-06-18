from seting import *
from bilding import *
from elevator import *
from floobuton import *


class ElevatorSystem:
    def __init__(self, num_of_elevators, num_of_floors, speed):

        self.num_of_floors = num_of_floors  
        self.elevators = [Elevator(i, num_of_floors, screen_height, elevator_image, ding_sound, speed)
                          for i in range(num_of_elevators)]  
        self.floor_buttons = [FloorButton(floor, screen_width - 500, screen_height - (floor + 1) * (screen_height // num_of_floors), 50, screen_height // num_of_floors) for floor in range(num_of_floors)]  # שימה של הכפתורים
        self.last_time = time.time()


    # def call_elevator(self, to_floor):
    #     for el in self.elevators:
    #         if to_floor in el.target:
    #             return 
    #         if to_floor == el.on_floor:
    #             return 
    #         self.floor_buttons[to_floor].click()  
    #         if self.floor_buttons == BUTTON_ACTIVE_COLOR:
    #             return
    #     if to_floor is not None:
    #         elevator = min(self.elevators, key=lambda x: x.time_to_floor(to_floor))
    #     self.floor_buttons[to_floor].arrival_time = elevator.new_call(to_floor) 
    
    def call_elevator(self, to_floor):
        for el in self.elevators:
            if to_floor in el.target:
                return False
            if to_floor == el.on_floor:
                return False
            #self.floor_buttons[to_floor].click()  
            if self.floor_buttons == BUTTON_ACTIVE_COLOR:
                return False
            if to_floor is not None:
                elevator = min(self.elevators, key=lambda x: x.time_to_floor(to_floor))
            self.floor_buttons[to_floor].arrival_time = elevator.new_call(to_floor) 
        return True 

    def update(self):
        for elevator in self.elevators:
            elevator.update()
            for button in self.floor_buttons:
                if button.floor_number == elevator.on_floor:
                    if not elevator.waiting and elevator.target: 
                        if button.color == BUTTON_ACTIVE_COLOR:
                            button.reset()
                            button.arrival_time += ARRIVAL_DELAY
                    if elevator.waiting and elevator.target: 
                        if button.color == BUTTON_ACTIVE_COLOR:
                            button.reset()
                            button.arrival_time = zero
                            elevator.arrival_time = zero
        for button in self.floor_buttons:
            if button.color == BUTTON_ACTIVE_COLOR and button.arrival_time > zero:
                button.arrival_time -= (time.time() - self.last_time)
        self.last_time = time.time()

    

    def draw(self, screen):
        for elevator in self.elevators:
            elevator.draw(screen)
        for button in self.floor_buttons:
            button.draw(screen)
    