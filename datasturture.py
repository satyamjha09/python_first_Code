# nums = [1,2,2,3,3,4,5,6,7]
# print(set(nums))

# nums = [10,20,30]
# print(nums[1])



# nums = [1,2,3]
# nums[0] = 100
# print(nums)

nums = [4,3,6,3,4,2]

nums.sort()

print(nums)

nums.reverse()

print(nums)

nums.append(100)
print(nums)

nums.extend([200,300,400])
print(nums)

nums.insert(4,543)
print(nums)


b = nums.copy()

print(b)