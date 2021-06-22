data = [2, 7, 4, 2, 4, 10, 5, 7, 2, 7]
print(f'{data}  initial')
average = sum(data) / len(data)
step = 0

if average % 1 != 0:
    print(f'Average = {average:.2f} is not a whole number\n')
    exit()


def indices(lst, element):
    result = []
    offset = - 1
    while True:
        try:
            offset = lst.index(element, offset + 1)
        except ValueError:
            return result
        result.append(offset)


while True:
    MAX = max(data)
    MIN = min(data)

    allMAXindices = indices(data, MAX)
    allMINindices = indices(data, MIN)

    # print(allMAXindices, allMINindices)

    fullset = []
    for imax in allMAXindices:
        for imin in allMINindices:
            if imax > imin:
                distanceLEFT = imax - imin
                distanceRIGHT = len(data) - imax + imin
            else:
                distanceRIGHT = imin - imax
                distanceLEFT = len(data) - imin + imax

            # set of coordinates for every max value
            # [index, left/right ditance, distance]
            coord = [imax]

            if distanceLEFT < distanceRIGHT:

                side = 'Left'
                coord.append(side)
                coord.append(distanceLEFT)
            else:
                side = 'Right'
                coord.append(side)
                coord.append(distanceRIGHT)
            fullset.append(coord)

    # find shortest distance
    tmp = fullset[0]
    for crd in fullset:
        if crd[2] < tmp[2]:
            tmp = crd
    # move a chip
    indexOfGOODmax = tmp[0]
    side = tmp[1]

    if indexOfGOODmax == len(data) - 1:
        indexOfGOODmax = -1

    if side == 'Right':
        data[indexOfGOODmax + 1] += 1
        data[indexOfGOODmax] -= 1
    else:
        data[indexOfGOODmax - 1] += 1
        data[indexOfGOODmax] -= 1

    step += 1
    print(f'{data}, step: {step}')
    if data.count(int(average)) == len(data):
        print('DONE')
        break
