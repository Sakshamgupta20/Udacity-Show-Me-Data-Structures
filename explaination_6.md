We used set here because, its a dictonary with no values so time complexity will be O(1)

UNION
    Here we have used set to store all values of first list
    Then if 1st list value if not present in 2nd list we add it in set

    Time Complexity -> 
        We parse through both lists once
        llist1 = L1 O(L1)
        llist2 = L2 O(L2)
        SET = S -> O(1)
        OVERALL => O(L1 + L2 + 1) -> O(N)

    Space Complexity -> 
        Storing Data
            llist1 = L1 O(L1)
            llist2 = L2 O(L2)
            output set = O(L1 + L2) => O(N) #Worst case if both lists have different values
    
INTERSACTION
    Here we have used set to store all values of smaller list
    Then if set has values of larger list we store it in seperate set

    Time Complexity -> 
        We parse through both lists once
        llist1 = L1 O(L1)
        llist2 = L2 O(L2)
        SET = S -> O(1)
        OVERALL => O(L1 + L2 + 1) -> O(N)

    Space Complexity -> 
        Storing Data
            llist1 = L1 O(L1)
            llist2 = L2 O(L2)
            temp set = S1 O(S1)
            output set = O(L1 + L2 + S1) => O(N) #Worst case if both lists have same values
    