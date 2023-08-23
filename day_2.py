# Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero.

# Note: Return 1, if there is at least one triplet following the condition else return 0.

# Example 1:

# Input: n=5, arr[]=(0, -1, 2, 3, 1) Output: 1

# Explanation: 0, -1, and 1 form a triplet with a sum equal to 0.

# Example 2:

# Input: n=3, arr[]=(1,2,3)

# Output: 0

# Explanation: No triplet with zero-sum exists.

################################################################################################################################################################################

#Solution

def triplet(arr,n):

    for i in range(n-1):
        s = set()

        for j in range(i+1,n):
            complement = -arr[i] - arr[j]

            if complement in s:
                return 1
            s.add(arr[j])
    
    return 0