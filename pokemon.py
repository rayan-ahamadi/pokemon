class Pokemon:
    def __init__(self, name_,level_,attackPower_):
        self.__name = name_
        self.__health = 100
        self.level = level_
        self.attackPower = attackPower_
        self.defence = 0 
    
    def showHealth(self):
        return self.__health

    def changeHealth(self,newValue):
        self.__health = newValue
    
    def showName(self):
        return self.__name
    
    def infoPokemon(self):
        return "nom : {}\nPoint de vie : {}\nStats de défense : {}\nStats d'attaque : {}\nNiveau : {}".format(self.__name,self.__health,self.defence,self.attackPower, self.level)
    
    