class NodeState:
    def __init__(self, number: int):
        self.number = number
        self.children = []

    def set_cost(self, cost: int):
        self.cost = cost


def create_search_tree(number: int, K: int): 
    if K <=0: 
        raise ValueError('K cannot be less or equal 0')
    if number == 1:
        return NodeState(1)
    
    node = NodeState(number)
    amount_children = min(K, number - 1)
    for i in range(1, amount_children + 1):
        child = create_search_tree(number - i, K)
        node.children.append(child)
    return node


def minimax_without_pruning(current_node: NodeState, max_player: bool):
    if current_node.number == 1:
        if max_player:
            current_node.cost = -1
            return -1
        else:
            current_node.cost = 1
            return 1
    if max_player:
        max_eval = float('-inf')
        for child in current_node.children:
            current_eval = minimax_without_pruning(child, False)
            max_eval = max(max_eval, current_eval)
        current_node.cost = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for child in current_node.children:
            current_eval = minimax_without_pruning(child, True)
            min_eval = min(min_eval, current_eval)
        current_node.cost = min_eval
        return min_eval
