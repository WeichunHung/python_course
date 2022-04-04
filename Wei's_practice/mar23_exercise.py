x = int(input("請輸入數字: "))

for n in range(2, x+1):
    if n == x:
        print("是質數")
        break
    if x % n == 0:
        print("不是質數")
        break


"""
n = int(input("請輸入數字:"))
x = 2

while x < n:
    if n % x == 0:
        print("不是質數")
        break
    x = x + 1
if x == n:
    print("是質數")
"""
"""
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

nums = [2, 7, 11, 15]
target = 9

for i in nums:
    print(i)
