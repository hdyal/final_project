import random 
starting_health = 150
end_health = ""
minotaur = 35
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
    print("I will ask you one question if you get it rigth you may proceed un harmmed.")
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
        if sneak_away_damage >= 10:
            print("You got away without the monster seeing you")
        elif sneak_away_damage <= 10:
            print("You roll was not high enough the monster spotted you you lose 5 hp")
            starting_health -= 5
            print("Your health is {}".format(starting_health))
def escape():
    global starting_health
    print("If you roll anything higher than a 10 you escaped")
    print("Anything lower than a 10 the monster returned before you could escape")
    dice_input = input("Hit enter see what number you get: ")
    sneak_away_damage = random.randint(0,20)
    if dice_input == "":
        print("You rolled a {}".format(sneak_away_damage))
        if sneak_away_damage >= 10:
            print("You escaped before the monster returned ")
        elif sneak_away_damage <= 10:
            print("You did not escape before the monster returned")

#if end_health == 0:
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
    print("As you walk through the foggy forest with the morning sun shining through. You feel a cold")
    print("breeze brushing over you. You instinctively grab your cloak and pull it tighter around your ")
    print("body. As you walk further the fog clears and you stop and see a warm inviting inn offering ")
    print("safety and comfort in this cold morning. As you look beyond the cottage you see the path ")
    print("lead deeper into the forest offering mystery and adventure. What choice do you make?")
    print()

def forest():
    global starting_health
    user_input = int(input("To go into the cottage type 1, to go deeper into the forest type 2: \n"))
    if user_input == 1:
        print()
        print("As you walk up to the cottage door you hear the soft murmur of multiple conversations.")
        print("You open the door and find inside you see the people talking amongst the tables.")
        print("You find yourself an empty table and order yourself a drink as you sit there enjoying your drink you hear a low rumble outside.")
        print("You go and explore and outside the inn you see a Giant Bear coming towards the inn ready to attack. Do you attack or do you run?")
        print()
        choice1a = input("To engage the bear type attack or Attack, to run away type run or Run: ")
        if choice1a == "attack" or choice1a == "Attack":
            giant_bear_fight()
            if starting_health == 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                print()
            print("After the battle you stand over the corpse of the slayed monster. Weary from a long battle you stay the night at the inn.")
            print("When morning arrives you decide that it is time to move one as you move towards the door of the inn you are stopped by a mysterious figure in a cloak")
            print("The figure saw you fight the bear and was impressed and wanted to offer you a chance at a dangerous quest.")
            print("The figure tells of an evil warlock that lives in a tower in the woods.")
            print("The figure tells you that this warlock wants to destroy everybody and create his own kingdom of monsters. ")
            print("The figure says to get to the warlocks castle you have to go down the wooded path")
            print("Before you leave he hands you a boost that increases it by five points")
            starting_health += 5
            print("Your new health is {}\n".format(starting_health))
            print("While walking down the path you see a giant figure  in the distance. You are cautious as you approach.")
            print("You are surprised to see a sphinx in the middle of the path asleep.")
            print("Not wanting to wake the monster you try to go around it and find that both sides of the sphinx are deep crevasses.")
            print("You know that the sphinx like to can only attack its victims after it gets a riddle wrong.")
            sphinx_riddle()
            print("After you get past the sphinx you see that you have exited the forest and have entered a cave.")
            cave()
        elif choice1a == "run" or choice1a == "Run":
            sneak_away()
            if starting_health == 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
            print("You successfully flee from the attacking bear and continue down the path that headed into the woods.")
            print("After you successfully ran away from the bear and find yourself lost in the woods")
            print("As you wonder through the woods trying to find your way out you see a human figure in the distance.")
            print("You start to walk closer to it, you notice that that there is a pungent odor coming from the direction of the human figure.")
            print("When you get closer you notice that the human appears to have pig liek ears and tusks.")
            print("You then realize that that is not a normal human being but really a pigman.")
            print("Before you have a chance to think about running away he run towards you ready to fight\n")
            print()
            pigman_fight()
            if starting_health == 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
            print("Having defeated the pigman you continue down the path and find yourself at the entrance to a cave. ")
            cave()
    if user_input == 2:
        print("You decide to walk past the cottage and into the foggy woods you can feel the fog cover you like a clock hiding you from all prying eyes.")
        print("As you continue walking through the woods you hear something move through the branches near you.")
        print("You stop and look to see what is making the noise. You quickly move to hide behind a boulder close to you.")
        print("As the morning light shines through the fog you see that the monster is really a griffin.")
        print("The monster has not seen you yet and you are faced with two options: do you try to sneak away or do you stand your ground and fight.\n")
        choice2a = input("To fight type fight to sneak away type sneak(all lower case): ")
        if choice2a[0] == "f" or "F":
            griffin_fight()
            if starting_health == 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                print()
            print("After defeating the griffin you take a moment to gather yourself before you continue.")
            print("As you walk down the path you see a cave. Do you go into the cave or continue around")
            choice2b = input("To go into the cave type cave, to continue type path (All lower case): ")
            if choice2b == "cave" or choice2b == "Cave":
                cave()
            elif choice2b == "path" or choice2b == "Path":
                path()
        elif choice2a == "sneak" or choice2a == "Sneak":
            sneak_away()
            if starting_health == 0:
                print("You have died at the hands of the foreces of evil.")
                print("Because of your death the evil warlock was able to grow his monster army and take over all the land.")
                print()
            print("You have made it around the griffin and you find yourself at a junction.")
            print("One way leads into a cave and the other way you continue down the path.")
            choice2b = input("To go into the cave type cave, to continue type path (All lower case): ")
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
    user_input = input("To fight the bat type fight, to escape the bat type escape(all lower case): ")
    if user_input == "fight" or user_input == "Fight":
        bat_fight()
        print("After you have finished off the bat you walk pass its lifeless body you see a bright area up.")
        print("Do you explore the area ahead or do you turn around and exit the cave")
        user_input = input("to explore type explore to turn around type leave(all lower case)\n")
        if user_input[0] == "e" or user_input == "E":
            print("As you get closer to the lit area you realize that the light source is not fromm the sunn but multiple torches on the walls of the cave")
            print("As you look around you see a chest and animal skin on the ground making a bed for somthing big to sleep on")
            print("You take a look inside of the chest and dicover a huge health boost that will give you 20 hp")
            starting_health += 20
            print("Your new health is {}".format(starting_health))
            print("You begin to wonder what lives in here it had to be something big judging by the bed.")
            print("you decide to leave before whatever sleeps in that bed gets back")
            escape()
        elif user_input[0] == "l" or user_input[0] == "L":
            print()
    elif user_input == "run" or user_input == "Run":
        sneak_away()

def path():
    print()

main()
# talk to somebody about checking to make sure that the if statement about checking health after a fight will work.
#forest choice1a leads to cave
