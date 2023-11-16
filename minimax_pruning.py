class NodeStateForPruning:
    def __init__(self, number: int):
        self.number = number
        self.children = []
        self.alpha = float('-inf')
        self.beta = float('inf')

    def set_cost(self, cost: int):
        self.cost = cost



def createAllNodeChildrenForPruning(number: int, K: int): #stwórz przestrzeń przeszukiwań
    if K <=0: 
        raise ValueError('K cannot be less or equal 0')
    if number == 1:
        return NodeStateForPruning(1)
    
    node = NodeStateForPruning(number)
    amount_children = min(K, number - 1)
    for i in range(1, amount_children + 1):
        child = createAllNodeChildrenForPruning(number - i, K)
        node.children.append(child)
    return node


def minimax_with_pruning(current_node: NodeStateForPruning, alpha: float, beta: float, max_player: bool): # znajdź ocenę każdej pozycji
    if current_node.number == 1:
        if max_player:
            current_node.cost = -1
            return -1
        else:
            current_node.cost = 1
            return 1
    current_node.alpha = alpha
    current_node.beta = beta
    if max_player:
        max_eval = float('-inf')
        for child in current_node.children:
            current_eval = minimax_with_pruning(child, current_node.alpha, current_node.beta, False)
            max_eval = max(max_eval, current_eval)
            current_node.alpha = max(current_node.alpha, current_eval)
            if current_node.beta <= current_node.alpha:
                break
        current_node.cost = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        for child in current_node.children:
            current_eval = minimax_with_pruning(child, current_node.alpha, current_node.beta, True)
            min_eval = min(min_eval, current_eval)
            current_node.beta = min(beta, current_eval)
            if current_node.beta <= current_node.alpha:
                break
        current_node.cost = min_eval
        return min_eval

