
#   Pylib Responsories
from pylib.botQ920 import Q90

i = 1
while True:

    #   Keeps sending attribute error (self is required?)
    print(i)
    q90 = Q90()
    q90.CompetitionVote()

    i += 1
    if i == 3:
        print('Ending the while loop.')
        break
