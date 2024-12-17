from fight import fight

class Card():
    def __init__(self,fights:list[fight]) -> None:
        self.fights = fights

    def update_outcomes(self,update:tuple):
        for fight in self.fights:
            if fight.name == update[0]:
                fight.update_outcome(update)
                break


    
    
            

        
