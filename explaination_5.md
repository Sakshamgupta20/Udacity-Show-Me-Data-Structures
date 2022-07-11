Here we have create a blockchain linked list to store the last block
linklist also contains a dictonary which store SHA256 hash as key and block as value

Adding a block to blockchain
    Time Complexity -> 
        We just update the tail based on previous value
        Overall => O(1)
    Space Complexity -> 
        We store all blocks in hashmap
        Total Blocks = N
        Overall => O(N)

Printing block chain
    Time Complexity -> 
        Overall => O(N)