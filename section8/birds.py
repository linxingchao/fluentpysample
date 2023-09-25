class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack')


def alert(birdie):
    birdie.quack()
    
def alert_duck(bidie:Duck) -> None:
    bidie.quack()
    
def alert_bird(birdie:Bird) -> None:
    birdie.quack() 