class SpaceAge:

    EARTH_SECONDS_YEAR = 31557600

    def __init__(self, seconds):
        self.mercury = seconds / self.EARTH_SECONDS_YEAR / 0.2408467
        self.venus = seconds / self.EARTH_SECONDS_YEAR / 0.61519726
        self.earth = seconds / self.EARTH_SECONDS_YEAR
        self.mars = seconds / self.EARTH_SECONDS_YEAR / 1.8808158
        self.jupiter = seconds / self.EARTH_SECONDS_YEAR / 11.862615
        self.saturn = seconds / self.EARTH_SECONDS_YEAR / 29.447498
        self.uranus = seconds / self.EARTH_SECONDS_YEAR / 84.016846
        self.neptune = seconds / self.EARTH_SECONDS_YEAR / 164.79132
    
    def on_mercury(self):
        return float(f'{self.mercury:.2f}')
    
    def on_venus(self):
        return float(f'{self.venus:.2f}')
    
    def on_earth(self):
        return float(f'{self.earth:.2f}')
    
    def on_mars(self):
        return float(f'{self.mars:.2f}')
    
    def on_jupiter(self):
        return float(f'{self.jupiter:.2f}')
    
    def on_saturn(self):
        return float(f'{self.saturn:.2f}')
    
    def on_uranus(self):
        return float(f'{self.uranus:.2f}')
    
    def on_neptune(self):
        return float(f'{self.neptune:.2f}')