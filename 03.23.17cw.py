def make_pi():
    return [3,1,4]

def same_first_last(nums):
    if len(nums) >= 1:
        return nums[0] == nums[-1]
    else:
        return False

def common_end(a, b):
    return a[-1] == b[-1] or a[0] == b[0]

def has23(nums):
    return 2 in nums or 3 in nums

def count_evens(nums):
    i = 0
    count = 0
    while i < len(nums):
        if nums[i]%2 == 0:
            count += 1
        i += 1
    return count

def big_diff(nums):
    i = 0
    biggest = 0
    smallest = 100
    while i < len(nums) :
        smallest = min(nums[i],smallest)
        biggest = max(nums[i], biggest)
        i += 1
    return biggest - smallest

def centered_average(nums):
    i = 0
    biggest = 0
    smallest = 100
    while i < len(nums):
        smallest = min(nums[i],smallest)
        biggest = max(nums[i], biggest)
        i += 1
    nums.remove(biggest)
    nums.remove(smallest)
    print nums
    j = 0
    sums = 0
    while j < len(nums):
        sums = sums + nums[j]
        j += 1
    return sums / len(nums)

def toDec(string,base):
    i = -1
    exp = 0
    total = 0
    while abs(i) <= len(string):
        total = total + int(string[i]) * base ** exp
        i += -1
        exp += 1
    return total
