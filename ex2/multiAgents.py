# Ron Harel 308433762

# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # the val the func will return
        score = successorGameState.getScore()
        successor_food_list = newFood.asList()
        num_successor_food_list = len(successor_food_list)
        num_current_food = len(currentGameState.getFood().asList())
        num_successor_power_pellets = len(successorGameState.getCapsules())
        num_current_power_pallets = len(currentGameState.getCapsules())
        ghosts_positions = []
        ghosts_dist = []
        food_dist = []

        # Case the next step will be win state then give very high score
        if successorGameState.isWin():
            return score * 1000

        # Case there are less food in the successor add to the score to encourage the pacman to go there
        if num_current_food > num_successor_food_list:
            score += 200

        # Find the distance from each food to the new position.
        for food in currentGameState.getFood().asList():
            food_dist.append(util.manhattanDistance(newPos, food))

        # Finding the closest food.
        min_food = min(food_dist)
        # Case the food is close then give high score
        if min_food <= 1:
            score += 200
        elif 1 < min_food <= 6:
            score += 100
        else:
            score -= 10

        # Each food that the pacman didn't eat yet is bad
        score -= 5 * num_current_food

        for ghost in newGhostStates:
            ghosts_positions.append(ghost.getPosition())

        for pos in ghosts_positions:
            ghosts_dist.append(util.manhattanDistance(pos, newPos))

        min_dis_ghost = min(ghosts_dist)

        # Case the ghost is close then give low score.
        if min_dis_ghost <= 1:
            score -= 10
        elif 1 < min_dis_ghost <= 6:
            score += 100
        else:
            score += 200

        # Case the next step makes the pacman stop give low score to make him not to go there.
        if action == Directions.STOP:
            score -= 10

        # Case the next step will make him eat big capsule give high score.
        if num_current_power_pallets < num_successor_power_pellets:
            score += 500

        return score
        # return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        # This function is for the pacman agent because it is the only agent we want to get the max score.
        # Therefore the agent index will always be 0.
        # The function will return the utility.
        def max_value(gameState, depth):
            depth += 1
            # Case we got the terminal state
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            value = -float("inf")
            for action in gameState.getLegalActions(0):
                succ = gameState.generateSuccessor(0, action)
                value = max(value, min_value(succ, depth, 1))
            return value

        # This function is for the ghosts agents because those are the agents we want to get the min score.
        # The function will return the utility.
        def min_value(gameState, depth, agent_index):
            # Case we got the terminal state
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            value = float("inf")
            for action in gameState.getLegalActions(agent_index):
                succ = gameState.generateSuccessor(agent_index, action)

                # In here i check if we got to the last agent.
                # If is is, then the next one is the pacman so I want to find the max value for him
                # Else I want to find the min value for the ghost
                if (agent_index + 1) % gameState.getNumAgents() == 0:
                    value = min(value, max_value(succ, depth))
                else:
                    value = min(value, min_value(succ, depth, (agent_index + 1)))
            return value

        # This function will the return the action based on the best utility.
        def MinMax_Decision(gameState):
            value = -float("inf")
            act = None
            for action in gameState.getLegalActions(0):
                # The root represent the pacman. therefore the next level will be a ghost, so I will use the min_value
                min_val = min_value(gameState.generateSuccessor(0, action), 0, 1)
                # This if will help me find the best action to do.
                if min_val > value:
                    value = min_val
                    act = action
            return act
        return MinMax_Decision(gameState)
        # util.raiseNotDefined()


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        # This function is for the pacman agent because it is the only agent we want to get the max score.
        # The function will return the utility.
        def max_value(gameState, depth, alpha, beta):
            depth += 1
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            value = -float("inf")
            for action in gameState.getLegalActions(0):
                successor = gameState.generateSuccessor(0, action)
                value = max(value, min_value(successor, depth, 1, alpha, beta))
                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value

        # This function is for the ghosts agents because those are the agents we want to get the min score.
        # The function will return the utility.
        def min_value(gameState, depth, agent_index, alpha, beta):
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            value = float("inf")
            for action in gameState.getLegalActions(agent_index):
                successor = gameState.generateSuccessor(agent_index, action)

                # In here i check if we got to the last agent.
                # If is is, then the next one is the pacman so I want to find the max value for him
                # Else I want to find the min value for the ghost
                if (agent_index + 1) % gameState.getNumAgents() == 0:
                    value = min(value, max_value(successor, depth, alpha, beta))
                    if alpha > value:
                        return value
                    beta = min(beta, value)
                else:
                    value = min(value, min_value(successor, depth, agent_index + 1, alpha, beta))
                    if alpha > value:
                        return value
                    beta = min(beta, value)
            return value

        # This function will the return the action based on the best utility.
        def alpha_beta_search(gameState):
            alpha = -float("inf")
            beta = float("inf")
            value = -float("inf")
            act = None
            for action in gameState.getLegalActions(0):
                successor = gameState.generateSuccessor(0, action)
                # The root represent the pacman. therefore the next level will be a ghost, so I will use the min_value
                max_val = min_value(successor, 0, 1, alpha, beta)
                # This if will help me find the best action to do.
                if max_val > value:
                    value = max_val
                    act = action
                if max_val > beta:
                    return act
                alpha = max(alpha, max_val)
            return act

        return alpha_beta_search(gameState)
        # util.raiseNotDefined()
