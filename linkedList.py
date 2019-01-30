class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


# Add two linked list: 2.5 Sum Lists: You have two numbers represented by.
# EXAMPLE Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.  Output: 2 -> 1 -> 9. That is, 912.
    def insert(self, data):
        """
        Inserts to the head of the list
        :param data:
        :return: None
        """
        new_head = Node(data)
        head = self.head
        if not head:  # list is empty
            self.head = new_head
        else:  # set cur head as the next to new_head
            new_head.next = head
            self.head = new_head  # set new head a the head of the list

    def insert_to_tail(self, data):
        """
        Inserts to the tail of the list
        :param data:
        :return: None
        """
        new_tail = Node(data)
        tail = self.tail
        if not tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail

    def delete(self, data):
        """
        Deletes a node from a list
        :param data: value of node to be deleted
        :return:
        """
        cur = self.head
        found = False
        prev = None
        while cur and not found:
            if cur.data != data:
                prev = cur
            else:
                found = True
                if prev is None:  # Head to be deleted
                    self.head = cur.next
                else:
                    prev.next = cur.next
            cur = cur.next
        if not found:  # Node not found
            raise ValueError("Node not Found")

    def traverse_list(self):
        """
        Traverses and prints node value for a list
        :return:
        """
        cur = self.head
        while cur:
            print(cur.data, "-> ", end='')
            cur = cur.next
        print()  # To avoid in-line print for next list

    def sum_to_tail(self, h1, h2):
        """
        Sums tow numbers represented by two linked list
        Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.  Output: 2 -> 1 -> 9. That is, 912.
        :param h1: head of list 1
        :param h2: head of list 2
        :return: head of new list
        """
        c = 0  # carry
        while h1 or h2:
            s = c  # sum
            if h1:
                s += h1.data
                h1 = h1.next
            if h2:
                s += h2.data
                h2 = h2.next
            self.insert_to_tail(int(s % 10))
            c = s / 10
        if int(c) > 0:
            self.insert_to_tail(int(c))  # last carry


# Delete node for a list
print("\n------------------ Delete a node from a linked list ---------------------------\n")
dlist = LinkedList()
dlist.insert(5)
dlist.insert(4)
dlist.insert(6)
dlist.insert(4)
print("List before deleting 4")
dlist.traverse_list()
print("List after deleting 4")
dlist.delete(4)
dlist.traverse_list()


# Sample input for sum_to_tail method
print("\n--------------------- Sum two lists and return head of new list --------------------\n")
print("Inserting Node ---------")
nlist = LinkedList()
nlist.insert(6)
nlist.insert(1)
nlist.insert(7)
nlist.traverse_list()

mlist = LinkedList()
mlist.insert(2)
mlist.insert(9)
mlist.insert(5)
mlist.traverse_list()

print (nlist.head.data)
olist = LinkedList()
olist.sum_to_tail(nlist.head, mlist.head)
olist.traverse_list()
