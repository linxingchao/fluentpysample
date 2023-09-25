
class Robot:
    def __init__(self):
        pass
    
    def handle_command(self,message):
        match message:
            case ['BEEPER',frequency,times]:
                pass