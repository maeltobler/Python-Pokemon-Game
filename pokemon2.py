import os
os.system("cls")

import sys, time
import random
from tkinter import *



#Leben
YourHealth =  100
OppHealth = 90
#Player Attacke Variable
QuickAttack = 15
Thunderbolt = 30
Tackle = 25
#Gegner Attacke Variable
Tackle2 = 25
QuickAttack2 = 15


#Text printet 1 vs 1
def print1by1(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print
#Ninetendo Logo
print(''' \u001b[31m
  _   _ _____ _   _ _______ ______ _   _ _____   ____  
 | \ | |_   _| \ | |__   __|  ____| \ | |  __ \ / __ \ 
 |  \| | | | |  \| |  | |  | |__  |  \| | |  | | |  | |
 | . ` | | | | . ` |  | |  |  __| | . ` | |  | | |  | |
 | |\  |_| |_| |\  |  | |  | |____| |\  | |__| | |__| |
 |_| \_|_____|_| \_|  |_|  |______|_| \_|_____/ \____/ 
\u001b[0m
''')
time.sleep(2)
print1by1('Loading...Loading...Loading...Loading...Loading\n')
time.sleep(2)
print('''




''')
time.sleep(1)
print1by1('Herzlich Willkommen bei Nintendo\n')
time.sleep(1)
#Spieler Battle Code
def gameFight(yH, oH, gO, dO, QuickAttack, Thunderbolt, Tackle) :
    OppHealth = oH
    if gO == '1' :
      OppHealth = OppHealth - QuickAttack
      time.sleep(0.5)
      print1by1('\nDein Pokemon benutzt Quick Attack\n')
    if gO == '2' :
      OppHealth = OppHealth - Thunderbolt
      time.sleep(0.5)
      print1by1('\nDein Pokemon benutzt Thunderbolt\n')
    if gO == '3' :
      OppHealth = OppHealth - Tackle
      time.sleep(0.5)
      print1by1('\nDein Pokemon benutzt Tackle\n')
    print1by1("Das Leben des gegners fällt zu %s\n" % OppHealth)
    return (OppHealth, QuickAttack, Thunderbolt, Tackle)
#Gegner Battle Code
def oppBattle(OppHealth, Randopp, QuickAttack2, Tackle2) :
    if Randopp == 'Tackle' :
        if OppHealth <= 0 :
          print1by1('\nBulbasaur wird ohnmächtig\n')
          print1by1('Du schlägst Trainer Bob\n')
          exit()
        else:
          time.sleep(0.5)
          print1by1('\nBulbasaur benutzt Tackle\n')
          YourHealth = 100 - Tackle2
          Tackle2 = Tackle2 + 25
          print1by1("Dein Leben fällt zu %s\n" % YourHealth)
    if Randopp == 'Quick Attack' :
        if OppHealth <= 0 :
          print1by1('Bulbasaur fainted\n')
          print1by1('Du schlägst Trainer Bob\n')
          exit()
          time.sleep(0.5) 
        else:
          print1by1('\nbulbasaur benutzt Quick Attack\n')
          YourHealth = 100 - QuickAttack2
          QuickAttack2 = QuickAttack2 + 15
          print1by1("Dein Leben fällt zu %s\n" % YourHealth)
    return (YourHealth, QuickAttack2, Tackle2)

#Pokemon Logo
print(''' \u001b[33m
                                    ,'
     _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|\u001b[0m
''')
#Wie heisst du
print1by1("Wie heisst du?")
WNinput = input('\n>> ')
print1by1('\nLass uns kämpfen %s!' % WNinput)

#Einleitung
time.sleep(0.5)
print1by1('\nDu wurdest von Trainer Bob herausgefordert\n')
time.sleep(0.5)
print1by1('\nTrainer Bob schickt Bulbasaur in den Kampf\n')
print(''' \u001b[32m
              `;,;.;,;.;.'
              ..:;:;::;: 
        ..--''' '' ' ' '''--.  
      ; .   .'        '.   .`;
     | /    /            \   '.|
     | |   :             :    :|
   .'| |   :             :    :|
 ,: /\ \.._\ __..===..__/_../ /`.
|'' |  :.|  `'          `'  |.'  ::.
|   |  ''|    :'';          | ,  `'':
|.:  \/  | /'-.`'   ':'.-'\ |  \,   |
| '  /  /  | / |...   | \ |  |  |';'|
 \ _ |:.|  |_\_|`.'   |_/_|  |.:| _ |
/,.,.|' \__       . .      __/ '|.,.,;
     | ':`.`----._____.---'.'   |
      \   `:"""-------'""' |   |
       ',-,-',             .'-=,=,
\u001b[0m
''')
time.sleep(0.5)
print1by1('\nDu erhälst einen Pokeball\n')
time.sleep(0.5)
print(''' \u001b[31m
        ▄███████████▄
     ▄███▓▓▓▓▓▓▓▓▓▓▓███▄
    ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███
   ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
 ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██
███████████░░███░░███████████
██░░░░░░░██░░███░░██░░░░░░░██
██░░░░░░░░██░░░░░██░░░░░░░░██
██░░░░░░░░░███████░░░░░░░░░██
 ██░░░░░░░░░░░░░░░░░░░░░░░██
  ██░░░░░░░░░░░░░░░░░░░░░██
   ██░░░░░░░░░░░░░░░░░░░██
    ███░░░░░░░░░░░░░░░███
     ▀███░░░░░░░░░░░███▀
        ▀███████████▀
\u001b[0m
''')
time.sleep(0.5)
print1by1('\nWelches Pokemon möchtest du wählen?\n')
time.sleep(0.5)
print('''
\tPickachu
\tSquirtle
\tCharmander
''')
time.sleep(0.5)
Pokemon_choice = input()
if Pokemon_choice == 'Pickachu':
  print(''' \u001b[33m
 quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     '
        :##.       ==             .###.       `.      `.    `'
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap'
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:'
\u001b[0m

Ein wildes Pickachu erscheint! Ab in den Kampf!

\u001b[31m Um käpfen zu können darfst du nur die Zahl der Attacke eingeben! \u001b[0m

  ''')


elif Pokemon_choice == 'Squirtle':
  print(''' \u001b[34m
                _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        '
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       '
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | '
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`."""""'-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     '
\_ .          |   `""""'    `.           . \     '
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"""`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              '
               \/    `""\"""""""`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'
\u001b[0m

 Ein wildes Squirtle erscheint! Ab in den Kampf!

 
\u001b[33m Um Kämpfen zu können darfst du nur die Zahl der Attacke eingeben! \u001b[0m

  ''')

elif Pokemon_choice == 'Charmander':
    print('''  \u001b[31m
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   '
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    |
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         """"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,'
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
                            `" " -'
  \u001b[0m

  Ein wildes Charmander erscheint! Ab in den Kampf!

  \u001b[33m Um kämpfen zu können darf nur die Zahl der Attacke eingegeben werden! \u001b[0m


    ''')
  





#Gegner moves
OppAttack = ['Tackle','Quick Attack']
Randopp = random.choice(OppAttack)



#Battle Algorithmus
while YourHealth >= 0  or OppHealth >= 0 :
  time.sleep(0.5)
  print1by1('\n1. Quick Attack -15 \n2. Thunderbolt -30\n3. Tackle -25\n')
  Attackinp = input('>> ')
  (OppHealth, QuickAttack, Thunderbolt, Tackle) = gameFight(YourHealth, OppHealth, Attackinp, "", QuickAttack, Thunderbolt, Tackle)
  (YourHealth, QuickAttack2, Tackle2) = oppBattle(OppHealth, Randopp, QuickAttack2, Tackle2)

  #Ende
  if YourHealth <= 0 :
    print1by1('Dein Pokemon ist in Ohnmacht gefallen\n')
    time.sleep(0.5)
    print1by1('Du wurdest ins nächste Pokemon Center gebracht\n')
    time.sleep(0.5)
    exit()
  if OppHealth <= 0 :
    print1by1('Bulbasaur ist in Ohnmacht gefallen\n')
    time.sleep(0.5)
    print1by1('Du schlägst Trainer Bob\n')
    time.sleep(0.5)
   
                                                                               

