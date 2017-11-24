class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i in range(0 ,len(nums) - 3):
            for l in range(i + 1, len(nums) - 2):
                m = l + 1
                r = len(nums) - 1
                sum = nums[i] + nums[l] + nums[m] + nums[r]
                while l < r:
                    if sum == target:
                        res.append([nums[i],nums[l],nums[m],nums[r]])
                        l += 1
                        r -= 1
                    elif sum < target:
                        while nums[l + 1] == nums[l]:
                            l += 1
                    else:
                        while nums[r] == nums[r - 1]:
                            r -= 1
        return res

time过不了

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = set()
        dict = {}
        if n < 4:
            return []
        
        nums.sort()
        for p in range(n):
            for q in range(p + 1, n):
                if nums[p] + nums[q] not in dict:
                    dict[nums[p] + nums[q]] = [(p, q)]
                else:
                    dict[nums[p] + nums[q]].append((p, q))
        for i in range(n):
            for j in range(i + 1, n - 2):
                T = target - nums[i] - nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]
用字典，把两个数的和存在字典里，同时存储两个数的索引。

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        length = len(nums)
        if length < 4:
            return []
        
        for item_idx in xrange(length - 3):
            if target < nums[item_idx] * 4 or target > nums[-1] * 4:
                break  #两种根本不可能满足条件的情况
            if item_idx > 0 and nums[item_idx - 1] == nums[item_idx]:
                continue #过滤重复元素
                
            item_idx_base = item_idx + 1
            for i in xrange(item_idx_base, length - 2):
                if target - nums[item_idx] < nums[i] * 3 or target - nums[item_idx] > nums[-1] * 3:
                    break
                
                if i > item_idx_base and nums[i - 1] == nums[i]:
                    continue
                    
                l = i + 1
                r = length - 1
                
                while l < r:
                    val = nums[item_idx] + nums[i] + nums[l] + nums[r] - target
                    if val < 0:
                        l += 1
                    elif val > 0:
                        r -= 1
                    else:
                        ret.append([nums[item_idx], nums[i], nums[l], nums[r]])
                        while(l < r and nums[l] == nums[l + 1]):
                            l += 1
                        l += 1 #考虑这里为什么要多加一个 l+=1
        return ret

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return

#迭代的思想