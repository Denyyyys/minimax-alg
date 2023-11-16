from minimax import (
	NodeState,
	createAllNodeChildren,
	minimax_without_pruning,
)
from minimax_pruning import (
	NodeStateForPruning, 
	createAllNodeChildrenForPruning,
	minimax_with_pruning
)
from utility import (
	traverse_way,
	get_gameplay_info,
	run_minimax_simulation_without_pruning,
	run_minimax_simulation_with_pruning,
	print_to_console,
	timer_minimax_with_pruning,
	timer_minimax_without_pruning,
	get_amount_nodes,
	get_amount_not_visited_nodes
)
import random
import csv


N = random.randint(8, 20)
K = 3
max_player = True
# print(f"N = {N}, K = {K}")
# ################        without pruning        ######################
# time = timer_minimax_without_pruning(N, K, max_player)
# print(f"Average time without pruning: {time}")
# run_minimax_simulation_without_pruning(N, K, max_player, print_to_console)

# print('\n\n\n')
# ################        with pruning        ######################

# time = timer_minimax_with_pruning(N, K, max_player)
# print(f"Average time with pruning: {time}")
# run_minimax_simulation_with_pruning(N, K, max_player, print_to_console)
#################################################################
###### 			measure average time 			################
# K = 3
# max_player = True
# data = [["N", "K", "avg_time_no_pruning","avg_time_with_pruning"]]
# for N in range(8, 20):
# 	average_time_no_pruning = timer_minimax_without_pruning(N, K, max_player, 40)
# 	average_time_with_pruning = timer_minimax_with_pruning(N, K, max_player, 40)
# 	data.append([N, K, average_time_no_pruning, average_time_with_pruning])

# with open('average_time.csv', mode="w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

N = 5
K = 3
root = createAllNodeChildrenForPruning(N, K)


number = get_amount_not_visited_nodes(root)
print(number)