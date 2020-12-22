import random

# player1 = user
# player2 = computer
my_list = ['R', 'P', 'S']
def game():
    player1 = input("choose any one: 'R' for Rock, 'P' for paper,'S' for scissors\n")
    player2 = random.choice(my_list)

    if player1 == player2:
        return 'It\'s a tie'

   # R > S, S > P, P > R
    if match_win(player1, player2):
       return 'You won'
    else:
       return 'You lost'


def match_win(player1, player2):
    # return true if playe1 wins

    if (player1 == 'R' and player2 == 'S') or (player1 == 'S' and player2 == 'P') or (player1 == 'P' and player2 == 'R'):
        return True
print(game())
