import EggBinCollection

def main():
    # initiate stuff
    layers, edges, gap = 4, 10, 2
    collection = EggBinCollection.EggBinCollection(layers, edges, gap)

    print("hi")
    collection.randomize_sex_for_test()

    collection.print_status()

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

    return

main()