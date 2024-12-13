# advent of code 2015
# day 19

# part 1
import re

input = open('day-19.txt', 'r').read()

def doChemistry(input, partTwo = False):
    reactionDict = {}
    for r in input.split('\n\n')[0].split('\n'):
        if r.split(' ')[0] in reactionDict.keys():
            reactionDict[r.split(' ')[0]].append(r.split(' ')[2])
        else:
            reactionDict[r.split(' ')[0]] = [r.split(' ')[2]]
    def splitMoleculeIntoAtoms(mol):
        atoms = []
        i = 0
        molSplit = [x for x in mol]
        while i < len(molSplit):
            if i == len(molSplit) - 1:
                atoms.append(molSplit[i])
                i += 1
            elif molSplit[i + 1].islower():
                atoms.append(''.join(molSplit[i:i + 2]))
                i += 2
            else:
                atoms.append(molSplit[i])
                i += 1
        return(atoms)
    baseMolecule = input.split('\n\n')[1]
    baseAtoms = splitMoleculeIntoAtoms(baseMolecule)
    if partTwo == False:
        allMolecules = []
        for i in range(len(baseAtoms)):
            if baseAtoms[i] in reactionDict.keys():
                for r in reactionDict[baseAtoms[i]]:
                    allMolecules.append(''.join(baseAtoms[:i] + [r] + baseAtoms[i + 1:]))
        return(len(set(allMolecules)))
    else:
        return(len(baseAtoms) - baseAtoms.count('Rn') - baseAtoms.count('Ar') - 2 * baseAtoms.count('Y') - 1)
doChemistry(input)

# part 2
doChemistry(input, partTwo = True)
