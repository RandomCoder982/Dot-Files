#!/home/irene/gits/Python-Venv/venv/bin/python

file_path = '/home/irene/copy'

# Open the file in read mode ('r')
with open(file_path, 'w') as file:
    for _ in range(5):
        line = file.readline()
        if not line :
            break
        print(line.strip())
