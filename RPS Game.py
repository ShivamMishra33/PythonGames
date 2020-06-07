import random


# instructions
def ins():
    with open('instructions.txt', 'r') as f1:
        for lines in f1:
            print(lines)


# checking if name and score are present
def rating(name):
    with open('score.txt', 'r') as f:
        score = 0
        for line in f:
            if name in line:
                a = line.split()
                score = int(a[1])
                break

        return score


# determine which game is being played
def determine_elements():
    your_choice = input('Enter the game you want to play...> ').split(',')
    if len(your_choice) <= 1:
        your_choice = ['rock', 'paper', 'scissors']
        return your_choice
    elif len(your_choice) >= 1:
        return your_choice


# creating the dictionary of winner
def winner(list_):
    length = len(list_)
    n = length // 2
    dict_winner = {}
    for element in list_:
        for i in range(n):
            popped = list_.pop(0)
            list_.append(popped)
            dict_winner[list_[n]] = list_[:n]

    return dict_winner


# creating the dictionary for loser
def loser(list_):
    length = len(list_)
    n = length // 2
    dict_loser = {}
    for element in list_:
        for i in range(n):
            popped = list_.pop(0)
            list_.append(popped)
            dict_loser[list_[n]] = list_[n + 1:]

    return dict_loser


# managing the cases of winning,losing,scores
def comparisons(player, com, points, win_, lose_, list_):
    if player == 'score':
        print('Your rating: {}'.format(points))
    elif com not in list_ or player not in list_:
        print('Invalid input')
    elif com in lose_[player]:
        print('Sorry, but computer chose {}'.format(com))
    elif com in win_[player]:
        print('Well done. Computer chose {} and failed'.format(com))
        points += 100
    elif com == player:
        print('There is a draw ({})'.format(com))
        points += 50
    return points


# main program
ins()
player_name = input('Enter your name:>> ')
print('Hello, {}'.format(player_name))
player_score = rating(player_name)
elements = determine_elements()
win = winner(elements)
print('You will be having advantage over the following entries if you will enter the below entry ')
print(win)
lose = loser(elements)
print('If you will choose the given entry you will be losing with the following entries ')
print(lose)
print("Okay, let's start")
player_choice = input("Please enter your choice... > ")
while player_choice != 'exit':
    com_choices = elements
    random.shuffle(com_choices)
    com_choice = com_choices[0]
    player_score = comparisons(player_choice, com_choice, player_score, win, lose, elements)
    player_choice = input('choose again:> ')
print('Bye!.......Hope you enjoyed...!!!!!!!')
