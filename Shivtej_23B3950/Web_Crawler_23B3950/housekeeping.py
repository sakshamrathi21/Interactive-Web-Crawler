import os

def make_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_data_files(project_name):
    
    crawled = project_name + '/crawled.txt'
    
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
    

def set_to_file(links, file):
    for link in sorted(links):
        append_to_file(file + '/crawled.txt', link)

