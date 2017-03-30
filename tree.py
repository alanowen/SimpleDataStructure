class TreeNode:
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self):
        self.root = TreeNode()

    def clear_tree(self):
        pass

    def is_tree_empty(self):
        return True if self.root.lchild is None \
                and self.root.rchild is None else False

    def get_tree_depth(self):
        pass

    def get_root(self):
        return self.root

    def get_parent(self, node):
        pass

    def insert_child(self, node):
        pass

    def delete_child(self, node):
        pass


class BinaryTree(Tree):
    def __init__(self):
        def _create(node):
            data = input('Node:')
            if data == '':
                node = None
            else:
                node.data = data
                node.lchild = TreeNode()
                node.rchild = TreeNode()
                _create(node.lchild)
                _create(node.rchild)
        super(BinaryTree, self).__init__()
        _create(self.root)

    def visit_in_pre_order(self, func):
        def _visit(node):
            if node:
                _visit(node.lchild)
                func(node)
                _visit(node.rchild)
        _visit(self.root)

    def visit_in_post_order(self, func):
        def _visit(node):
            if node:
                _visit(node.rchild)
                _visit(node.lchild)
                func(node)
        _visit(self.root)

    def visit_in_middle_order(self, func):
        def _visit(node):
            if node:
                func(node)
                _visit(node.rchild)
                _visit(node.lchild)
        _visit(self.root)

    def visit_in_pre_order_no_recursive(self, func):
        pass

    def visit_in_pre_order_no_recursive(self, func):
        pass

    def visit_in_pre_order_no_recursive(self, func):
        pass


class ThreadBinaryTree(Tree):
    def __init__(self):
        super(ThreadBinaryTree, self).__init__()


if __name__ == '__main__':
    tree = BinaryTree()
    tree.visit_in_post_order(lambda n: print(n.data))
    print(tree.is_tree_empty())
