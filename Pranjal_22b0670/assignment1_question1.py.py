'''
    Olympics Medals
'''

from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()

# dictionary for the data
totalData = {}

# looping through the directory
for fileName in os.listdir(args.path):
    if fileName.endswith(".txt"):
        with open(os.path.join(args.path, fileName), 'r') as file:
            # loop through data of file and set the values for the data
            for line in file:
                country, gold, silver, bronze = line.strip().split('-')
                gold, silver, bronze = map(int, [gold, silver, bronze])

                if country not in totalData:
                    totalData[country] = [0, 0, 0]

                totalData[country][0] += gold
                totalData[country][1] += silver
                totalData[country][2] += bronze

# sort as per gold medals and break ties lexicographically
sortedData = dict(sorted(totalData.items(), key=lambda x: (-x[1][0], x[0])))

# print the sorted data
for country, medals in sortedData.items():
    print(f"{country}: {medals}")
