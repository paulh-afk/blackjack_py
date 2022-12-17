player1_name = input('Player\'s name 1: ')
player2_name = input('Player\'s name 2: ')

print('Hello {p1_name} and {p2_name}, welcome to'.format(
    p1_name=player1_name, p2_name=player2_name))

print('''
####### #  ####     #######  #    ####     #######  ####  ####
   #       #           #    # #   #           #    #    # #
   #    #  #    ###    #   #   #  #    ###    #    #    # ###
   #    #  #           #   #####  #           #    #    # #
   #    #  ####        #   #   #  ####        #     ####  ####
''')

print('The goal is to be the first player to get three in a row on a 3-by-3 grid')

print('''
 -- -- --
|  |  |  |
|  |  |  |
 -- -- --
|  |  |  |
|  |  |  |
 -- -- --
|  |  |  |
|  |  |  |
 -- -- --
''')
