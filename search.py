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
    def __init__(self, state, price):
        self.path = list()
        self.price = price
        self.state = state

    def get_state(self):
        return self.state

    def get_path(self):
        return self.state

    def add_node_to_path(self, node):
        self.path += node
        self.price += node.price

    def solution(self):
        return self.path, self.price

    def expand(self, problem):
        list_nodes = list()
        # print(12)
        # print(problem.getSuccessors(self.state))
        #for tup in problem:
        #    print(tup)
        #    (state, direction, cost) = tup
        #    list_nodes.append(Node(state, cost))
        # print(9)

        # print(1)
        # print(problem)
        # print(self.state)
        # print(problem.getSuccessors(self.state))
        # print(2)
        list_n = problem.getSuccessors(self.state)
        # print(list_n)
        # list_nodes.append(problem.getSuccessors(self.state)[0][0])
        # print(list_nodes)
        # print(list_nodes[0])
        # print(list_nodes[1])
        # print(12)
        node_list = list()
        for success in list_n:
            (n, dir, cost) = success
            # print(n)
            # print(dir)
            # print(cost)
            # print(success)
            node_list.append(Node(n, cost))
        # print(72)
        # print(node_list)
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
    path = list()
    first_node = Node(problem.getStartState(), 0)
    frontier = util.Stack()
    frontier.push(first_node)
    frontier_list = list()
    frontier_list.append(Node(problem.getStartState(), 0))
    # frontier = [()]
    # print(2)
    # print(problem.getStartState())
    # print(3)
    # print(frontier.pop().price)
    # print(frontier.pop().price)
    # print(frontier.pop().state)
    # print(4)
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # node = frontier.pop()
    # print(5)
    # print(node.state)
    # print(problem.getSuccessors(node.state))
    closed_list = set()
    count = 1
    print(166)
    print(count)
    print(len(frontier_list))
    while not frontier.isEmpty():
        count += 1
        print(161)
        # print(frontier)
        node = frontier.pop()
        if problem.isGoalState(node.state):
            print(175)
            return path
        closed_list.add(node.state)
        # print(10)
        for child in node.expand(problem):
            if child.state not in closed_list and child not in frontier_list:
                frontier.push(child)
                frontier_list.append(child)
                path.append(child.state)
        # print(closed_list)

    print("I'm here\n")
        # frontier.extend(node.expand(problem))
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
