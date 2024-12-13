# advent of code 2022
# day 7

# part 1
import re

log = open('input.txt', 'r').read().split('\n')[:-1]

def makeFileSpace(log, partTwo=False):

    def mapLogToTree(log):
        tree = {'/':{}}
        lineage = ['/']
        for line in log:
            if line[0:4] == '$ cd':
                if line[5:] == '/':
                    env = tree['/']
                    lineage = ['/']
                elif line[5:] == '..':
                    env = tree
                    lineage.pop(-1)
                    for directory in lineage:
                        env = env[directory]
                else:
                    env = env[line[5:]]
                    lineage.append(line[5:])
            elif line[0:4] == '$ ls':
                pass
            elif line[0:3] == 'dir':
                env[line[4:]] = {}
            else:
                fileInfo = re.search(r'(\d+)\s(.*)', line)
                size = int(fileInfo.groups()[0])
                name = fileInfo.groups()[1]
                env[name] = size
        return(tree)

    def navigateTree(tree, lineage=''):
        dirDict = {}
        for key in tree.keys():
            if lineage == '':
                dictName = key
            else:
                dictName = lineage + '/' + key
            dirDict[dictName] = 0
            if type(tree[key]) is dict:
                for sub in tree[key].keys():
                    if type(tree[key][sub]) is int:
                        dirDict[dictName] += tree[key][sub]
                    else:
                        subDict = navigateTree({sub: tree[key][sub]}, dictName)
                        dirDict[dictName] += subDict[dictName + '/' + sub]
                        dirDict.update(subDict)
        return(dirDict)      

    tree = mapLogToTree(log)
    dirs = navigateTree(tree)
    
    if partTwo is False:
        return(sum([dir for dir in dirs.values() if dir <= 100000]))
    else:
        return(min([dir for dir in dirs.values() if dir >= (30000000 + dirs['/'] - 70000000)]))

makeFileSpace(log)

# part 2
makeFileSpace(log, True)
