class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]
    
    def personal_best(self):
        return max(self.scores)
    
    def personal_top_three(self):
        sorted_list = self.scores.copy()
        sorted_list.sort(reverse=True)
        return sorted_list[:3]
            
