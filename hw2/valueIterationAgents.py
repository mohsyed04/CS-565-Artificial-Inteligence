# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        import copy

        for itr in range (iterations):
            previous_values = copy.deepcopy(self.values) #save previous state values to refer for the iteration

            for state in mdp.getStates():
                max_value = -100

                for action in mdp.getPossibleActions(state): #this also handles states with no actions
                    value_s = 0

                    for next_state,prob in mdp.getTransitionStatesAndProbs(state, action): 
                        reward = mdp.getReward(state,action,next_state) #r(s,a,s')
                        value_sPrime = previous_values[next_state]  # V(s')
                        value_s += prob * (reward + discount*value_sPrime) #the value iteration equation

                    if max_value < value_s:
                        max_value = value_s 

                    self.values[state] = max_value; #update the value for each state with the max value


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        mdp = self.mdp 
        discount = self.discount
        
        Qvalue = 0
        for next_state,prob in mdp.getTransitionStatesAndProbs(state, action): 
                        reward = mdp.getReward(state,action,next_state)
                        value_sPrime = self.values[next_state]
                        Qvalue += prob * (reward + discount*value_sPrime)

        return Qvalue
            

        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        mdp = self.mdp
        max_val = -100
        direction = "exit"
        if mdp.isTerminal(state) == True:
            return "exit"
        else:
            for action in mdp.getPossibleActions(state):
                Q_value = self.computeQValueFromValues(state, action)
                if max_val < Q_value:
                    max_val = Q_value
                    direction = action

                '''max_val = Q_value if max_val < Q_value else max_val
                direction = action if max_val < Q_value else None'''
    
        return direction  

        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
