class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_sorted_list = sorted(nums1+nums2)
        if(len(new_sorted_list) % 2 == 0):
            median = (new_sorted_list[len(new_sorted_list)//2] + new_sorted_list[(len(new_sorted_list)//2) - 1]) / 2
        else:
            median = new_sorted_list[len(new_sorted_list)//2]      
        return median