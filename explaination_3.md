1. Min Heap to get a node that has lower frequency
2. Tree to crete huffman tree

Time Complexity -> 
    Worst Case => All charactes are different in data
    1. We parse through all the characters to create a dictonary => O(N)
    2. Parcing throgh dictonary to create minheap => O(nLogn)
    3. Creating tree with help of min heap => O(N)
    4. Creating encoded values dict with help of huffman tree => O(N)
    5. Mapping encoded values with data => O(N)

    Overall => O(4N + NLogN) => NLogN

Space Complexity ->
    Worst Case => All charactes are different in data
    OVERALL => O(N)
    
