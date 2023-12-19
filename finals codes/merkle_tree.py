import hashlib

class MerkleNode:
    def __init__(self, data) -> None:
        self.right = None
        self.left = None
        self.hash = hashlib.sha256(data.encode()).hexdigest()


class MerkleTree:
    def __init__(self, datalist) -> None:
        
        self.nodes = []
        for data in datalist:
            self.nodes.append(MerkleNode(data))
        self.root = self.create_tree(self.nodes)
    
    def create_tree(self, nodes):

        if(len(nodes) > 1):
            next_level =[]
            for i in range(0, len(nodes), 2):
                left_node = nodes[i]
                right_node = nodes[i+1] if i+1<len(nodes) else nodes[i]
                parent_node = MerkleNode(left_node.hash + "-" +right_node.hash)
                next_level.append(parent_node)
            return self.create_tree(next_level)
        return nodes[0]
    
    def add_leaf_node(self, data):
        self.nodes.append(MerkleNode(data))
        self.root = self.create_tree(self.nodes)
    
    def remove_leaf_node(self, data):
        temp_node = MerkleNode(data)
        for node in self.nodes:
            if node.hash == temp_node.hash:
                self.nodes.remove(node)

        self.root = self.create_tree(self.nodes)

def compare(tree1, tree2):
    if tree1.hash != tree2.hash:
        return False
    left = True
    right = True
    if tree1.left and tree2.left:
        left = compare(tree1.left, tree2.left)
        right = compare(tree1.right, tree2.right)
    
    return left and right



# Test MerkleTree
data_list = ['data1', 'data2', 'data3']
data_list2 = ['data1', 'data2', 'data3']

# Initialize Merkle tree
tree2 = MerkleTree(data_list2)
tree = MerkleTree(data_list)
print("TreeHash: ")
print(tree.root.hash)
print(tree2.root.hash)
print(compare(tree.root, tree2.root))

tree2.add_leaf_node('data5')
tree.add_leaf_node('data4')
print("TreeHash: ")
print(tree.root.hash)
print(tree2.root.hash)

tree2.remove_leaf_node('data1')
tree.remove_leaf_node('data1')
print("TreeHash: ")
print(tree.root.hash)
print(tree2.root.hash)

print(compare(tree.root, tree2.root))
            
