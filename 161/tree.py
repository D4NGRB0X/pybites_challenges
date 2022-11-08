import os


def count_dirs_and_files(directory='.'):
    dir_count = []
    file_count = []
    for _, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_count.append(dir)
        for file in files:
            file_count.append(file)

    return len(dir_count), len(file_count)




