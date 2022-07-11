import sys
from collections import deque

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class MinHeap():
    def __init__(self,max_size):
        self.maxsize = max_size
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = (-1 * sys.maxsize,None)
        self.front = 1

    def getValue(self,pos):
        if self.heap[pos] == 0:
            return 0
        else:
            return self.heap[pos][0]

    def parent(self,pos):
        return pos // 2

    def leftChild(self,pos):
        return 2 * pos
    
    def rightChild(self,pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return (pos*2) > self.size

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def minHeapify(self,pos):
        if(self.isLeaf(pos)):
            return

        if(self.getValue(pos) > self.getValue(self.leftChild(pos)) or self.getValue(pos) > self.getValue(self.rightChild(pos))):
            if(self.getValue(self.leftChild(pos)) < self.getValue(self.rightChild(pos))):
                self.swap(pos, self.leftChild(pos))
                self.minHeapify(self.leftChild(pos))
            else:
                self.swap(pos, self.rightChild(pos))
                self.minHeapify(self.rightChild(pos))

    def insert(self,element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.heap[self.size] = element

        current = self.size

        while self.getValue(current) < self.getValue(self.parent(current)):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT {}: ".format(self.heap[i])
            + " LEFT CHILD {}: ".format(self.heap[2 * i])
            + " RIGHT CHILD {}: ".format(self.heap[2 * i + 1]))

    def remove(self):
        if(self.size == 0):
            return None
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size-= 1
        self.minHeapify(self.front)
        return popped

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left 
    
    def get_right_child(self):
        return self.right 
    
    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def set_left_child(self,node):
        self.left = self.checkNodeType(node)
    
    def set_right_child(self,node):
        self.right = self.checkNodeType(node)

    def checkNodeType(self,element):
        #If type of element is Node then no need to create another node
        if(type(element[1]) == Node):
            return element[1]
        return Node(element[1])


    def __repr__(self):
        return str(self.value)
    
class Tree():
    def __init__(self):
        self.root = None

    def set_root(self,node):
        self.root = node
    
    def get_root(self):
        return self.root

    def get_huffman_encoded_values(self):
        return self.get_binary_rec(self.get_root(),{},"")

    def get_binary_rec(self,node,output,current):
        if(node is None):
            return

        if not node.has_left_child() and not node.has_right_child():
            output[node.value] = current
        else:
            self.get_binary_rec(node.get_left_child(),output,current + "0")
            self.get_binary_rec(node.get_right_child(),output,current + "1")

        return output

    def get_huffman_decoded_values(self,data):
        if(data is None):
            return

        output = ""
        node = self.get_root()
        for char in data:
            if(char == '0' and node.has_left_child()):
                node = node.get_left_child()
            elif(char == '1' and node.has_right_child()):
                node = node.get_right_child()
            
            if(not node.has_right_child() and not node.has_left_child()):
                output += node.value
                node = self.get_root()
        return output

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "HUFFMAN Tree \n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s

def get_huffman_tree(data):
    huffman_tree = Tree()
    if(not data):
        return huffman_tree

    #Get character count with help of dictonary
    character_frequency = dict()
    for char in data:
        character_frequency[char] = character_frequency.get(char,0) + 1

    heap = MinHeap(len(character_frequency))
    heap_dict = [(value,key) for key,value in character_frequency.items()]

    #Insert elements in minheap
    for i in heap_dict:
        heap.insert(i)
    heap.minHeap()                        
    huffman_tree.set_root(getTree(heap))
    return huffman_tree

def getTree(heap):
    if(heap.size == 1):
        return Node(heap.remove())
    while(heap.size > 1):
        #Get 2 minimum elements and add them in tree
        min_element_1 = heap.remove()
        min_element_2 = heap.remove()
        node = Node(min_element_1[0] +  min_element_2[0])
        node.set_left_child(min_element_1)
        node.set_right_child(min_element_2)

        heap.insert((node.get_value(),node))
        heap.minHeap()
    return heap.remove()[1]

def huffman_encoding(data):

    #Get huffman tree with help of min heap
    huffman_tree = get_huffman_tree(data)
    print(huffman_tree)
    encoded_data = huffman_tree.get_huffman_encoded_values()   
    print("\n HUFFMAN ENCODED DATA: ", encoded_data)
    result = ""
    for char in data:
        result += encoded_data[char]
    return result                                                                                                           

def huffman_decoding(data,tree):
    if(not data):
        return data
    return tree.get_huffman_decoded_values(data)


print('''
CASE 1: 
Empty Data
In this case output should be empty
''')
case_1 = ""
encoded_data = huffman_encoding(case_1)
print("\n ENCODED DATA:",encoded_data) #
print("\n DECODED DATA:",huffman_decoding(encoded_data,get_huffman_tree(case_1))) #


print('''
CASE 2: 
Single Alphabet Data
In this case output should be Same as case
''')
case_2 = "ABC"
encoded_data = huffman_encoding(case_2)
print("\n ENCODED DATA:",encoded_data) #10011
print("\n DECODED DATA:",huffman_decoding(encoded_data,get_huffman_tree(case_2))) #ABC

print('''
CASE 3: 
Multiple Alphabet Data
''')
case_3 = "AAAAAAABBBCCCCCCCDDEEEEEE"
encoded_data = huffman_encoding(case_3)
print("\n ENCODED DATA:",encoded_data) #1111111111111100100100110101010101010000000010101010101
print("\n DECODED DATA:",huffman_decoding(encoded_data,get_huffman_tree(case_3))) #AAAAAAABBBCCCCCCCDDEEEEEE