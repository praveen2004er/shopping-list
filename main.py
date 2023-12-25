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
    print("Config read completed!!!")
else:
    print("No config file provided.")
    exit()

file_path = 'groceries_list.txt'  
lines_list = read_file_lines(file_path)

query_to_positions = {}

for line in lines_list:
    query = line.strip()
    store_position_map = get_store_positions_for_query(config, query)
    query_to_positions[query] = store_position_map


position_to_queries = {}
for query, position_map in query_to_positions.items():
    for position in position_map:
        query_set = position_to_queries.get(position, set())
        query_set.add(query)
        position_to_queries[position] = query_set

sorted_position_to_queries = {key: position_to_queries[key] for key in sorted(position_to_queries)}
print(sorted_position_to_queries)