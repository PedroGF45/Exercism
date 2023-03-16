import string
import random

alphabet = string.ascii_uppercase
class Robot:

    # all names being used
    names = []

    def __init__(self):
        self.reset()

    def reset(self):
        
        # construct the name of the robot
        letters = ''.join(random.choice(alphabet) for i in range(2))
        numbers = ''.join(str(random.randint(0,9)) for i in range(3))
        name = letters + numbers

        # if name is not being used by another robot
        if  name not in self.names:
            self.names += [name]
            self.name = name
        else:
            self.reset()
