def getData(path='data/day19.txt'):
    with open(path) as f:
        data = f.read().split('\n\n')
    data1 = [i.splitlines()[1:] for i in data]
    data2 = [[list(map(int,j.split(','))) for j in i] for i in data1]
    return data2

def distSq(p1,p2):
    dx = (p1[0]-p2[0])
    dy = (p1[1]-p2[1])
    dz = (p1[2]-p2[2])
    out = dx**2 + dy**2 + dz**2
    return out, [dx,dy,dz]

def getDists(scanner):
    out=[]
    for i,p1 in enumerate(scanner):
        for j,p2 in enumerate(scanner):
            if i>j:
                out.append(distSq(p1,p2))
    return out

def detectOverlap(dist1, dist2):
    commonCount=0
    for i,s1 in enumerate(dist1):
        for j,s2 in enumerate(dist2):
            if i>j:
                continue
            if s1[0]==s2[0]:
                commonCount+=1
    # print(commonCount)
    if commonCount >= 12:
        return True
    return False

def getOverlap(dists):
    overlap=[]
    for i in range(len(dists)):
        for j in range(len(dists)):
            if i>=j:
                continue
            if detectOverlap(dists[i], dists[j]):
                overlap.append([i,j])
    return overlap
scanners = getData()
dists = [getDists(i) for i in scanners]


# dist1,dist2,scanner1,scanner2=(dists[0],dists[16],scanners[0],scanners[16])
# print(
#     scanner1
#     )
x,y,z = 1,2,3
swaps = [
    (x,y,z),
    (x,z,y),
    (y,x,z),
    (y,z,x),
    (z,x,y),
    (z,y,x),]

negations = [
    (1,1,1),
    (-1,1,1),
    (-1,-1,1),
    (-1,-1,-1),
    (-1,1,-1),
    (1,-1,1),
    (1,-1,-1),
    (1,1,-1),]
out=[]
for s in swaps:
    for n in negations:
       out.append((s[0]*n[0],s[1]*n[1],s[2]*n[2]))
