# please dont publish this file
# this is only for your use
# this file wasn't originally part of the pacman project

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

import multiAgents
i_nodes = 0
def func(currentGameState):
    global i_nodes
    i_nodes += 1
    return currentGameState.getScore()
multiAgents.scoreEvaluationFunction = func
gs___ = 0
def dec(f):
    def func_B(self, agentIndex, action):
        global gs___
        gs___ += 1
        return f(self,agentIndex,action)
    return func_B
import pacman
pacman.GameState.generateSuccessor = dec(pacman.GameState.generateSuccessor)
import sys
args = pacman.readCommand(sys.argv[1:])
pacman.runGames(**args)
print("nodes expanded: ",gs___, " treated-as-leaves:",i_nodes)