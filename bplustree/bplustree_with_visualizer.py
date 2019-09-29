"""
Developed by:
 - Vasilis Dimitriadis - WckdAwe ( http://github.com/WckdAwe )
 - Taxiarchis Kouskouras - TheNotoriousCS ( https://github.com/TheNotoriousCS )
The following algorithms have been developed based on:
 - https://en.wikipedia.org/wiki/B%2B_tree
 - https://www.javatpoint.com/b-plus-tree
 - https://web.stanford.edu/class/cs346/2015/notes/Blink.pptx

Influenced a lot by:
 - https://gist.github.com/savarin/69acd246302567395f65ad6b97ee503d
 - https://github.com/pschafhalter/python-b-plus-tree
 - http://www.cburch.com/cs/340/reading/btree/
"""
from __future__ import annotations

from bplustree import BPlusTree, LeafNode
from graphviz import Digraph, nohtml


class GraphableBPlusTree(BPlusTree):

    def view_graph(self, graph_name='bplustree'):
        if self.root.is_empty():
            print('The B+ Tree is empty!')
            return

        g = Digraph('g', filename=graph_name+'.gv', node_attr={'shape': 'record', 'height': '.1'})
        g.format = 'svg'
        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)

            if not isinstance(node, LeafNode):
                queue += node.values

            design = ''
            if isinstance(node, LeafNode):
                for i in range(len(node.keys)):
                    design += '<f' + str(i*2) + '> | {{ <f' + str(i*2 + 1) + '> {' + str(i) + '} | {{' + ', '.join(map(str, node.values[i])) + '}} }}| '
                design += '<f' + str(len(node.keys)*2) + '>'
            else:
                for i in range(len(node.keys)):
                    design += '<f' + str(i*2) + '> | <f' + str(i*2 + 1) + '> {' + str(i) + '} | '
                design += '<f' + str(len(node.keys)*2) + '>'

            g.node('node'+str(node.uid), nohtml(design.format(*node.keys)))

            if not isinstance(node, LeafNode):
                for i, value in enumerate(node.values):
                    mid_key = len(value.keys)
                    g.edge('node{}:f{}'.format(node.uid, i*2), 'node{}:f{}'.format(value.uid, mid_key))
            else:
                pass
        g.view()


if __name__ == '__main__':
    print('Initializing B+ tree...')
    bplustree = GraphableBPlusTree(order=5)
    bplustree.insert(13, 'November')
    bplustree.insert(0, '_')
    bplustree.insert(7, 'Hotel')
    bplustree.insert(8, 'India')
    bplustree.insert(5, 'Echo')
    bplustree.insert(6, 'Golf')
    bplustree.insert(4, 'Delta')
    bplustree.insert(1, 'Alpha')
    bplustree.insert(2, 'Bravo')
    bplustree.insert(3, 'Charlie')
    bplustree.insert(9, 'Juliet')
    bplustree.insert(2, 'Bravo2')
    bplustree.insert(10, 'Kilo')
    bplustree.insert(11, 'Lima')
    bplustree.insert(12, 'Mike')
    bplustree.insert(17, 'Romeo')
    bplustree.insert(14, 'Oscar')
    bplustree.insert(15, 'Papa')
    bplustree.insert(16, 'Quebec')

    bplustree.view_graph()
