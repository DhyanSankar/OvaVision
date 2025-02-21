import EggBinCollection
import xrzController # resolve this

def main():
    layers, edges, gap = 4, 10, 2
    controller = xrzController()
    collection = EggBinCollection(layers, edges, gap, controller)
    collection.randomize_sex_for_test()
    EggBinCollection.print_status()

