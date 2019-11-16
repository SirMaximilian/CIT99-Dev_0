from cflib.positioning.motion_commander import MotionCommander



def is_close(range):
    MIN_DISTANCE = 0.1  # m

    if range is None:
        return False
    else:
        return range < MIN_DISTANCE

class CarefulMotionCommander(MotionCommander):
    
    def object_avoid(self):
        pass

    def careful_left(self, distance_m, velocity=VELOCITY): #positive on y axis
        pass

    def careful_right(self, distance_m, velocity=VELOCITY): #negative on y axis
        pass

    def careful_forward(self, distance_m, velocity=VELOCITY): #positive on x axis
        pass

    def careful_back(self, distance_m, velocity=VELOCITY): #negative on x axis
        pass

    def careful_up(self, distance_m, velocity=VELOCITY): #positive on z axis
        pass

    def careful_down(self, distance_m, velocity=VELOCITY): #negative on z axis
        pass