import random

battling = True
battle_lost = False
battle_won = False
knight_hp = 200
wizard_hp = 150
dentist_hp = 100
boss_hp = 500
knight_cooldown = False
is_knight_defending = False
wizard_cooldown = False
is_wizard_charging = False
dentist_cooldown = False
is_boss_charging = False

def hp_calc():
    global battle_lost
    global battle_won
    global battling
    global knight_hp
    global wizard_hp
    global dentist_hp
    global boss_hp
    if (knight_hp <= 0) and (wizard_hp <= 0) and (dentist_hp <= 0):
        battle_lost = True
        battling = False
    if (boss_hp <= 0):
        battle_won = True
        battling = False
    if knight_hp > 200:
        knight_hp = 200
    if wizard_hp > 150:
        wizard_hp = 150
    if dentist_hp > 100:
        dentist_hp = 100
    if boss_hp > 500:
        boss_hp = 500
    if knight_hp < 0:
        knight_hp = 0
    if wizard_hp < 0:
        wizard_hp = 0
    if dentist_hp < 0:
        dentist_hp = 0

def display_health():
    display_health_ask = str(input("Check HP Totals? YES or NO\n"))
    if display_health_ask == "YES":
        global knight_hp
        global wizard_hp
        global dentist_hp
        global boss_hp
        print(f"                                                    \nKnight HP: {knight_hp}")
        print(f"                                                    Wizard HP: {wizard_hp}")
        print(f"                                                    Dentist HP: {dentist_hp}")
        print(f"                                                    Boss HP: {boss_hp}/n")
    elif display_health_ask == "NO":
        print("\n")

def knight_turn():
    global boss_hp
    global knight_hp
    global knight_cooldown
    global is_knight_defending
    if knight_hp > 0:
        knight_move_choice = str(input("Knight: ATTACK or DEFEND\n"))
        if knight_move_choice == "ATTACK":
            boss_hp = boss_hp - 40
            print("Knight struck valiantly for 40 damage!")
            knight_cooldown = False
        elif knight_move_choice == "DEFEND":
            if knight_cooldown == False:
                is_knight_defending = True
                knight_cooldown = True
                print("Knight raises their shield! Next damage negated!")
            elif knight_cooldown == True:
                print("Knight cannot defend twice in a row!")
                knight_cooldown = False

def wizard_turn():
    global boss_hp
    global wizard_hp
    global wizard_cooldown
    global is_wizard_charging

    if wizard_hp > 0:
        if wizard_cooldown == False:
            wizard_move_choice = str(input("Wizard: ATTACK or CHARGE\n"))
            if wizard_move_choice == "ATTACK":
                boss_hp = boss_hp - 50
                print("Wizard cast a fireball for 50 damage!")
            elif wizard_move_choice == "CHARGE":
                is_wizard_charging = True
                wizard_cooldown = True
                print("Wizard begins to cast a powerful spell!")
        elif wizard_cooldown == True:
            boss_hp = boss_hp - 150
            print("Wizard summons a thunderstorm for 150 damage!")
            wizard_cooldown = False

def dentist_turn():
    global boss_hp
    global dentist_hp
    global knight_hp
    global wizard_hp
    global dentist_cooldown
    if dentist_hp > 0:
        dentist_move_choice = str(input("Dentist: ATTACK or HEAL\n"))
        if dentist_move_choice == "ATTACK":
            boss_hp = boss_hp - 30
            print("Dentist jabbed with needles for 30 damage!")
            dentist_cooldown = False
        elif dentist_move_choice == "HEAL":
            if dentist_cooldown == False:
                heal_target = str(input("Heal Target: KNIGHT, WIZARD, or DENTIST\n"))
                if heal_target == "KNIGHT":
                    knight_hp = knight_hp + 100
                    print("Dentist gave Knight a check-up! Healed 100 HP!")
                elif heal_target == "WIZARD":
                    wizard_hp = wizard_hp + 100
                    print("Dentist gave Wizard a check-up! Healed 100 HP!")
                elif heal_target == "DENTIST":
                    dentist_hp = dentist_hp + 100
                    print("Dentist gave themselves a check-up!? Healed 100 HP!")
                elif heal_target == "BOSS":
                    boss_hp = boss_hp + 100
                    print("Dentist gave the boss a check-up!? WHY!? Healed 100 HP...")
                dentist_cooldown = True
                print("Knight raises their shield! Next damage negated!")
            elif dentist_cooldown == True:
                print("Dentist cannot heal twice in a row!")
                dentist_cooldown = False

def boss_turn():
    boss_move_choice = random.randint(1,3)
    if boss_move_choice == 1:
        print("BOSS ATTACK 1")
    elif boss_move_choice == 2:
        print("BOSS ATTACK 2")
    elif boss_move_choice == 3:
        print("BOSS ATTACK 3")

while battling is True:
    knight_turn()
    hp_calc()
    display_health()
    wizard_turn()
    hp_calc()
    display_health()
    dentist_turn()
    hp_calc()
    display_health()

if battle_lost == True:
    print("The party was defeated...")
if battle_won == True:
    print("The party was victorious!")