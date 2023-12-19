import hashlib

class MerkleNode:
    def __init__(self, data):
        self.data = data
        self.hash = hashlib.sha256(data.encode()).hexdigest()
        self.left = None
        self.right = None

def create_leaf_nodes(data):
    leaf_nodes = []
    for d in data:
        node = MerkleNode(d)
        leaf_nodes.append(node)
    return leaf_nodes

def build_tree(leaf_nodes):
    nodes = leaf_nodes[:]
    while len(nodes) > 1:
        new_nodes = []
        for i in range(0, len(nodes), 2):
            node = MerkleNode('')
            node.left = nodes[i]
            if i + 1 < len(nodes):
                node.right = nodes[i + 1]
            node.hash = hashlib.sha256((node.left.hash + (node.right.hash if node.right else '')).encode()).hexdigest()
            new_nodes.append(node)
        nodes = new_nodes[:]
    return nodes[0]

def compare_merkle_roots(root1, root2):
    return root1.hash == root2.hash

# Example usage
data1 = ["Data1", "Data2", "Data3", "Data4"]
data2 = ["Data1", "Data2", "ChangedData", "Data4"]

leaf_nodes1 = create_leaf_nodes(data1)
leaf_nodes2 = create_leaf_nodes(data2)

merkle_root1 = build_tree(leaf_nodes1)
merkle_root2 = build_tree(leaf_nodes2)

if compare_merkle_roots(merkle_root1, merkle_root2):
    print("Datasets are consistent.")
else:
    print("Datasets have discrepancies.")
