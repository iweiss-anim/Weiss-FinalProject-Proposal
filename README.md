Project Title: RPGs: "Just How You Remember 'Em!"

Video URL: https://youtu.be/XSJHXDaGNWk

GitHub URL: https://github.com/iweiss-anim/Weiss-FinalProject-Proposal

*RPGs: "Just How You Remember 'Em!"* is a text-based, RPG-inspired demo, containing a fully-programmed battle system and a boss fight. Taking inspiration from classic RPG tropes, the demo utilizes traditional roles for two of its party members, being the Knight and the Wizard. The third party member, however, being the group's healer, is a dentist. The enemy present in the boss fight is simply named "Boss". While this started out as a placeholder name, I later decided to keep it, with the context of the Boss being an actual corporate boss of a company. 

The programming of the game relies on several key features. First, every character has a set amount of health points, which are managed by the hp_calc function. This function ensures that characters' HP cannot exceed their maximum, and is used to declare a character "Down" when their HP reaches zero. The "is_(character)_down" variables do not prevent the party members from being healed, still allowing for them to be revived. The main purpose of this condition is to prevent Boss from attacking characters who have already been defeated. 


The most important functions in the program make up each character's turns. The party members use if statements and player inputs to select one of two moves, their ATTACK or their secondary option. Knight's DEFEND is the first, enabling the "is_knight_defending" variable, which interacts with the Boss' attacks. This variable is reset to False at the beginning of the Knight's turn. The DEFEND command cannot be used two turns in a row. This is checked by the "knight_cooldown" variable, which is instead reset to false at the end of the Knight's next turn (After attacking or after failing a second DEFEND). 

Wizard's CHARGE works similarly, using the turn to set the "is_wizard_charging" variable to True. If Wizard's turn starts while the variable is true, the player input system is simply replaced by the Wizard casting the more powerful spell, then setting the variable back to False. 

The Dentist's HEAL functions much like the Knight's DEFEND, not being usable two turns in a row. In addition, the HEAL command lets the player choose a target to heal, between the Knight, Wizard, and the Dentist themselves. The HEAL move also has functionality to heal the Boss, which is not stated in the dialogue prompt, being an intentionally hidden easter egg. There is special dialogue present upon healing the Boss. 


The Boss' turn system works similarly to those of the party members, with the key difference being how they select their moves. Instead of using player-input, the Boss can use one of three attacks at random. 

The first attack simply deals damage to one party member, but the way the party member is selected is more complex. To start, the game generates a random number between 0 and 2. 0 selects the Knight, 1 selects the Wizard, and 2 selects the Dentist. However, These targets are dependant on which party members are Down. After the target is selected, the game checks if that party member is Down. If they are not, they are hit by the Boss' attack. If the selected party member is Down, however, the target will switch to the next party member, in the same order as they take their turns. If the second party member in the order is also Down, the move will hit the third, remaining, party member. 

The Boss' second attack is the simplest of the three, being an AOE move which damages all members of the party. The move requires no targeting system, instead dealing damage across the board. No measures are needed to prevent the Boss from attacking party members who are Down, as the hp_calc function prevents HP from dropping below 0. 

The Boss' third attack works similarly to the Wizard's, being a charge move. When the move is selected, "is_boss_charging" is set to True, and dialogue is displayed. At the beginning of the Boss' turns, the game checks if "is_boss_charging" is True. If it is True, then the random move selection is bypassed in order to complete the second turn of the charge attack. A party member is randomly selected using the same logic as the standard attack, with the main difference being that the charge is guaranteed to bring a party member down to 0 HP. 

The strategy for countering the Boss' charge attack is to use the Knight's DEFEND. However, thanks to the cooldown on DEFEND, the player must not be too hasty in using the command. If a player uses DEFEND on the same turn the Boss begins charging, they will be left vulnerable to having a party member defeated. Mechanically, the code for the Knight's DEFEND blocking Boss' attacks is simple. At the beginning of Boss' turn, the game checks if "is_knight_defending" is True. If it is True, the Boss' attack is unsuccessful, even on the second turn of its charge. 


The battle can end in two ways, being victory and defeat. These states are determined in the hp_calc function. If all party members' "is_(character)_down" variables are set to True, the "battle_lost" variable is made True, which ends the "battling" gameplay loop and displays loss dialogue. If the Boss' HP reaches zero, the "battle_won" variable is set to true, which also ends the loop, with different dialogue. 