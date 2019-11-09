"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
while True:
    player1 = input('Player1: please enter:')
    if player1 == 'quit':
        a = input('Do you want to quit the program? Y or N')
        if a == 'Y':
            quit()
        elif a == 'N':
            continue
        else:
            print('Please type again!')
            continue
    player2 = input('Player2: please enter:')
    if player1 == 'Rock' and player2 == 'Scissors':
        print('Congratulations! Player1 wins!')
        continue
    elif player1 == 'Rock' and player2 == 'Paper':
        print('Congratulations! Player2 wins!')
        continue
    elif player1 == 'Scissors' and player2 == 'Rock':
        print('Congratulations! Player2 wins!')
        continue
    elif player1 == 'Scissors' and player2 == 'Paper':
        print('Congratulations! Player1 wins!')
        continue
    elif player1 == 'Paper' and player2 == 'Scissors':
        print('Congratulations! Player2 wins!')
        continue
    elif player1 == 'Paper' and player2 == 'Rock':
        print('Congratulations! Player1 wins!')
        continue
    elif player1 == player2 == 'Rock' or player1 == player2 == 'Scissors' or player1 == player2 == 'Rock':
        print('Tie! Do again!')
        continue
    else:
        print('Invaild input! Please enter again')
        continue


"""
Sample code:

print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')
"""