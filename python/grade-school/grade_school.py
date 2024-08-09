class School:
    def __init__(self):
        self.students      = {}
        self.added_history = []

    def add_student(self, name, grade):
        if name not in self.students:

            self.students[name] = grade

            self.added_history.append(True)
        else:
            self.added_history.append(False)

    def roster(self):
        
        if len(self.students.values()) == 0:
            return []
        max_value = max(self.students.values())
        ans = []

        print(f'MAX: {max_value}')
        for i in range(1, max_value + 1, 1):
            temp = []
            print(f'i: {i}')
            for student in self.students.keys():
                if self.students[student] == i:
                    temp += [student]
                    print(temp)
            temp = sorted(temp)
            ans += temp            
        return ans

    def grade(self, grade_number):

        ans = []

        for student in self.students.keys():
            if self.students[student] == grade_number:
                ans += [student]

        return sorted(ans)

    def added(self):
        return self.added_history
    
    def grad(self):
        return self.grades
        
