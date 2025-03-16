#!/usr/bin/env python3 
def get_data(fin):
    with open(fin) as f:
        raw_data = f.read().splitlines()
    filtered = [[j for j in i if j in 'ABCD'] for i in raw_data[2:4]]
    out={}
    for i,line in enumerate(filtered):
        for j,letter in enumerate(line):
            key = 'abcd'[j] + str(i)
            out[key]=letter
    return out

fin = './data/day23_ex.txt'
move_cost = {'A':1,'B':10,'C':100,'D':1000}
location_dict = {
    0:(1),
    1:(0,2),
    2:(1,3,'a0'),
    3:(2,4),
    4:(3,5,'b0'),
    5:(4,6,),
    6:(5,7,'c0'),
    7:(6,8),
    8:(7,9,'d0'),
    9:(8,10),
    10:(9),
   'a0':('a1',2),
   'a1':('a0'),
   'b0':('b1',4),
   'b1':('b0'),
   'c0':('c1',6),
   'c1':('c0'),
   'd0':('d1',8),
   'd1':('d0')
}
stopping_locations=[0,1,3,5,7,9,10]


print(get_data(fin))    
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
