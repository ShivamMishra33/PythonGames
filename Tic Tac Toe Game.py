def Win_List(inputs):
    winner_list = [inputs[0:3], inputs[3:6], inputs[6:], inputs[0::3], inputs[1::3], inputs[2::3],
                   inputs[0::4], inputs[2:7:2]]
    return winner_list


def User_Input(input_word, sym):
    while True:
        new = input('Enter the coordinates:').split(' ')
        if len(new[0]) > 1 or len(new[1]) > 1:
            print('You should enter numbers!')
            continue
        user = [int(ele) for ele in new]
        inputs = [letter for letter in input_word]
        if user[0] not in [1, 2, 3] or user[1] not in [1, 2, 3]:
            print('Coordinates should be from 1 to 3!')
        elif user[0] == 1 and user[1] == 3:
            if inputs[0] == ' ':
                inputs[0] = sym
                break
            elif inputs[0] != ' ':
                print('This cell is occupied! Choose another one!')
        elif user[0] == 1 and user[1] == 2:
            if inputs[3] == ' ':
                inputs[3] = sym
                break
            elif inputs[3] != ' ':
                print('This cell is occupied! Choose another one!')
        elif user[0] == 1 and user[1] == 1:
            if inputs[6] == ' ':
                inputs[6] = sym
                break
            elif inputs[6] != ' ':
                print('This cell is occupied! Choose another one!')
        elif user[0] == 2 and user[1] == 3:
            if inputs[1] == ' ':
                inputs[1] = sym
                break
            elif inputs[1] != ' ':
                print('This cell is occupied! Choose another one!')
        elif user[0] == 2 and user[1] == 2:
            if inputs[4] == ' ':
                inputs[4] = sym
                break
            elif inputs[4] != ' ':
                print('This cell is occupied! Choose another one!')
        elif user[0] == 2 and user[1] == 1:
            if inputs[7] == ' ':
                inputs[7] = sym
                break
            elif inputs[7] != ' ':
                print('This cell is occupied! Choose another one!')
        elif user[0] == 3 and user[1] == 3:
            if inputs[2] == ' ':
                inputs[2] = sym
                break
            elif inputs[2] != ' ':
                print('This cell is occupied! Choose another one!')
        elif user[0] == 3 and user[1] == 2:
            if inputs[5] == ' ':
                inputs[5] = sym
                break
            elif inputs[5] != ' ':
                print('This cell is occupied! Choose another one!')
        elif user[0] == 3 and user[1] == 1:
            if inputs[8] == ' ':
                inputs[8] = sym
                break
            elif inputs[8] != ' ':
                print('This cell is occupied! Choose another one!')

    return "".join(inputs)


def Status(element):
    print('---------')
    print(f'| {element[0]} {element[1]} {element[2]} |')
    print(f'| {element[3]} {element[4]} {element[5]} |')
    print(f'| {element[6]} {element[7]} {element[8]} |')
    print('---------')


def Check(inp):
    win = Win_List(inp)
    if 'OOO' in win:
        return 'O wins'
    elif 'XXX' in win:
        return 'X wins'
    elif inp.count(' ') == 0:
        return 'Draw'


# main program
inputs_ = '_________'
inputs_ = inputs_.replace('_', ' ')
Status(inputs_)
new_inputs = User_Input(inputs_, 'X')
Status(new_inputs)
while True:
    new_inputs = User_Input(new_inputs, 'O')
    Status(new_inputs)
    result = Check(new_inputs)
    if result == 'X wins' or result == 'O wins' or result == 'Draw':
        print(result)
        break

    new_inputs = User_Input(new_inputs, 'X')
    Status(new_inputs)
    result = Check(new_inputs)
    if result == 'X wins' or result == 'O wins' or result == 'Draw':
        print(result)
        break
