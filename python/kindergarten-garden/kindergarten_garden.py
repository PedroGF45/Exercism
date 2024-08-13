class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')
        if students:
            self.students = sorted(students)
        else:
            self.students = ["Alice",
                            "Bob",
                            "Charlie",
                            "David",
                            "Eve",
                            "Fred",
                            "Ginny",
                            "Harriet",
                            "Ileana",
                            "Joseph",
                            "Kincaid",
                            "Larry"]
                            
        self.plants_map = {"G": "Grass",
                       "C": "Clover",
                       "R": "Radishes",
                       "V": "Violets"}
        
    def plants(self, student):
        index = self.students.index(student) * 2
        return [self.plants_map[plant] for row in self.diagram for plant in row[index: index + 2] ]
