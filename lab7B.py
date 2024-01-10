
""" Given functions """

def empty_tree_fn():
    return 0

def leaf_fn(key):
    return key**2

def inner_node_fn(key, left_value, right_value):
    return key + left_value



""" Self-made functions """

def is_empty_tree(tree):
    """ Checks if tree is empty """

    return isinstance(tree, list) and not tree

def is_leaf(tree):
    """ Checks if elemnt in tree is a leaf """
    return isinstance(tree, int)

def is_subtree(tree):
    """ Checks if element in tree is a subtree """

    return isinstance(tree, list)

def key(tree):
    """ Returns key element """
    
    return tree[1]

def left_subtree(tree):
    """ Returns left subtree """
    
    return tree[0]

def right_subtree(tree):
    """ Returns right subtree """
    
    return tree[2]



def traverse(tree, node_func, leaf_func, empty_func):
    """ Function that checks each branch in a tree recursively """

    if is_empty_tree(tree):
        return empty_func()
    
    if is_leaf(tree):
        
        return leaf_func(tree)

    elif is_subtree(tree):
        left = traverse(left_subtree(tree), node_func, leaf_func, empty_func)
        right = traverse(right_subtree(tree), node_func, leaf_func, empty_func)
        return node_func(key(tree), left, right)
    
   

def contains_key(value, tree):
    """ Returns whether or not a tree contains a certain value """

    def node_func(key, left, right):
        if value == key or left or right:
            return True
        return False
    
    def leaf_func(tree):
        if value == tree:
            return True
        return False
        
    def empty_func():
        return False

    return traverse(tree, node_func, leaf_func, empty_func)
    


def tree_size(tree):
    """ Function that returns size of tree """
    
    def node_func(key, left, right):
   
        return left + 1 + right

    def leaf_func(tree):
        return 1

    def empty_func():
        return 0

    return traverse(tree, node_func, leaf_func, empty_func)



def tree_depth(tree):
    """ Function that returns depth of tree """

    def node_func(key, left, right):
        #res = 1 + left if (1 + left) > (1 + right) else 1 + right
        
        left_or_right = left if left >= right else right

        return left_or_right + 1

    def leaf_func(tree):
        return 1

    def empty_func():
        return 0

    return traverse(tree, node_func, leaf_func, empty_func)

# print(tree_depth([1, 5, [10, [], 14]]))

if __name__ == '__main__':

    """ Traverse """
    assert traverse([[2, 3, []], 5, [6, 7, 8]], inner_node_fn, leaf_fn, empty_tree_fn) == 12
    assert traverse([6, 5, 8], inner_node_fn, leaf_fn, empty_tree_fn) == 41
    assert traverse([[], 5, [7, 10, []]], inner_node_fn, leaf_fn, empty_tree_fn) == 5
    assert traverse([[10, 4, [2, 3, [4, 5, 7]]], 5, [1, 2, [2, 3, 4]]], inner_node_fn, leaf_fn, empty_tree_fn) == 109 # 10^2 + 4 + 5
    assert traverse([[4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, 2]]]]]], 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4,[4 , 4,[2, 3, 4]]]]]]]], inner_node_fn, leaf_fn, empty_tree_fn) == 24
    assert traverse([], inner_node_fn, leaf_fn, empty_tree_fn) == 0


    """ Contains key """
    assert contains_key(6, []) == False
    assert contains_key(6, [7, 6, 8]) == True
    assert contains_key(2, [[6, 7, 8], 5, [1, 2, 3]]) == True
    assert contains_key(9, [[1, 2, [2, 3, 4]], 5, [10, 4, [2, 3,[4, 5, 7]]]]) == False
    assert contains_key(10, [[1, 2, [2, 3, 4]], 5, [10, 4, [2, 3,[4, 5, 7]]]]) == True
    assert contains_key([], [2, 5, 5]) == False
    assert contains_key([], []) == False
    

    """ Tree size """
    assert tree_size([2, 5, []]) == 2
    assert tree_size([[6, 7, 8], 5, [1, 2, 3]]) == 7
    assert tree_size([[1, 2, []], 4, [[], 5, 6]]) == 5
    assert tree_size([[10, 4, [2, 3, [4, 5, 7]]], 5, [1, 2, [2, 3, 4]]]) == 13
    assert tree_size([[4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, 2]]]]]], 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4,[4 , 4,[2, 3, 4]]]]]]]]) == 29
    assert tree_size([]) == 0


    """ Tree depth """
    assert tree_depth([[1, 2, [2, 3, 4]], 5, [10, 4, [2, 3,[4, 5, 7]]]]) == 5
    assert tree_depth([1, 2, 3]) == 2
    assert tree_depth([[1, 2, [4, 6, 1]], 2, [1, 5, [7, 8, 9]]]) == 4
    assert tree_depth(9) == 1
    assert tree_depth([1, 2, []]) == 2
    assert tree_depth([[1, 2, [2, 3, []]], 5, [10, 4, [2, 3,[[], 5, []]]]]) == 4
    assert tree_depth([[], 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [2, 3, 4]]]]]]]]) == 9
    assert tree_depth([4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [2, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4,[4 , 4,[2, 3, 4]]]]]]]]]]]]]]) == 15
    assert tree_depth([[4, 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4, 2]]]]]], 4, [4, 4, [4, 4, [4, 4, [4, 4, [4, 4,[4 , 4,[2, 3, 4]]]]]]]]) == 9
    assert tree_depth([[1,3,1],2,[2,4,2]]) == 3
    assert tree_depth([]) == 0


    print("The code passed all the tests")