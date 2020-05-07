import sys

class Node:
    def __init__(self, state, parent, frontier):
        self.state = state
        self.frontier = frontier
        self.parent = parent
    
    def print(self):
        print(self.state)
        if self.parent:
            self.parent.print()
        else:
            print("SUCCESS^")

class Problem:
    def __init__(self):
        self.initialState = [0,0,0]
        self.goalstate = [3,3,1]

    @staticmethod
    def breadthFirstSearch(nodes):
        newNodes = []
        for node in nodes:
            node.frontier = Problem.frontier(node)
            if node.frontier:
                newNodes.extend(node.frontier)
            else:
                return
        Problem.breadthFirstSearch(newNodes)

    @staticmethod
    def depthFirstSearch(nodes, depth, maxDepth):
        while nodes:
            node = nodes.pop(0)
            node.frontier = Problem.frontier(node)
            if node.frontier:
                if depth + 1 < maxDepth:
                    Problem.depthFirstSearch(node.frontier, depth + 1, maxDepth)
            else:
                sys.exit(0)

    @staticmethod
    def IDS(nodes):
        for i in range(0,15):
            nodesCopy = nodes.copy()
            Problem.depthFirstSearch(nodesCopy, 0, i)

    @staticmethod
    def frontier(node):
        possibleNodes = []
        moves = []
        boatSide = None
        if node.state[2] == 1:
            #boat on right side
            moves = [[-2, 0], [-1, -1], [0, -2], [-1, 0], [0, -1]]
            boatSide = 0
        else:
            #boat on left side
            moves = [[2, 0], [1, 1], [0, 2], [1, 0], [0, 1]]
            boatSide = 1

        for move in moves:
            newState = [node.state[0] + move[0], node.state[1] + move[1], boatSide]
            if problem.isGoal(newState):
                goalNode = Node(newState, node, None)
                goalNode.print()
                return
            if Problem.isValidState(newState):
                newNode = Node(newState, node, None)
                possibleNodes.append(newNode)
        return possibleNodes

    @staticmethod
    def isGoal(state):
        if state == [3,3,1]:
            return True
        return False

    @staticmethod
    def isValidState(state):
        if state[0] > 3 or state[0] < 0:
            return False
        if state[1] > 3 or state[1] < 0:
            return False
        if state[2] > 1 or state[2] < 0:
            return False
        if state[1] > state[0] and not state[0] == 0:
            return False
        if state[1] < state[0] and not state[0] == 3:
            return False
        return True

problem = Problem()

node = Node([0,0,0], None, None)

# goal = Problem.breadthFirstSearch([node])

# goal = Problem.depthFirstSearch([node], 0, 15)

goal = Problem.IDS([node])