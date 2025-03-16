import json
import time

def flatten(inList):
    """turn a list of lists into a flat list of tuples,
       containing the value and the depth of each list member"""
    outList = []
    flatten_recurse(inList,outList)
    return outList
def flatten_recurse(inList, outList, depth=0):
    for i in inList:
        if type(i)==int:
            outList.append((i, depth))
        else:
            flatten_recurse(i, outList, depth+1)

def findExploder(flatList):
    for i,j in enumerate(flatList):
        if j[1]==4:
            return i
    return -1

def explode(flatList, index):
    index=findExploder(flatList)
    exploders = flatList[index:index+2]


    del flatList[index+1: index+2]

    flatList[index] = (0, exploders[0][1]-1)
    if index>0:
        flatList[index-1]= (flatList[index-1][0] + exploders[0][0],
                            flatList[index-1][1] )
    if index < len(flatList) -1:
        flatList[index + 1] = (flatList[index+1][0] + exploders[1][0],
                            flatList[index+1][1])

def explodeAll(flatList):
    explodeIndex = findExploder(flatList)
    while explodeIndex > -1:
        explode(flatList, explodeIndex)
        explodeIndex = findExploder(flatList)
        # print('E:', flatList)

def findSplitter(flatList):
    for i,j in enumerate(flatList):
        if j[0]>9:
            return i
    return -1

def split(flatList, splitIndex):
    # splitIndex = findSplitter(flatList)
    value = flatList[splitIndex][0]
    newValue = value//2
    newLevel = flatList[splitIndex][1] + 1

    if value % 2 == 0:
        left,right = newValue, newValue
    else:
        left, right = newValue, newValue + 1

    flatList[splitIndex] = (left, newLevel)
    flatList.insert(splitIndex+1, (right, newLevel))
    # print('S:', flatList)

def reduce(flatList):
    splitIndex = findSplitter(flatList)
    explodeIndex = findExploder(flatList)

    while explodeIndex > -1 or splitIndex > -1:
        explodeAll(flatList)
        splitIndex = findSplitter(flatList)
        if splitIndex > -1:
            split(flatList, splitIndex)
            splitIndex = findSplitter(flatList)
        explodeIndex = findExploder(flatList)

def add(flatList1, flatList2):
    out1 = [(i[0], i[1]+1) for i in flatList1]
    out2 = [(i[0], i[1]+1) for i in flatList2]
    return out1 + out2

# def magnitude_list(input):
#     if type(input)==int:
#         return input
#     return 3*magnitude_list(input[0]) + 2*magnitude_list(input[1])

def magnitude(flat):
    while len(flat) > 1:
        for i in range(len(flat)-1):
            if flat[i][1] == flat[i+1][1]:
                newVal = flat[i][0]*3 + flat[i+1][0]*2
                newDepth = flat[i][1]-1
                del flat[i]
                flat[i] = (newVal, newDepth)
                break
        # print(flat)
    return flat[0][0]

print()

with open('./data/day18.txt') as data:
    inputList = list(map(json.loads, data.read().splitlines()))
# inputList = [
#     [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
#     [[[5,[2,8]],4],[5,[[9,9],0]]],
#     [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
#     [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
#     [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
#     [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
#     [[[[5,4],[7,7]],8],[[8,3],8]],
#     [[9,3],[[9,9],[6,[4,9]]]],
#     [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
#     [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]],
# ]
start = time.time()
flattenedInput = [flatten(i) for i in inputList]
acc=flattenedInput[0]
print(acc)
for i in range(1, len(flattenedInput)):
    acc = add(acc,flattenedInput[i])
    reduce(acc)

print('Part 1:',magnitude(acc), time.time()-start)
start = time.time()
part2=[]
for i, num1 in enumerate(flattenedInput):
    for j, num2 in enumerate(flattenedInput):
        if i!=j:
            newSum = add(num1,num2)
            reduce(newSum)
            part2.append(magnitude(newSum))
print('Part 2:', max(part2), time.time()-start)
