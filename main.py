from file_util import read_file_lines
from config_util import read_config
from store_util import get_product_ids_for_query
from store_util import get_store_positions_for_query
import sys

# Get the command-line arguments
args = sys.argv
config = {}

if len(args) > 1:
    config_file_path = args[1]
    config = read_config(config_file_path)
    print(config)
else:
    print("No config file provided.")
    exit()

file_path = 'groceries_list.txt'  
lines_list = read_file_lines(file_path)

for line in lines_list:
    print(line.strip())

print(get_store_positions_for_query(config, 'milk'))