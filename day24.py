def get_data(loc):
    with open(loc) as f:
        rawdata = f.read().splitlines()
    data= list(map(lambda x: x.split(' '), rawdata))
    check,add= [], [],
    for i in range(len(data)):
        if i % 18 == 5:
            check.append(int(data[i][2]))
        elif i % 18 == 15:
            add.append(int(data[i][2]))
    return check,add

# if check>0 then append add to stack
# if check<0 then we pop the latest add from stack
# this must be true:
#     w_new==add_prev+w_old+check_new
#     w_new and w_old are bounded 1 to 9
#     w_new-w_old = check_new+add_prev
#     w_old = w_new-check_new-add_prev
#     w_old = w_new-w_diff
#     w_new = w_old+w_diff

check,add = get_data('./data/day24.txt')

# for i in range(len(check)):
#     if check[i]>0:
#         print('push',add[i])
#     else:
#         print('pop',check[i])

stack=[]
lows = [0]*14
highs = [0]*14
possibilities = 1
for i in range(14):
    if check[i]>0: # if the check is positive then we push the add to the stack and remember its index
        stack.append((i,add[i]))
        continue
    # j is the index of the popped add. the index of the thing we need our check number to work with
    j,add_prev=stack.pop() 
    w_diff = add_prev+check[i]
    possibilities = possibilities*(9-abs(w_diff))
    # print(j,i,w_diff)

    # w_new-w_prev = w_diff. 
    #     for the highs we wnt the top of the range ie if it's 6, then 9 and 3 
    #     for the lows we want the bottom of the range ie if it's 6, then 7 and 1
    #     keeping in mind that w_new and w_old are bounded 1 to 9 and the formulas:
    #     w_old = w_new-w_diff
    #     w_new = w_old+w_diff
    
    if w_diff>0: # new>old
        highs[j] = 9-w_diff
        highs[i] = 9
        lows[j] = 1
        lows[i] = 1+w_diff
    else:
        highs[j] = 9
        highs[i] = 9+w_diff
        lows[j] = 1-w_diff
        lows[i] = 1
#the highest and lowest submarine numbers are as follows
print('Part 1:', ''.join(map(str,highs)))
print('Part 2:', ''.join(map(str,lows)))
print('There are',possibilities,'valid submarine numbers')
print(100*possibilities/9**14,'percent of all possible submarine numbers are valid')
