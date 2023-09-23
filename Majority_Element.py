def check_majority(nums, M):
    # Check if M appears more than n/2 times in nums
    # Runs in O(n)
    
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] == M:
            count += 1
    if count > n/2:
        return True
    else:
        return False

def candidate_element(nums):
    # Is there a candidate value M that may appear more than n/2 times?
    # Runs in O(n)
    
    n = len(nums)
    B = []
    if n == 1:
        return nums[0]
    
    else:
        if n//2 == 1 and check_majority(nums, nums[n-1]):
            return nums[n-1]
        
        else:
            nums = nums[:n-1]
            for i in range(n/2):
                if nums[i] == nums[i + 1]:
                    B.append(nums[i])
            return majority_element(B)

def majority_element(nums):
    # Is there a value M that appears more than n/2 times?
    # Runs in O(n)
    
    candidate = candidate_element(nums)
    return [candidate, check_majority(nums, candidate)]