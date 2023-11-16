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
	timer_minimax_without_pruning
)
import random



N = random.randint(8, 20)
K = 3
max_player = True
print(f"N = {N}, K = {K}")
################        without pruning        ######################
time = timer_minimax_without_pruning(N, K, max_player)
print(f"Average time without pruning: {time}")
run_minimax_simulation_without_pruning(N, K, max_player, print_to_console)

print('\n\n\n')
################        with pruning        ######################

time = timer_minimax_with_pruning(N, K, max_player)
print(f"Average time with pruning: {time}")
run_minimax_simulation_with_pruning(N, K, max_player, print_to_console)
#################################################################
