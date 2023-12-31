import sys 
import time 
from abc import ABC, abstractmethod 

sys.path.append('src/')
from common.constants import BUTTON_UP_INDEX
from common.constants import BUTTON_DOWN_INDEX 
from common.constants import BUTTON_A_INDEX
from common.constants import BUTTON_XBOX_INDEX 

class WheelControllerStrategy(ABC): 
    def __init__(self) -> None:
        self.last_press = time.time() 

    @abstractmethod
    def execute(self, controller, state) -> None: 
        pass 

class WheelReverseFlagStrategy(WheelControllerStrategy): 
    def execute(self, controller, state) -> None:
        current_time = time.time()
        if controller.button_is_pressed(controller.index, BUTTON_UP_INDEX) and current_time - self.last_press > 1: 
            state['reverse'] = not state['reverse'] 
            self.last_press = current_time

class WheelCruiseFlagStrategy(WheelControllerStrategy): 
    def execute(self, controller, state) -> None:
        current_time = time.time()
        if controller.button_is_pressed(controller.index, BUTTON_DOWN_INDEX) and current_time - self.last_press > 1: 
            state['cruise'] = not state['cruise']
            state['cruise_throttle']= state['throttle']
            self.last_press = current_time
              
class WheelLightFlagStrategy(WheelControllerStrategy): 
    def execute(self, controller, state) -> None:
        current_time = time.time()
        if controller.button_is_pressed(controller.index, BUTTON_A_INDEX) and current_time - self.last_press > 1: 
            state['light'] = not state['light'] 
            self.last_press = current_time 

class WheelSafeFlagStrategy(WheelControllerStrategy): 
    def execute(self, controller, state) -> None:
        current_time = time.time()
        if controller.button_is_pressed(controller.index, BUTTON_XBOX_INDEX) and current_time - self.last_press > 1: 
            state['safe'] = not state['safe']
            self.last_press = current_time 
            