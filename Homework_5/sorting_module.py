__author__ = 'zjb'

# linear search is O(n), such as:
def search(vals,target):
    for item in vals:
        if item == target:
            return True
    return False

def indexof(vals,target):
    '''
    Returns -1 if not in list
    :param vals:
    :param target:
    :return:
    '''
    for i in range(len(vals)):
        if vals[i] == target:
            return i
    return -1 #yuck. False? None? Explode?

# if data is sorted, we can do binary search:
def bsearch(vals,target):
    if len(vals) == 0:
        return False
    mid = len(vals)//2
    if target == vals[mid]:
        return True
    if target < vals[mid]:
        return bsearch(vals[:mid],target)
    else:
        return bsearch(vals[mid+1:],target)

def bindex(vals,target):
    if len(vals) == 0:
        raise ValueError() # or something else?
    mid = len(vals)//2
    if target == vals[mid]:
        return mid
    if target < vals[mid]:
        return bindex(vals[:mid],target)
    else:
        return mid+1 + bindex(vals[mid+1:],target)

def bindex_rec(vals,left,right,target):
    '''
    left inclusive, right exclusive
    :param vals:
    :param left:
    :param right:
    :param target:
    :return:
    '''
    if left >= right:
        return -1
    mid = (right+left)//2
    if target == vals[mid]:
        return mid
    if target < vals[mid]:
        return bindex_rec(vals,left,mid,target)
    else:
        return bindex_rec(vals,mid+1,right,target)

# helper function:
def bindex2(vals,target):
    return bindex_rec(vals,0,len(vals),target)

def sort_them(nums):
    # selection sort in place:
    for finger in range(len(nums)-1):
    # find smallest number from where our finger is
        smallest = finger
        for index in range(finger,len(nums)):
            if nums[index] < nums[smallest]:
                smallest = index
            # put it at the finger
        nums[smallest], nums[finger] = nums[finger], nums[smallest]

def mergesort(nums):
    '''
    returns a sorted copy of the list
    :param nums:
    :return:
    '''
    if len(nums) <= 1:
        return nums[:]
    # divide list into two halves
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    # sort each half (mergesort)
    left = mergesort(left)
    right = mergesort(right)
    # merge two sorted piles back together
    lf = 0
    rf = 0
    sorted = []
    while lf < len(left) and rf < len(right):
        if left[lf] < right[rf]:
            sorted.append(left[lf])
            lf += 1
        else:
            sorted.append(right[rf])
            rf += 1
    if lf == len(left):
        sorted.extend(right[rf:])
    else:
        sorted.extend(left[lf:])
    return sorted

nums = [4, 7, 2, 1, 8, 3, 6]
print("5?", search(nums,5))
print("1?", search(nums,1))

nums = [5, -3, 7, 12, 9, 6, -8, 4, 11]
#sort_them(nums)
nums = mergesort(nums)
print(nums)
print("5?", bindex2(nums,5))
print("12?", bindex2(nums,12))
print("0?", bindex2(nums,0))
