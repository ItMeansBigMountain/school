def sort(nums):
    for i in range(len(nums)):
        minposition = i
        
        for x in range(i,len(nums)):
            if nums[x] < nums[minposition]:
                minposition = x

        temp = nums[i]
        nums[i] = nums[minposition]
        nums[minposition] = temp




arr = [5,3,8,6,7,2]
sort(arr)
print(arr)