class Clock:
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = ((hour % 24) + (minute // 60)) % 24

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        return (self.minute == other.minute and self.hour == other.hour)

    def __add__(self, minutes):
        self.hour = (self.hour + ((self.minute + minutes) // 60)) % 24
        self.minute = (self.minute + minutes) % 60
        return self.__str__()

    def __sub__(self, minutes):
        self.hour = (self.hour + ((self.minute - minutes) // 60)) % 24
        self.minute = (self.minute - minutes) % 60
        return self.__str__()
