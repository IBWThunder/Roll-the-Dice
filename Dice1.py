# making a dice roller game.
import random
print('Roll the dice by pressing [ENTER].')
dice_roll = input()
while dice_roll == '':
    dice_num = random.randint(1,6)
    print(dice_num)
    if dice_num == 6:
        print('You got the highest number!')
    elif dice_num == 1:
        print('You got the lowest number!')
    print('Do you wish to play again? (Y/N)')
    answer = input()
    if answer == 'n' or answer == 'N':
        break