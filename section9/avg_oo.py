
class Avg:
    def __init__(self):
        self.series = []
        
    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)
    
def make_avg():
    series = []
    
    def avg(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    
    return avg

def make_avg2():
    count = 0
    total = 0
    
    def avg(new_value):
        nonlocal count
        nonlocal total
        count += 1
        total += new_value
        return total / count
    return avg