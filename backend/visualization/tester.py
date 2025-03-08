import EggBinCollection
import GreedySearch

def main():
    # initiate stuff
    layers, edges, gap = 4, 10, 2
    # collection = EggBinCollection.EggBinCollection(layers, edges, gap)

    # print("hi")
    # collection.randomize_sex_for_test()

    # collection.print_status()

def test_alg():
    initial_arr = [
        [["m", "m", "m", "m"], ["f", "f", "f", "f"]],
        [["m", "m", "m", "m"], ["f", "f", "f", "f"]],
        [["0", "0", "0", "0"], ["0", "0", "0", "0"]],
    ]

    goal_arr = [
        [["f", "f", "f", "f"], ["m", "m", "m", "m"]],
        [["f", "f", "f", "f"], ["m", "m", "m", "m"]],
        [["0", "0", "0", "0"], ["0", "0", "0", "0"]],
    ]

    initial_state = EggBinCollection.EggBinCollection(initial_arr, 1)
    goal_state = EggBinCollection.EggBinCollection(goal_arr, 1)

    path_finder = GreedySearch.GraphSearchAlgorithm(goal_state)
    end = path_finder.search(initial_state, goal_state)

    # paths_taken_reversed = []
    # paths_taken = []
    # current = end

    # while current.parent!=None:
    #     print(current.previous_action)
    #     paths_taken_reversed.append(current.previous_action)
    #     current=current.parent

    # # print(paths_taken_reversed)

    # for i in range(len(paths_taken_reversed)):
    #     paths_taken.append(paths_taken_reversed[len(paths_taken_reversed)-i-1])
    
    return end

print(test_alg())