
nums = [2,4,5,64,332,33,123,5,794,759,56878,64] 
target= 127
ans =0
arr_len = len(nums) 
for x in range(arr_len):
    ans = target - nums[x]                
    if ans in nums and (nums.index(ans) != x ) :
    	print( x,nums.index(ans) )
    	break  