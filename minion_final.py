def minion_game(word):

    lookup_dict = {'A': True, 'B': False, 'C': False, 'D': False, 
                   'E': True, 'F': False, 'G': False, 'H': False, 
                   'I': True, 'J': False, 'K': False, 'L': False, 
                   'M': False, 'N': False, 'O': True, 'P': False, 
                   'Q': False, 'R': False, 'S': False, 'T': False, 
                   'U': True, 'V': False, 'W': False, 'X': False, 
                   'Y': False, 'Z': False}     


    s, k = 0, 0

    for x in range(len(word)):
       if lookup_dict[word[x]] is True:
           k += len(word) - x
       else:
           s += len(word) - x

    if s > k:
       print("Stuart", s)
    elif k > s:
       print("Kevin", k)
    else:
        print("Draw")
