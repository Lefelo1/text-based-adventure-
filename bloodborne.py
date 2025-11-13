import os 
import time
score = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(seconds):
    time.sleep(seconds)

def clinic():
    clear_screen()
    print(""" 
----------------------------------
🩸Bloodborne text based adventure🐺
----------------------------------
""")
    
    pause(5)
    clear_screen()
    print("""
You wake up straped to a bed staring at a bundle of needles.
As you start trying to break free the needles come down upon you.
Little creatures start crawling on you as you lie there helpless,
passing out slowly. You awaken in the Hunter's Dream, find a way 
to leave before you are gone forever...
""")
    pause(7)
    clear_screen()
    print("You wake up next to the door of a clinic and as you walk \nout you see an abnormally large wolf feasting on a corpse.")
    
    choice = input("\nDo you 'face' the the wolf or do you 'pass' the wolf? ").lower()
    
    if choice == "face":
        hunters_dream()
    
    elif choice == "pass":
        central_yharnam()
    
    else:
        print("invalid choice")
        clinic()
        

def hunters_dream():
    clear_screen()
    print("""
As you approach the wolf it's attention snaps to you.
The beast was savage and had a face that made you think
that you had already died and this is hell. as you study
the beast it leaps at you and you become it's next meal.
""")
    pause(13)
    clear_screen()
    print(" YOU DIED")
    pause(9)
    clear_screen()
    
    print(""" 
-----------------
💤Hunter's Dream💤
-----------------
    """)
    pause(5)
    clear_screen()
    print("""
You wake up on the ground of a graveyard next to a 
lady who looks... like a doll? who is wheeling an 
old man in a wheel chair. The old man greets you 
and states his name which is Greman, the first hunter. 
Gherman tells you that this is the Hunter's Dream and 
this is one of if not the only safe and peaceful place 
in this accursed nightmare.
""")
    pause(7)
    hunters_dream2()
 
def hunters_dream2():
    clear_screen()
    print("""
As you explore the area you see a door that says 
Iosefka's clinic you have a feeling that you have
heard that name before. Then after more exploring 
you see gravestones with the same little demon like 
creatures that dragged you into this dark place.
""")
    choice = input("Do you 'inspect' the grave or do you 'open' the door? ").lower()
    
    if choice == "inspect":
        central_yharnam()
    
    elif choice == "open":
        print("The door does not open from this way.")
        hunters_dream2()
    else:
        print("")
        hunters_dream2()
    
def central_yharnam():
    clear_screen()
    print("""
------------------  
🏢Central Yharnam🏢 
------------------
""")
    print("""
As you touch the gravestone you see a blindingly bright
and you feel weightly, like you are being carried away by 
some greater force. Then just like the needles you pass
out out of no where. You wake up in the middle of an empty 
street that looks like it could belong to London in the 
early 1800's.
""")
    pause(7)
    clear_screen()
    print(""" 
You walk around looking at the absract sights under the bright
evening light. Until you stumble into a group of people down a 
flight of stairs gathered around a massive pile of burning bodies 
about 16 or 17 feet tall and wide. Then you turn your head left 
and you see an empty allyway that is heavily foggy, obscuring your 
sight down the allyway.
    """)
    choice = input("Do you 'left' and venture into the ally or go down the 'stairs' into the group of people around the pile of bodies? ").lower()
    
    if choice == "left":
       game_over("You fell a great height turning into a stain on the floor.")
       
    elif choice == "stairs":
        tomb_of_oedon()
    
    else:
        print("")
        central_yharnam()
        
def tomb_of_oedon():
   clear_screen()
   print("""
You go down the stairs all the people around the bodies turn to you
and rush your way. You look at the weapons in your hands then you 
point your gun at one and you pull the trigger. He falls to the 
floor and the others pause for a brief second but they continue 
your way so you lift your clever and bring it down upon them.
You continue going through Yharnam until you see a weird man
in the middle of a graveyard.
   """)
   pause(7)
   choice = input("\nDo you 'ask' who he is or do you 'attack' him?").lower()

   if choice == "ask":
       cathedral_ward()
   
   elif choice == "attack":
       game_over("You run to attack the man and as you are running at him you are shoot down by his shotgun")
    
   else:
       tomb_of_oedon()
       
def cathedral_ward():
    clear_screen()
    print("""
When you ask who he is he stands up and walks your way. He speaks
his name Gascoige, after he says his name he sniffs the air. with
a grim voice he says I smell beast in the air...
""")
    pause(7)
    print("""He grabs you and sniffs you causing you to push him.
It's you! You are a beast! He exclams as you push him. He draws
his weapons and shoots at you with a shotgun prompting you to roll
out of the way. As the fight goes on you have the upper hand he stops...
""")
    pause(7)
    print("""He stares at you I was right you are a filthy beast.
His weapons fall out of his hands and he looks up at the moon.
He falls to his knees and starts screaming in pain as his body
shifts in a burtal visciral way into a lanky, furry, wolf faced 
monster like the one you saw at the door to Iosefca's clinic. 
He gets up and lets out a louder more frighting scream that 
barely sounds human and charges at you. As he is about you hit
you, you shoot him in the neck making him fall to his knees infornt
of you. You take advantage of this and you run your blade aross his 
neck, his head falls to the floor and this fight over.""")
    pause(9)
    clear_screen()
    print("""
----------------
PREY SLAUGHTERED
----------------
""")
    pause(5)
    clear_screen()
    print("""
After that intense encounter you look up and the sun is setting, you go through
the door beyond the graveyard and you enter a dark room with a light shining 
behide a laddle so you climb it. When you get up the laddle you are greeted 
by a very very short hunched back chapel dweller who greets you and aknowleges 
your hunter statis. He requests that you lead anyone you can find to here for 
safety and care.
""")
    pause(7)
    cathedral_ward2()
   
def cathedral_ward2():
    clear_screen()
    print("""
You walk through the chapel looking for every way you could go because at
this point in time you have learned that rushing ahead thoughtlessly will
lead to your untimely demise. after searching the entire cathedral for 
ways to go you find two. an old door with a poster that says no hunters
allowed in our sacuray and a giant gate with many beasts of monsterous 
size behind it leading to a greater cathedral.
""")
    pause(7)
    choice = input("Do you go through the 'door' with a do not open sign or the 'gate' with many horrific sights behind it? ").lower()
    
    if choice == "go":
        old_yharnam()
        
    elif choice == "tell":
        second_fight()
        
    else:
        print("")
        cathedral_ward2()
        
        
def old_yharnam():
    clear_screen()
    print('''
As you push the old door it creeks open and you are greeted by a gattling 
gun on a distant building followed by a man screaming, "You there, hunter!
Didn't you see the warning? Turn back at once!"
''')
    pause(7)
    choice = input("Do you 'leave' or do you 'ignore' his warning").lower()

    if choice == "leave":
        cathedral_ward2()
    
    elif choice == "ignore":
        old_yharnam2()

    else:
        old_yharnam()

def old_yharnam2():
    clear_screen()
    print('''
"You are a skilled hunter!" he exclams as he reves up the gattling
gun.''')       
    pause(2)
    print('''
"Adept, merciless, half-cut with blood. As the best hunters are..."''')
    pause(4)
    print('''
"Which is why I must stop you!" He speaks proudly as the gun starts up
''')
    choice = input("Do you 'run' through Old Yharnam or do you 'hide' behind a wall? ").lower()
    
    if choice == "run":
        abandoned_workshop()

    elif choice == "hide":
        game_over("You run behind a wall, but the wall was to brittle from age to resist the contiuous ran of bullets")
    
    else:
        old_yharnam2()
        
def abandoned_workshop():
    clear_screen()
    print("""You run deeper into Old Yharnam dodging and weaving bullets until the man with a 
gattling gun is out of sight. All this running has lead you into a tower that is 
mostly destroyed in the middle. This sight leads you to turn and walk away but as
you start walking you are pushed into the hollow tower but you manage to grab a 
ledge and pull yourself up. You look ahead and you see a door that is surpisingly 
well kept considering the condiction of the rest of old yharnam so you open the door.
""")
    pause(7)
    abandoned_workshop2()

def abandoned_workshop2():
    clear_screen()
    print("""
------------------
Abandoned Workshop
------------------
""")
    pause(5)
    print("""
The door leads to a place that looks exactly like the hunter's dream but... destroyed?
You see the doll looking women here but she is not moving so you touch her hand and it
is cloth that feels oddly human like. After you find that out you go inside the shed on
top of the little hill and you see a black slimey cord on the table.
""")
    choice = input("Do you 'inspect' the table or 'go back'? ").lower()
    
    if choice == "inspect":
       cord_1() 
    
    elif choice == "go back":
        cathedral_ward()
    else:
        print("")
        abandoned_workshop2()
        
def cord_1():
    clear_screen()
    global score
    score += 1
    print(f"you have {score} cord(s)")
    pause(5)
    cathedral_ward2()

def second_fight():
    clear_screen()
    print("""
As you slip through the gate and run pass monstrosities of all types and sizes some as
tall as the grand structures of this torn down place. You run up 15 massive flights of 
stairs and you enter the Grand Catherdral and you see a lady on her knees bent over 
praying. As you approch the lady she starts growing and white fur englufs her body
transforming her into one of the beast and she lets out a blood curtling scream.     
""")
    pause(7)
    clear_screen()
    print("""
You strike her leg as she runs towards you shattering the bone and leaaving her crippled.
As she falls you go for her head but she stands up abruptly with her leg back in perfect
condiction. She lunges at you.
""")
   
    choice = input("Do you 'shoot' her or do you 'dodge'? ").lower
   
    if choice == "shoot":
       game_over("You try to get a clean shot off but her speed throws you off causing you grase her face and giving her a chance to crush you.")
   
    elif choice == "dodge":
        forbidden_wood()
    
    else:
        second_fight()

def forbidden_wood():    
    print("""
As she lunges at you, you get out of the way and she falls stomach first so you take advantage of this.
You cut her head off in one clean motion and you collect the skull at the alter.""") 
    
    print("""
----------------
PREY SLAUGHTERED
----------------
""")
    pause(5)

    print("""
Afterwards you pick up the skull you get a suddent burst of knowledge you now know much of the surface
level secrets of yharnam but you know now that there are vastly deep levels that your eyes are open to 
but yet to see. With this new knowledge you go to a mysterious man behind a door and you tell him the 
code to enter but as you walk through you realize that the man is accually dead. You contiue down the 
stairs until you hit the bottom and end up in a forest and in this forest you look up and realise that
it's nighttime.
""")
    pause(10)
    forbidden_wood2()

def forbidden_wood2():
    clear_screen()
    print("""
---------------
Forbidden Woods
---------------
""")
    pause(5)
    print("""
You explore the woods and as you do you find yourself getting lost often in the way that the forest is
almost like it is a maze thst leads to something greater. You wander for what seems like hours until you
see a building that looks like a clinic with a giant crater in the upper wall and a path that leads to a 
peice of land with no trees.
""")
    pause(7)
    choice = input("Do you 'enter' the clinic or 'go straight'? ").lower()
    
    if choice == "enter":
        iosefka_clinic()
        
    elif choice == "go straight":
        third_fight()
        
    else:
        print("")
        forbidden_wood()
        
def iosefka_clinic():
    clear_screen()
    print("""
You climb over the broken wall into the clinic. As you explore the clinic you start to realize that 
this clinic was not one for helpping this was a cruel lab that experimented with live patients. It
seems like a recent change of heart because the blood is still red. As you wander around you find
Iosefca dead, strapped onto a bed but she is not human anymore. She has turned into a short slimey
skinned squid faced biolumincent lab test. 
""")
    pause(7)
    
    choice = input("Do you 'touch' the body or do you 'leave'? ").lower()
    
    if choice == "touch":
       cord_2()
        
    elif choice == "leave":
        forbidden_wood()
        
    else:
        print("")
        iosefka_clinic()

def cord_2():
    clear_screen()
    global score
    score += 1
    print(f"you have {score} forths of a cord")
    pause()
    forbidden_wood()

def third_fight():
    clear_screen()
    print("""
As you enter the clearing you see three dark figures the one in the middle 
holds a scimitar, the one on the left holds a scimitar with a candle, and 
the one on the right holds a flamethrower.
""")
    
    pause(5)
    
    choice = input("Do you go for the shadow on the 'left', 'right', or 'middle'? ").lower
    
    if choice == "left":
        byregenwerth()

    elif choice == "right":
        game_over("As you approch the shadow with a flamethrower he sets you on fire and you burn to death.")
    
    elif choice == "middle":
        game_over("As you approch the one in the middle you are surronded and cut down.")
    else:
        third_fight()

def byregenwerth():
    clear_screen()
    print("""
As you approch the one on the left you shoot the sword out of his hand and you cut him down.
This enrages the other two and they start shooting snakes at you after preforming a ritual.
You realize you have to end this fast before the snakes overwhelm you so you run towards the 
shadow with the scimitar and you use he as a shield against the flames of the flamethrower
then you throw his body to the ground. You grab a snake and hurry towards the third shadow
as he reloads the gas canister and you choke him out with the snake.
""")
    pause(10)
    print("""
----------------
PREY SLAUGHTERED
----------------
""")
    pause(5)
    byregenwerth2()
    
def byregenwerth2():   
    clear_screen()
    print("""
After you made short work of the shadows of Yharnam you enter Byregenwerth. after your
first two steps you can tell something is not right but you continue on through this 
strangly empty place until you reach the center. It looks like you just left earth
and landed on Mars everything looks alien and nothing feels right anymore. You get
to a broken bridge that leads stright into the sea and that is the only way that is 
not covered by abloslute nonsensory monsters.
""")
    choice = input("Do you 'leave' or do you 'jump' into the sea? ").lower
    
    
    if choice == "leave":
        cathedral_ward()
        
    elif choice == "jump":
        yahargul()
    
    else:
        print("")
        byregenwerth()

def yahargul():
    clear_screen
    print('''
As you get prepared to jump an old man in a chair appears from smoke
and he says "We are born of the blood, made men by the blood, undone by 
the blood. Our eyes are yet to open. Fear the old blood!"
You jump into the sea and you end up in a place with water at your feet 
and a fogged area 20 feet away with a giant spider in the middle with 
many on it's babies crawling around.
''')
    pause(7)
    clear_screen()
    print("""
You easily beat the massive spider because of it's vacuous nature.
upon defeat the spider explodes sending it's clear blood everywhere
""")
    print("""
----------------
PREY SLAUGHTERED
----------------          
""")
    pause(5)
    yahargul2()

def yahargul2():
    print("""
The world has offcial stopped trying to make since. Everything is so 
augmented and distorted the purple sky behind the red moon looks right 
at home. As you explore this place the path is very straight until you 
reach a split between the right and the left but you can't see either 
way all to well.
""")
    choice = input("Do you go 'right' or 'left'? ").lower
    
    if choice == "right":
        game_over("you fell in a pit of burning bodies.")
        
    elif choice == "left":
        nightmare_of_menis()
    
    else:
        print("")
        yahargul()
        
def nightmare_of_menis():
    clear_screen
    print("""
You reach an empty castle section and a giant mass of bodie bigger than the  
castle section drops down. As you prepare for a rough fight the mass is set 
on fire by a mage trying to hit you and you take advantage of this. You run
in the door behind the mass and bump into a mummy in a chair.         
""")
    pause(7)
    nightmare_of_menis2()

def nightmare_of_menis2():
    clear_screen()
    print("""
You get injected into what seems like someone's dream and there is a giant
flaming eye in the sky but everything else looks rather plesent.
""")
    
    choice = input("Do you 'run' or 'hide'").lower
    
    if choice == "run":
        game_over("your mind was instantly lost as you were forced to gaze upon the great flaming eye.")
    
    elif choice == "hide":
        fourth_fight()
    else:
        nightmare_of_menis2() 
        
def fourth_fight():     
    clear_screen()      
    print("""
As the giant eye shuts you rush into a strange tower and you see a man
with a cage on his head running around so you chase him. You follow him 
until he vanishes aubruptly.
""")
    
    choice = input("Do you go 'right, 'left', or 'down'").lower
    
    if choice == "right":
        game_over("You get trapped inside a mirror")

    elif choice == "left":
        game_over("You walk into a pacted room of armed seletons and they beat you to death. ")
    
    elif choice == "down":
        cord_3()
    else:
        fourth_fight()
        
def mergos_loft():
    clear_screen()
    print("""
You pin him down so he retaleated by summoning a tentecle your way but you
dodged it and shot him dead. This causes a bridge to form in the middle of 
the tower that leads to a nursary looking place where you can hear a baby 
crying at all times and every path looks the same.
""")
    pause(7)
    choice = input("Do you go 'right' or 'left'").lower()
    
    if choice == "right":
        game_over("As you progress through the right passage you are crushed by a giant crib.")
    
    elif choice == "left":
        clear_screen()
        print("""
As you progress through the left passage you see a tall black figure with many swords in her hands
and you notice that the crying sound has amplifided. The tall figure turns to you and starts swinging
wildly in all directions.             
""")
        choice = input("Do you 'run' or do you 'attack'? ")
        
        if choice == "run":
            clear_screen()
            print("""
You run behind the figure as she swings and she can't reach far enough 
behind so you continuously slash her back until she falls.
""")
            pause(5)
            clear_screen()
            print("""
---------------
NIGHTMARE SLAIN          
---------------
""")
            pause(5)
            cord_3()
    elif choice == "attack":
        game_over("You are cut into tiny peices.")
        
    else:
        mergos_loft()

def cord_3():
    global score
    score += 1
    print(f"you have {score} cord(s)")
    pause(5)  
    hunters_dream_end()

def hunters_dream_end():
    print('''
After you defeated the figure you are transported back to the Hunter's Dream
but every thing is deastoyed and on fire. You see the strange lady again and
she says "German awaits you." then she points to a field of white flowers.
''')
    choice = input("do you 'inspect' the tombstones or 'enter' the field of white flowers? ")
    
    if choice == "inspect":
        tomb_transport()
        
    elif choice == "enter":
        final_fight()
    
    else:
        hunters_dream_end()    

def tomb_transport():
    print("These tombs contain every main location you have been to until this point.")
    choice = (str(input("\nDo you want to 'go back' or go to location '1', '2', '3', '4', '5', '6','7', or '8'").lower()))
    
    if choice == "go back":
        hunters_dream_end()
    
    elif choice == "1":
        central_yharnam()
        
    elif choice == "2":
        cathedral_ward_altered()
    
    elif choice == "3":
        abandoned_workshop()
    
    elif choice == "4":
        forbidden_wood()
    
    elif choice == "5":
        byregenwerth()
        
    elif choice == "6":
        yahargul()
    
    elif choice == "7":
        nightmare_of_menis()

    elif choice == "8":
        mergos_loft()  
    
    else:
        print("")
        tomb_transport()

def cathedral_ward_altered():
    print("""""""")
    choice = input("Do you 'inspect' the dead body or 'go' through the door with a do not open sign or 'tell' the msyterious man the code?")
    
    if choice == "inspect":
       cord_4()
    
    elif choice == "go":
        abandoned_workshop()
        
    elif choice == "tell":
        forbidden_wood()
        
    else:
        print("")
        cathedral_ward_altered()
        
def cord_4():
    global score
    score += 1
    pause(5)
    print(f"you have {score} cord(s)")
    cathedral_ward_altered()

def final_fight():
    print(""" """)
    choice = input("Do you 'accept death' or 'fight back'? ")
    if choice == "accept death":
        ending_1()
    
    elif choice == "fight back" and score >= 3:
        ending_3()
        
    elif choice == "fight back":
        ending_2()
        
    else:
        final_fight()
        
def ending_1():
    print("")
    win("escaped the nightmare.")

def ending_2():
    print("")
    win("been anoited as the main hunter of the night by the moon presence.")

def ending_3():
    print("")
    win("become a great one and you now rule the nightmare.")
        
def game_over(reason):
    print("\nYou may never escape this accursed nightmare because " + reason)
    play_again_lost()


def play_again_lost():
    choice = input("\nDo you want to 'try again' and continue to hold hope that you will see the morning sun or 'give up and accept the cruel fate that you have been subjected to?'").lower()
    
    if choice == "try again":
        clinic()
    
    elif choice == "give up":
        print("You have lost all faith in escape so you settle into the endless cycle of hunting and slowly lose your mind.\nThank you for playing. have a good day")
    
    else:
        print("")
        play_again_lost()

def win(reason):
    print("You have " + reason)
    play_again_win()
    
def play_again_win():
    choice = input("Do you want to 'start' a new nightmare or 'end' this cycle")
    if choice == "start":
        clinic()
    
    elif choice == "end":
        print("You have conquered the nightmare and now you are free to be and you have decided to keep it that way.\n Have a good day.")
    
    else:
        print("")
        play_again_win()
        
        
clinic()