import random
from TypeNormal import TypeNormal
from TypeFeu import TypeFeu
from TypeEau import TypeEau
from TypeTerre import TypeTerre



class Combat:
    def __init__(self) -> None:
        pass

    def twoPokemonAlive(self,pokemon_object1,pokemon_object2):
        if pokemon_object1.showHealth() <= 0:
            return False
        elif pokemon_object2.showHealth() <= 0:
            return False
        else:
            return True
        
    def damage(self,pokemon_objectAtt,pokemon_objectDef):
        ##Celui qui lance l'attaque pokemon_objectAtt, celui qui défend l'attaque pokemon_objectDef
        # self.giveDégats(pokemon_objectAtt,pokemon_objectDef) retourne les dégats que va prendre pokemon_objectDef
        damage = max(1, (pokemon_objectAtt.level * self.giveDégats(pokemon_objectAtt,pokemon_objectDef)) - pokemon_objectDef.defence) 
        hisNewHealth = pokemon_objectDef.showHealth() - damage
        #Applique la nouvelle santé de celui qui prend l'attaque
        pokemon_objectDef.changeHealth(hisNewHealth)
        if pokemon_objectDef.showHealth() < 0:
            #si la santé d'un pokémon est inférieur à 0 après des dommages subies trop important
            pokemon_objectDef.changeHealth(0)
        print("{} attaque {}...".format(pokemon_objectAtt.showName(),pokemon_objectDef.showName()))    
        print("{} a subi des dégats de {} PV. Son PV est à : {}\n".format(pokemon_objectDef.showName(),damage,pokemon_objectDef.showHealth()))

    def winnerIs(self,pokemon_object1,pokemon_object2):
        if pokemon_object1.showHealth() <= 0:
            print("{} a gagné".format(pokemon_object2.showName()))
        elif pokemon_object2.showHealth() <= 0:
            print("{} a gagné".format(pokemon_object1.showName()))
        else:
            return 0
        
    def loserIs(self,pokemon_object1,pokemon_object2):
        if pokemon_object1.showHealth <= 0:
            print("{} a perdu".format(pokemon_object1.showName()))
        elif pokemon_object2.showHealth <= 0:
            print("{} a perdu".format(pokemon_object2.showName()))
        else:
            return 0
    
    def canAttack(self):
        return random.choice([0,1])
    
    def giveDégats(self,pokemon_object,ennemy_pokemon) -> float:
        attack = 0
        if type(pokemon_object) is TypeNormal:
            if type(ennemy_pokemon) is TypeNormal:
                return pokemon_object.attackPower * 0.75
            elif type(ennemy_pokemon) is TypeFeu:
                return pokemon_object.attackPower * 0.75
            elif type(ennemy_pokemon) is TypeEau:
                return pokemon_object.attackPower * 0.75
            elif type(ennemy_pokemon) is TypeTerre:
                return pokemon_object.attackPower * 0.75

        if type(pokemon_object) is TypeFeu:
            if type(ennemy_pokemon) is TypeNormal: 
                return pokemon_object.attackPower * 1.0
            elif type(ennemy_pokemon) is TypeFeu:
                return pokemon_object.attackPower *  1.0
            elif type(ennemy_pokemon) is TypeEau:
                return pokemon_object.attackPower *  0.5
            elif type(ennemy_pokemon) is TypeTerre:
                return pokemon_object.attackPower *  2
        
        if type(pokemon_object) is TypeEau:
            if type(ennemy_pokemon) is TypeNormal: 
                return pokemon_object.attackPower * 1.0
            elif type(ennemy_pokemon) is TypeFeu:
                return pokemon_object.attackPower * 2
            elif type(ennemy_pokemon) is TypeEau:
                return pokemon_object.attackPower * 1.0
            elif type(ennemy_pokemon) is TypeTerre:
                return pokemon_object.attackPower * 0.5

        if type(pokemon_object) is TypeTerre:
            if type(ennemy_pokemon) is TypeNormal: 
                return pokemon_object.attackPower * 1.0
            elif type(ennemy_pokemon) is TypeFeu:
                return pokemon_object.attackPower * 0.5
            elif type(ennemy_pokemon) is TypeEau:
                return pokemon_object.attackPower * 2.0
            elif type(ennemy_pokemon) is TypeTerre:
                return pokemon_object.attackPower * 1.0





    