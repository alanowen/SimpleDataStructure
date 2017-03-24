class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return '<Node:%s>' % self.data

    # def __repr__(self):
    #     return '<Node:%s>' % self.data


class LinkList:
    def __init__(self, *args):
        self.first = Node(None)
        for i in args:
            n = self.first.next
            p = Node(i)
            p.next = n
            self.first.next = p

    def list_all(self):
        n = self.first.next
        while n:
            print(n.data)
            n = n.next

    def append(self, data):

        last = self.get_tail()
        n = Node(data)
        last.next = n

    def get_tail(self):
        n = self.first.next
        if n:
            while n.next:
                n = n.next
            return n
        return self.first

    def get_length(self):
        i = 0
        n = self.first
        while n:
            i += 1
            n = n.next
        return i

    def get_item_at(self, index):
        length = self.get_length()
        if index >= length:
            raise IndexError()
        n = self.first.next
        for i in range(index):
            n = self.first.next
        return n

    def insert_item_at(self, index):
        length = self.get_length()
        if index >= length:
            raise IndexError()


if __name__ == '__main__':
    l1 = LinkList([1, 2, 3, 4])
    l2 = LinkList()
    l1.list_all()
    l2.list_all()
    l2.append(12)
    l2.append(13)
    l2.append(14)
    l2.list_all()
    print(l2.get_length())
    print(l1.get_length())
    print(l2.get_item_at(3))
