import os
import time

score = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(seconds):
    time.sleep(seconds)

# ----------------------------------------
#               START OF GAME
# ----------------------------------------

def clinic():
    clear_screen()
    print(""" 
------------------------------------
🩸 Bloodborne Text-Based Adventure 🐺
------------------------------------
""")
    
    pause(5)
    clear_screen()
    print("""
You wake up strapped to a bed, staring at a bundle of needles.
As you struggle to break free, the needles plunge down upon you.
Strange, tiny creatures crawl across your skin as you lie helpless,
slowly losing consciousness. You awaken in the Hunter's Dream—
find a way to escape before you're lost forever...
""")
    pause(7)
    clear_screen()
    print("You wake beside the door of a clinic. As you walk out, you see an abnormally large wolf feasting on a corpse.")

    choice = input("\nDo you 'face' the wolf or do you 'pass' the wolf? ").lower()

    if choice == "face":
        hunters_dream()
    elif choice == "pass":
        central_yharnam()
    else:
        print("Invalid choice.")
        clinic()

# ----------------------------------------
#          HUNTER'S DREAM (DEATH)
# ----------------------------------------

def hunters_dream():
    clear_screen()
    print("""
As you approach the wolf, its attention snaps toward you.
The beast is savage, its horrifying face convincing you
that you must already be dead—this must be hell.
Before you can react, it leaps and you become its next meal.
""")
    pause(13)
    clear_screen()
    print("      YOU DIED")
    pause(9)
    clear_screen()

    print(""" 
-------------------
💤 Hunter's Dream 💤
-------------------
    """)
    pause(5)
    clear_screen()
    print("""
You awaken on the ground of a graveyard beside a woman
who looks... like a doll. She pushes an old man in a wheelchair.
The old man greets you and introduces himself as Gehrman,
the first hunter. He explains that this is the Hunter's Dream—
one of the only safe places in this accursed nightmare.
""")
    pause(7)
    hunters_dream2()

def hunters_dream2():
    clear_screen()
    print("""
As you explore, you find a door labeled
'Iosefka's Clinic'—a name that feels familiar.
Further exploration reveals gravestones attended by
the same small demon-like creatures that dragged you away.
""")
    choice = input("Do you 'inspect' the grave or do you try to 'open' the door? ").lower()
    
    if choice == "inspect":
        central_yharnam()
    elif choice == "open":
        print("The door does not open from this side.")
        pause(2)
        hunters_dream2()
    else:
        print("Invalid choice.")
        hunters_dream2()

# ----------------------------------------
#             CENTRAL YHARNAM
# ----------------------------------------

def central_yharnam():
    clear_screen()
    print("""
-------------------- 
🏢 Central Yharnam 🏢 
--------------------
""")
    print("""
As you touch the gravestone, a blinding light surrounds you.
You feel weightless, as if pulled by some greater force.
Just like the needles, you pass out without warning.
You awaken in the middle of an empty street that resembles
London in the early 1800s.
""")
    pause(7)
    clear_screen()
    print(""" 
You wander, taking in the eerie sights under the bright evening sky.
Eventually, you stumble upon a group of townsfolk down a staircase,
gathered around a massive burning pile of bodies.
To your left is a fog-filled alleyway, its depths completely obscured.
""")
    choice = input("Do you go 'left' into the alleyway or go down the 'stairs' toward the mob? ").lower()
    
    if choice == "left":
        game_over("you stepped into dense fog and fell from a great height, becoming a bloodstain on the pavement.")
    elif choice == "stairs":
        tomb_of_oedon()
    else:
        print("Invalid choice.")
        central_yharnam()

# ----------------------------------------
#              TOMB OF OEDON
# ----------------------------------------

def tomb_of_oedon():
    clear_screen()
    print("""
You descend the stairs. The Huntsmen around the burning bodies
turn toward you and rush in your direction. You raise your pistol
and fire—one drops instantly. The others hesitate, but soon continue
their charge. You strike them down with your cleaver and press onward
through Yharnam until you encounter a strange man in a graveyard.
""")
    pause(7)
    choice = input("\nDo you 'ask' who he is or do you 'attack' him? ").lower()

    if choice == "ask":
        cathedral_ward()
    elif choice == "attack":
        game_over("the man fires his shotgun before you can swing—your story ends here.")
    else:
        print("Invalid choice.")
        tomb_of_oedon()

# ----------------------------------------
#            CATHEDRAL WARD
# ----------------------------------------

def cathedral_ward():
    clear_screen()
    print("""
When you ask who he is, he rises and approaches.
He introduces himself as Gascoigne. Suddenly, he sniffs the air.
With a grim voice, he mutters, 'I smell beast...'
""")
    pause(7)
    print("""
He grabs you and sniffs again, prompting you to shove him away.
"It's you! You're a beast!" he shouts, drawing his weapons
and firing a shotgun blast that you barely dodge.
The fight rages on. You gain the upper hand—until he stops.
""")
    pause(7)
    print("""
He stares at you. "I was right... you're a filthy beast."
His weapons fall from his hands as he looks up toward the moon.
His body begins to twist and distort into a lupine monster—
just like the one you saw at Iosefka's Clinic.
He lunges, but you fire a shot into his throat, dropping him.
You finish the fight with one swift strike.
""")
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
After that intense encounter, the sun begins to set.
You enter the chapel beyond the graveyard and climb a ladder.
At the top, a short, hunched chapel dweller greets you,
acknowledging your new status as a hunter. He asks you to
lead any survivors you find back here for safety.
""")
    pause(7)
    cathedral_ward2()

def cathedral_ward2():
    clear_screen()
    print("""
You explore the chapel carefully—rushing ahead has only
brought you death so far. After searching thoroughly,
you find two paths:

1. An old door with a poster reading:
   'NO HUNTERS ALLOWED IN OUR SANCTUARY.'

2. A massive gate behind which lurk towering beasts,
   leading toward a grander cathedral.
""")
    pause(7)
    choice = input("Do you go through the 'door' or through the 'gate'? ").lower()
    
    if choice == "door":
        old_yharnam()
    elif choice == "gate":
        second_fight()
    else:
        print("Invalid choice.")
        cathedral_ward2()

# ----------------------------------------
#               OLD YHARNAM
# ----------------------------------------

def old_yharnam():
    clear_screen()
    print('''
As you push open the old door, it creaks loudly.
Instantly, a distant gatling gun fires from a rooftop.
A man’s voice echoes through the ruins:

"You there, hunter! Didn’t you see the warning?
Turn back at once!"
''')
    pause(7)
    choice = input("Do you 'leave' or do you 'ignore' his warning? ").lower()

    if choice == "leave":
        cathedral_ward2()
    elif choice == "ignore":
        old_yharnam2()
    else:
        print("Invalid choice.")
        old_yharnam()

def old_yharnam2():
    clear_screen()
    print('''
"You are a skilled hunter!" he shouts as he revs the gatling gun.
''')
    pause(2)
    print('''
"Adept, merciless, half-cut with blood—as the best hunters are!"
''')
    pause(4)
    print('''
"Which is why I must stop you!"
The gun begins roaring to life.
''')
    choice = input("Do you 'run' through Old Yharnam or do you 'hide' behind a wall? ").lower()
    
    if choice == "run":
        abandoned_workshop()
    elif choice == "hide":
        game_over("the wall you hid behind crumbled instantly under the barrage of bullets.")
    else:
        print("Invalid choice.")
        old_yharnam2()

# ----------------------------------------
#           ABANDONED WORKSHOP
# ----------------------------------------

def abandoned_workshop():
    clear_screen()
    print("""
You sprint deeper into Old Yharnam, dodging and weaving through bullets
until the gatling fire fades behind you. All this running leads you into
a ruined tower with a hollow center. The sight alone makes you hesitate,
but before you can escape, something pushes you inside.

You manage to grab a ledge and pull yourself up. Ahead is a door—
surprisingly well-kept considering the decay surrounding it.
You open it cautiously.
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
The room looks exactly like the Hunter’s Dream—only ruined and still.
A lifeless doll lies on the floor. When you touch her hand, it feels
like cloth, yet disturbingly human.

Inside the small shed, you find a strange, black, slimy umbilical cord
resting on a table.
""")
    choice = input("Do you 'inspect' the table or 'go back'? ").lower()
    
    if choice == "inspect":
        cord_1()
    elif choice == "go back":
        cathedral_ward()
    else:
        print("Invalid choice.")
        abandoned_workshop2()

def cord_1():
    clear_screen()
    global score
    score += 1
    print(f"You have {score} cord(s).")
    pause(5)
    cathedral_ward2()

# ----------------------------------------
#             SECOND FIGHT
# ----------------------------------------

def second_fight():
    clear_screen()
    print("""
You slip through the gate and sprint past monstrosities of all shapes
and sizes—some nearly as tall as the grand cathedral itself. After
ascending fifteen massive flights of stairs, you enter the Grand Cathedral.

A kneeling woman prays at the altar. As you approach, she begins to grow.
White fur engulfs her body as she transforms into a towering beast.
She lets out a bloodcurdling scream.
""")
    pause(7)
    clear_screen()
    print("""
You strike her leg as she charges, shattering the bone.
She collapses, but instantly regenerates the injury.
With a sudden burst of impossible movement, she lunges at you.
""")
   
    choice = input("Do you 'shoot' her or do you 'dodge'? ").lower()

    if choice == "shoot":
        game_over("your shot grazed her face, leaving you open as she crushed you effortlessly.")
    elif choice == "dodge":
        forbidden_wood()
    else:
        print("Invalid choice.")
        second_fight()

# ----------------------------------------
#              FORBIDDEN WOODS
# ----------------------------------------

def forbidden_wood():
    clear_screen()
    print("""
As she lunges, you slip aside. She crashes to the floor and you seize
the moment—one clean strike ends her. Upon victory, you collect a skull
from the altar.
""")
    pause(5)
    print("""
----------------
PREY SLAUGHTERED
----------------
""")
    pause(5)

    print("""
With the skull in hand, a surge of knowledge floods your mind.
You now understand some of Yharnam’s surface-level secrets,
but you sense vastly deeper truths just beyond your grasp.

You speak a code through a door to a mysterious man—though you soon
realize he has already died. Past his chamber, you descend a long stairway
into a vast forest. Night has fallen.
""")
    pause(10)
    forbidden_wood2()

def forbidden_wood2():
    clear_screen()
    print("""
----------------
Forbidden Woods
----------------
""")
    pause(5)
    print("""
You navigate the woods, often getting lost in its twisting paths.
The forest feels intentionally maze-like, guiding you toward something.

After wandering for what feels like hours, you find:
- A ruined building resembling a clinic, with a massive hole in the wall.
- A path leading farther forward into leafless, open land.
""")
    pause(7)
    choice = input("Do you 'enter' the clinic or 'go straight'? ").lower()
    
    if choice == "enter":
        iosefka_clinic()
    elif choice == "go straight":
        third_fight()
    else:
        print("Invalid choice.")
        forbidden_wood2()

# ----------------------------------------
#            IOSEFKA'S CLINIC
# ----------------------------------------

def iosefka_clinic():
    clear_screen()
    print("""
You climb through the broken wall into the clinic. As you explore, it
becomes clear this was no place of healing—it was a laboratory of cruelty.
Fresh blood stains the tables, suggesting recent experiments.

Deep inside, you find Iosefka herself—dead, strapped to a bed.
She is no longer human. Her body is a short, slime-covered, bioluminescent,
squid-faced mutation.
""")
    pause(7)
    
    choice = input("Do you 'touch' the body or do you 'leave'? ").lower()
    
    if choice == "touch":
        cord_2()
    elif choice == "leave":
        forbidden_wood()
    else:
        print("Invalid choice.")
        iosefka_clinic()

def cord_2():
    clear_screen()
    global score
    score += 1
    print(f"You have {score} cord(s).")
    pause(5)
    forbidden_wood()

# ----------------------------------------
#              THIRD FIGHT
# ----------------------------------------

def third_fight():
    clear_screen()
    print("""
As you enter the clearing, you see three dark figures:
- The one in the middle wields a scimitar.
- The one on the left carries a burning candle and blade.
- The one on the right holds a flamethrower.
""")
    
    pause(5)
    
    choice = input("Do you go for the 'left', 'right', or 'middle' shadow? ").lower()

    if choice == "left":
        byregenwerth()
    elif choice == "right":
        game_over("the flamethrower engulfs you in fire the moment you approach.")
    elif choice == "middle":
        game_over("the remaining two encircle you and cut you down.")
    else:
        print("Invalid choice.")
        third_fight()

# ----------------------------------------
#              BYRGENWERTH
# ----------------------------------------

def byregenwerth():
    clear_screen()
    print("""
You shoot the left shadow’s sword from his hand and cut him down.
The other two roar in fury and unleash serpents from their bodies.
You rush the second shadow, using him as a shield against the flames.
When he collapses, you grab a serpent and choke the third shadow
as he reloads his canister.
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
After defeating the Shadows of Yharnam, you enter Byrgenwerth.
The silence is unsettling. Every step feels wrong.

You eventually reach a broken bridge leading straight into a vast sea.
It is the only unobstructed path—everything else crawls with abominations.
""")
    choice = input("Do you 'leave' or do you 'jump' into the sea? ").lower()
    
    if choice == "leave":
        cathedral_ward()
    elif choice == "jump":
        yahargul()
    else:
        print("Invalid choice.")
        byregenwerth2()

# ----------------------------------------
#                YAHARGUL
# ----------------------------------------

def yahargul():
    clear_screen()
    print('''
As you prepare to jump, an old man in a chair appears in swirling smoke.

"We are born of the blood, made men by the blood, undone by the blood.
Our eyes are yet to open. Fear the Old Blood!"

You leap into the sea and emerge in a chamber with water at your feet.
Ahead, within thick fog, a massive spider waits—its children skittering.
''')
    pause(7)
    clear_screen()
    print("""
You defeat the vacuous spider with relative ease.
On death, its body bursts, spraying clear fluid everywhere.
""")
    print("""
----------------
PREY SLAUGHTERED
----------------          
""")
    pause(5)
    yahargul2()

def yahargul2():
    clear_screen()
    print("""
The world has abandoned all logic. The purple sky behind the red moon
feels disturbingly natural here. The path forward is straight until you
reach a fork: right or left, though both are obscured by thick fog.
""")
    choice = input("Do you go 'right' or 'left'? ").lower()
    
    if choice == "right":
        game_over("you fall into a pit of burning bodies.")
    elif choice == "left":
        nightmare_of_menis()
    else:
        print("Invalid choice.")
        yahargul2()

# ----------------------------------------
#          NIGHTMARE OF MENSIS
# ----------------------------------------

def nightmare_of_menis():
    clear_screen()
    print("""
-----------------------
 Nightmare of Mensis
-----------------------
""")
    pause(4)
    print("""
You reach an empty castle section and a giant mass of bodies bigger than the  
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
    
    choice = input("Do you 'run' or 'hide'").lower()
    
    if choice == "run":
        game_over("your mind was instantly lost as you were forced to gaze upon the great flaming eye.")
    
    elif choice == "hide":
        fourth_fight()
    else:
        nightmare_of_menis2() 
# ----------------------------------------
#              FOURTH FIGHT
# ----------------------------------------

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
    pause(8)
    print("""
----------------
PREY SLAUGHTERED
----------------
""")
    pause(5)
    mergo_loft()

# ----------------------------------------
#            MERGO'S LOFT
# ----------------------------------------

def mergo_loft():
    clear_screen()
    print("""
The elevator rises toward the unseen peak of the nightmare.
At the top, you find a crying infant echoing through the halls of
an impossible palace.

Shadowy nurses rush to protect the unseen child. You cut them down
as you ascend the endless staircase. The wailing grows unbearable.
""")
    pause(8)

    print("""
Eventually, you confront a final Wet Nurse—a towering, ethereal being
that phases in and out of existence. The battle is relentless.
""")
    pause(6)

    choice = input("Do you 'press' the attack or do you 'retreat'? ").lower()

    if choice == "press":
        mergo_loft2()
    elif choice == "retreat":
        game_over("the Wet Nurse enveloped you in darkness and carved you apart.")
    else:
        print("Invalid choice.")
        mergo_loft()

def mergo_loft2():
    clear_screen()
    print("""
You push forward relentlessly—dodging, slashing, firing, bleeding.
At last, the final blow lands. The Wet Nurse dissolves into smoke.
The crying stops.

A strange, quivering umbilical cord remains where the child should be.
""")
    pause(8)
    cord_3()

def cord_3():
    clear_screen()
    global score
    score += 1
    print(f"You have {score} cord(s).")
    pause(5)
    hunters_dream_endgame()

# ----------------------------------------
#          RETURN TO HUNTER'S DREAM
# ----------------------------------------

def hunters_dream_endgame():
    clear_screen()
    print("""
-------------------
 The Hunter's Dream
-------------------
""")
    pause(4)
    print("""
You awaken once more in the Dream. But the workshop is burning.
Ash falls like snow. The Doll appears at your side, gentle and calm.

\"Good hunter… the night is coming to an end. You must now choose
how this dream shall conclude.\"
""")
    pause(8)

    print("""
You see Gehrman waiting under the tree. The first hunter.
He gestures for you to approach.
""")
    pause(5)

    choice = input("Do you 'submit' to Gehrman or do you 'refuse'? ").lower()

    if choice == "submit":
        ending_1()
    elif choice == "refuse":
        ending_2_or_3()
    else:
        print("Invalid choice.")
        hunters_dream_endgame()

# ----------------------------------------
#              ENDING 1
# ----------------------------------------

def ending_1():
    clear_screen()
    print("""
Gehrman places a gentle hand upon your shoulder.

\"Very well, good hunter. Your hunt is over.\"

He swings his scythe in a single swift motion.
You awaken in the real world at dawn, sitting on the floor
outside the abandoned workshop. Peaceful. alive again.
""")
    pause(10)
    print("""
----------------
   ENDING: 1
  Dawn of Man
----------------
""")
    pause(5)
    play_again()

# ----------------------------------------
#      ENDING 2 OR 3 DECISION POINT
# ----------------------------------------

def ending_2_or_3():
    clear_screen()
    print("""
You refuse. Gehrman sighs.

\"Good hunter… your resolve is admirable.\"
He rises slowly and draws his scythe. The battle begins.
After a long and brutal duel, you defeat him.
""")
    pause(8)

    print("""
But as Gehrman falls, a massive, pale presence descends from the moon.
The Moon Presence wraps its tendrils around you—
""")
    pause(6)

    if score >= 3:
        ending_3()
    else:
        ending_2()

# ----------------------------------------
#                ENDING 2
# ----------------------------------------

def ending_2():
    clear_screen()
    print("""
The Moon Presence binds you easily. You collapse helplessly.
Your mind melts into a haze as it reshapes your body.

When you awaken, you are kneeling at the workshop door,
the new caretaker of the Dream—bound forever.
""")
    pause(10)
    print("""
-----------------------
   ENDING: 2
 Bound to the Dream
-----------------------
""")
    pause(5)
    play_again()

# ----------------------------------------
#                ENDING 3
# ----------------------------------------

def ending_3():
    clear_screen()
    print("""
The Moon Presence lunges, but the cords you consumed burst with energy.
You resist its grip. The creature shrieks as you overpower it.

Your form mutates beyond humanity—tentacles, eyes, shifting flesh.
But you are not a beast. You are something greater.
You cradle the Doll's hand as she lifts you gently.
""")
    pause(10)
    print("""
------------------------
    ENDING: 3
  Ascended Hunterling
------------------------
""")
    pause(5)
    play_again()

# ----------------------------------------
#               GAME OVER
# ----------------------------------------

def game_over(reason):
    clear_screen()
    print(f"You died because {reason}")
    pause(5)
    print("\n      YOU DIED")
    pause(5)
    play_again()

# ----------------------------------------
#           PLAY AGAIN LOOP
# ----------------------------------------

def play_again():
    choice = input("\nDo you want to play again? ('yes' or 'no'): ").lower()

    if choice == "yes":
        global score
        score = 0
        clinic()
    elif choice == "no":
        clear_screen()
        print("Thank you for playing!")
        pause(3)
    else:
        print("Invalid choice.")
        play_again()

# ----------------------------------------
#              START GAME
# ----------------------------------------

clinic()
