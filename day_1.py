# 📋 Day 1 Problem Statement 👨‍💻

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i th line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store

#####################################################################################################################################################################################

#Solution

def maximun_area(hei):
    maximun_area = 0

    l = 0
    r = len(h)-1

    while l<r:
        th = min(h[l], h[r])
        maximun_area = max(maximun_area, th * (r-l))

        if h[l] < h[r]:
            l += 1
        else:
            r -= 1

    return maximun_area
