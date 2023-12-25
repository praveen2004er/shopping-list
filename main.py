from file_util import read_file_lines

file_path = 'groceries_list.txt'  
lines_list = read_file_lines(file_path)

for line in lines_list:
    print(line.strip())
