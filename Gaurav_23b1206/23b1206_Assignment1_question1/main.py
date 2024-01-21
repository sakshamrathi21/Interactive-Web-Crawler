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

    # read the file
    f = open(args.path + fileName, "r")
    lines = f.readlines()

    # loop through data of file and set the values for the data
    for line in lines:

        country, gold, silver, bronze = line.split("-")
        gold = int(gold)
        silver = int(silver)
        bronze = int(bronze)


        if country in totalData.keys():
            _gold, _silver, _bronze = totalData[country]
            totalData[country] = [_gold + gold, _silver + silver, _bronze + bronze]
        else:
            totalData[country] = [gold, silver, bronze]

# sort as per gold medals and break ties lexicographically


sorted_dict = sorted(totalData.items(),key = lambda x: (-x[1][0], x[0]))



print(sorted_dict)
