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
is_wizard_charging = False
dentist_cooldown = False
is_boss_charging = False
is_knight_down = False
is_wizard_down = False
is_dentist_down = False

def hp_calc():
    global battle_lost
    global battle_won
    global battling
    global knight_hp
    global wizard_hp
    global dentist_hp
    global boss_hp
    global is_knight_down
    global is_wizard_down
    global is_dentist_down
    if knight_hp <= 0:
        is_knight_down = True
    else:
        is_knight_down == False
    if wizard_hp <= 0:
        is_wizard_down = True
    else:
        is_wizard_down == False
    if dentist_hp <= 0:
        is_dentist_down = True
    else:
        is_dentist_down == False
    if (is_knight_down == True) and (is_wizard_down == True) and (is_dentist_down == True):
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
        print(f"\n                                                    Knight HP: {knight_hp}")
        print(f"                                                    Wizard HP: {wizard_hp}")
        print(f"                                                    Dentist HP: {dentist_hp}")
        print(f"                                                    Boss HP: {boss_hp}\n")
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
            print("Knight struck valiantly for 40 damage!\n")
            knight_cooldown = False
        elif knight_move_choice == "DEFEND":
            if knight_cooldown == False:
                is_knight_defending = True
                knight_cooldown = True
                print("Knight raises their shield! Next damage negated!\n")
            elif knight_cooldown == True:
                print("Knight cannot defend twice in a row!\n")
                knight_cooldown = False

def wizard_turn():
    global boss_hp
    global wizard_hp
    global is_wizard_charging

    if wizard_hp > 0:
        if is_wizard_charging == False:
            wizard_move_choice = str(input("Wizard: ATTACK or CHARGE\n"))
            if wizard_move_choice == "ATTACK":
                boss_hp = boss_hp - 50
                print("Wizard cast a fireball for 50 damage!\n")
            elif wizard_move_choice == "CHARGE":
                is_wizard_charging = True
                print("Wizard begins to cast a powerful spell!\n")
        elif is_wizard_charging == True:
            boss_hp = boss_hp - 150
            print("Wizard summons a thunderstorm for 150 damage!\n")
            is_wizard_charging = False

def dentist_turn():
    global boss_hp
    global dentist_hp
    global knight_hp
    global wizard_hp
    global is_boss_charging
    if dentist_hp > 0:
        dentist_move_choice = str(input("Dentist: ATTACK or HEAL\n"))
        if dentist_move_choice == "ATTACK":
            boss_hp = boss_hp - 30
            print("Dentist jabbed with needles for 30 damage!\n")
            dentist_cooldown = False
        elif dentist_move_choice == "HEAL":
            if dentist_cooldown == False:
                heal_target = str(input("Heal Target: KNIGHT, WIZARD, or DENTIST\n"))
                if heal_target == "KNIGHT":
                    knight_hp = knight_hp + 100
                    print("Dentist gave Knight a check-up! Healed 100 HP!\n")
                elif heal_target == "WIZARD":
                    wizard_hp = wizard_hp + 100
                    print("Dentist gave Wizard a check-up! Healed 100 HP!\n")
                elif heal_target == "DENTIST":
                    dentist_hp = dentist_hp + 100
                    print("Dentist gave themselves a check-up!? Healed 100 HP!\n")
                elif heal_target == "BOSS":
                    boss_hp = boss_hp + 100
                    print("Dentist gave the boss a check-up!? WHY!? Healed 100 HP...\n")
                dentist_cooldown = True
                print("Knight raises their shield! Next damage negated!\n")
            elif dentist_cooldown == True:
                print("Dentist cannot heal twice in a row!\n")
                dentist_cooldown = False

def boss_turn():
    global boss_hp
    global knight_hp
    global wizard_hp
    global dentist_hp
    global is_boss_charging
    if is_boss_charging == False:
        boss_move_choice = random.randint(1,3)
        if boss_move_choice == 1:
            # RANDOMLY CHOOSE PARTY MEMBER
            # boss_attack_target == 
            print("BOSS ATTACK 1")
        elif boss_move_choice == 2:
            if is_knight_defending == False:
                knight_hp = knight_hp - 30
                wizard_hp = wizard_hp - 30
                dentist_hp = dentist_hp - 30
                print("Boss pelts the party with moderately-sized rocks!")
            elif is_knight_defending == True:
                print("Knight defended the party!")
        elif boss_move_choice == 3:
            # RANDOMLY CHOOSE PARTY MEMBER
            # boss_charge_target == 
            print("BOSS ATTACK 3")

    elif is_boss_charging == True:
        print("BOSS USES THEIR CHARGED ATTACK")

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