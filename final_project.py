import random 
from pygame import mixer 
starting_health = 150 
end_health = ""
minotaur = 35 # used
giant_bat = 15 # used
griffin = 25 # used
sphinx = 40 # used
giant_bear = 20 # used 
pigman = 25 # used
evil_Warlock = 100
end_monster_health = ""
# damage from being seen while senaking away is 5 hp 
# create a damage_dealt function for each monster
# the damage dealt is a function to be used to calculate how much damage you dealt to the minotaur

def minotaur_fight(): # add if statement after a fight to see if the player is dead
    end_monster_health = minotaur
    global starting_health
    while True:
        dice_input = input("To determine your damage dealt and the damage taken hit enter ")
        if dice_input == "":
            damage_dealt_roll = random.randint(0,15)
            damage_taken_roll = random.randint(0,15)
            print("The damage you have dealt is {}".format(damage_dealt_roll))
            print("The damage you have taken is {}".format(damage_taken_roll))
            end_monster_health -= damage_dealt_roll
            print("the monster health is {}\n".format(end_monster_health))
            starting_health -= damage_taken_roll
            print("Your health is {}".format(starting_health))
        if starting_health <= 0:
            print("You have died at the hands of the foreces of evil.")
            break 
        elif end_monster_health <= 0:
            print("You killed the minotaur, Your health is {}\n".format(starting_health))
            break

def griffin_fight():
    end_monster_health = griffin
    global starting_health
    while True:
        dice_input = input("To determine your damage dealt and the damage taken hit enter ")
        if dice_input == "":
            damage_dealt_roll = random.randint(0,15)
            damage_taken_roll = random.randint(0,10)
            print("The damage you have dealt is {}".format(damage_dealt_roll))
            print("The damage you have taken is {}".format(damage_taken_roll))
            end_monster_health -= damage_dealt_roll
            print("the monster health is {}\n".format(end_monster_health))
            starting_health -= damage_taken_roll
            print("Your health is {}".format(starting_health))
        if starting_health <= 0:
            print("You have died at the hands of the foreces of evil.") 
            break
        elif end_monster_health <= 0:
            print("You killed the grffin, Your health is {}\n".format(starting_health))
            break

def sphinx_riddle(): 
    global starting_health
    print("I do not battle like the other monsters I prefer a battle of wits.")
    print("I will ask you one question if you get it right you may proceed un harmmed.")
    print("But if you get it wrong you will lose 10 health points")
    print()
    print("Here is the riddle")
    print("What’s the capital in France? ")
    user_input = input("Enter your anwser in all lower case: ")
    if user_input == "f" or user_input == "F":
        print("Congratulations you have given the right answer you may proceed")
        print("Before you go take this health boost")
        starting_health += 10
        print("Your current health is {}\n".format(starting_health))
    if user_input != "f" or user_input == "F":
        print("you have given the wrong answer")
        starting_health -= 10
        print("Your current health is {}\n".format(starting_health))

def giant_bear_fight():
    end_monster_health = giant_bear
    global starting_health
    while True:
        dice_input = input("To determine your damage dealt and the damage taken hit enter ")
        if dice_input == "":
            damage_dealt_roll = random.randint(0,15)
            damage_taken_roll = random.randint(0,10)
            print("The damage you have dealt is {}".format(damage_dealt_roll))
            print("The damage you have taken is {}".format(damage_taken_roll))
            end_monster_health -= damage_dealt_roll
            print("the giant bear's health is {}\n".format(end_monster_health))
            starting_health -= damage_taken_roll
            print("Your health is {}".format(starting_health))
        if starting_health <= 0:
            print("You have died at the hands of the foreces of evil.") 
            break
        elif end_monster_health <= 0:
            print("You killed the bear, Your health is {}\n".format(starting_health))
            break

def pigman_fight():
    end_monster_helath = pigman
    global starting_health
    while True:
        dice_input = input("To determine your damage dealt and the damage taken hit enter ")
        if dice_input == "":
            damage_dealt_roll = random.randint(0,15)
            damage_taken_roll = random.randint(0,10)
            print("The damage you have dealt is {}".format(damage_dealt_roll))
            print("The damage you have taken is {}\n".format(damage_taken_roll))
            end_monster_helath -= damage_dealt_roll
            print("The pigman's health is {}".format(end_monster_helath))
            starting_health -= damage_taken_roll
            print("Your health is {}".format(starting_health))
        if starting_health <= 0:
            print("You have died at the hands of the foreces of evil.") 
            break
        elif end_monster_helath <= 0:
            print("After defeating the pigman you notince that he is carrying a pouch you decide to go through it")
            print("inside you find a health boost that increases your health by 10 hp")
            starting_health += 10
            print("You killed the pigman, Your health is {}\n".format(starting_health))
            break

def bat_fight():
    end_monster_helath = giant_bat
    global starting_health
    while True:
        dice_input = input("To determine your damage dealt and the damage taken hit enter ")
        if dice_input == "":
            damage_dealt_roll = random.randint(0,15)
            damage_taken_roll = random.randint(0,10)
            print("The damage you have dealt is {}".format(damage_dealt_roll))
            print("The damage you have taken is {}\n".format(damage_taken_roll))
            end_monster_helath -= damage_dealt_roll
            print("The bat's health is {}".format(end_monster_helath))
            starting_health -= damage_taken_roll
            print("Your health is {}".format(starting_health))
        if starting_health <= 0:
            print("You have died at the hands of the foreces of evil.")
            break 
        elif end_monster_helath <= 0:
            print("You have defeated the giant bat ")
            break

def warlock_final_fight():
    end_monster_health = evil_Warlock
    global starting_health
    while True:
        dice_input = input("To determine your damage dealt and the damage taken hit enter ")
        if dice_input == "":
            damage_dealt_roll = random.randint(0,15)
            damage_taken_roll = random.randint(0,15)
            print("The damage you have dealt is {}".format(damage_dealt_roll))
            print("The damage you have taken is {}".format(damage_taken_roll))
            end_monster_health -= damage_dealt_roll
            print("the warlocks health is {}\n".format(end_monster_health))
            starting_health -= damage_taken_roll
            print("Your health is {}".format(starting_health))
        if starting_health <= 0:
            print("You have died at the hands of the foreces of evil.")
            break    
        elif end_monster_health <= 0:
            print("You killed the evil warlock, Your health is {}\n".format(starting_health))
            break

def sneak_away():
    global starting_health
    print("If you roll anything higher than a 10 you get away with no damage")
    print("Anything lower than a 10 you recive 5 damage")
    dice_input = input("Hit enter see what number you get: ")
    sneak_away_damage = random.randint(0,20)
    if dice_input == "":
        print("You rolled a {}".format(sneak_away_damage))
        if sneak_away_damage <= 10:
            print("You got away without the monster seeing you")
        elif sneak_away_damage <= 10:
            print("You roll was not high enough to escape, you lose 5 hp")
            starting_health -= 5
            print("Your health is {}".format(starting_health))

#if end_health <= 0:
            #print("You have died at the hands of the foreces of evil.")
            #print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
 
#The damage taken function is used to calculate the amount of damage you recive while in battle 
    # How do I stop this loop when you beat the monster
#The GreAt JouRney
print()
print("[][][][][][] []       [][][][][]     [][][][][]     [][][]     [][][][][]        []       []       []   [][][]   []    []  [][][]      [][][]   [][][][][]   []         []")
print("     []      []      []        []   []             []      [] []         []     [][]      []       [] []      [] []    [] []     []   []    [] []        []   []       []")
print("     []      []       [][][][][]   []              []          [][][][][][]    []  []  [][][][]    [] []      [] []    [] []      []  []    []  [][][][][]     []     []")
print("     []      [][][][]   []         []    [][][][]  []           []            [][][][]    []       [] []      [] []    [] [][][][][]  []    []   []             []   []")
print("     []      []    []    []        []          []  []            []          []      []   []       [] []      [] []    [] []     []   []    []    []              [][]")
print("     []      []    []     []       []          []  []             []        []        []  []  []   [] []      [] []    [] []      []  []    []     []              []")
print("     []      []    []      [][][]   [][][][][][]   []              [][][]  []          [] []     []    [][][][]   [][][]  []       [] []    []      [][][]        []")
print()
#The great journey is a choose your own adventure game. You start off by seeing the game tite then read the story as it apperas which will change depending on what decsion you decide to make 
# to call any function put the functions name and then paratheseis example damage_dealt()
def main():
    mixer.init()
    filename = "final-music.mp3"
    mixer.music.load(filename)
    mixer.music.play(loops=-1)
    forest()
    cave()
    path()
def forest():
    global starting_health
    print("As you walk through the foggy forest with the morning sun shining through. You feel a cold")
    print("breeze brushing over you. You instinctively grab your cloak and pull it tighter around your ")
    print("body. As you walk further the fog clears and you stop and see a warm inviting inn offering ")
    print("safety and comfort in this cold morning. As you look beyond the cottage you see the path ")
    print("lead deeper into the forest offering mystery and adventure. What choice do you make?")
    print()
    while True:
        user_input = int(input("To go into the cottage type 1, to go deeper into the forest type 2: "))
        if user_input == 1 or user_input == 2:
            break
    if user_input == 1:
        print()
        print("As you walk up to the cottage door you hear the soft murmur of multiple conversations.")
        print("You open the door and find inside you see the people talking amongst the tables.")
        print("You find yourself an empty table and order yourself a drink as you sit there enjoying your drink you hear a low rumble outside.")
        print("You go and explore and outside the inn you see a Giant Bear coming towards the inn ready to attack. Do you attack or do you run?")
        print()
        while True:
            choice1a = input("To engage the bear type attack or Attack, to run away type run or Run: ")
            if choice1a == "attack" or choice1a == "Attack" or choice1a == "run" or choice1a == "Run": 
                break
        if choice1a == "attack" or choice1a == "Attack":
            giant_bear_fight()
            if starting_health <= 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                raise SystemExit
            print("After the battle you stand over the corpse of the slayed monster. Weary from a long battle you stay the night at the inn.")
            print("When morning arrives you decide that it is time to move one as you move towards the door of the inn you are stopped by a mysterious figure in a cloak")
            print("The figure saw you fight the bear and was impressed and wanted to offer you a chance at a dangerous quest.")
            print("The figure tells of an evil warlock that lives in a tower in the woods.")
            print("The figure tells you that this warlock wants to destroy everybody and create his own kingdom of monsters. ")
            print("The figure says to get to the warlocks castle you have to go down the wooded path")
            print("Before you leave he hands you a boost that increases it by five points\n")
            starting_health += 5
            print("Your new health is {}\n".format(starting_health))
            print("While walking down the path you see a giant figure  in the distance. You are cautious as you approach.")
            print("You are surprised to see a sphinx in the middle of the path asleep.")
            print("Not wanting to wake the monster you try to go around it and find that both sides of the sphinx are deep crevasses.")
            print("You know that the sphinx like to can only attack its victims after it gets a riddle wrong.")
            sphinx_riddle()
            if starting_health <= 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                raise SystemExit
            print("After you get past the sphinx you see that you have exited the forest and have entered a cave.")
            cave()
        elif choice1a == "run" or choice1a == "Run":
            sneak_away()
            if starting_health <= 0:
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                raise SystemExit
            print("You successfully flee from the attacking bear and continue down the path that headed into the woods.")
            print("After you successfully ran away from the bear and find yourself lost in the woods")
            print("As you wonder through the woods trying to find your way out you see a human figure in the distance.")
            print("You start to walk closer to it, you notice that that there is a pungent odor coming from the direction of the human figure.")
            print("When you get closer you notice that the human appears to have pig like ears and tusks.")
            print("You then realize that that is not a normal human being but really a pigman.")
            print("Before you have a chance to think about running away he run towards you ready to fight\n")
            print()
            pigman_fight()
            if starting_health <= 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                raise SystemExit
            print("Having defeated the pigman you continue down the path and find yourself at the entrance to a cave. ")
            cave()
    if user_input == 2:
        print("You decide to walk past the cottage and into the foggy woods you can feel the fog cover you like a clock hiding you from all prying eyes.")
        print("As you continue walking through the woods you hear something move through the branches near you.")
        print("You stop and look to see what is making the noise. You quickly move to hide behind a boulder close to you.")
        print("As the morning light shines through the fog you see that the monster is really a griffin.")
        print("The monster has not seen you yet and you are faced with two options: do you try to sneak away or do you stand your ground and fight.")
        while True:
            choice2a = input("To fight type fight to sneak away type sneak(all lower case): ")
            if choice2a == "fight" or choice2a == "Fight" or choice2a == "sneak" or choice2a == "Sneak":
                break
        if choice2a == "fight" or choice2a == "Fight":
            griffin_fight()
            if starting_health <= 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                raise SystemExit
            print("After defeating the griffin you take a moment to gather yourself before you continue.")
            print("As you walk down the path you see a cave. Do you go into the cave or continue around\n")
            while True:
                choice2b = input("To go into the cave type cave, to continue type path (All lower case): ")
                if choice2b == "cave" or choice2b == "Cave" or choice2b == "path" or choice2b == "Path":
                    break
            if choice2b == "cave" or choice2b == "Cave":
                cave()
            elif choice2b == "path" or choice2b == "Path":
                path()
        elif choice2a == "sneak" or choice2a == "Sneak":
            sneak_away()
            if starting_health <= 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                raise SystemExit
            print("You have made it around the griffin and you find yourself at a junction.")
            print("One way leads into a cave and the other way you continue down the path.")
            while True:
                choice2b = input("To go in type cave, to continue type path (All lower case): ")
                if choice2b == "cave" or choice2b == "Cave" or choice2b == "path" or choice2b == "Path":
                    break
            if choice2b == "cave" or choice2b =="Cave":
                cave()
            elif choice2b == "path" or choice2b == "Path":
                path()
            
def cave():
    global starting_health
    print("As you enter the cave you can hear the sound of water dripping off the stalactite and the sound of your footsteps echoing off the wall")
    print("While you walk deeper into the cave your only ligth source is small holes and cracks that lead to the surface")
    print("You then notice the sound of wings flapping in the darkness ahead of you. You continue to move forward ready to fight or run.")
    print("The sound of the flapping gets louder as you move closer to the source, you see through a crack in the wall that you are face to face witha giant bat.")
    print("Do you fight the bat or do try to run pass the bat\n")
    while True:
        user_input = input("To fight the bat type fight, to escape the bat type run(all lower case): ")
        if user_input == "fight" or user_input == "Fight" or user_input == "run" or user_input == "Run":
            break
    if user_input == "fight" or user_input == "Fight":
        bat_fight()
        if starting_health <= 0:
            print("You have died at the hands of the foreces of evil.")
            print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
            raise SystemExit
        print("After you have finished off the bat you walk pass its lifeless body you see a bright area up.")
        print("Do you explore the area ahead or do you turn around and exit the cave")
        while True:
            user_input = input("to explore type explore to turn around type leave(all lower case): ")
            if user_input == "explore" or user_input == "Explore" or user_input == "leave" or user_input == "Leave":
                break
        if user_input == "explore" or user_input == "Explore":
            print("As you get closer to the lit area you realize that the light source is not fromm the sunn but multiple torches on the walls of the cave")
            print("As you look around you see a chest and animal skin on the ground making a bed for somthing big to sleep on")
            print("You take a look inside of the chest and dicover a huge health boost that will give you 20 hp")
            starting_health += 20
            print("Your new health is {}\n".format(starting_health))
            print("You begin to wonder what lives in here it had to be something big judging by the bed.")
            print("you decide to leave before whatever sleeps in that bed gets back")
            print("while on the way out of the cave you start to hear the loud foot prints of something coming towrds you.")
            print("You were not able to leave before the monster comes back, you prepare yourself for battle because you have no other choice")
            minotaur_fight()
            if starting_health <= 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                raise SystemExit
            print("After defeating the minotaur you exit the cave and head along the path")
            path()
        elif user_input == "leave" or user_input == "Leave":
            print("You were able to leave the cave and you continued down the path")
            path()
    elif user_input == "run" or user_input == "Run":
        sneak_away()
        if starting_health <= 0:
            print("You have died at the hands of the foreces of evil.")
            print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
            raise SystemExit
        print()
        print("You were able to run away form the giant bat and you started to follow the path")
        path()
def path():
    global starting_health
    print("As you walk down the path down the path you start to see a what looks like a castle in the distance.")
    print("intrigued by the sudden apperance of a castle this far into the woods you decide to investagate.")
    print("When you get close enough to the entrance of the castle you notice that a giant minotaur is guarding.")
    print("You become suspicous becuase no human castle uses monsters as guards.")
    print("You then remember hearing that a evil warlock uses's monsters in his army")
    print("Do you fight the giant or try to sneak inside.")
    while True:
        user_input = input("To fight type battle, to sneak type sneak (all lower case): ")
        if user_input == "battle" or user_input == "sneak":
            break
    if user_input == "battle":
        minotaur_fight()
        if starting_health <= 0:
            print("You have died to the to the army  of evil and the land was lost to darkness")
            raise SystemExit
        print("Having defeated the minotaur you proceed into the castle and start to look around")
        print("You come to a door do you enter or continue to look around? ")
        while True:
            choice1a = input("Type yes to enter, type no to explore somewhere else (all lowercase): ")
            if choice1a == "yes" or choice1a == "no":
                break
        if choice1a == "yes" or choice1a == "Yes": # add no if statement 
            print("You go inside and see that there is a huge pot sitting over a fire with a mysterious liquid boiling inside.")
            print("You then see a shelf and on the shelf ther are two bottled potions one is a health boost and the other is a poison that hurts you.")
            print("You consider taking both but the bottles are to big to carry and you also hear loud noise coming from the hallway.")
            print("You have to decide quickly which potion to drink")
            while True:
                choice1b = input("type 1 or type 2: ")
                if choice1b == "1" or choice1b == "2":
                    break  
            if choice1b == "1":
                print("you pick up the potion and drink the contents of the bottle.")
                print("You then feel a surge of pain you then realize that you drank the posion")
                starting_health -= 8
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to darkness")
                    raise SystemExit
                print("Your current health is {}".format(starting_health))
            elif choice1b == "2" or choice1b == "two" or choice1b == "Two":
                print("you pick up the potion and drink the contents of the bottle.")
                print("You then feel a surge of strength because you drank the health boost")
                starting_health += 8
                print("Your current health is {}".format(starting_health))
            print("After drinking the potion you exit the room and you see the source of the thumping ")
            print("At the end of the hall you see the giant bear.")
            print("You see on the other side of the hall is a staircase leading up.")
            print("Do you attack the bear or do you try to sneak pass\n")
            while True:
                user_input = input("To fight type fight, To sneak type sneak (all lowercase): ")
                if user_input == "fight" or user_input == "sneak":
                    break
            if user_input == "fight":  
                giant_bear_fight()
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to darkness")
                    raise SystemExit
                print("You beat the bear and traval up the stairs and find your self at the entrance a a throne room you gather your courage and enter.")
                print("As you enter the throne room you see a man sitting at the other end of the room.")
                print("He sees you and say's how dare you enter my castle destroys my monster guards and mess with my potion room.")
                print("For what you have done you shall die. He shots a fireball you were just able to dodge it at the last minute.")
                print("You quickly down a health potion you have been saving for emergencys.")
                starting_health += 25
                print("Your new health is {}".format(starting_health))
                warlock_final_fight()
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to the evil warlock:")
                    print("He was able to destroy all humans and tranform the land to be populated with nothing but monsters")
                    raise SystemExit
                print("CONGRATS") 
                print("You were able to get vanquish the land of the evil warlock and all his monsters")
                print("The humans now expand their terrritory with no fear of the monsters")
            elif user_input == "sneak":
                sneak_away()
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to the evil warlock:")
                    print("He was able to destroy all humans and tranform the land to be populated with nothing but monsters")
                print("You traval up the stairs and find your self at the entrance a a throne room you gather your courage and enter.")
                print("As you enter the throne room you see a man sitting at the other end of the room.")
                print("He sees you and say's how dare you enter my castle destroys my monster guards and mess with my potion room.")
                print("For what you have done you shall die. He shots a fireball you were just able to dodge it at the last minute.")
                print("You quickly down a health potion you have been saving for emergencys.")
                starting_health += 20
                print("Your new health is {}".format(starting_health))
                warlock_final_fight()
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to the evil warlock:")
                    print("He was able to destroy all humans and tranform the land to be populated with nothing but monsters")
                    raise SystemExit
                print("CONGRATS") 
                print("You were able to get vanquish the land of the evil warlock and all his monsters")
                print("The humans now expand their terrritory with no fear of the monsters")
                raise SystemExit
        elif choice1a == "no":
            print("You decide that your time would be better off searching the rest of the castle.")
            print("As you walk through the hall you start to head in the direction of a staircase when a ginat bear gets in front of you.")
            giant_bear_fight()
            if starting_health <= 0:
                print("You have died to the to the army  of evil and the land was lost to darkness")
                raise SystemExit
            print("You amde it pass the bear and come face to face with a giant throne room door you gather your courage and enter.")
            print("As you enter the throne room you see a man sitting at the other end of the room.")
            print("He sees you and say's how dare you enter my castle destroys my monster guards and mess with my potion room.")
            print("For what you have done you shall die. He shots a fireball you were just able to dodge it at the last minute.")
            print("You quickly down a health potion you have been saving for emergencys.")
            starting_health += 20
            print("Your new health is {}".format(starting_health))
            warlock_final_fight()
            if starting_health <= 0:
                print("You have died to the army of evil and the land was lost to the evil warlock:")
                print("He was able to destroy all humans and tranform the land to be populated with nothing but monsters")
                raise SystemExit
            print("CONGRATS") 
            print("You were able to get vanquish the land of the evil warlock and all his monsters")
            print("The humans now expand their terrritory with no fear of the monsters")
            raise SystemExit
    elif user_input == "sneak":
        sneak_away()
        if starting_health <= 0:
            print("You have died to the to the army  of evil and the land was lost to darkness")
            raise SystemExit
        print("After making it pass the guard you decide to look around")
        print("You come to a door do you enter or continue to look around? ")
        while True:
            choice1a = input("Type yes to enter, type no to explore somewhere else (all lowercase): ")
            if choice1a == "yes" or choice1a == "no":
                break
        if choice1a == "yes" or choice1a == "Yes": # add no if statement 
            print("You go inside and see that there is a huge pot sitting over a fire with a mysterious liquid boiling inside.")
            print("You then see a shelf and on the shelf ther are two bottled potions one is a health boost and the other is a poison that hurts you.")
            print("You consider taking both but the bottles are to big to carry and you also hear loud noise coming from the hallway.")
            print("You have to decide quickly which potion to drink")
            while True:
                choice1b = input("type 1 or type 2: ")
                if choice1b == "1" or choice1b == "2":
                    break  
            if choice1b == "1":
                print("you pick up the potion and drink the contents of the bottle.")
                print("You then feel a surge of pain you then realize that you drank the posion")
                starting_health -= 8
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to darkness")
                    raise SystemExit
                print("Your current health is {}".format(starting_health))
            elif choice1b == "2" or choice1b == "two" or choice1b == "Two":
                print("you pick up the potion and drink the contents of the bottle.")
                print("You then feel a surge of strength because you drank the health boost")
                starting_health += 8
                print("Your current health is {}".format(starting_health))
            print("After drinking the potion you exit the room and you see the source of the thumping ")
            print("At the end of the hall you see the giant bear.")
            print("You see on the other side of the halll is a staircase leading up.")
            print("Do you attack the bear or do you try to sneak pass\n")
            while True:
                user_input = input("To fight type fight, To sneak type sneak (all lowercase): ")
                if user_input == "fight" or user_input == "sneak":
                    break
            if user_input == "fight":  
                giant_bear_fight()
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to darkness")
                    raise SystemExit
                print("You beat the bear and traval up the stairs and find your self at the entrance a a throne room you gather your courage and enter.")
                print("As you enter the throne room you see a man sitting at the other end of the room.")
                print("He sees you and say's how dare you enter my castle destroys my monster guards and mess with my potion room.")
                print("For what you have done you shall die. He shots a fireball you were just able to dodge it at the last minute.")
                print("You quickly down a health potion you have been saving for emergencys.")
                starting_health += 25
                print("Your new health is {}".format(starting_health))
                warlock_final_fight()
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to the evil warlock:")
                    print("He was able to destroy all humans and tranform the land to be populated with nothing but monsters")
                    raise SystemExit
                print("CONGRATS") 
                print("You were able to get vanquish the land of the evil warlock and all his monsters")
                print("The humans now expand their terrritory with no fear of the monsters")
            elif user_input == "sneak":
                sneak_away()
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to the evil warlock:")
                    print("He was able to destroy all humans and tranform the land to be populated with nothing but monsters")
                print("You traval up the stairs and find your self at the entrance a a throne room you gather your courage and enter.")
                print("As you enter the throne room you see a man sitting at the other end of the room.")
                print("He sees you and say's how dare you enter my castle destroys my monster guards and mess with my potion room.")
                print("For what you have done you shall die. He shots a fireball you were just able to dodge it at the last minute.")
                print("You quickly down a health potion you have been saving for emergencys.")
                starting_health += 20
                print("Your new health is {}".format(starting_health))
                warlock_final_fight()
                if starting_health <= 0:
                    print("You have died to the to the army  of evil and the land was lost to the evil warlock:")
                    print("He was able to destroy all humans and tranform the land to be populated with nothing but monsters")
                    raise SystemExit
                print("CONGRATS") 
                print("You were able to get vanquish the land of the evil warlock and all his monsters")
                print("The humans now expand their terrritory with no fear of the monsters")
        elif choice1a == "no":
            print("You decide that your time would be better off searching the rest of the castle.")
            print("As you walk through the hall you start to head in the direction of a staircase when a ginat bear gets in front of you.")
            giant_bear_fight()
            if starting_health <= 0:
                print("You have died to the to the army  of evil and the land was lost to darkness")
                raise SystemExit
            print("You amde it pass the bear and come face to face with a giant throne room door you gather your courage and enter.")
            print("As you enter the throne room you see a man sitting at the other end of the room.")
            print("He sees you and say's how dare you enter my castle destroys my monster guards and mess with my potion room.")
            print("For what you have done you shall die. He shots a fireball you were just able to dodge it at the last minute.")
            print("You quickly down a health potion you have been saving for emergencys.")
            starting_health += 20
            print("Your new health is {}".format(starting_health))
            warlock_final_fight()
            if starting_health <= 0:
                print("You have died to the to the army  of evil and the land was lost to the evil warlock:")
                print("He was able to destroy all humans and tranform the land to be populated with nothing but monsters")
                raise SystemExit
            print("CONGRATS") 
            print("You were able to get vanquish the land of the evil warlock and all his monsters")
            print("The humans now expand their terrritory with no fear of the monsters") 
            raise SystemExit 
if __name__ == "__main__":    
    main()

# talk to somebody about checking to make sure that the if statement about checking health after a fight will work.
#forest choice1a leads to cave