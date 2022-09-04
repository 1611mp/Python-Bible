# My own class coin
import random
class Rupee:
    def __init__(self,rare=False):
        self.rare = rare
        if self.rare:
            self.value = 1.50
        else:
            self.value = 1.00
    
        self.colour = "silver"
        self.num_edges = 1
        self.diameter = 21.93
        self.thickness = 1.45
        self.heads = False


    def rust(self):
        self.colour = "golden brown"

    def clean(self):
        self.colur = "silver"

    def flip(self):
        heads_option = [True,False]
        choice = random.choice(heads_option)
        self.heads = choice

    # def __del__(self):
    #     print("Coin Spent!")

coin1 = Rupee()
coin1.clean()
print(coin1.colour)