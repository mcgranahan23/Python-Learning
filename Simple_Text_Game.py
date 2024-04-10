
# Miles McGranahan

rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}


def gh():
    print('You are in the Great Hall')
    m = input('Enter next move: ')
    while m != 'south' and m != 'exit':
        m = (input('Invalid move, Enter next move: '))
    if m == 'south':
        print('Moving to the ', rooms['Great Hall']['South'])
        return br()
    if m == 'exit':
        print('Thank you for playing.')
        exit()
    else:
        print('error gh')
        return


def br():
    print('You are in the Bedroom')
    brm = input('Enter next move:')
    if brm == 'exit':
        print('Thank you for playing.')
        exit()
    while brm != 'north' and brm != 'east':
        brm = (input('Invalid move, Enter next move: '))
    if brm == 'north':
        print('Moving to the', rooms['Bedroom']['North'])
        return gh()
    elif brm == 'east':
        print('Moving to the', rooms['Bedroom']['East'])
        return cl()
    else:
        print('error br')
        return


def cl():
    print('You are in the Cellar')
    c = input('Enter next move: ')
    if c == 'exit':
        print('Thank you for playing.')
        exit()
    while c != 'west' and c != 'east':
        c = (input('Invalid move, Enter next move: '))
    if c == 'west':
        print('Moving to the', rooms['Great Hall']['South'])
        return br()
    if c == 'east':
        return end()
    else:
        print('error cl')
        return


def end():
    print('You have reached the end of the game.')
    print('Would you like to continue playing? y/n ')
    e = input('')
    if e == 'exit':
        print('Thank you for playing.')
        exit()
    if e == 'n':
        print('Thank you for playing.')
        exit()
    if e == 'y':
        print('Moving to the', rooms['Bedroom']['North'])
        return gh()


directions = ['north', 'south', 'east', 'west']
print('You are starting in the', rooms['Bedroom']['North'])
print()
movement = input('Enter first move: ')

while movement != 'exit':

    if movement in directions:
        move = movement

        if move == 'south':
            print('Moving to the', rooms['Great Hall']['South'])
            br()
        else:
            input('Invalid move, enter first move:')
    else:
        print('Invalid direction, use: east, north, south, west')
        break
else:
    print('Goodbye, thanks for playing!')
