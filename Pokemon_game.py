#importing stuff
import random

#create user class
class User(object):
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.attacking_pokemon = None

    #set_pokemon
    def set_pokemon(self, set_of_pokemon):
        self.pokemon = set_of_pokemon

    #list_pokemon
    def list_pokemon(self):
        count = 0 
        print(f"{self.name}'s pokemon are:")
        for pokemon in self.pokemon:
            print(f">>>>{self.pokemon[count]}") 
            count += 1

    #switch whenever you want
    def switch(self, pokemon_number):
        self.attacking_pokemon = self.pokemon[pokemon_number - 1]
        print(f"{self.name} has successfully set attacking pokemon to  {self.attacking_pokemon}.")


    def is_end_game(self):
        pass

    def print_attacks(self):
        pass

    def attack(self, attack_name, enemy):
        self.attacking_pokemon.attack(attack_name, enemy)


class Computer(User):
    def play_turn(self, enemy):
        pass

    def attack(self, enemy):
        pass

    def switch(self):
        pass
    

#create pokiemon class
class Pokemon(object):
  
    def __init__(self, hp, max_hp, max_ap, name):
        self.hp = hp
        self.max_hp= max_hp
        self.max_ap = max_ap
        self.name = name
        self.knocked_out = False
        self.attacks = self.set_attacks()
        self.pokemon_type = self.set_type()

    def set_type(self):
        return None

    def set_attacks(self):
        self.attacks = {}

    def get_attacks(self):
        return list(self.attacks.keys())

    def print_attacks(self):
        for attack in self.attacks:
            print(attack)

    def add_attacks(self, attack_dictionary):
        self.attacks = attack_dictionary

    def get_attack_power(self, attack, enemy):
        pass

    def attack(self, attack_name, enemy):
        print("~~~~~~~~~~~~")
        print(f"{self.name} uses {attack_name}")
        print("~~~~~~~~~~~~")
        attack_roll = random.randint (0,100)
        if  attack_roll < self.attacks[attack_name][1]:
            print ("the attack was successful")
            print()
            if self.attacks[attack_name][0] > self.max_ap:
                attack_min = self.max_ap - 20
                attack_max = self.max_ap
                
                damage = random.randint(attack_min, attack_max)

            else:
                attack_min = self.attacks[attack_name][0] - 20
                attack_max = self.attacks[attack_name][0]

                damage = random.randint(attack_min, attack_max)
            print(f"{self.name} deals {damage} to the defending pokemon!")
            enemy.take_damage(damage)
            
        else: 
            print ("the attack was not successful")
            

    def take_damage(self, damage_amount):
        print(f"the defending {self.name}'s hp before the attack was {self.hp}")
        self.hp -= damage_amount
        if self.hp <= 0:
            self.hp = 0
            self.knocked_out = True 
            print("the defending pokemon has been knocked out")
            print()
        else:
            print(f"the defending {self.name} now has: {self.hp} health!")
            print()

    def heal(self):
        if self.hp + 30 >= self.max_hp:
            print(f"{self.name}'s hp was already max")
        else:
            self.hp +=30
            print(f"{self.name}'s hp is now {self.hp}")
        

#create grass class
class GrassType(Pokemon):
    def set_type(self):
        return 'grass'

    #Grass type attack dictionary
    def set_attacks(self):
        return {"leaf Storm": [130,90],"Mega Drain":[50,100],"Razer Leaf":[55,95]}

    def get_attack_power(self, attack, enemy):
        pass

    def __str__ (self):
        return f"{self.name} TYPE: GRASS HP:{self.hp} AP:{self.max_ap}"

#create water class
class WaterType(Pokemon):
    def set_type(self):
        return 'water'

    #water class attack dictionary
    def set_attacks(self):
        return {"Bubble":[40,100], "Hydro Pump": [185,30],"surf":[70,90]}

    def get_attack_power(self, attack, enemy):
        pass

    def __str__ (self):
        return f"{self.name} TYPE: WATER HP:{self.hp} AP:{self.max_ap}"

#create fire class
class FireType(Pokemon):
    def set_type(self):
        return 'fire'

    #fire type class attack dictionary
    def set_attacks(self):
        return {"Fireball":[50,25],"Fire Punch":[85,80], "Ember": [60,100]}

    def get_attack_power(self, attack, enemy):
        pass

    def __str__ (self):
        return f"{self.name} TYPE: FIRE HP:{self.hp} AP:{self.max_ap}"

#create list of available pokemon
def game_loop():
    pokemon_list = [
        GrassType(60,60, 50, 'Bulbasoar'),
        GrassType(40,40, 70, 'Bellsprout'),
        GrassType(50,50, 60, 'Oddish'),
        FireType(40,40, 70, 'Charmander'),
        FireType(30,30, 50, 'Ninetails'),
        FireType(40,40, 60, 'Ponyta'),
        WaterType(80,80, 20, 'Squirtle'),
        WaterType(70,70, 40, 'Psyduck'),
        WaterType(100,100, 50, 'Polywag')]

#kindly welcome the user
    print("<welcome to game!!!>")
    print()

# create user lol

    user_name = input("what do you want your name to be? >  ")
    player = User(user_name)
    print(f"hello {player.name}")

#user picks pokemon
    print("pokemon available:")
    num = 1
    for pokemon in pokemon_list:
        print(f"--------{num}. {pokemon}")
        num += 1

    print()
    user_choices = []
    num_choices = []
    choices = ["First", "Second", "Third"]
    for i in range(3):
        while True:
            choice = int(input(f"choose your {choices[i]} pokeman >  "))
            if choice not in num_choices:
                user_choices.append(pokemon_list[choice-1])
                num_choices.append(choice)
                break
            else:
                print("You already chose that, you idiot!")
                
    


    #populate user pokeon list
    player.set_pokemon(user_choices)
    print()
    print("your pokemon are:")

    #print the list
    print(f"1.>>>>{player.pokemon[0].name}") 
    print(f"2.>>>>{player.pokemon[1].name}") 
    print(f"3.>>>>{player.pokemon[2].name}") 

    #create opponent
    enemy_name = input("What do you want your nemesis stinky stinky name to be? >  ")
    enemy = Computer(enemy_name)
    print(f"you have been challenged by ++ {enemy.name} ++")

    print()
    #assign enemy pokes 
    cpu_choices = []
    max = 8
    for i in range (3):
        cpu_randomint = random.randint(0,max)
        cpu_choices.append(pokemon_list[cpu_randomint])
        pokemon_list.remove(pokemon_list[cpu_randomint]) 
        max -= 1

    #print the enemy pokemon
    enemy.set_pokemon(cpu_choices)
    print()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()

    player.list_pokemon()
    print()
    enemy.list_pokemon()


    #set your attacking pokemon
    pick_attacking_pokemon = int(input("Which pokemon do you wanna fight with, please type a number"))
    player.switch(pick_attacking_pokemon)
    
    #set enemy attacker
    cpu_random_pokemon = random.randint(0,2)
    enemy_attacker = cpu_choices[cpu_random_pokemon]
    print(f'your oppenent has chosen {enemy_attacker}')

    #game loop
    game_over = False
    Turn_order = True
    while game_over == False:
        
        #checks the enemy list to see if you have won
        if len(cpu_choices) == 0:
                print("all of the enemys pokeon are knocked out, you win!!!!!")
                game_over = True
       
        print("---------------------------------------")
        if player.attacking_pokemon.hp == 0 and len(user_choices) >0:
            user_choices.remove(player.attacking_pokemon)
            #checks the enemy list to see if you have lost
            if len(user_choices) == 0:
                print(" all your pokemon are dead you have lost and got all your pokemon killed you should feel bad")
                game_over= True
            if game_over == False:
                print("your pokemon has been knocked out")
                print()
                player.list_pokemon()
                pick_attacking_pokemon = int(input("Which pokemon do you wanna fight with, please type a number"))
                player.switch(pick_attacking_pokemon)
                print(player.attacking_pokemon)
            
        else:
            pass
            
        
        #printing move options
        player.print_attacks
        print("1. Attack")
        print("2. Heal")
        print("3. Switch")
        print("4. list pokemon")
        print("5. Quit")
        
        #sets your turn
        if Turn_order== True:

            choice_user_pick = int(input("Which number do you want to do?"))
            #attacking
            if choice_user_pick == 1 and player.attacking_pokemon.hp > 0: #attack
                 #attacking, defending and knock out-ing?
                num = 1
                for attack in player.attacking_pokemon.set_attacks():
                    print(f"{num}: {attack}")
                    num += 1


                attack_choice = int(input(f"{player.name}, choose an attack"))

                player.attacking_pokemon.get_attacks()
            
                chosen_attack = list(player.attacking_pokemon.attacks)[attack_choice - 1]
                print(f"your pokeomin used{list(player.attacking_pokemon.attacks)[attack_choice - 1]}")
                #choose an attack name
                player.attack(chosen_attack, enemy_attacker)
                #breaks up text
                end_turn = input("your turn is over, press enter to continue  ")
                if end_turn == '':
                    Turn_order = False
                else:
                    Turn_order = False 

            #heal
            if choice_user_pick == 2 and player.attacking_pokemon.hp > 0:
                Pokemon.heal(player.attacking_pokemon)
                #breaks up text
                end_turn = input("your turn is over, press enter to continue  ")
                if end_turn == '':
                    Turn_order = False
                else:
                    Turn_order = False 

            #switch
            if choice_user_pick == 3 and player.attacking_pokemon.hp > 0: 
                player.list_pokemon()
                pick_attacking_pokemon = int(input("Which pokemon do you wanna fight with, please type a number"))
                player.switch(pick_attacking_pokemon)
                print (player.attacking_pokemon)
                #breaks up text
                end_turn = input("your turn is over, press enter to continue  ")
                if end_turn == '':
                    Turn_order = False
                else:
                    Turn_order = False 
            
            #lists your pokemon
            if choice_user_pick == 4:
                player.list_pokemon()
                print("~~~~~~~~~~~~~~~~")
                Turn_order = True

            #ends the game
            if choice_user_pick == 5:
                game_over = True
            
        #enemy's turn
        if Turn_order == False:
            print()
            print("its your oppenents turn now")
            print()
            
                        
            if game_over == False:
                if enemy_attacker.hp <= 0 : #enemy pokeon dead now he switch
                    #removes the dead pokemon from the list 
                    cpu_choices.remove(enemy_attacker)
                    #checks to see if you have won
                    if len(cpu_choices) == 0:
                        print("all of the enemys pokeon are knocked out, you win!!!!!")
                        game_over = True
                    #if you havent won then it will swap pokemon
                    if game_over == False:
                        #enemy select the new pokemon
                        enemy_attacker = cpu_choices[0]
                        print(f"the enemys pokeon died now he is using {enemy_attacker} ")
                #enemy attacks
                cpu_attack_choice = random.randint(0,2)
                chosen_attack= list(enemy_attacker.attacks)[cpu_attack_choice - 1]
                        
                
                enemy_attacker.attack(chosen_attack, player.attacking_pokemon )
                #breaks up the text
                end_turn = input("your enemy's turn is over, press enter to continue: ")
                if end_turn == '':
                    Turn_order = True
                
        

game_loop()