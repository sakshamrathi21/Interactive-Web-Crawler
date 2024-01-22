'''
    Olympics Medals
'''

from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required = True)
args = parser.parse_args()

# dictionary for the data
totalData = {}

# looping through the directory
for fileName in os.listdir(args.path):

    fr = open(args.path + fileName, 'r')
    text = fr.read()
    fr.close()
    # loop through data of file and set the values for the data
    line_list = text.split('\n')

    #one empty item shows up at the end
    line_list.pop()
    

    

    for line in line_list:
        alist = line.split('-')
        
        strtointlist = list(alist[1:])
        listtoadd = []
        for l in strtointlist:
            listtoadd.append(int(l))

        if (alist[0] not in totalData.keys()):
            
            totalData[alist[0]] = listtoadd
        else:
            listtoincrement = totalData[alist[0]]
            listtoincrement[0] += listtoadd[0] 
            listtoincrement[1] += listtoadd[1]
            listtoincrement[2] += listtoadd[2]
            totalData[alist[0]] = listtoincrement
        


# sort as per gold medals and break ties lexicographically

sortedlist = sorted(totalData.items(), key = lambda x: (1000-x[1][0], x[0]), reverse = False)

#made it a tuple using lambda
#did 1000-x because one was to be arranged reversed and one wasnt


totalData.clear()

for k,v in sortedlist:
    totalData[k] = v

print(totalData)

