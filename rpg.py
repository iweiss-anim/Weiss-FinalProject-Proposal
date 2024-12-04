def main():
    battling = True
    knight_hp = 200
    wizard_hp = 150
    dentist_hp = 100
    boss_hp = 1000
    if (knight_hp <= 0) and (wizard_hp <= 0) and (dentist_hp <= 0):
        battling = False
    if (boss_hp <= 0)
        battling = False

def knight_turn(knight_hp, boss_hp):
    if knight_hp > 0:
        knight_move_choice = str(input("Knight: ATTACK or DEFEND"))
        if knight_move_choice == "ATTACK":
            boss_hp == boss_hp - 40
            print("Knight struck valiantly for 40 damage!")
        elif knight_move_choice == "DEFEND":
            if knight_cooldown = False:
                is_knight_defending = True
                knight_cooldown = True
            elif knight_cooldown = True:
                print("Knight cannot defend twice in a row!")
                


            


def gameloop():
    knight_turn():