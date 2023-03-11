import json
import time
import random
from TypeNormal import TypeNormal
from TypeFeu import TypeFeu
from TypeEau import TypeEau
from TypeTerre import TypeTerre
from combat import Combat

def to_dict(pokemon_object):
        types = "none"
        if type(pokemon_object) is TypeNormal:
            types = "Normal"
        elif type(pokemon_object) is TypeFeu:
            types = "Feu"
        elif type(pokemon_object) is TypeEau:
            types = "Eau"
        elif type(pokemon_object) is TypeTerre:
            types = "Terre"

        name = pokemon_object.showName()
        pv = pokemon_object.showHealth()
        return {
            'name': name,
            "PV": pv,
            "level": pokemon_object.level,
            "powerLevel": pokemon_object.attackPower,
            "défense": pokemon_object.defence,
            "type": types
        }

def save_pokemon(pokemon_object,where):
    file = "JSON/{}.json".format(where) 
    with open(file,"r+") as f:
        data = json.load(f)
        data["pokemon"].append(to_dict(pokemon_object))
        f.seek(0)
        json.dump(data,f,indent=2)

def random_pokemon():
    with open('JSON/pokemon.json') as f:
        data = json.load(f)
        random_objet = random.choice(data["pokemon"])
        if random_objet["type"] == "Normal":
            return TypeNormal(random_objet["name"],random_objet["level"],random_objet["powerLevel"],random_objet["d\u00e9fense"])
        elif random_objet["type"] == "Feu":
            return TypeFeu(random_objet["name"],random_objet["level"],random_objet["powerLevel"],random_objet["d\u00e9fense"])
        elif random_objet["type"] == "Eau":
            return TypeEau(random_objet["name"],random_objet["level"],random_objet["powerLevel"],random_objet["d\u00e9fense"])
        elif random_objet["type"] == "Terre":
            return TypeTerre(random_objet["name"],random_objet["level"],random_objet["powerLevel"],random_objet["d\u00e9fense"])
        
def choosePokemon():
    with open("JSON/pokedex.json") as f: 
        data = json.load(f)
        i=1
        for pokemon in data["pokemon"]:
            print("{} - {}".format(i,pokemon["name"]))
            i+=1
        n = input("Avec quel pokémon voulez vous combattre ? (Donnez un nombre)")   
        i = 1
        n = int(n)
        for pokemon in data["pokemon"]:
            if i == n:
                match pokemon["type"]:
                    case "Normal":
                        return TypeNormal(pokemon["name"],pokemon["level"],pokemon["powerLevel"],pokemon["d\u00e9fense"])
                    case "Feu":
                        return TypeFeu(pokemon["name"],pokemon["level"],pokemon["powerLevel"],pokemon["d\u00e9fense"])
                    case "Eau":
                        return TypeEau(pokemon["name"],pokemon["level"],pokemon["powerLevel"],pokemon["d\u00e9fense"])
                    case "Terre":
                        return TypeTerre(pokemon["name"],pokemon["level"],pokemon["powerLevel"],pokemon["d\u00e9fense"])
            i+=1
            
        
def pokemonFight():        
    pokemon1 = choosePokemon()
    pokemon2 = random_pokemon()
    print("{} va combattre {}".format(pokemon1.showName(),pokemon2.showName()))
    ## instancie le nouveau combat
    newCombat = Combat()
    escape = False
    tour = 1
    #Faire combattre deux pokémon
    while newCombat.twoPokemonAlive(pokemon1,pokemon2):
        if tour == 1 :
            escape
            attack = input("1- Lancer une attaque\n2- Fuite\n:")
            if str(attack) == "1":
                if newCombat.canAttack() == 1:
                    newCombat.damage(pokemon1,pokemon2)
                    tour = 2
                else: 
                    print("{} a raté son attaque !!!!\n".format(pokemon1.showName()))
                    tour = 2
            elif str(attack) == "2" : 
                print("Vous avez fui le combat")
                escape = True
                break
        elif tour == 2 : 
            if newCombat.canAttack() == 1:
                newCombat.damage(pokemon2,pokemon1)
                tour = 1
            else: 
                print("{} a raté son attaque !!!!\n".format(pokemon2.showName()))
                tour = 1
        time.sleep(2.0)
    if escape == False:
        newCombat.winnerIs(pokemon1,pokemon2)
    print("\n")
    if pokemon2.showHealth() <= 0:
        with open("JSON/pokedex.json") as f:
            data = json.load(f)
            alreadyIn = False
            for pokemon in data["pokemon"]:
                alreadyIn
                if pokemon["name"] == pokemon2.showName():
                    alreadyIn = True
            if alreadyIn == False: 
                pokemon2.changeHealth(100)
                save_pokemon(pokemon2,"pokedex")
                print("nouveau pokémon: {}, ajouté au pokédex".format(pokemon2.showName()))
    
    print("\n")

def pokedex():
    with open("JSON/pokedex.json") as f:
        data = json.load(f)
        i=1
        for pokemon in data["pokemon"]:
            print("{} - Nom : {}\n    Type : {}\n    PV: {}\n    Niveau : {}\n    Puissance D'attaque : {}\n    Défense : {}\n".format(i,pokemon["name"],pokemon["type"],pokemon["PV"],pokemon["level"],pokemon["powerLevel"],pokemon["d\u00e9fense"]))
            i+=1
        n = input("Quitter le pokédex (Y/y)")
        return n
    
def ajoutPokemon():
    name = input("Nom du nouveau pokémon : ")
    level = input("Niveau de départ du pokémon : ")
    powerLevel = input("Puissance d'attaque du pokémon : ")
    defence = input("Stats défensif du pokémon : ")
    type = ""
    while(type != "Normal" and type != "Feu" and type != "Eau" and type != "Terre" ):
        type = input("Type du pokémon (Normal, Feu, Terre,Eau) : ")

    match type:
        case "Normal":
            newPokemon = TypeNormal(name,int(level),int(powerLevel),int(defence))
            save_pokemon(newPokemon,"pokemon")
            print("Pokemon {} ajouté avec succès".format(newPokemon.showName()))   
            return 0
        case "Feu":
            newPokemon = TypeFeu(name,int(level),int(powerLevel),int(defence))
            save_pokemon(newPokemon,"pokemon")
            print("Pokemon {} ajouté avec succès".format(newPokemon.showName()))   
            return 0
        case "Eau":
            newPokemon = TypeEau(name,int(level),int(powerLevel),int(defence))
            save_pokemon(newPokemon,"pokemon")
            print("Pokemon {} ajouté avec succès".format(newPokemon.showName()))   
            return 0
        case "Terre":
            newPokemon = TypeTerre(name,int(level),int(powerLevel),int(defence))
            save_pokemon(newPokemon,"pokemon")
            print("Pokemon {} ajouté avec succès".format(newPokemon.showName()))   
            return 0
    


def menuPrincipal():
    n=0
    while(int(n) not in range(1,5)):
        print("1 - Nouveau Combat")
        print("2 - Pokédex ")
        print("3 - Ajouter Pokémon")
        print("4 - Quitter le jeu")
        n = input("Choisissez un chiffre pour le choix d'écran : ")

    match n:
        case "1":
            pokemonFight()
            menuPrincipal()
        case "2":
            pokedex()
            menuPrincipal()
        case "3":
            ajoutPokemon()
            menuPrincipal()
        case "4":
           pass
        case _:
            menuPrincipal()
            
        
    
menuPrincipal()