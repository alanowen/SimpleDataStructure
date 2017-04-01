class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return '<Node:%s>' % self.data

    # def __repr__(self):
    #     return '<Node:%s>' % self.data


class TreeNode:
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
