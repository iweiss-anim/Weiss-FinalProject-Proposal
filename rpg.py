import random
import time

battling = True
battle_lost = False
battle_won = False
knight_hp = 200
wizard_hp = 150
dentist_hp = 100
boss_hp = 2000
knight_cooldown = False
is_knight_defending = False
is_wizard_charging = False
dentist_cooldown = False
is_boss_charging = False
is_knight_down = False
is_wizard_down = False
is_dentist_down = False

def cutscene_print(text):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(0.02)
    print()

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
    if boss_hp > 2000:
        boss_hp = 2000
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

def opening_cutscene():
    cutscene_print("Under the blood moon, an ancient evil stirs... (ENTER to continue)")
    input()
    cutscene_print("The most diabolical of eldritch forces... CAPITALISM")
    input()
    cutscene_print("And with it, our three intrepid heroes must face... The BOSS...")
    input()
    print("\nTHE BOSS APPROACHES!\n\n")
    
def knight_turn():
    global boss_hp
    global knight_hp
    global knight_cooldown
    global is_knight_defending
    if knight_hp > 0:
        knight_move_choice = str(input("Knight: ATTACK or DEFEND\n"))
        is_knight_defending = False
        if knight_move_choice == "ATTACK":
            boss_hp = boss_hp - 40
            cutscene_print("Knight struck valiantly for 40 damage!\n")
            knight_cooldown = False
        elif knight_move_choice == "DEFEND":
            if knight_cooldown == False:
                is_knight_defending = True
                knight_cooldown = True
                cutscene_print("Knight raises their shield! Next damage negated!\n")
            elif knight_cooldown == True:
                cutscene_print("Knight cannot defend twice in a row!\n")
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
                cutscene_print("Wizard cast a fireball for 50 damage!\n")
            elif wizard_move_choice == "CHARGE":
                is_wizard_charging = True
                cutscene_print("Wizard begins to cast a powerful spell!\n")
        elif is_wizard_charging == True:
            boss_hp = boss_hp - 150
            cutscene_print("Wizard summons a thunderstorm for 150 damage!\n")
            is_wizard_charging = False

def dentist_turn():
    global boss_hp
    global dentist_hp
    global knight_hp
    global wizard_hp
    global is_boss_charging
    global dentist_cooldown
    if dentist_hp > 0:
        dentist_move_choice = str(input("Dentist: ATTACK or HEAL\n"))
        if dentist_move_choice == "ATTACK":
            boss_hp = boss_hp - 30
            cutscene_print("Dentist jabbed with needles for 30 damage!\n")
            dentist_cooldown = False
        elif dentist_move_choice == "HEAL":
            if dentist_cooldown == False:
                heal_target = str(input("Heal Target: KNIGHT, WIZARD, or DENTIST\n"))
                if heal_target == "KNIGHT":
                    knight_hp = knight_hp + 100
                    dentist_cooldown = True
                    cutscene_print("Dentist gave Knight a check-up! Healed 100 HP!\n")
                elif heal_target == "WIZARD":
                    wizard_hp = wizard_hp + 100
                    dentist_cooldown = True
                    cutscene_print("Dentist gave Wizard a check-up! Healed 100 HP!\n")
                elif heal_target == "DENTIST":
                    dentist_hp = dentist_hp + 100
                    dentist_cooldown = True
                    cutscene_print("Dentist gave themselves a check-up!? Healed 100 HP!\n")
                elif heal_target == "BOSS":
                    boss_hp = boss_hp + 100
                    dentist_cooldown = True
                    cutscene_print("Dentist gave the boss a check-up!? WHY!? Healed 100 HP...\n")
            elif dentist_cooldown == True:
                cutscene_print("Dentist cannot heal twice in a row!\n")
                dentist_cooldown = False

def boss_turn():
    global boss_hp
    global knight_hp
    global wizard_hp
    global dentist_hp
    global is_boss_charging
    global is_knight_defending
    if is_boss_charging == False:
        boss_move_choice = random.randint(0,2)
        if boss_move_choice == 0:
            if is_knight_defending == False:
                boss_attack_target = random.randint(0,2)
                if boss_attack_target == 0:
                    if is_knight_down == False:
                        knight_hp = knight_hp - 50
                        print("Boss attacks!")
                        cutscene_print("Boss attacked Knight for 50 damage!")
                    elif is_knight_down == True:
                        if is_wizard_down == False:
                            wizard_hp = wizard_hp - 50
                            print("Boss attacks!")
                            cutscene_print("Boss attacked Wizard for 50 damage!")
                        elif is_wizard_down == True:
                            dentist_hp = dentist_hp - 50
                            print("Boss attacks!")
                            cutscene_print("Boss attacked Dentist for 50 damage!")
                elif boss_attack_target == 1:
                    if is_wizard_down == False:
                            wizard_hp = wizard_hp - 50
                            print("Boss attacks!")
                            print("Boss attacked Wizard for 50 damage!")
                    elif is_wizard_down == True:
                        if is_dentist_down == False:
                            dentist_hp = dentist_hp - 50
                            print("Boss attacks!")
                            cutscene_print("Boss attacked Dentist for 50 damage!")
                        elif is_dentist_down == True:
                            knight_hp = knight_hp - 50
                            print("Boss attacks!")
                            cutscene_print("Boss attacked Knight for 50 damage!")
                elif boss_attack_target == 2:
                    if is_dentist_down == False:
                            dentist_hp = dentist_hp - 50
                            print("Boss attacks!")
                            cutscene_print("Boss attacked Dentist for 50 damage!")
                    elif is_dentist_down == True:
                        if is_knight_down == False:
                            knight_hp = knight_hp - 50
                            print("Boss attacks!")
                            cutscene_print("Boss attacked Knight for 50 damage!")
                        elif is_knight_down == True:
                            wizard_hp = wizard_hp - 50
                            print("Boss attacks!")
                            cutscene_print("Boss attacked Wizard for 50 damage!")
            elif is_knight_defending == True:
                print("Boss attacks!")
                cutscene_print("Knight defended the party! Damage negated!")
        elif boss_move_choice == 1:
            if is_knight_defending == False:
                knight_hp = knight_hp - 30
                wizard_hp = wizard_hp - 30
                dentist_hp = dentist_hp - 30
                print("Boss pelts the party with moderately-sized rocks!")
                cutscene_print("30 damage to all party members!")
            elif is_knight_defending == True:
                print("Boss pelts the party with moderately-sized rocks!")
                cutscene_print("Knight defended the party! Damage negated!")
        elif boss_move_choice == 2:
            is_boss_charging = True
            cutscene_print("Boss began charging a POWERFUL ATTACK!")
    elif is_boss_charging == True:
        if is_knight_defending == False:
            boss_attack_target = random.randint(0,2)
            if boss_attack_target == 0:
                if is_knight_down == False:
                    knight_hp = knight_hp - 999
                    print("BOSS ATTACKS WITH FULL FORCE!")
                    cutscene_print("Boss strikes down Knight! 999 Damage!")
                    is_boss_charging = False
                elif is_knight_down == True:
                    if is_wizard_down == False:
                        wizard_hp = wizard_hp - 999
                        print("BOSS ATTACKS WITH FULL FORCE!")
                        cutscene_print("Boss strikes down Wizard! 999 Damage!")
                        is_boss_charging = False
                    elif is_wizard_down == True:
                        dentist_hp = dentist_hp - 999
                        print("BOSS ATTACKS WITH FULL FORCE!")
                        cutscene_print("Boss strikes down Dentist! 999 Damage!")
                        is_boss_charging = False
            elif boss_attack_target == 1:
                if is_wizard_down == False:
                        wizard_hp = wizard_hp - 999
                        print("BOSS ATTACKS WITH FULL FORCE!")
                        cutscene_print("Boss strikes down Wizard! 999 Damage!")
                        is_boss_charging = False
                elif is_wizard_down == True:
                    if is_dentist_down == False:
                        dentist_hp = dentist_hp - 999
                        print("BOSS ATTACKS WITH FULL FORCE!")
                        cutscene_print("Boss strikes down Dentist! 999 Damage!")
                        is_boss_charging = False
                    elif is_dentist_down == True:
                        knight_hp = knight_hp - 999
                        print("BOSS ATTACKS WITH FULL FORCE!")
                        cutscene_print("Boss strikes down Knight! 999 Damage!")
                        is_boss_charging = False
            elif boss_attack_target == 2:
                if is_dentist_down == False:
                        dentist_hp = dentist_hp - 999
                        print("BOSS ATTACKS WITH FULL FORCE!")
                        cutscene_print("Boss strikes down Dentist! 999 Damage!")
                        is_boss_charging = False
                elif is_dentist_down == True:
                    if is_knight_down == False:
                        knight_hp = knight_hp - 999
                        print("BOSS ATTACKS WITH FULL FORCE!")
                        cutscene_print("Boss strikes down Knight! 999 Damage!")
                        is_boss_charging = False
                    elif is_knight_down == True:
                        wizard_hp = wizard_hp - 999
                        print("BOSS ATTACKS WITH FULL FORCE!")
                        cutscene_print("Boss strikes down Wizard! 999 Damage!")
                        is_boss_charging = False
            is_boss_charging = False
        elif is_knight_defending == True:
            print("Boss attacks!")
            cutscene_print("Knight defended the party! Damage negated!")
            is_boss_charging = False
        is_boss_charging = False

opening_cutscene()

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
    boss_turn()
    hp_calc()
    display_health()

if battle_lost == True:
    print("The party was defeated...")
if battle_won == True:
    print("The party was victorious!")