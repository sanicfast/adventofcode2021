import time

def parseInput(input):
    out = [_[2:].split('..') for _ in input[13:].split(', ') ]
    return [[int(j) for j in i] for i in out]

def move(x, y, xvel, yvel):
    x += xvel
    y += yvel
    xvel += (xvel<0) - (xvel>0)
    yvel -=1
    return x,y,xvel,yvel

def checkTarget(x, y, target):
      xzone = target[0][0] <= x <= target[0][1]
      yzone = target[1][0] <= y <= target[1][1]
      return xzone and yzone

def checkTraj(xvel, yvel, target):
    x,y = 0,0
    maxY = 0
    while x < target[0][1] and (y > target[1][0]):
        x, y, xvel, yvel = move(x, y, xvel, yvel)
        maxY = max(y,maxY)
        # print(x,y,xvel,yvel)
        if checkTarget(x, y, target):
            return maxY
    return False

day17='target area: x=217..240, y=-126..-69'
test='target area: x=20..30, y=-10..-5'

target = parseInput(day17)
maxOfMaxes = 0
maxX = target[0][1]
minY = target[1][0]
solutions = []
print(f'maxX={maxX}, minY={minY}')
startTime = time.time()
for x in range(maxX+1):
    for y in range(minY,-minY+1):
        height = checkTraj(x,y,target)
        maxOfMaxes = max(height, maxOfMaxes)
        if type(height)==int:
            solutions.append([x,y])
print('part1:',maxOfMaxes)
print('part2:',len(solutions))
print(time.time()-startTime, 'seconds')
