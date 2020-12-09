import argparse

def terrainFile(inputFile):
    terrain=[]
    for line in inputFile.readlines():
        parsedLine=line.strip()

        terrainLine=[]
        for i in range(0, len(parsedLine)): 
            terrainLine.append(line[i])
        terrain.append(terrainLine)
    return terrain


parser = argparse.ArgumentParser("simple_example")
parser.add_argument("increment", help="The sloper increased by increment.", type=int)
parser.add_argument("jumps", help="The jump by jumps.", type=int)
args = parser.parse_args()

inputFile = open('input', 'r')
terrain=terrainFile(inputFile)
inputFile.close()

treeNumber=0
sloper=0
increment=args.increment

jumper=1
jumps=args.jumps

for i in terrain:
    if (jumps != 1):
        if (jumper % jumps == 0):
            jumper+=1
            continue

    if (i[sloper] == '#'):
        treeNumber += 1
    sloper = (sloper + increment) % len(i)
    jumper+=1

print(treeNumber)
