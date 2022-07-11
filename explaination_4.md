Here we have used recursion to check user in each group

Time Complexity -> 
    We parse through all of users in the group and all the group
    Users per group -> U
    Sub groups inside group -> G
    OVERALL => O(U + G) -> O(N)

Space Complexity -> 
    Storing Data
        Users per group -> U
        Sub groups inside group -> G
        OVERALL => O(N)

    Finding User -> 
        We dont use and space while checking for user
