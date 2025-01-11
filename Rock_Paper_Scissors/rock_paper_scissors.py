import ascii
import random

game_images = [ascii.rock, ascii.paper, ascii.scissors]
player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if 0 <= player_choice <= 2:
    print(game_images[player_choice])

bot_choice = random.randint(0, 2)
print('Computer choice: ')
print(game_images[bot_choice])


if player_choice >= 3 or player_choice < 0:
    print('You typed an invalid number. You lose!')
elif player_choice == 0 and bot_choice == 2:
    print('You win!')
elif bot_choice == 0 and player_choice == 2:
    print('You lose!')
elif bot_choice > player_choice:
    print('You lose!')
elif player_choice > bot_choice:
    print('You win!')
elif bot_choice == player_choice:
    print('It\'s a draw!')
