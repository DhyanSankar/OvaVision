import time
import math
import threading
import sys
import os

# Add the root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(root_dir)

import backend.visualization.EggBinCollection as EggBinCollection
import backend.visualization.GreedySearch as GreedySearch
import backend.visualization.motors.xrzController as xrzController


class EggSorter:
    """Class to manage egg sorting with thread control and stop mechanism"""
    
    def __init__(self):
        # Flag to control when sorting should stop
        self.stop_requested = False
        self.sorting_thread = None
        self.controller = None
        self.egg_collection = None
        self.current_command_index = 0
        self.commands = []
        self.thread_lock = threading.Lock()
    
    def initialize(self, initial_arr=[[["m", "m", "m", "m"], ["f", "f", "f", "f"]], [["m", "m", "m", "m"], ["f", "f", "f", "f"]], [["0", "0", "0", "0"], ["0", "0", "0", "0"]]]):
        """Initialize controller and egg collection"""
        # Initialize the controller directly - xrzController handles motor initialization
        self.controller = xrzController.XRZController()
        
        # Initialize the egg collection with the same data as test_alg
        
        self.egg_collection = EggBinCollection.EggBinCollection(initial_arr, 1)
        
        # Reset the controller
        print("Initializing controller...")
        self.controller.resetXRZ()
    
    def start_sorting(self):
        """Start the sorting process in a separate thread"""
        # Run the test algorithm to get the commands
        self.commands = test_alg()
        
        if not self.commands:
            print("No sorting commands generated!")
            return
        
        self.current_command_index = 0
        self.stop_requested = False
        
        print(f"\nStarting sorting thread with {len(self.commands)} commands...")
        self.sorting_thread = threading.Thread(target=self.sorting_process)
        self.sorting_thread.daemon = True
        self.sorting_thread.start()
        
        # Start a thread to listen for the stop command
        input_thread = threading.Thread(target=self.listen_for_stop)
        input_thread.daemon = True
        input_thread.start()
    
    def sorting_process(self):
        """The main sorting process that runs in a separate thread"""
        try:
            print(f"Executing {len(self.commands)} sorting commands...")
            
            # Execute each command in sequence until stop is requested
            while self.current_command_index < len(self.commands) and not self.stop_requested:
                with self.thread_lock:
                    current_index = self.current_command_index
                    command = self.commands[current_index]
                
                print(f"\nExecuting command {current_index+1}/{len(self.commands)}")
                self.execute_egg_movement(command)
                
                # Update the egg collection state to match the physical state
                with self.thread_lock:
                    self.egg_collection = self.egg_collection.get_next_state(command)
                    self.current_command_index += 1
                
                # Print the current arrangement
                print("Current arrangement:")
                for layer in self.egg_collection.output_as_array():
                    print(layer)
                
                # Check if we need to stop after each command
                if self.stop_requested:
                    break
            
            if self.stop_requested:
                print("\nSorting stopped at user request!")
            else:
                print("\nSorting complete!")
            
            # Reset the controller when done
            print("Resetting controller...")
            self.controller.resetXRZ()
            print("Done!")
            
        except Exception as e:
            print(f"Error in sorting process: {e}")
            # Make sure to reset controller even if there's an error
            self.controller.resetXRZ()
    
    def execute_egg_movement(self, command):
        """
        Executes a single egg movement command using the xrzController
        
        Args:
            command: A command in format [[src_layer, src_bin, src_egg], [dst_layer, dst_bin, dst_egg]]
        """
        source, destination = command
        src_layer, src_bin, src_egg = source
        dst_layer, dst_bin, dst_egg = destination
        
        # Get source egg type for logging
        egg_type = self.egg_collection.bin_array[src_layer][src_bin].egg_array[src_egg]
        
        print(f"Moving {egg_type} egg from [{src_layer}][{src_bin}][{src_egg}] to [{dst_layer}][{dst_bin}][{dst_egg}]")
        
        try:
            # Get cartesian positions
            src_pos = tuple(self.egg_collection.bin_array[src_layer][src_bin].egg_index_to_cartesian_pos(src_egg))
            dst_pos = tuple(self.egg_collection.bin_array[dst_layer][dst_bin].egg_index_to_cartesian_pos(dst_egg))
            
            # Move to source position
            print(f"Moving to source position {src_pos}")
            x, y, z = src_pos
            r = math.sqrt(x*x + y*y)
            theta = math.atan2(y, x) * 180 / math.pi  # Convert to degrees
            
            # Use the controller's setXRZ method
            self.controller.setXRZ(x, theta, z)
            
            # Simulate picking up egg
            print("Picking up egg...")
            time.sleep(1)
            
            # Move to destination position
            print(f"Moving to destination position {dst_pos}")
            x, y, z = dst_pos
            r = math.sqrt(x*x + y*y)
            theta = math.atan2(y, x) * 180 / math.pi  # Convert to degrees
            
            # Use the controller's setXRZ method
            self.controller.setXRZ(x, theta, z)
            
            # Simulate placing egg
            print("Placing egg...")
            time.sleep(1)
            
            print(f"Movement completed: {egg_type} egg moved from {source} to {destination}")
            print(f"Resulting in the following egg arrangement: { self.egg_collection.output_as_array() }")
        except Exception as e:
            print(f"Error during movement: {e}")
            raise
    
    def request_stop(self):
        """Request that the sorting process stops after the current command"""
        with self.thread_lock:
            self.stop_requested = True
        print("\nStop requested. Finishing current movement...")
    
    def listen_for_stop(self):
        """Listen for stop command from input"""
        print("Sorting in progress. Type 'stop' and press Enter to stop the process.")
        while not self.stop_requested and self.sorting_thread.is_alive():
            command = input().strip().lower()
            if command == 'stop':
                self.request_stop()
                break
    
    def save_current_state(self):
        """Save the current state of the egg collection"""
        with self.thread_lock:
            current_state = self.egg_collection.output_as_array()
        
        print("\nCurrent egg arrangement:")
        for layer in current_state:
            print(layer)
        
        print(f"Progress: {self.current_command_index}/{len(self.commands)} commands completed")
        
        # Here you could save to a file if needed
        return current_state
    
    def run_alg(initial_arr=[[["m", "m", "m", "m"], ["f", "f", "f", "f"]], [["m", "m", "m", "m"], ["f", "f", "f", "f"]], [["0", "0", "0", "0"], ["0", "0", "0", "0"]]], goal_arr = [[["f", "f", "f", "f"], ["m", "m", "m", "m"]], [["f", "f", "f", "f"], ["m", "m", "m", "m"]], [["0", "0", "0", "0"], ["0", "0", "0", "0"]],]):
        """
        Test function from tester.py to generate the sorting commands
        Returns a list of commands to execute
        """

        initial_state = EggBinCollection.EggBinCollection(initial_arr, 1)
        goal_state = EggBinCollection.EggBinCollection(goal_arr, 1)

        path_finder = GreedySearch.GraphSearchAlgorithm(goal_state)
        paths_taken = path_finder.search(initial_state, goal_state)

        current = initial_state

        text = "START ARRAY: \n" + initial_state.print_status()
        text += "\nGOAL ARRAY:  \n" + goal_state.print_status() 

        text+=("\nSORT START\n")
        text += initial_state.print_status

        for i in range(len(paths_taken)):
            text += "---------\n"
            current = current.get_next_state(paths_taken[i])
            text += current.output_as_array()
        text += "SORT END" + "\nACTIONS TAKEN: " + paths_taken
        
        return text


def test_alg():
    """
    Test function from tester.py to generate the sorting commands
    Returns a list of commands to execute
    """
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
    paths_taken = path_finder.search(initial_state, goal_state)

    current = initial_state

    text = "START ARRAY: \n" + initial_state.print_status()
    text += "\nGOAL ARRAY:  \n" + goal_state.print_status() 

    text+=("\nSORT START\n")
    text += initial_state.print_status

    for i in range(len(paths_taken)):
        text += "---------\n"
        current = current.get_next_state(paths_taken[i])
        text += current.output_as_array()
    text += "SORT END" + "\nACTIONS TAKEN: " + paths_taken
    
    return text


def run_egg_sorter():
    """Main function to execute the egg sorting process with thread control"""
    sorter = EggSorter()
    sorter.initialize()
    sorter.start_sorting()
    
    try:
        # Wait for sorting thread to complete
        if sorter.sorting_thread:
            sorter.sorting_thread.join()
    except KeyboardInterrupt:
        # Handle Ctrl+C
        print("\nKeyboard interrupt detected!")
        sorter.request_stop()
        # Give some time for the thread to finish gracefully
        time.sleep(2)
    
    # Save final state
    final_state = sorter.save_current_state()
    print("Egg sorter has completed or been stopped.")


if __name__ == "__main__":
    run_egg_sorter()