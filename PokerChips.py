data = [13, 8, 28, 21, 30, 6, 13, 27, 23, 1]
print(f'{data}  initial')
average = sum(data) / len(data)

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


step = 0

while True:
    maxvalue = max(data)
    minvalue = min(data)

    maxindices = indices(data, maxvalue)
    minindices = indices(data, minvalue)

    # print(allMAXindices, allMINindices)

    fullset = []
    for imax in maxindices:
        for imin in minindices:
            if imax > imin:
                distance_left = imax - imin
                distance_right = len(data) - imax + imin
            else:
                distance_right = imin - imax
                distance_left = len(data) - imin + imax

            # set of coordinates for every max value
            # [index, left/right ditance, distance]
            coord = [imax]

            if distance_left < distance_right:

                side = 'Left'
                coord.append(side)
                coord.append(distance_left)
            else:
                side = 'Right'
                coord.append(side)
                coord.append(distance_right)
            fullset.append(coord)

    # find shortest distance
    tmp = fullset[0]
    for crd in fullset:
        if crd[2] < tmp[2]:
            tmp = crd
    # move a chip
    index_of_target_max = tmp[0]
    side = tmp[1]

    if index_of_target_max == len(data) - 1:
        index_of_target_max = -1

    if side == 'Right':
        data[index_of_target_max + 1] += 1
        data[index_of_target_max] -= 1
    else:
        data[index_of_target_max - 1] += 1
        data[index_of_target_max] -= 1

    step += 1
    print(f'{data}, step: {step}')
    if data.count(int(average)) == len(data):
        print('DONE')
        break
