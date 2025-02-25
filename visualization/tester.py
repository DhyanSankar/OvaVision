import EggBinCollection

def main():
    # initiate stuff
    layers, edges, gap = 4, 10, 2
    collection = EggBinCollection.EggBinCollection(layers, edges, gap)

    print("hi")
    collection.randomize_sex_for_test()

    collection.print_status()

main()