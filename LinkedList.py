
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        # first we make a new node
        new_node = Node(value)

        # if no head is found that means the LL is empty
        if not self.head:
            self.head = new_node

# whenever there is already
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_from_head(self):
        # if nothing is list return None
        if not self.head:
            return

        new_head = self.head.next
        removed = self.head
        self.head = new_head
        removed.next = None
        return removed.value

    def contains(self, target):
        # when the head None
        curr_node = self.head
        while curr_node:
            if curr_node.value == target:
                return True
            curr_node = curr_node.next
        return False

    def sizeHelper(self, node):
        if not node:
            return 0
        return 1 + self.sizeHelper(node.next)

    def size(self):
        return self.sizeHelper(self.head)


ll = Linked_List()
ll.add_to_head(3)
ll.add_to_head(2)
ll.add_to_head(1)
ll.add_to_head(0)


print(ll.contains(3))
print(ll.contains(100))

print(ll.size())
