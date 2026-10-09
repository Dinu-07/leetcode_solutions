class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        list_ = []
        for i in events:
            if counter!=10:
                if i == 'WD' or i=='NB':
                    score+=1
                elif i=='W':
                    counter+=1
                else:
                    score+=int(i)
        list_.append(score)
        list_.append(counter)
        return list_
                
        