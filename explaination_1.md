Here I have used 2 data structures 
1 -> Hash map => To student key value pairs
2 -> Queue (First In First Out)=> To store keys
Here when cache is full, we get the 1 element from queue and remove it from cache.


Time Complexity -> 

    CASE 1 -> Queue is empty
        Hash map -> O(1)
        Queue PUT -> O (1)
        Overall ADD => O(2) -> O(1)

    CASE 2 -> Queue is full
        Hash map PUT -> O(1)
        Hash map POP -> O(1)
        Queue POP -> O(1)
        Overall => O(3) -> O(1)

    CASE 3 -> Same element is getting updated
        Hash map PUT -> O(1)
        Queue UPDATE -> O(N)
        Overall => O(1 + N) => O(N)
        
Space Complexity -> 
    N -> Keys, M -> Values
    Hash Map -> O(N + M)
    Queue -> O(N)
    Overall -> O(2N + M) => O(N)
