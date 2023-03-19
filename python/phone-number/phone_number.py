class PhoneNumber:
    def __init__(self, number):
        self.number = str(filter(lambda x: x.isdigit(), number))
        
