""" This script creates sorted copy of the file. """
import os

CURSORS = []  # keeping cursors of temporary files
LAST_VALUES = []  # keeping last numbers of each temp file
TEMP_SIZE = 2_000_000  # numbers count in each temp file

dir_path = 'temp_dir'

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def min_index(arr: list):
    """ Returns the index of minimum value in 'arr' """
    if not arr:
        return None

    m = arr[0]  # min value
    m_index = 0
    for i in range(len(arr)):
        if arr[i] < m:
            m = arr[i]
            m_index = i

    return m_index


with open('huuuge.txt', 'r', encoding='utf-8') as file:
    i = 0
    for line in file:
        if i % 2_000_000 == 0:
            CURSORS.append(open(os.path.join(dir_path, f'file{i // TEMP_SIZE}.txt'), 'w+'))
        CURSORS[-1].write(line)
        i += 1

LAST_VALUES = [CURSORS[i].readline() for i in range(len(CURSORS))]

with open('sorted_huuuge.txt', 'w', encoding='utf-8') as file:
    while LAST_VALUES:
        current_index = min_index(LAST_VALUES)
        if current_index is None:
            break
        file.write(f'{LAST_VALUES[current_index]}\n')
        LAST_VALUES[current_index] = int(CURSORS[current_index].readline())
        i = 0
        while i < len(LAST_VALUES):
            if LAST_VALUES[i] == '':
                del LAST_VALUES[i]
                CURSORS[i].close()
                del CURSORS[i]
            i += 1


# closing all opened temp files
for file in CURSORS:
    file.close()
