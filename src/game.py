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
        time.sleep(5)
        train_exp = self.level*25
        self.exp_to_next_level = self.exp_to_next_level - 100
        if self.exp_to_next_level <= 0:
            self.level += 1
            self.exp_to_next_level = self.level*100
            self.health = self.level*10
            self.attack_damage_range = f"{math.floor(self.level/2)} - {self.level}"
        print("You practice some new combat techniques, and gain some EXP points.")
        print(" ")
    
    def attack(self, opponent):
        damage = random.randint(math.floor(self.level/2), self.level)
        opponent.health = opponent.health - damage
    
    def retreat(self):
        exp = self.level*100
        current_exp = exp - self.exp_to_next_level
        exp_lost = current_exp/2
        self.exp_to_next_level = self.exp_to_next_level + exp_lost

    def battle(self, opponent):
        turn = True
        self_health = self.health
        opponent_health = opponent.health
        while True:
            if turn == True:
                self.attack(opponent)
                opponent_health = opponent.health
                print(f"{self.name} attacks {opponent.name}")
                print(f"{opponent.name} Health = {opponent.health}")
                print(" ")
            if turn == False:
                opponent.attack(self)
                self_health = self.health
                print(f"{opponent.name} attacks {self.name}")
                print(f"{self.name} Health = {self.health}")
                print(" ")
            if self_health < 1:
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
            if opponent_health < 1:
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
                print(f"You Defeated {opponent.name}!")
                print(f"You Gained {opponent.exp_to_next_level} EXP")
                print(" ")
                self.exp_to_next_level = self.exp_to_next_level - opponent.exp_to_next_level
                if self.exp_to_next_level <= 0:
                    self.level += 1
                    self.exp_to_next_level = self.level*100
                    self.health = self.level*10
                    self.attack_damage_range = f"{math.floor(self.level/2)} - {self.level}"
                self.health = self.level*10
                break
            turn = not turn
            time.sleep(1)

def explore_func(player):
    goblin = Being("Goblin", random.randint(math.ceil(player.level/2), player.level))
    rogue_knight = Being("Rogue Knight", random.randint(math.ceil(player.level/1.8), math.ceil(player.level*1.2)))
    werewolf = Being("Werewolf", random.randint(math.ceil(player.level/1.6), math.ceil(player.level*1.4)))
    ogre = Being("Ogre", random.randint(math.ceil(player.level/1.4), math.ceil(player.level*1.6)))
    dragon = Being("Dragon", random.randint(math.ceil(player.level/1.2), math.ceil(player.level*1.8)))

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
        'Attack': explore_battle,
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