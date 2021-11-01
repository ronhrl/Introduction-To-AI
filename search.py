# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class Node:

    def __init__(self, state, price, price_path, direction, path):
        self.price_path = 0
        self.path = list()
        self.state = state
        self.price_path += price + price_path
        self.direction = direction
        if len(path) > 0:
            for dir in path:
                self.path.append(dir)
        self.path.append(direction)

    def get_state(self):
        return self.state

    def get_price(self):
        return self.price_path

    def get_path(self):
        return self.path

    def __eq__(self, other):
        return self.state == other.state

    # def add_node_to_path(self, node):
    #    self.path += node
    #    self.price += node.price

    # def solution(self):
    #    return self.path, self.price

    def expand(self, problem):
        # print(53)
        # print(self.state)
        list_n = problem.getSuccessors(self.state)
        # print(56)
        # print(list_n)
        node_list = list()
        for success in list_n:
            (n, dir, cost) = success
            node_list.append(Node(n, cost, self.price_path, dir, self.path))
        return node_list


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    first_node = Node(problem.getStartState(), 0, 0, "", "")
    frontier = util.Stack()
    frontier.push(first_node)
    frontier_list = list()
    frontier_list.append(first_node)
    # path = first_node.get_path()
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.isGoalState(node.state):
            return node.get_path()[1:]
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier_list:
                frontier.push(child)
                frontier_list.append(child)
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    first_node = Node(problem.getStartState(), 0, 0, "", "")
    frontier = util.Queue()
    frontier.push(first_node)
    frontier_list = list()
    frontier_list.append(first_node)
    # path = first_node.get_path()
    closed_list = set()
    while frontier:
        node = frontier.pop()
        # print(173)
        if problem.isGoalState(node.state):
            print(144)
            print(node.get_path()[1:])
            return node.get_path()[1:]
        closed_list.add(node.state)
        for child in node.expand(problem):
            # print("frontier")
            # print(closed_list)
            # print("child")
            # print(child.state)
            if child.state not in closed_list and child not in frontier_list:
                # print(192)
                frontier.push(child)
                frontier_list.append(child)

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    first_node = Node(problem.getStartState(), 0, 0, "", "")
    frontier = util.PriorityQueue()
    frontier.push(first_node, first_node.price_path)
    frontier_list = list()
    frontier_list.append(first_node)
    # path = first_node.get_path()
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.isGoalState(node.state):
            return node.get_path()[1:]

        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier_list:
                frontier.push(child, child.price_path)
                frontier_list.append(child)
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    first_node = Node(problem.getStartState(), 0, 0, "", "")
    f = lambda n: n.price_path + heuristic(n.state, problem)
    frontier = util.PriorityQueueWithFunction(f)
    frontier.push(first_node)
    frontier_list = list()
    frontier_list.append(first_node)
    closed_list = set()
    while frontier:
        node = frontier.pop()
        if problem.isGoalState(node.state):
            return node.get_path()[1:]
        closed_list.add(node.state)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier_list:
                frontier.push(child)
                frontier_list.append(child)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
