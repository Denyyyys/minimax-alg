from typing import List, Callable
import time
from minimax import (
	NodeState,
	create_search_tree,
	minimax_without_pruning
)
from minimax_pruning import (
	NodeStateForPruning,
	create_search_tree_for_pruning,
	minimax_with_pruning
)


def traverse_way(current_node: NodeState | NodeStateForPruning, way: List[NodeState] | List[NodeStateForPruning]):
	way.append(current_node)
	for child in current_node.children:
		if child.cost == current_node.cost:
			traverse_way(child, way)
		found_end = None   
		for node in way:
			if node.number == 1:
				found_end = node
				break
		if found_end is not None:
			break
	return way


def get_tokens_taken(way: List[NodeState] | List[NodeStateForPruning]):
	if len(way) == 0:
		raise ValueError("Way cannot be empty")
	tokens_taken = []
	for i in range(len(way) -1):
		tokens_taken.append(way[i].number - way[i + 1].number)
	return tokens_taken


def get_gameplay_info(way: List[NodeState] | List[NodeStateForPruning], max_player: bool):
	if len(way) == 0:
		raise ValueError("Way cannot be empty")
	info = ""
	if max_player and way[0].cost == -1 or (not max_player and way[0].cost == 1):
		info = "First player always lose :(\n------------------------------------\n"
	else:
		info = "First player can always win :D\n------------------------------------\n"
	tokens_taken = get_tokens_taken(way)
	for index, token_taken in enumerate(tokens_taken):
		info += f"{'First' if index % 2 == 0 else 'Second'} player takes {token_taken} {'token' if token_taken == 1 else 'tokens'}\n"
	info += f"{'First' if index % 2 == 1 else 'Second'} player has 1 token, so he lose"
	return info


def print_to_console(info: str):
	print(info)


def run_minimax_simulation_without_pruning(
		N: int, 
		K: int,
		max_player: bool, 
		display_info_func: Callable[[str], None]) -> NodeState:
	
	root = create_search_tree(N, K)
	minimax_without_pruning(root, max_player)
	way = []
	traverse_way(root, way)
	info = get_gameplay_info(way, max_player)
	if display_info_func:
		display_info_func(info)
	return root


def run_minimax_simulation_with_pruning(
		N: int, 
		K: int,
		max_player: bool, 
		display_info_func: Callable[[str], None] = None) -> NodeStateForPruning:
	
	root = create_search_tree_for_pruning(N, K)
	minimax_with_pruning(root, float('-inf'), float('inf'), max_player)
	way = []
	traverse_way(root, way)
	info = get_gameplay_info(way, max_player)
	if display_info_func:
		display_info_func(info)
	return root


def timer_minimax_without_pruning(
		N: int,
		K: int,
		max_player: bool,
		sample_times = 5
		):
	execution_times = []
	for _ in range(sample_times):
		root = create_search_tree(N, K)
		start_time = time.time()
		minimax_without_pruning(root, max_player)
		stop_time = time.time()
		execution_time = stop_time - start_time
		execution_times.append(execution_time)
	
	average_time = sum(execution_times) / len(execution_times)
	return average_time


def timer_minimax_with_pruning(
		N: int,
		K: int,
		max_player: bool,
		sample_times = 5
		):
	execution_times = []
	for _ in range(sample_times):
		root = create_search_tree_for_pruning(N, K)
		start_time = time.time()
		minimax_with_pruning(root, float('-inf'), float('inf'), max_player)
		stop_time = time.time()
		execution_time = stop_time - start_time
		execution_times.append(execution_time)
	
	average_time = sum(execution_times) / len(execution_times)
	return average_time


total_amount = 0

def get_amount_nodes(node: NodeState | NodeStateForPruning):
	for child in node.children:
		get_amount_nodes(child)
	global total_amount
	total_amount += 1
	return total_amount
