# Specify the file path
file_path = '/home/irene/copy.txt'

# Specify the number of lines to read
num_lines_to_read = 5

print("Starting", "\n")
# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read the first few lines
    for _ in range(num_lines_to_read):
        line = file.readline()
        if not line:
            break  # Break the loop if the end of the file is reached
        print(line.strip()) 
