class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    # Insert node
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2*self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)
    
    def delete(self, key):
        pass

    def search(self, key):
        pass

    # Insert nonfull
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2*self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    # Split the child
    def split_child(self, i, x):
        t = self.t
        y = i.child[x]
        z = BTreeNode(y.leaf)
        i.child.insert(x+1, z)
        i.keys.insert(x, y.keys[t-1])
        z.keys = y.keys[t: (2*t) - 1]
        y.keys = y.keys[0: t-1]
        if not y.leaf:
            z.child = y.child[t: 2*t]
            y.child = y.child[0: t-1]    

    # Print the tree
    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

b = BTree(3)
for i in range(10):
    b.insert(i)
b.print_tree(b.root)
