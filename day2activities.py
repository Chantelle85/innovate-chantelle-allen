# #Activity 1
variable_1 =input("Enter a number")
if variable_1.isnumeric():
    print("This is a number")
else:
    print("This is not a number!")

#Activity 2
from random import randint as r

ghostbusters_char = [
    'Melissa McCarthy', 'Kristen Wiig', 'Kate McKinnon','Leslie Jones', 'Zach Woods', 'Ed Begley Jr.',
    'Charles Dance', 'John Milhiser', 'Ben Harris','Karan Soni', 'Bess Rous', 'Steve Higgins'
]

def ghostbusters_game(char_list):
    lives = 3
    print('How is your knowledge on the Ghostbusters cast list? Lets check, you have 3 lives. Press enter to continue')
    input()
    while lives > 0:
        question = r(0, 11)
        character = char_list[question]
        print(f'is {character} in the ghostbusters film? [Y/N]\n')
        user_answer = input()
        if question <= 8:
            if user_answer.capitalize() =="Y" or user_answer.capitalize() =="YES":
                print(f'{character} is a character in Ghostbusters!')
            elif user_answer.capitalize() =="N" or user_answer.capitalize() =="NO":
                 print(f'{character} is a character in Ghostbusters!')
            else:
                print(f'{character}'' is not a character in Ghostbusters')
        
    print('Sorry you have run out of lives!\n GAME OVER!')

ghostbusters_game(ghostbusters_char)



