import random
import time

class RandomizedQuickSort:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.recursion_depth = 0
        self.max_depth = 0
    
    def reset_stats(self):
        """Reset statistics counters"""
        self.comparisons = 0
        self.swaps = 0
        self.recursion_depth = 0
        self.max_depth = 0
    
    def partition(self, arr, low, high, show_steps=False):
        """
        Standard partition using the last element as pivot
        Returns the partition index
        """
        pivot = arr[high]
        i = low - 1
        
        if show_steps:
            print(f"  Partitioning range [{low}:{high}], pivot = {pivot}")
        
        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        
        if show_steps:
            print(f"  After partition: {arr[low:high+1]}, pivot_index = {i+1}")
        
        return i + 1
    
    def randomized_partition(self, arr, low, high, show_steps=False):
        """
        Randomized partition: randomly select pivot and swap with last element
        Then call standard partition
        """
        # Randomly select pivot index
        random_index = random.randint(low, high)
        
        if show_steps:
            print(f"  Random pivot index: {random_index}, value: {arr[random_index]}")
        
        # Swap random element with last element
        arr[random_index], arr[high] = arr[high], arr[random_index]
        
        return self.partition(arr, low, high, show_steps)
    
    def quicksort_recursive(self, arr, low, high, show_steps=False):
        """
        Recursive randomized quick sort
        """
        if low < high:
            self.recursion_depth += 1
            self.max_depth = max(self.max_depth, self.recursion_depth)
            
            if show_steps:
                print(f"\nRecursion depth {self.recursion_depth}:")
                print(f"Sorting subarray: {arr[low:high+1]}")
            
            # Partition the array
            pi = self.randomized_partition(arr, low, high, show_steps)
            
            # Recursively sort elements before and after partition
            self.quicksort_recursive(arr, low, pi - 1, show_steps)
            self.quicksort_recursive(arr, pi + 1, high, show_steps)
            
            self.recursion_depth -= 1
    
    def sort(self, arr, show_steps=False):
        """
        Main function to sort array using randomized quick sort
        """
        self.reset_stats()
        
        if show_steps:
            print("=" * 70)
            print("RANDOMIZED QUICK SORT - Step by Step")
            print("=" * 70)
            print(f"Original array: {arr}\n")
        
        self.quicksort_recursive(arr, 0, len(arr) - 1, show_steps)
        
        if show_steps:
            print("\n" + "=" * 70)
            print(f"Sorted array: {arr}")
            print("=" * 70)
        
        return arr


def compare_deterministic_vs_randomized():
    """
    Compare deterministic quick sort (always choosing last element)
    with randomized quick sort
    """
    print("\n" + "=" * 70)
    print("COMPARISON: Deterministic vs Randomized Quick Sort")
    print("=" * 70)
    
    # Test on already sorted array (worst case for deterministic)
    sorted_arr = list(range(1, 21))
    
    print("\nTest Case 1: Already Sorted Array (Worst case for deterministic)")
    print(f"Array: {sorted_arr}")
    print("-" * 70)
    
    # Deterministic Quick Sort
    det_sorter = RandomizedQuickSort()
    arr1 = sorted_arr.copy()
    start = time.time()
    det_sorter.partition = lambda arr, low, high, show=False: standard_partition(arr, low, high, det_sorter)
    det_sorter.quicksort_recursive(arr1, 0, len(arr1) - 1)
    det_time = time.time() - start
    
    print(f"Deterministic Quick Sort:")
    print(f"  Comparisons: {det_sorter.comparisons}")
    print(f"  Swaps: {det_sorter.swaps}")
    print(f"  Max recursion depth: {det_sorter.max_depth}")
    print(f"  Time: {det_time:.6f} seconds")
    
    # Randomized Quick Sort
    rand_sorter = RandomizedQuickSort()
    arr2 = sorted_arr.copy()
    start = time.time()
    rand_sorter.sort(arr2)
    rand_time = time.time() - start
    
    print(f"\nRandomized Quick Sort:")
    print(f"  Comparisons: {rand_sorter.comparisons}")
    print(f"  Swaps: {rand_sorter.swaps}")
    print(f"  Max recursion depth: {rand_sorter.max_depth}")
    print(f"  Time: {rand_time:.6f} seconds")
    
    # Test on random array
    random_arr = random.sample(range(1, 101), 20)
    
    print("\n" + "-" * 70)
    print("\nTest Case 2: Random Array")
    print(f"Array: {random_arr}")
    print("-" * 70)
    
    # Randomized Quick Sort on random array
    rand_sorter2 = RandomizedQuickSort()
    arr3 = random_arr.copy()
    start = time.time()
    rand_sorter2.sort(arr3)
    rand_time2 = time.time() - start
    
    print(f"Randomized Quick Sort:")
    print(f"  Comparisons: {rand_sorter2.comparisons}")
    print(f"  Swaps: {rand_sorter2.swaps}")
    print(f"  Max recursion depth: {rand_sorter2.max_depth}")
    print(f"  Time: {rand_time2:.6f} seconds")


def standard_partition(arr, low, high, sorter):
    """Helper function for deterministic partition"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        sorter.comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            sorter.swaps += 1
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    sorter.swaps += 1
    
    return i + 1


def experiment_with_different_inputs():
    """
    Experiment with different types of input arrays
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT: Randomized Quick Sort on Different Input Types")
    print("=" * 70)
    
    sorter = RandomizedQuickSort()
    
    test_cases = [
        ("Random array", random.sample(range(1, 51), 15)),
        ("Sorted array", list(range(1, 16))),
        ("Reverse sorted", list(range(15, 0, -1))),
        ("All same elements", [5] * 15),
        ("Nearly sorted", [1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 13, 12, 14, 15]),
        ("Few unique values", [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
    ]
    
    for name, arr in test_cases:
        print(f"\n{name}:")
        print(f"Input:  {arr}")
        
        arr_copy = arr.copy()
        sorter.reset_stats()
        start = time.time()
        sorter.sort(arr_copy)
        elapsed = time.time() - start
        
        print(f"Output: {arr_copy}")
        print(f"Stats: Comparisons={sorter.comparisons}, Swaps={sorter.swaps}, "
              f"Max_Depth={sorter.max_depth}, Time={elapsed:.6f}s")


def multiple_runs_analysis():
    """
    Run randomized quick sort multiple times on same input
    to show variation in performance
    """
    print("\n" + "=" * 70)
    print("ANALYSIS: Multiple Runs on Same Input")
    print("=" * 70)
    
    input_arr = random.sample(range(1, 51), 20)
    print(f"Input array: {input_arr}\n")
    
    runs = 5
    stats = []
    
    for i in range(runs):
        sorter = RandomizedQuickSort()
        arr_copy = input_arr.copy()
        sorter.sort(arr_copy)
        stats.append({
            'comparisons': sorter.comparisons,
            'swaps': sorter.swaps,
            'depth': sorter.max_depth
        })
        print(f"Run {i+1}: Comparisons={sorter.comparisons}, "
              f"Swaps={sorter.swaps}, Max_Depth={sorter.max_depth}")
    
    # Calculate averages
    avg_comp = sum(s['comparisons'] for s in stats) / runs
    avg_swaps = sum(s['swaps'] for s in stats) / runs
    avg_depth = sum(s['depth'] for s in stats) / runs
    
    print(f"\nAverage over {runs} runs:")
    print(f"  Comparisons: {avg_comp:.1f}")
    print(f"  Swaps: {avg_swaps:.1f}")
    print(f"  Max Depth: {avg_depth:.1f}")


# Main execution
if __name__ == "__main__":
    # Example 1: Detailed step-by-step execution
    print("EXAMPLE 1: Step-by-Step Execution")
    print("=" * 70)
    
    sorter = RandomizedQuickSort()
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    print(f"Array to sort: {arr}\n")
    
    sorted_arr = sorter.sort(arr.copy(), show_steps=True)
    
    print(f"\nFinal Statistics:")
    print(f"  Total comparisons: {sorter.comparisons}")
    print(f"  Total swaps: {sorter.swaps}")
    print(f"  Maximum recursion depth: {sorter.max_depth}")
    
    # Example 2: Compare deterministic vs randomized
    compare_deterministic_vs_randomized()
    
    # Example 3: Different input types
    experiment_with_different_inputs()
    
    # Example 4: Multiple runs analysis
    multiple_runs_analysis()
    
    print("\n" + "=" * 70)
    print("EXPERIMENTS COMPLETED!")
    print("=" * 70)