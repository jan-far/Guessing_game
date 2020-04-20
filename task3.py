import random


def limiter(count, num):
    while count != 0:
        try:
            guess = int(input('Guess a number: '))
            count -= 1
            if guess == (random.randint(1, num)):
                print('YOU GOT IT RIGHT!')
                break
            else:
                print("\n That was Wrong!")
                if count > 1:
                    print(f'You have {count} guesses left\n')
                else:
                    print(f'You have {count} guess left\n')
        except UnboundLocalError:
            print("Variable 'guess' not defined")
        except ValueError:
            print("Invalid value, please input a number")
    else:
        print('You ran out of guessing Life')
        print('GMAE OVER!')


def easy():
    print('''	__EASY LEVEL__ You have 6 GUESSES....''')
    limiter(6, 10)


def medium():
    print('''	__MEDIUM LEVEL__ You have 4 guesses...''')
    limiter(4, 20)


def hard():
    print('''	__HARD LEVEL__ You have 3 guesses...''')
    limiter(3, 50)


def choice():
    user_choice = input('Enter your desired level: ').upper()
    if user_choice == 'EASY':
        easy()
    elif user_choice == 'MEDIUM':
        medium()
    elif user_choice == 'HARD':
        hard()
    else:
        print("Not a valid LEVEL, try again")
        choice()


print('''There are 3 levels;
    EASY,
    MEDIUM,
    HARD \n''')

choice()