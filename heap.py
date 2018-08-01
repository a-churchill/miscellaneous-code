import numpy as np


class MaxHeap:
    """
    An implementation of a max heap data structure
    Holds integers only

    Attributes:
        heap_arr    Array representation of heap

    Methods:
        get_max     Returns maximum element

        extract_max Returns and deletes maximum element

        insert      Inserts new element into heap

        edit_val    Edits the value at the given index
    """

    
    # Python methods
    def __init__(self, input):
        """
        Constructor, initializes heap from list
        
        
        Arguments:
            input {list[int]} -- List used to initialize heap
        """
        self.create_heap(input)
        return

    def __len__(self):
        """
        Returns number of elements in heap

        Returns:
            int -- Length of heap
        """
        return len(self.heap_arr)

    def __str__(self):
        """
        Returns sorted string representation of heap

        Returns:
            string -- String representation of heap
        """
        old = self.heap_arr.copy()
        result = []
        while len(self) != 0:
            result.append(self.extract_max())
            # print("Current result: {0}".format(str(result)))
        self.heap_arr = old
        return str(result)
        
    # public methods
    def get_max(self):
        """
        Returns maximum value in heap

        Returns:
            int -- Max value in heap
        """
        return self.heap_arr[0]

    def extract_max(self):
        """
        Returns and deletes maximum value in heap

        Returns:
            int -- Max value in heap
        """
        temp = self.heap_arr[0]
        self.heap_arr[0] = self.heap_arr[-1]
        self.heap_arr[-1] = temp
        result = self.heap_arr.pop()
        self.heapify(0)
        return result

    def insert(self, val):
        """
        Inserts given value into heap
        
        Arguments:
            val {int} -- Value to insert
        """
        if type(val) != int:
            return
        # index of inserted value
        index = len(self.heap_arr)
        self.heap_arr.append(val)
        # checks if parent is less than inserted value
        swap_needed = (self.heap_arr[self.parent(index)] < val)
        while (index >= 1 and swap_needed):
            # swaps parent and inserted value
            parent_val = self.heap_arr[self.parent(index)]
            self.heap_arr[index] = parent_val
            self.heap_arr[self.parent(index)] = val
            index = self.parent(index)
            swap_needed = (self.heap_arr[self.parent(index)] < val)

        return

    def edit_val(self, key, new_val):
        """
        Changes the value of the element with the given key value to the new value. Only changes the first instance
        
        Arguments:
            key {int} -- Key (value) of the element to change
            new_val {int} -- New value of element
        """
        # check input
        if type(new_val) != int:
            return
        if self.heap_arr.count(key) == 0:
            return
        loc = self.heap_arr.index(key)
        # swap last element and element to switch
        self.heap_arr[loc] = self.heap_arr[-1]
        self.heap_arr.pop()
        self.heapify(key)
        self.insert(new_val)

    # private methods
    def parent(self, i):
        """
        Returns the parent of the element at index i
        
        Arguments:
            i {int} -- Index to find parent of

        Returns:
            int -- Index of parent
        """
        result = i + 1
        result = result // 2
        result -= 1
        return result

    def left(self, i):
        """
        Returns the left child of element at index i 
        
        Arguments:
            i {int} -- Index to find left child of

        Returns:
            int -- Index of left child
        """
        return (i + 1)*2 - 1

    def right(self, i):
        """
        Returns the right child of the element at index i
        
        Arguments:
            i {int} -- Index to find right child of

        Returns:
            int -- Index of right child
        """
        return (i + 1)*2
    
    def heapify(self, i):
        """
        Fixes error in max heap rules at root specified by index i

        Assumes left(i) and right(i) are valid max heaps
        
        Arguments:
            i {int} -- Index of root with error
        """

        if self.left(i) >= len(self) and self.right(i) >= len(self):
            return
        elif self.right(i) >= len(self): # node has one child only
            assert(self.left(i) == len(self) - 1)
            left_val = self.heap_arr[self.left(i)]
            current_val = self.heap_arr[i]
            if current_val >= left_val:
                return
            else:
                # swap
                self.heap_arr[self.left(i)] = current_val
                self.heap_arr[i] = left_val
                self.heapify(self.left(i))
                return
        # print("Recurse continuing. Length: {0}; left: {1}; right: {2}".format(str(len(self)), str(self.left(i)), str(self.right(i))))
        left_val = self.heap_arr[self.left(i)]
        right_val = self.heap_arr[self.right(i)]
        current_val = self.heap_arr[i]
        if current_val >= left_val and current_val >= right_val:
            return
        else:
            if left_val > right_val:
                # swap
                self.heap_arr[self.left(i)] = current_val
                self.heap_arr[i] = left_val
                self.heapify(self.left(i))
            else: # right > left
                self.heap_arr[self.right(i)] = current_val
                self.heap_arr[i] = right_val
                self.heapify(self.right(i))


    def create_heap(self, arr):
        """
        Creates heap data structure from unordered list of ints
        
        Arguments:
            arr {list[int]} -- Unordered list to create heap from
        """
        if arr is None or len(arr) == 0:
            self.heap_arr = []
            return
        self.heap_arr = arr
        for i in range(len(arr)//2 + 1, -1, -1):
            self.heapify(i)

    

# testing
def main():
    with open("tests.txt", "r") as tests_file:
        tests = tests_file.read()
        tests = tests.split("\n")
        counter = 1
        for test in tests:
            if test == "":
                continue
            params = test.split("~")
            initial = num_list(params[0])
            instructions = params[1]
            instructions = instructions[1:-1]
            if len(instructions) == 0:
                instructions = []
            else:
                instructions = [x.strip() for x in instructions.split(',')]
            vals = num_list(params[2])
            results = num_list(params[3])
            final = num_list(params[4])
            # print("Initial: {0}".format(str(initial)))
            # print("Instructions: {0}".format(str(instructions)))
            # print("Vals: {0}".format(str(vals)))
            # print("Results: {0}".format(str(results)))
            # print("Final: {0}".format(str(final)))
            print("Test {0}:".format(counter))
            counter += 1
            run_test(initial, instructions, vals, results, final)
            print("====================")
            print()

def run_test(initial, instructions, vals, results, final):
    """
    Runs a test with the given parameters
    
    Arguments:
        initial {list[int]} -- List of integers to initialize the heap
        instructions {list[string]} -- List of instructions to call
        vals {list[int]} -- List of values (if any) to use with the method calls
        results {list[int]} -- List of expected results (if any) of the method calls
        final {list[int]} -- String representation of the expected heap at the end of all method calls
    """

    mh = MaxHeap(initial)
    vals.reverse()
    my_vals = vals
    # print("my_vals: {0}".format(str(my_vals)))
    actual_results = []
    for instr in instructions:
        # print("Current my_vals: {0}".format(str(my_vals)))
        val = my_vals.pop()
        if instr == "get_max":
            actual_results.append(mh.get_max())
        elif instr == "extract_max":
            actual_results.append(mh.extract_max())
        elif instr == "insert":
            actual_results.append(None)
            mh.insert(val)
        elif instr == "edit_val":
            actual_results.append(None)
            mh.edit_val(val[0], val[1])
        else:
            raise Exception("Incorrect argument for method to use")
    actual_results = str(actual_results)
    expected_results = str(results)
    heap = str(mh)
    exp_heap = str(final)

    print("Actual results:   {0}".format(actual_results))
    print("Expected results: {0}".format(expected_results))
    if actual_results.strip() == expected_results.strip():
        print("PASS!")
    else:
        print("FAIL")
    print()
    print("Actual heap:   {0}".format(heap))
    print("Expected heap: {0}".format(exp_heap))
    if exp_heap.strip() == heap.strip():
        print("PASS!")
    else:
        print("FAIL")

def num_list(to_parse):
    """
    Creates list from its string representation
    
    Arguments:
        to_parse {string} -- String representation of list, can include 'None' or internal lists, represented by separation with '#'
    
    Returns:
        list[int] -- List represented in to_parse
    """
    if len(to_parse) == 2:
        return []
    inter = to_parse[1:-1]
    inter = [x.strip() for x in inter.split(',')]
    result = []
    for n in inter:
        if n == "None":
            result.append(None)
        elif "#" in n:
            result.append([int(x) for x in n.split("#")])
        else:
            result.append(int(n))
    return result


if __name__ == '__main__':
    main()
