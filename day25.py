import numpy as np

def get_data(loc):
    with open(loc) as f:
        rawdata = f.read().splitlines()
    cucumber_array = np.zeros((len(rawdata), len(rawdata[0])), dtype=int)
    for i in range(len(rawdata)):
        for j in range(len(rawdata[i])):
            if rawdata[i][j] == '>':
                cucumber_array[i][j] = 1
            elif rawdata[i][j] == 'v':
                cucumber_array[i][j] = 2
    return cucumber_array

def move(cucumber_array, num):
    direction_axis = int(num == 1)
    free_spaces = np.where(cucumber_array == 0, 1, 0)
    movers = np.where(cucumber_array == num, 1, 0)
    moved_movers = np.roll(movers, 1, direction_axis) 
    successful_moves = (moved_movers * free_spaces)
    cucumber_array = cucumber_array + successful_moves*num - np.roll(successful_moves,-1,direction_axis)*num
    return cucumber_array


# cucumber_array = get_data('./data/day25_ex1.txt') #58
cucumber_array = get_data('./data/day25.txt') #
iterations = 0
while True:
    iterations+=1
    old_positions = np.copy(cucumber_array)
    cucumber_array=move(cucumber_array, 1)
    cucumber_array=move(cucumber_array, 2)
    if np.array_equal(cucumber_array, old_positions):
        break
print(f'Part 1: Number of iterations: {iterations}')


