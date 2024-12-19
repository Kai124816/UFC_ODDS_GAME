from predictions import picks

class person():
    def __init__(self,username:str,password:str,picks:picks,total_payout:int,total_profit:int) -> None:
        self.username = username
        self.password = password
        self.picks = picks
        self.total_payout = total_payout
        self.total_profit = total_profit
    
    def change_password(self,new_password:str) -> None:
        self.password = new_password
        