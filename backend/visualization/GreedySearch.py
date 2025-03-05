from typing import List, Collection, Tuple, Callable, Optional, Union, Set, Dict, Type, Iterable
import random
from collections import deque
import heapq
import EggBinCollection


class GreedyBestSearch(): # maybe use Astar instead???
    """ Partial class representing a search strategy.
    To be subclassed (multiple inheritance) with a mixin that
    that implements a search algorithm (i.e. TreeSearchAgent or GraphSearchAgent)

    Greedy Best is implemented with a priority queue. 
    """
    frontier : List[Tuple[float, EggBinCollection.EggBinCollection]]
    total_extends = 0
    total_enqueues = 0
    heuristic = None

    def __init__(self, goal_state, heuristic = "hamming"):
        self.heuristic = self.hamming_heuristic
        self.frontier = []        

    def enqueue(self, state: EggBinCollection.EggBinCollection): # probably same as alpha as well
        """ Add the state to the frontier, unless path COST exceeds the cutoff """
        # removed cutoff stuff
        heapq.heappush(self.frontier, (self.heuristic(state), state)) # used path_cost without adding the heuristic value
        self.total_enqueues+=1

    def dequeue(self) -> Tuple[float, EggBinCollection.EggBinCollection]:
        """  Choose and remove the state with LOWEST ESTIMATED REMAINING COST TO GOAL from the frontier."""
        if self.frontier:
            self.total_extends += 1
            _, state = heapq.heappop(self.frontier)
            return state
        else:
            raise Exception("Frontier is empty, cannot dequeue.")
    
    def hamming_heuristic(state: EggBinCollection.EggBinCollection):
        return 0
    

class GraphSearchAlgorithm(GreedyBestSearch):
    """
    Mixin class for the graph search (extended state filter) algorithm.
    
    Needs to be mixed in with a "strategy" subclass of GoalSearchAgent that
    implements the other methods (i.e. RandomSearch, DFS, BFS, UCS, etc.)

    When implementing a efficient filter, you'll want to use sets, not lists.
    Sets are like python dictionaries, except they only store keys (no values).
    The "in" keyword invokes a key lookup.
    Check out the documentation: https://docs.python.org/3/tutorial/datastructures.html#sets
    """
    def search(self, initial_state : EggBinCollection.EggBinCollection, goal_state: EggBinCollection.EggBinCollection):
        """ Perform a search from the initial_state, which constitutes the initial frontier.
        
        Graph search is similar to tree search, but it manages an "extended filter" 
        to avoid re-extending previously extended states again.

        Create a set of extended states. Before extending any state, check if the state has already been extended.
        If so, skip it. Otherwise, extend and add to the set. 
        """
        self.enqueue(initial_state)
        extended_states = []  # Set to track extended states
    
        while len(self.frontier) > 0:
            state = self.dequeue()

            if state in extended_states:
                continue  # Skip already extended states
        
            if state.is_goal_state(goal_state):
                print("Goal state found!")
                return state

            # if gui_callback_fn(state):
            #     print("Search terminated by GUI callback.")
            #     return None

            extended_states.append(state)
        
            actions = state.get_all_actions()

            for action in actions:
                next_state = state.get_next_state(action)

                # Avoid revisiting parent state
                if next_state != state.parent:
                    self.enqueue(next_state)

            # probably recode it so that i can just get all the things

        print("Search failed to find a solution.")
        return None

# we need to code state.parent
    
def main():
    # instantiate a goal state
    # GraphSearchAlgorithm.search(initial_state, goal_state)

    # however, we must make the search algorithm print the actions. we do not have this yet. 
    # maybe within EggBinCollection, we couild have self.parent and have self.actions_taken. they both start at none.
    # we now have the above, but getting the appropriate actions taken would "backtrack" later. it is okay
    # figure out a way to instantiate stuff correctly. 

    return -1