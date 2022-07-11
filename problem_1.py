from queue import Queue
class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = 5
        self.num_elements = 0
        self.cache = dict()
        self.q = Queue(maxsize = capacity)
        

    def get(self, key):
        if(key in self.cache):
            self.update_queue(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if(key in self.cache):
            self.update_queue(key)
            self.cache[key] = value
        #If queue is not full then add elements directly
        elif(not self.q.full()):
            self.cache[key] = value
            self.q.put(key)
        #If queue is full and element is new then get first element from queue and remove it
        else:
            least_used_key = self.q.get()
            self.cache.pop(least_used_key)
            self.cache[key] = value
            self.q.put(key)
    
    #When element exists in cache then update its queue position to last element in queue
    def update_queue(self,key):
        helper_q = Queue(maxsize = self.capacity)
        while(not self.q.empty()):
            last = self.q.get()
            if(last != key):
                helper_q.put(last)
        self.q = helper_q
        self.q.put(key)
            
        
            

def create_full_queue():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    our_cache.set(5, 5);
    return our_cache



case_1 = create_full_queue()
case_1.set(6, 6);
print('''
CASE 1: 
ADDING new ELEMENT when queue is full
In this case 1 is least used so it should be removed from cache
OUTPUT: {}
'''.format(case_1.cache)) # {2: 2, 3: 3, 4: 4, 5: 5, 6: 6}




case_2 = create_full_queue()
case_2.get(1)
case_2.get(3)
case_2.set(6, 6)

print('''
CASE 2: Getting elements from cache then adding new elements
In this case 2 is least used so it should be removed from cache
OUTPUT: {}
'''.format(case_2.cache)) # {1: 1, 3: 3, 4: 4, 5: 5, 6: 6}

case_3 = create_full_queue()
case_3.set(1,1)
case_3.set(2,2)
case_3.set(6, 6)

print('''
CASE 3: Getting elements from cache then adding new elements
In this case 3 is least used so it should be removed from cache
OUTPUT: {}
'''.format(case_3.cache)) # {1: 1, 2: 2, 4: 4, 5: 5, 6: 6}