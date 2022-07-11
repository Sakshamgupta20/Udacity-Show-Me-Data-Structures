import hashlib
import datetime
class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)
    
        return sha.hexdigest()

    def __repr__(self):
        return '''[{} {} {} {}]'''.format(self.timestamp,self.data,self.previous_hash,self.hash)

    def __str__(self):
        return '''[{} {} {} {}]'''.format(self.timestamp,self.data,self.previous_hash,self.hash)
    

class BlockChain:
    def __init__(self):
        self.tail = None
        self.blocks = dict()

    def add(self,block):
        if block is None:
            return

        if self.tail is None or block.previous_hash == self.tail or self.blocks[self.tail].previous_hash is None:
            self.tail = block.hash
        self.blocks[block.hash] = block

    def __repr__(self):
        curr = self.tail
        output = ""
        while(curr is not None):
            block = self.blocks[curr]
            output = " <-- " + str(block) + output
            curr = block.previous_hash    
        return  "None" + output   
        

# Test case 1
print('''
CASE 1: 
Passing No Blocks in blockchain
''') # Empty sets
blockchain = BlockChain()
print(blockchain)

# Test case 2
print('''
CASE 2: 
Passing 1 Block in blockchain
''') # Empty sets
blockchain = BlockChain()
blockchain.add(Block(datetime.datetime.now(),1,None))
print(blockchain)

# Test case 3
print('''
CASE 3: 
Passing multiple Blocks in blockchain
''') # Empty sets
blockchain = BlockChain()
block1 = Block(datetime.datetime.now(),1,None)
block2 = Block(datetime.datetime.now(),2,block1.hash)
block3 = Block(datetime.datetime.now(),3,block2.hash)
block4 = Block(datetime.datetime.now(),4,block3.hash)
blockchain.add(block1)
blockchain.add(block2)
blockchain.add(block3)
blockchain.add(block4)
print(blockchain)

