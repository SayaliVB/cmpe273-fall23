import hashlib

class MerkleNode:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.hash = ''

        if data is not None:
            self.update_hash(data)

    def update_hash(self, data):
        sha256 = hashlib.sha256()
        sha256.update(data.encode('utf-8'))
        self.hash = sha256.hexdigest()

class MerkleTree:
    def __init__(self, data_list=None):
        self.root = None
        self.leaf_nodes = []
       
        if data_list is not None:
            for data in data_list:
                self.add_leaf_node(data)

    def add_leaf_node(self, data):
        new_node = MerkleNode(data=data)
        self.leaf_nodes.append(new_node)
        self.update_tree()

    def update_tree(self):
        current_level = self.leaf_nodes
        while len(current_level) > 1:
            parent_level = []
            for index in range(0, len(current_level), 2):
                left_node = current_level[index]
                right_node = current_level[index + 1] if index + 1 < len(current_level) else left_node

                parent_node = MerkleNode(left=left_node, right=right_node)
                parent_node.update_hash(left_node.hash + right_node.hash)

                parent_level.append(parent_node)

            current_level = parent_level

        if len(current_level) == 1:
            self.root = current_level[0]

    def remove_node(self, query_data):
        query_hash = hashlib.sha256(query_data.encode('utf-8')).hexdigest()
       
        for index, leaf in enumerate(self.leaf_nodes):
            if leaf.hash == query_hash:
                del self.leaf_nodes[index]
                self.update_tree()
                return True
        return False

# Test MerkleTree
data_list = ['data1', 'data2', 'data3']

# Initialize Merkle tree
tree = MerkleTree(data_list)

# Add data to the tree
tree.add_leaf_node('data4')
tree.add_leaf_node('data5')

# Remove data from the tree
successful_removal = tree.remove_node('data3')
print(successful_removal)  # Output: True