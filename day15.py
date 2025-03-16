import math
import queue
import time

def dijkstra(data='data/day15_ex.txt', part2=True):
    def getData(location):
        with open(location) as f:
            raw = f.read().splitlines()
        out=[]
        for row in raw:
            out.append([int(_) for _ in row])
        dim = len(out),len(out[0])
        if part2:
            out,dim = part2(out,dim)
        return out,dim

    def initialize():
        currentLocation = 0,0
        dist = [([math.inf]*dim[1]) for i in range(dim[0])]
        dist[currentLocation[0]][currentLocation[1]]=0
        placesVisited = set()
        theQueue = queue.PriorityQueue()
        theQueue.put((0,0,0)) # cost, row, col
        return currentLocation,dist,placesVisited,theQueue

    def part2(tile,dim):
        newMap = [([0]*dim[1]*5) for i in range(dim[0]*5)]
        for row in range(dim[0]*5):
            for col in range(dim[1]*5):
                newVal = tile[row % dim[0]][col % dim[1]]
                bump = row // dim[0] + col // dim[1]
                # print(row,col,len(newMap),len(newMap[0]))
                newMap[row][col] = ((newVal + bump - 1) % 9) + 1
                # print(newMap[row][col])
        return newMap,(dim[0]*5, dim[1]*5)

    def getNeighbors(currentLocation):
        up    = currentLocation[0]+1 ,currentLocation[1]
        down  = currentLocation[0]-1 ,currentLocation[1]
        left  = currentLocation[0]   ,currentLocation[1]-1
        right = currentLocation[0]   ,currentLocation[1]+1
        out=[]
        for direction in [up, down, left, right]:
            if 0<=direction[0]<dim[0] and 0<=direction[1]<dim[1]:
                if direction not in placesVisited:
                    out.append(direction)
        return out

    def updateDist(currentLocation,neighbor):
        newValue = (dist[currentLocation[0]][currentLocation[1]] +
                    dangerMatrix[neighbor[0]][neighbor[1]]
                    )
        if newValue < dist[neighbor[0]][neighbor[1]]:
            dist[neighbor[0]][neighbor[1]] = newValue
            # print(f'updating {neighbor} with weight {newValue}')
    def nextLocation():
        weight,row,col = theQueue.get()
        currentLocation=row,col
        return currentLocation

    dangerMatrix, dim = getData(data)
    currentLocation, dist, placesVisited, theQueue = initialize()
    while not theQueue.empty():
        if currentLocation in placesVisited: # check if we've visited this spot
            # print(f'currentLocation: {currentLocation} in placesVisited')
            currentLocation = nextLocation()
            continue
        # if currentLocation == (dim[0]-1,dim[1]-1):
            # break
        # print(f'currentLocation {currentLocation} not in placesVisited')
        placesVisited.add(currentLocation) # add currentLocation to placesVisited
        neighbors = getNeighbors(currentLocation) # get neighbors
        # print(f'neighbors: {neighbors}')
        for neighbor in neighbors:
            updateDist(currentLocation,neighbor) # update dists
            theQueue.put((dist[neighbor[0]][neighbor[1]], neighbor[0],neighbor[1]))
        currentLocation = nextLocation()
    print()
    print(dangerMatrix[0])
    # for row in dangerMatrix:
        # print(row)
    return dist[dim[0]-1][dim[1]-1]

start = time.time()
print(dijkstra(data='data/day15.txt'))
print(time.time() - start)
