from datetime import datetime
from multiprocessing import Process, Queue

def gameflow(que, word, x_start, x_end):
    vowels = ['A', 'E', 'I', 'O', 'U']
    s_cnt, k_cnt = 0, 0
    for x in range(x_start, x_end):
        for y in range(x_start, len(word) + 1):
            if x >= y:
                pass
            else:
                if word[x] in vowels:
                    k_cnt += 1
                else:
                    s_cnt += 1
    que.put([s_cnt, k_cnt])

def minion_game(word):
    lw = len(word)
    que = Queue()
    is1, ie1 = 0, int(lw / 5) + 1
    is2, ie2 = ie1, int(lw / 2) + 1
    is3, ie3 = ie2, int(lw / 1.3) + 1
    is4, ie4 = ie3, lw + 1
    
    p1 = Process(target=gameflow, args=(que, word, is1, ie1,))
    p2 = Process(target=gameflow, args=(que, word, is2, ie2,))
    p3 = Process(target=gameflow, args=(que, word, is3, ie3,))
    p4 = Process(target=gameflow, args=(que, word, is4, ie4,))

    procs = [p1, p2, p3, p4]
    lst = []
    s, k = 0, 0
    for p in procs:
        p.start()
    
    for p in procs:
        lst.append(que.get())



    for p in procs:
        p.join()

    for l in lst:
        s += l[0]
        k += l[1]

    print("Stewart", s)
    print("Kevin", k)


begin_time = datetime.now()

word = '''
BANANA
'''
                
# if s_cnt > k_cnt:
#     print(f"Stuart {s_cnt}")
# elif s_cnt < k_cnt:
#     print(f"Kevin {k_cnt}")
# else:
#     print("Draw")
print("----------------REAL CASE----------------------")
minion_game(word)
print(datetime.now() - begin_time)