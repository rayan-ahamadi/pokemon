from pokemon import Pokemon

class TypeNormal(Pokemon):
    def __init__(self, name_, level_, attackPower_,defence_):
        super().__init__(name_, level_, attackPower_)
        self.defence = defence_

    
    