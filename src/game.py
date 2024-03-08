import inquirer
from inquirer.themes import BlueComposure
import math
import random
import time

class Being:
    def __init__(self, name="Adventurer", level=1):
        self.name = name
        self.level = level
        self.exp_to_next_level = self.level*100
        self.health = self.level*10
        self.attack_damage_range = f"{math.floor(self.level/2)} - {self.level}"
    
    def check_stats(self):
        print(f"Level = {self.level}")
        print(f"Exp to next level = {self.exp_to_next_level}")
        print(f"Health = {self.health}")
        print(f"Attack Damage Range = {self.attack_damage_range}")
        print(" ")

    def train(self):
        print("You spend some time training...")
        print(" ")
        time.sleep(5)
        train_exp = self.level*25
        self.exp_to_next_level = self.exp_to_next_level - 100
        print("You practice some new combat techniques, and gain 100 EXP points.")
        print(" ")
        if self.exp_to_next_level <= 0:
            print("""
         ⣠⠤⠤⣄⣠⣤⣤⡤⠤⠤⠤⠤⠤⠤⠤⣤⣤⣤⣠⠤⠤⣄⠀⠀⠀⠀
⠀⠀    ⠀⡜⢁⡶⠶⢤⡇⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠸⡦⠾⠶⡄⢳⠀⠀⠀
⠀⠀    ⠀⡇⢸⠀⠀⠀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡇⢸⡆⠀⠀
⠀⠀    ⠀⢧⠘⣆⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢠⠇⣸⠀⠀⠀
⠀⠀    ⠀⠈⢦⡘⠦⣀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⣀⡴⠋⡰⠃⠀⠀⠀
⠀⠀⠀    ⠀⠀⠙⠦⣌⡙⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⣁⡴⠚⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀    ⠀⠀⠀⠉⠉⠚⠳⣄⠀⠀⠀⠀⣠⠖⠓⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠈⢳⡀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⢀⡇⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⢀⡜⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀  ⠀⠀  ⠀⠀⠀⠀⢀⣞⣀⣀⣀⣀⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀  ⠀⠀  ⠀⠀⣾⠉⠉⠉⠉⠉⠉⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀  ⠀⠀  ⠀⠀⠀⢀⡷⠤⠤⠤⠤⠤⠤⠼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠈⠓⠒⠒⠒⠒⠒⠒⠒⠁
                """)
            print("Congrats your level has increased!")
            print(" ")
            remaining_exp = self.exp_to_next_level * -1
            self.level += 1
            self.exp_to_next_level = self.level*100
            self.exp_to_next_level = self.exp_to_next_level - remaining_exp
            self.health = self.level*10
            self.attack_damage_range = f"{math.floor(self.level/2)} - {self.level}"
    
    def attack(self, opponent):
        damage = random.randint(math.floor(self.level/2), self.level)
        opponent.health = opponent.health - damage
        print(f"Level {self.level} {self.name} Attacks Level {opponent.level} {opponent.name}!")
        print(f"{self.name} inflicts {damage} damage to {opponent.name}!")
        print(f"{opponent.name} Health = {opponent.health}")
        print(" ")
    
    def retreat(self):
        exp = self.level*100
        current_exp = exp - self.exp_to_next_level
        exp_lost = current_exp/2
        self.exp_to_next_level = self.exp_to_next_level + exp_lost
        print(f"You run away and lose {exp_lost} EXP points.")
        print(" ")
    
    def heal(self):
        heal = self.level*10
        heal_quart = heal/4
        heal_amount = random.randint(1, heal_quart)
        self.health = self.health + heal_amount
        print(f"{self.name} performs some first aid on themself!")
        print(f"Health increased by {heal_amount}")
        if self.health > heal:
            self.health = heal
        print(f"{self.name} Health = {self.health}")
        print(" ")

    def battle(self, opponent):
        turn = True
        while True:
            if turn == True:

                def battle_attack():
                    self.attack(opponent)

                choices = {
                    'Attack': battle_attack,
                    'Heal': self.heal
                }
                questions = [
                    inquirer.List('prompts',
                                message=f"Choose your action",
                                choices=list(choices.keys()),
                                ),
                ]
                answers = inquirer.prompt(questions, theme=BlueComposure())
                result = choices[answers['prompts']]()

            if turn == False:
                opponent.attack(self)
                
            if self.health < 1:
                print("""
                       ______
                    .-"      "-.
                   /            \\
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
                """)
                print("You Died!")
                print(" ")
                exit()
            if opponent.health < 1:
                print("""
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
                """)
                print(f"You Defeated {opponent.name}!")
                print(f"You Gained {opponent.exp_to_next_level} EXP")
                print(" ")
                self.exp_to_next_level = self.exp_to_next_level - opponent.exp_to_next_level
                if self.exp_to_next_level <= 0:
                    print("""
         ⣠⠤⠤⣄⣠⣤⣤⡤⠤⠤⠤⠤⠤⠤⠤⣤⣤⣤⣠⠤⠤⣄⠀⠀⠀⠀
⠀⠀    ⠀⡜⢁⡶⠶⢤⡇⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠸⡦⠾⠶⡄⢳⠀⠀⠀
⠀⠀    ⠀⡇⢸⠀⠀⠀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡇⢸⡆⠀⠀
⠀⠀    ⠀⢧⠘⣆⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢠⠇⣸⠀⠀⠀
⠀⠀    ⠀⠈⢦⡘⠦⣀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⣀⡴⠋⡰⠃⠀⠀⠀
⠀⠀⠀    ⠀⠀⠙⠦⣌⡙⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⣁⡴⠚⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀    ⠀⠀⠀⠉⠉⠚⠳⣄⠀⠀⠀⠀⣠⠖⠓⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠈⢳⡀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⢀⡇⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⢀⡜⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀  ⠀⠀  ⠀⠀⠀⠀⢀⣞⣀⣀⣀⣀⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀  ⠀⠀  ⠀⠀⣾⠉⠉⠉⠉⠉⠉⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀  ⠀⠀  ⠀⠀⠀⢀⡷⠤⠤⠤⠤⠤⠤⠼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠈⠓⠒⠒⠒⠒⠒⠒⠒⠁
                """)
                    print("Congrats your level has increased!")
                    print(" ")
                    remaining_exp = self.exp_to_next_level * -1
                    self.level += 1
                    self.exp_to_next_level = self.level*100
                    self.exp_to_next_level = self.exp_to_next_level - remaining_exp
                    if self.exp_to_next_level <= 0:
                        remaining_exp = self.exp_to_next_level * -1
                        self.level += 1
                        self.exp_to_next_level = self.level*100
                        self.exp_to_next_level = self.exp_to_next_level - remaining_exp
                    self.health = self.level*10
                    self.attack_damage_range = f"{math.floor(self.level/2)} - {self.level}"
                self.health = self.level*10
                break
            turn = not turn
            time.sleep(1)

def explore_func(player):
    goblin = Being("Goblin", random.randint(math.ceil(player.level/2), player.level))
    rogue_knight = Being("Rogue Knight", random.randint(math.ceil(player.level/1.7), math.ceil(player.level*1.2)))
    werewolf = Being("Werewolf", random.randint(math.ceil(player.level/1.3), math.ceil(player.level*1.4)))
    ogre = Being("Ogre", random.randint(math.ceil(player.level), math.ceil(player.level*1.6)))
    dragon = Being("Dragon", random.randint(math.ceil(player.level/0.8), math.ceil(player.level*2)))

    ran_num = 1
    if player.level > 4:
        ran_num = random.randint(1,2)
    if player.level > 9:
        ran_num = random.randint(1,3)
    if player.level > 14:
        ran_num = random.randint(1,4)
    if player.level > 19:
        ran_num = random.randint(1,5)
    
    if ran_num == 1:
        foe = goblin
        picture = """
             ,      ,   
            /(.-""-.)\\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \\
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\\
      /       '----'       \\
      """
    if ran_num == 2:
        foe = rogue_knight
        picture = """
  /\\
  ||
  ||
  ||
  ||          ||
  ||         .--.
  ||        /.--.\\
  ||        |====|
  ||        |`::`|
 _||_   .-;`\..../`;_.-^-._
  /\   /  |...::..|`   :   `|
 |:'\ |   /'''::''|   .:.   |
  \ /\;-,/\   ::  |..:::::..|
   \ <` >  >._::_.| ':::::' |
    `""`  /   ^^  |   ':'   |
          |       \    :    /
          |        \   :   / 
          |___/\___|`-.:.-`
           \_ || _/    `
           <_ >< _>
           |  ||  |
           |  ||  |
          _\.:||:./_
         /____/\____\\
        """
    if ran_num == 3:
        foe = werewolf
        picture = """
                        /\\
                        ( ;`~v/~~~ ;._
                     ,/'"/^) ' < o\  '".~'\\\--,
                   ,/",/W  u '`. ~  >,._..,   )'
                  ,/'  w  ,U^v  ;//^)/')/^\;~)'
               ,/"'/   W` ^v  W |;         )/'
             ;''  |  v' v`" W }  \\
            "    .'\    v  `v/^W,) '\)\.)\/)
                     `\   ,/,)'   ''')/^"-;'
                          \\
                           '". _
                                \\
        """
    if ran_num == 4:
        foe = ogre
        picture = """
                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\\
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \\
                   /      ,               \,-`\`_,-`\_,..--'\\
                  ,`    ,/,              ,>,   )     \--`````\\
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \\
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo
        """
    if ran_num == 5:
        foe = dragon
        picture = """
                 ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\\//    ))#############\\
   -###############\\     (oo)   //###############-
  -#################\\   / VV \ //#################-
 -###################\\ /      \/###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
        """

    def explore_battle():
        player.battle(foe)

    choices = {
        'Battle': explore_battle,
        'Retreat': player.retreat
    }
    questions = [
        inquirer.List('prompts',
                    message=f"You come across a level {foe.level} {foe.name}, what do you do?",
                    choices=list(choices.keys()),
                    ),
    ]
    print(picture)
    print(" ")
    answers = inquirer.prompt(questions, theme=BlueComposure())
    result = choices[answers['prompts']]()

def game_func(player):
    def explore():
        explore_func(player)
    
    choices = {
        'Check Stats': player.check_stats,
        'Explore': explore,
        'Train': player.train,
        'Quit': quit
    }
    questions = [
        inquirer.List('prompts',
                    message="Choose your action Adventurer!",
                    choices=list(choices.keys()),
                    ),
    ]
    answers = inquirer.prompt(questions, theme=BlueComposure())
    result = choices[answers['prompts']]()
    if answers['prompts'] != quit:
        return game_func(player)

player = Being()
game_func(player)