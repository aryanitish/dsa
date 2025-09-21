class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_size = len(nums)
        pivot = 101 
        swap = 0

        # Pivot is first descending number
        for i in range(1, num_size):
            if nums[num_size - 1 - i] < nums[num_size - i]:
                pivot = num_size - 1 - i
                break
        
        # Pivot = 101 means last permutation as max array size is 100
        if pivot == 101:
            nums.reverse()
            return
        # Find smallest number larger than nums[pivot] on right side
        else:
            # assign bigger number index as swap 
            if nums[pivot + 1] > nums[pivot]:
                swap = pivot + 1
            else:
                swap = pivot
            
            # index boundary check
            if pivot + 2 < num_size:
                for i in range(pivot + 2, num_size):
                    if nums[i] > nums[pivot]: 
                        if nums[i] < nums[swap]:
                            swap = i

        # Swap pivot number with smallest larger number on right
        nums[pivot], nums[swap] = nums[swap], nums[pivot]

        # Sort numbers after new swapped pivot
        nums[pivot+1:] = sorted(nums[pivot+1:])
