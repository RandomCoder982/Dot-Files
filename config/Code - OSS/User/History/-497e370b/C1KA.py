# Specify the file path
file_path = '/home/irene/copy.txt'

# Specify the number of lines to read
num_lines_to_read = 5

print("Starting", "\n")

with open(file_path, 'r+') as file:
    # Read the first few lines
    lines = [file.readline().strip() for _ in range(num_lines_to_read)]

    # Move the file cursor back to the beginning
    file.seek(0)

    # Modify the lines as needed (for example, comment out lines starting with 'monitor=')
    modified_lines = [line.replace("#", "") if 'monitor=' in line else line for line in lines]

    # Write the modified lines back to the file
    file.write('\n'.join(modified_lines))

print("\n"+"Finished")
