
def getage():

    age = int(input('How old are you:    '))

    while age < 18:
        remainder = 18 - age
        print(f'you are {age} years old')
        print(f'you have {remainder} more years')
        print(f'you are under-age! try again!')
        age = int(input('what is your age: '))



        if age > 18:
            increment = age - 18
            print('you are good to go')
            print(f'you are {age} years old ,you have been an adult for {increment} years :)')

def identity():
    adult = input('Are you an adult?y(yes) or n (no):  ')

    if adult == 'yes':
        print('okay :-), let\'s find out')
        findout = getage()
        print(findout)

    elif adult == 'no':
        findout = getage()
        print(findout)


identity()



