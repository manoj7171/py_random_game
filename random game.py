import random

com_amount = 1000
user_amount = 100
round = 1

while com_amount >0 and user_amount >0:
    print('\n=====================\n')
    print('round ',round)

    if round%2 == 1:
        try:
            x = float(input(f'Enter your betting amount in multipication of 10 and less than Rs.{user_amount}. Enter 0 to exit : '))
            if x>user_amount:
                print(f'Please enter amount less than {user_amount}')
                continue
            if x%10 !=0:
                print('Type value in multipication of 10')
                continue
            if x == 0:
                print('Game Exit')
                break

            user_value = input('enter your betting l for low h for high : ')
            if user_value =='l':
                print('you say low. So I say high')
            elif user_value == 'h':
                print('you say high. So I say low')
            else:
                print('Error : enter correct letter l or h')
                continue
        except:
            print('please enter a reliable value')
            continue        
        
    else:
        com_value = random.randint(1, 6)*3
        x=user_amount
        while x >= user_amount and x>=com_amount:
            x = random.randint(1, 10)*10
        print('I bet Rs.',x)

        if com_value < 10:
            user_value = 'h'
            print('I say low So you are high')
        else:
            user_value = 'l'
            print('I say High So you are low')

    value = random.randint(1, 6)*3
    print('The Random value is ',value,' & ',end='')
    if value < 10:
        print('is low')
        if user_value == 'l':
            print('congratulation you won')
            com_amount = com_amount - x
            user_amount = user_amount + x
        else:
            print('sorry, I won') 
            com_amount = com_amount + x
            user_amount = user_amount - x   
    else:
        print('is high')
        if user_value == 'h':
            print('congratulation you win')
            com_amount = com_amount - x
            user_amount = user_amount + x
        else:
            print('sorry, I won') 
            com_amount = com_amount + x
            user_amount = user_amount - x 

        
    print('\nyou have Rs.',user_amount)
    print('I have Rs.',com_amount)
    round = round + 1


