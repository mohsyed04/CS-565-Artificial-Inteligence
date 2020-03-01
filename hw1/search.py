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
    return  [s, s, w, s, w, w, s, w]

'''to reverse the reversed path, first push all the values into a stack and pop and save the values in another list to get the correct order'''
def getPath(target, parent, actions,startState): #accepts the goal/target, parent dictionary, actionsa dictionary and the start state
    stack = []  #list as stack
    path = []   #to hold the path in correct order
    current_state = target #initialize the surrent state to the goal state and traverse back to buid a reveresed path. target is a state tuple
    while (current_state != startState): #loop until you hit the start state
        stack.append(actions[current_state]) 
        current_state = parent[current_state] #move back to parent state

    while (len(stack) > 0): #reverse the path to get in right order
        action = stack.pop()
        path.append(action)
    return path

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack=util.Stack()
    path = []
    start_state = (problem.getStartState(), [],0) #get start state and add empty action and cost to get to the start state before pushing on stack

    if problem.isGoalState(start_state[0]): #if the start state is a goal state, return an empty list of actions
        print("goal reached")
        return path

    visited = []    #list to hold visited states
    parent = {}     #to save the (state: parent state/node) pairs
    actions = {}    #to save the (state: action to get there)  pairs
    stack.push(start_state) #each stack item is of format (state,action to get to the state, cost to get to the state )
    
    
    while(stack.isEmpty() == False): #loop until stack is empty
        
        item = stack.pop() # pop an item from the stack

        if item[0] not in visited: #check the visited list before processing, if visited, ignore the state. item[0] means state of the item
            if problem.isGoalState(item[0]): #if its a goal state, add to the solution and return
                path = getPath(item[0],parent,actions,start_state[0]) ##call a function to create a path in reverse order and return the path list in correct order
                return path 

            visited.append(item[0]) #else append it to the visited list and do:

            successors = problem.getSuccessors(item[0]) #push all the of its successors onto the stack
            for scr in successors: #for each successor of the current state
                if scr[0] not in visited: #check if the current successor is already visited, if not, do:
                    stack.push((scr[0],scr[1],scr[2])) #push the successor in the same stack item format of (state,action,cost)
                    #scr(0) is the state and scr(1) is the action required to get to state scr[0]
                    parent[scr[0]] = item[0] # save the parent state (item[0]) of the current state/successor [scr[0]] in the parent dictionary 
                    actions[scr[0]] = scr[1] #save the action reuired (scr[1]) to get to the current state/successor  (scr[0])

    return path #if goal is not found return an empty list
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    stack = util.PriorityQueue()
    path = []
    start_state = (problem.getStartState(), [],0) #get start state and add empty action and cost to get to the start state before pushing on stack

    if problem.isGoalState(start_state[0]): #if the start state is a goal state, return an empty list of actions
        print("goal reached")
        return path

    visited = []    #list to hold visited states
    parent = {}     #to save the (state: parent state/node) pairs
    actions = {}    #to save the (state: action to get there)  pairs
    stack.push((start_state),start_state[2]) #each stack item is of format (state,action to get to the state, cost to get to the state )
    
    
    while(stack.isEmpty() == False): #loop until stack is empty
        
        item = stack.pop() # pop an item from the stack

        if item[0] not in visited: #check the visited list before processing, if visited, ignore the state. item[0] means state of the item
            if problem.isGoalState(item[0]): #if its a goal state, add to the solution and return
                path = getPath(item[0],parent,actions,start_state[0]) ##call a function to create a path in reverse order and return the path list in correct order
                return path 

            visited.append(item[0]) #else append it to the visited list and do:

            successors = problem.getSuccessors(item[0]) #push all the of its successors onto the stack
            for scr in successors: #for each successor of the current state
                if scr[0] not in visited: #check if the current successor is already visited, if not, do:
                    stack.push((scr[0],scr[1],scr[2]),scr[2]) #push the successor in the same stack item format of (state,action,cost)
                    #scr(0) is the state and scr(1) is the action required to get to state scr[0]
                    parent[scr[0]] = item[0] # save the parent state (item[0]) of the current state/successor [scr[0]] in the parent dictionary 
                    actions[scr[0]] = scr[1] #save the action reuired (scr[1]) to get to the current state/successor  (scr[0])

    return path #if goal is not found return an empty list
    util.raiseNotDefined()

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
