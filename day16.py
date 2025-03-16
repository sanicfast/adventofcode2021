import functools

with open('data/day16.txt') as f:
    day16 = f.read()

def convertHex(hex):
    hexMap = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111',
        '\n': '',
    }
    out = ''.join([hexMap[i] for i in hex])
    return out

# test = 'D2FE28'
# test = '38006F45291200'
# test = '8A004A801A8002F478'
# test = '620080001611562C8802118E34'
# test= 'C0015000016115A2E0802F182340'
# test= 'A0016C880162017C3686B18A3D4780'
binPackets = convertHex(day16)
binTest = convertHex(test)
packetVersionList = []
head=0
def parse(binPackets):
    # while len(binPackets)-1d
    global packetVersionList
    global head
    packetVersion = int(binPackets[head:head+3],2)
    packetID = int(binPackets[head+3:head+6],2)
    packetVersionList.append(packetVersion)
    head += 6
    if packetID == 4:
        packetType = 'literal'
    else:
        packetType = 'operator'

    if packetType == 'literal':
        valueBin=''
        while binPackets[head]=='1':
            valueBin = valueBin + binPackets[head+1:head+5]
            head += 5
        valueBin = valueBin + binPackets[head+1:head+5]
        head += 5
        value = int(valueBin,2)
        return value


    if packetType == 'operator':
        lengthTypeID = binPackets[head]
        head += 1
        args=[]
        if lengthTypeID == '0':
            valueBin = binPackets[head:head+15]
            head += 15
            value = int(valueBin,2)
            subPacketsEnd = value + head
            while subPacketsEnd > head:
                args.append(parse(binPackets))

        else:
            valueBin = binPackets[head:head+11]
            head += 11
            value = int(valueBin,2)
            numSubPackets = value
            for _ in range(numSubPackets):
                args.append(parse(binPackets))
        if packetID == 0:
            out = sum(args)
        elif packetID == 1:
            out = functools.reduce(lambda x,y : x*y , args)
        elif packetID == 2:
            out = min(args)
        elif packetID == 3:
            out = max(args)
        elif packetID == 5:
            if args[0]>args[1]:
                out = 1
            else:
                out = 0
        elif packetID == 6:
            if args[0]<args[1]:
                out = 1
            else:
                out = 0
        elif packetID == 7:
            if args[0] == args[1]:
                out = 1
            else:
                out = 0
        return out


part2 = parse(binPackets),
print(
    'part1: ', sum(packetVersionList),
    '\n',
    'part2: ', part2
)
