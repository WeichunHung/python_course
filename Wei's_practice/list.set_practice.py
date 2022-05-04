# 題目：
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_] #印出不重複數字, 把重複數字變_
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

s = set(nums) #變set
l = list(s) #變list
i = len(nums) - len(s) #重複的數量
for x in range(i):
    l.append("_")

print(len(s), l)

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4, _ , _ , _ , _ , _]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
