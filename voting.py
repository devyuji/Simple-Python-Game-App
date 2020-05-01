# Voting app
def entery(name_candidate1):
    # mini database 
    store = {
        'raghavan' : 19 , 
        "ranchi" : 21,
        "debojyoyti" : 19,
        "harsh" : 18,
        "orange" : 21,
        "apple" : 19,
        "banana" :20,
        "koyal" : 56
    }
    length_candidate = len(name_candidate1)
    count = []
    for index,j in enumerate(name_candidate1):
        print(index,j,end= ' ')
    print()
    for i in store.keys():
        if (store[i] >= 18):
            if not(i in name_candidate1):
                print(f"It's your turn {i}")
                c = int(input())
                count.append(c)
        else:
            print(f"You are not eligible to Vote! {i}")
    return count

def counting(count1,length,name1):
    winner = []
    s = set(count1)
    c = 0
    index1 = []
    for i in s:
        c = 0
        for j in count1:
            if i == j:
                c = c + 1
                p = j
        winner.append(c)
        index1.append(p)
    if len(winner) == 1:
        k = index1[0]
        return (name1[k])
    return winner

def winner_draw(win,name,length):
        s = set(win)
        if len(s) == 1:
            print("DRAW!") 
            return "NO ONE"
        else:
            max1 = max(win)
            ind = win.index(max1)
            return name[ind]

#__main__
no_candidate = int(input("Enter the number of candidate\n"))
name_candidate = []
print("Enter the name of the candidate")
for i in range(no_candidate):
    a = input()
    name_candidate.append(a)
store = entery(name_candidate)
w = counting(store,no_candidate,name_candidate)
if (type(w) == str):
    print('Winner is :',w)
else:
    print("Winner is :",winner_draw(w,name_candidate,no_candidate))