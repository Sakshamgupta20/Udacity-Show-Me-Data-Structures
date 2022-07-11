class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    union= set()

    node = llist_1.head
    while(node is not None):
        union.add(node.value)
        node = node.next
    
    node = llist_2.head
    while(node is not None):
        if(node.value not in union):
            union.add(node.value)
        node = node.next
    return union
    

def intersection(llist_1, llist_2):
    smaller_node,larger_node = (llist_1.head,llist_2.head) if llist_1.size() <= llist_2.size() else (llist_2.head,llist_1.head)

    smaller_dict = set()
    intersection = set()
    while(smaller_node is not None):
        smaller_dict.add(smaller_node.value)
        smaller_node = smaller_node.next
    
    while(larger_node is not None):
        if(larger_node.value in smaller_dict):
            intersection.add(larger_node.value)
        larger_node = larger_node.next
    return intersection

# Test case 1
print('''
CASE 1: 
Passing No values in both lists
''') # Empty sets

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))


# Test case 2
print('''
CASE 2: 
Passing values in one of the lists
''')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,2,3,4,5,6,7]
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # {1, 2, 3, 4, 5, 6, 7}
print (intersection(linked_list_1,linked_list_2)) # Empty set

# Test case 2
print('''
CASE 3: 
Passing same values in both lists
''')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,2,3,4,5,6,7]
element_2 = [1,2,3,4,5,6,7]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # {1, 2, 3, 4, 5, 6, 7}
print (intersection(linked_list_1,linked_list_2)) # {1, 2, 3, 4, 5, 6, 7}