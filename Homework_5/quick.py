__author__ = 'Pratik'


def sorting(list, start, end):
    # if len(list) == 1 and start <= end and end >= 0:
    #     return
    # pivot = start
    # left = start + 1
    # right = end
    #
    # while left <= right:
    #     while left <= end:
    #         if list[pivot] > list[left] and left <= right:
    #             left += 1
    #         else:
    #             break
    #     while right >= start:
    #         if list[right] > list[pivot] and right >= left:
    #             right -= 1
    #         else:
    #             break
    #     if list[left] < list[right]:
    #         list[left], list[right] = list[right], list[left]
    #     else:
    #         break
    # list[pivot], list[right] = list[right], list[pivot]
    # sorting(list, start, right-1)
    # sorting(list, right+1, end)


    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right and left <= end and right >= start:
        if list[pivot] > list[left]:
            left += 1
        elif list[right] > list[pivot]:
            right -= 1
        else:
            list[left], list[right] = list[right], list[left]
    list[pivot], list[right] = list[right], list[pivot]
    sorting(list, start, right)
    sorting(list, right+1, end)

if __name__ == '__main__':
    list1 = [5, -3, 7, 12, 9, 6, -8, 4, 11]
    sorting(list1, 0, len(list1) - 1)
    print(list1)


# def sortBoard(nums):
#     # if len(boardList) == 1:
#     #     return boardList[0]
#     # pivot = 0
#     # leftPointer = 1
#     # rightPointer = len(boardList)
#     # while(leftPointer <= rightPointer):
#     #     while(boardList[leftPointer].sum < boardList[pivot].sum):
#     #         leftPointer += 1
#     #     while(boardList[rightPointer].sum > boardList[pivot].sum):
#     #         rightPointer -= 1
#     #     boardList[leftPointer], boardList[rightPointer] = boardList[rightPointer], boardList[leftPointer]
#     # boardList[pivot], boardList[rightPointer] = boardList[rightPointer], boardList[pivot]
#     # rightPointer += 1
#     # sortBoard(boardList[:rightPointer])
#     # sortBoard(boardList[rightPointer+1:])
#     '''
#     returns a sorted copy of the list
#     :param nums:
#     :return:
#     '''
#     if len(nums) <= 1:
#         return nums[:]
#     # divide list into two halves
#     mid = len(nums)//2
#     left = nums[:mid]
#     right = nums[mid:]
#     # sort each half (mergesort)
#     left = sortBoard2(left)
#     right = sortBoard2(right)
#     # merge two sorted piles back together
#     lf = 0
#     rf = 0
#     sorted = []
#     while lf < len(left) and rf < len(right):
#         if left[lf].sum < right[rf].sum:
#             sorted.append(left[lf])
#             lf += 1
#         else:
#             sorted.append(right[rf])
#             rf += 1
#     if lf == len(left):
#         sorted.extend(right[rf:])
#     else:
#         sorted.extend(left[lf:])
#     return sorted
#
#
#
# def sortBoard2(nums):
#     # if len(boardList) == 1:
#     #     return
#     # pivot = start
#     # leftPointer = start + 1
#     # rightPointer = end
#     # while(leftPointer <= rightPointer):
#     #     while(boardList[leftPointer] < boardList[pivot]):
#     #         leftPointer += 1
#     #         if (leftPointer > rightPointer):
#     #             break
#     #     while(boardList[rightPointer] > boardList[pivot]):
#     #         rightPointer -= 1
#     #         if (rightPointer < leftPointer):
#     #             break
#     #     boardList[leftPointer], boardList[rightPointer] = boardList[rightPointer], boardList[leftPointer]
#     # boardList[pivot], boardList[rightPointer] = boardList[rightPointer], boardList[pivot]
#     # rightPointer += 1
#     # sortBoard2(boardList, start, rightPointer)
#     # sortBoard2(boardList, rightPointer+1, end)
#
#     '''
#     returns a sorted copy of the list
#     :param nums:
#     :return:
#     '''
#     if len(nums) <= 1:
#         return nums[:]
#     # divide list into two halves
#     mid = len(nums)//2
#     left = nums[:mid]
#     right = nums[mid:]
#     # sort each half (mergesort)
#     left = sortBoard2(left)
#     right = sortBoard2(right)
#     # merge two sorted piles back together
#     lf = 0
#     rf = 0
#     sorted = []
#     while lf < len(left) and rf < len(right):
#         if left[lf] < right[rf]:
#             sorted.append(left[lf])
#             lf += 1
#         else:
#             sorted.append(right[rf])
#             rf += 1
#     if lf == len(left):
#         sorted.extend(right[rf:])
#     else:
#         sorted.extend(left[lf:])
#     return sorted