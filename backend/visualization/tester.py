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

    print("GOAL")
    print(goal_arr)

    initial_state = EggBinCollection.EggBinCollection(initial_arr, 1)
    goal_state = EggBinCollection.EggBinCollection(goal_arr, 1)

    path_finder = GreedySearch.GraphSearchAlgorithm(goal_state)
    paths_taken = path_finder.search(initial_state, goal_state)

    current = initial_state
    print("SORT START")
    print(initial_arr)

    for i in range(len(paths_taken)):
        current = current.get_next_state(paths_taken[i])
        print(current.output_as_array())
    print("SORT END")
    
    return paths_taken

print(test_alg())