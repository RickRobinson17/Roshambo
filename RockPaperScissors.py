import random


def play():


    user = input("User Please enter Rock(r),Paper(p),or Scissors(s): ".lower())


    computer = random.choice(['r','p','s'])


    print(f"User:{user}" + " "+f"CPU:{computer}" )


    if user == computer:
        print('tie')
        return 'tie'


    if (is_win(user,computer)):
        return 'You Won!'
        

    return 'You Lose'



# r>s, s>p, p>r


def is_win(player,oppenent):

    if (player == 'r' and oppenent == 's' )or(player == 's' and oppenent == 'p')or (player == 'p' and oppenent == 'r') :
        print('You Won!')
    else:
        print('You Lose!')




play()
