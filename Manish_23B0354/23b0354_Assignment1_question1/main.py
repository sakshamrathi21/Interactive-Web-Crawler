
#    Olympics Medals


from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()

# dictionary for the data
totalData = {}


def check_key(dic: dict, key: str) -> bool:
    if key in dic.keys():
        return True
    return False


def create_list(list1: list) -> list:
    value = list(list1)
    value.pop(0)
    value = [int(x) for x in value]
    return value


def add(list1: list, list2: list) -> list:
    return [list1[i]+list2[i] for i in range(len(list1))]


# looping through the directory
for fileName in os.listdir(args.path):

    # read the file
    with open(args.path + fileName, 'r') as file:
        for line in file:
            line_list = line.split('-')
            key = line_list[0]
            if not check_key(totalData, key):
                value = create_list(line_list)
                totalData[key] = value
            else:
                value = create_list(line_list)
                value = add(value, totalData[key])
                totalData[key] = value
        file.close()


def sorted_dict(dict1: dict) -> dict:
    return dict(sorted(dict1.items(), key=lambda x: (-x[1][0], x[0])))


totalData = sorted_dict(totalData)
print(totalData)


# sort as per gold medals and break ties lexicographically
