battling = True
knight_hp = 200
wizard_hp = 150
dentist_hp = 100
boss_hp = 1000
if (knight_hp <= 0) and (wizard_hp <= 0) and (dentist_hp <= 0):
    battle_lost = True
    battling = False
if (boss_hp <= 0):
    battle_won = True
    battling = False

def knight_turn():
    global boss_hp
    if knight_hp > 0:
        knight_move_choice = str(input("Knight: ATTACK or DEFEND\n"))
        if knight_move_choice == "ATTACK":
            boss_hp = boss_hp - 500
            print("Knight struck valiantly for 40 damage!")
        elif knight_move_choice == "DEFEND":
            if knight_cooldown == False:
                is_knight_defending = True
                knight_cooldown = True
                print("Knight raises their shield! Next damage negated!")
            elif knight_cooldown == True:
                print("Knight cannot defend twice in a row!")

while battling is True:
    knight_turn()

while battling is False:
    if battle_lost == True:
        print("The party was defeated...")
    if battle_won == True:
        print("The party was victorious!")