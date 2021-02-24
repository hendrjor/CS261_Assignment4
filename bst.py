# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """Adds a new value to the tree"""
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return

        current = self.root
        while current is not None:  # runs until the desired node is reached
            if value < current.value:
                if current.left is None:
                    current.left = node
                    return
                current = current.left

            elif value >= current.value:
                if current.right is None:
                    current.right = node
                    return
                current = current.right

    def contains(self, value: object) -> bool:
        """Determines if the binary tree contains the given value"""
        current = self.root
        while current is not None:  # runs until the value is found
            if value < current.value:
                current = current.left
            elif value >= current.value:
                if current.value == value:  # if the value is found, return True
                    return True
                current = current.right
        return False

    def get_first(self) -> object:
        """Returns the first value stored at the root node"""
        if self.root is None:
            return None
        return self.root.value

    def remove_first(self) -> bool:
        """Removes the root node from the tree"""
        pass
        # values = Queue()
        # current = self.root
        # if current.right is None and current.left is not None:
        #     self.root = current.left
        #     return True
        #
        # address = 0
        # current = current.right
        #
        # while current.left is not None:  # runs until the value is found
        #     address += 1
        #     values.enqueue(current.value)
        #     current = current.left
        #
        # print(values)
        #
        # delete = self.root.right
        # for i in range(address):
        #     delete = delete.left
        # return delete

    def remove(self, value) -> bool:
        """Removes the first instance of the given value in the binary tree"""
        pass
        # current = self.root
        # while current is not None:  # runs until the value is found
        #     if value < current.value:
        #         current = current.left
        #     elif value >= current.value:
        #         if current.value == value:  # if the value is found, return True
        #             return True
        #         current = current.right

    def pre_order_traversal(self) -> Queue:
        """Traverses the binary tree in pre-order"""
        values = Queue()
        if self.root is None:
            return values
        values.enqueue(self.root)

        if self.root.left is not None:
            values = self.pre_order_traversal_helper(self.root.left, values)

        if self.root.right is not None:
            values = self.pre_order_traversal_helper(self.root.right, values)

        return values

    def pre_order_traversal_helper(self, node, values):
        """Helps traverse the binary tree recursively"""
        node_added = False
        if node.left is not None:
            values.enqueue(node.value)
            self.pre_order_traversal_helper(node.left, values)
            node_added = True

        if node.right is not None:
            if node_added is not True:
                values.enqueue(node.value)
            self.pre_order_traversal_helper(node.right, values)

        if node.left is None and node.right is None:
            values.enqueue(node.value)

        return values

    def in_order_traversal(self) -> Queue:
        """Traverses the binary tree in order"""
        values = Queue()
        if self.root is None:
            return values
        order = self.in_order_traversal_helper(self.root, values)
        return order

    def in_order_traversal_helper(self, node, values):
        """Helps traverse the binary tree recursively"""
        if node.left is not None:
            self.in_order_traversal_helper(node.left, values)

        values.enqueue(node.value)

        if node.right is not None:
            self.in_order_traversal_helper(node.right, values)
        return values

    def post_order_traversal(self) -> Queue:
        """Traverses and returns values in post-order"""
        values = Queue()
        if self.root is None:
            return values

        if self.root.left is not None:
            values = self.post_order_traversal_helper(self.root.left, values)

        if self.root.right is not None:
            values = self.post_order_traversal_helper(self.root.right, values)
        values.enqueue(self.root)

        return values

    def post_order_traversal_helper(self, node, values):
        """Helps traverse the binary tree recursively"""
        if node.left is not None:
            self.post_order_traversal_helper(node.left, values)

        if node.right is not None:
            self.post_order_traversal_helper(node.right, values)

        values.enqueue(node.value)
        return values

    def by_level_traversal(self) -> Queue:
        """Traverses and returns values in highest level first"""
        values = Queue()
        temp_values = Queue()
        if self.root is None:
            return values

        node = self.root
        values.enqueue(node)
        temp_values.enqueue(node)  # creates temp list so the program can access past nodes

        while temp_values.is_empty() is False:

            node = temp_values.dequeue()

            if node.left is not None:
                values.enqueue(node.left)
                temp_values.enqueue(node.left)
            if node.right is not None:
                values.enqueue(node.right)
                temp_values.enqueue(node.right)

        return values

    def is_full(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_complete(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_perfect(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def size(self) -> int:
        """Returns the total number of nodes in the tree"""
        temp_values = Queue()
        if self.root is None:
            return 0

        count = 1
        node = self.root
        temp_values.enqueue(node)  # creates temp list so the program can access past nodes

        while temp_values.is_empty() is False:
            node = temp_values.dequeue()

            if node.left is not None:
                temp_values.enqueue(node.left)
                count += 1

            if node.right is not None:
                temp_values.enqueue(node.right)
                count += 1

        return count

    def height(self) -> int:
        """Determines the height of the binary tree"""
        return self.height_helper(self.root)

    def height_helper(self, node):
        """Recursively goes through the binary tree to determine height"""
        if node is None:
            return -1

        left_height = self.height_helper(node.left)
        right_height = self.height_helper(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def count_leaves(self) -> int:
        """Counts the number of leaves in the binary tree"""
        if self.root is None:
            return 0
        leaves = Queue()
        leaves = self.count_leaves_helper(self.root, leaves)
        count = 0
        while leaves.is_empty() is False:
            leaves.dequeue()
            count += 1
        return count

    def count_leaves_helper(self, node, leaves):
        """Recursively goes through the binary tree"""
        if node.left is not None:
            self.count_leaves_helper(node.left, leaves)

        if node.right is not None:
            self.count_leaves_helper(node.right, leaves)

        if node.left is None and node.right is None:
            leaves.enqueue(node)

        return leaves

    def count_unique(self) -> int:
        """Counts the number of unique nodes in the tree"""
        unique = Queue()
        # temp = Queue()
        in_order = self.in_order_traversal()
        # print(in_order)

        iterations = 0
        while in_order.is_empty() is False:
            temp_val = in_order.dequeue()
            # print(temp_val)
            # temp.enqueue(temp_val)
            if in_order.is_empty() is False:
                temp_val2 = in_order.dequeue()
                if temp_val2 != temp_val:
                    unique.enqueue(temp_val)
                    in_order.enqueue(temp_val)
            else:
                unique.enqueue(temp_val)

        count = 0
        while unique.is_empty() is False:
            unique.dequeue()
            count += 1

        return count


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    # """ add() example #1 """
    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # tree = BST()
    # print(tree)
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree)
    # tree.add(15)
    # tree.add(15)
    # print(tree)
    # tree.add(5)
    # print(tree)

    # """ add() example 2 """
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # tree = BST()
    # tree.add(10)
    # tree.add(10)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # tree.add(5)
    # print(tree)
    # tree.add(-1)
    # print(tree)

    # """ contains() example 1 """
    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))

    # """ contains() example 2 """
    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))

    # """ get_first() example 1 """
    # print("\nPDF - method get_first() example 1")
    # print("----------------------------------")
    # tree = BST()
    # print(tree.get_first())
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree.get_first())
    # print(tree)

    # """ remove() example 1 """
    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.remove(7))
    # print(tree.remove(15))
    # print(tree.remove(15))
    #
    # """ remove() example 2 """
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.remove(20))
    # print(tree)
    #
    # """ remove() example 3 """
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    # print(tree.remove(20))
    # print(tree)
    # # comment out the following lines
    # # if you have not yet implemented traversal methods
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    # """ remove_first() example 1 """
    # print("\nPDF - method remove_first() example 1")
    # print("-------------------------------------")
    # tree = BST([10, 15, 5])
    # print(tree.remove_first())
    # print(tree)

    # """ remove_first() example 2 """
    # print("\nPDF - method remove_first() example 2")
    # print("-------------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7])
    # print(tree.remove_first())
    # print(tree)

    # """ remove_first() example 3 """
    # print("\nPDF - method remove_first() example 3")
    # print("-------------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)

    # """ Traversal methods example 1 """
    # print("\nPDF - traversal methods example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    # """ Traversal methods example 2 """
    # print("\nPDF - traversal methods example 2")
    # print("---------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    # """ Comprehensive example 2 """
    # print("\nComprehensive example 2")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'N/A   {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in 'DATA STRUCTURES':
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print('', tree.pre_order_traversal(), tree.in_order_traversal(),
    #       tree.post_order_traversal(), tree.by_level_traversal(),
    #       sep='\n')
    #
