import unittest
import hrw
import mmh3


class Ring(object):
    '''A ring of nodes supporting rendezvous hashing based node selection.'''
    def __init__(self, nodes=None):
        nodes = nodes or {}
        self._nodes = set(nodes)
        self.hash_function = lambda x: mmh3.hash128(x)

    def add(self, node):
        '''Add the given node to the _nodes set.'''
        if node not in self._nodes:
            self._nodes.add(node)
        
    def nodes(self):
        return self._nodes
    
    def remove(self, node):
        '''Remove the given node from the _nodes set.'''
        if node in self._nodes:
            self._nodes.remove(node)
        
    def hash(self, key):
        '''Return the node to which the given key hashes to.'''
        assert len(self._nodes) > 0
        ''' 
        TODO
        1. Loop through all the nodes.
        2. Compute the weight for each node for the given key.
        3. return the node that gave the highest weight.
        '''
        high_score = -1
        high_node = None
        for node in self._nodes:
            score = self.hash_function("%s-%s" % (str(key), str(node)))
            print(score)
            if score > high_score:
                (high_score, high_node) = (score, node)
            elif score == high_score:
                (high_score, high_node) = (score, max(str(node), str(high_node)))
        return high_node


class RingTest(unittest.TestCase):
    def setUp(self):
        self.node1 = '127.0.0.1:3000'
        self.node2 = '127.0.0.1:4000'
        self.node3 = '127.0.0.1:5000'
        

    def test_add_remove(self):
        ring = hrw.Ring()
        ring.add(self.node1)
        ring.add(self.node2)
        ring.add(self.node3)
        self.assertEqual({self.node1, self.node2, self.node3}, ring.nodes())
        
        ring.remove(self.node1)
        self.assertEqual({self.node2, self.node3}, ring.nodes())
        ring.remove(self.node2)
        ring.remove(self.node3)
        self.assertEqual(set(), ring.nodes())


    def test_hash(self):
        ring = hrw.Ring({self.node1})
        keys = [str(x) for x in range(100)]
        for k in keys:
            self.assertEqual(self.node1, ring.hash(k))

        ring.add(self.node2)
        ring.add(self.node3)
        counts = {
            self.node1: 0,
            self.node2: 0,
            self.node3: 0
        }
        key2node_1 = []
        for k in keys:
            node = ring.hash(k)
            key2node_1.append((k, node))
            counts[node] += 1
        
        key2node_2 = []
        for k in keys:
            node = ring.hash(k)
            key2node_2.append((k, node))
        
        # Two iterations should generate the same key-2-node mapping.
        self.assertEqual(key2node_1, key2node_2)
        print ("Num of entries / node:", counts)
        # For 100 keys, each slot should have at least 10 entries.
        self.assertTrue(10 <= counts[self.node1])
        self.assertTrue(10 <= counts[self.node2])
        self.assertTrue(10 <= counts[self.node3])
        

if __name__ == "__main__":
    unittest.main()