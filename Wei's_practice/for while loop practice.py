'''
#1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
nums = [2,7,11,15]

for i in nums:
    for a in nums:
        if i + a == 9:
            n = nums.index(i)
            print(n)
'''         
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

strs = ['flower','flow','flight']
