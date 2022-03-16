""" This script creates sorted copy of the file. """
import os
import shutil

FILES = []  # keeping cursors of temp files
SORTED_FILES = []  # keeping cursors of sorted temp files
CURSOR_VALUES = []  # keeping current numbers of each cursor
TEMP_SIZE = 2_000_000  # numbers count in each temp file

temp_path = 'temp_dir'
sorted_temp_path = 'sorted_temp_dir'

# create directories for temp files and sorted temp files
if not os.path.exists(temp_path):
    os.makedirs(temp_path)
if not os.path.exists(sorted_temp_path):
    os.makedirs(sorted_temp_path)

# create temp files
with open('huuuge.txt', 'r', encoding='utf-8') as file:
    i = 0
    for line in file:
        if i % TEMP_SIZE == 0:
            FILES.append(open(os.path.join(temp_path, f'file{i // TEMP_SIZE}.txt'), 'a+', encoding='utf-8'))
        FILES[-1].write(line)
        i += 1

for file in FILES:  # put file cursor at the beginning of temp files
    file.seek(0, 0)

# create sorted temp files
i = 0
for file in FILES:
    sorted_numbers = sorted(map(int, file))
    SORTED_FILES.append(open(os.path.join(sorted_temp_path, f'sorted{i}.txt'), 'a+', encoding='utf-8'))
    for number in sorted_numbers:
        SORTED_FILES[-1].write(f'{number}\n')
    i += 1

for file in SORTED_FILES:  # put file cursor at the beginning of sorted temp files
    file.seek(0, 0)

# add first values of sorted temp files
CURSOR_VALUES = [int(cursor.readline()) for cursor in SORTED_FILES]

with open('sorted_huuuge.txt', 'w', encoding='utf-8') as file:
    while CURSOR_VALUES: # while CURSOR_VALUES is not empty
        # find index of min value in CURSOR_VALUES
        current_index = CURSOR_VALUES.index(min(CURSOR_VALUES))

        file.write(f'{CURSOR_VALUES[current_index]}\n')

        # read next value from file
        next_value = SORTED_FILES[current_index].readline()
        if len(next_value) != 0:  # if it is not the last line
            # update value for the file
            CURSOR_VALUES[current_index] = int(next_value)
        else:
            # if the next value is the last line
            # delete the value from CURSOR_VALUES
            # and delete corresponding file from SORTED_FILES
            del CURSOR_VALUES[current_index]
            SORTED_FILES[current_index].close()
            del SORTED_FILES[current_index]

for file in FILES:
    file.close()

# delete temp files
shutil.rmtree(temp_path)
shutil.rmtree(sorted_temp_path)
