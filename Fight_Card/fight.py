class fight():
    def __init__(self,name:str,fighter1:str,fighter2:str,fighter1_ml:int,fighter2_ml:int,fighter1_props:dict,fighter2_props:dict,outcome:list) -> None:
        self.name = name
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.fighter1_ml = fighter1_ml
        self.fighter2_ml = fighter2_ml
        self.fighter1_props = fighter1_props
        self.fighter2_props = fighter2_props
        self.outcome = outcome
    
    def update_outcome(self,update:list):
        self.outcome = update

    

        
        