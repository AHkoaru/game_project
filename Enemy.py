import numpy as np

class Enemy():
    def __init__(self, spawn_position,speed):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 10, spawn_position[1] - 10, spawn_position[0] + 10, spawn_position[1] + 10])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"
        self.speed = speed

    def move(self, character):
        distance_x = character[0] - self.center[0]
        distance_y = character[1] - self.center[1]

        if abs(distance_x) > abs(distance_y):
            if distance_x > 0:
                self.position[0] += self.speed
                self.position[2] += self.speed
            else:
                self.position[0] -= self.speed
                self.position[2] -= self.speed
        else:
            if distance_y > 0:
                self.position[1] += self.speed
                self.position[3] += self.speed
            else:
                self.position[1] -= self.speed
                self.position[3] -= self.speed

        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

