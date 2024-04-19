class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        _sum = sum(nums)
        nums = nums + nums
        min_length = float("inf")
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]

        rem = target%_sum

        holder = {0:-1}

        for i in range(len(nums)):
            diff = nums[i] - rem

            if diff in holder:
                min_length = min(min_length, i-holder[diff])

            holder[nums[i]] = i

        if min_length == float("inf"): return -1

        return min_length + n*(target//_sum)

        

        # _sum = 0
        # holder = {0:1}
        # i = 0
        # min_length = 10e5
        # while i<10e5:
        #     _sum+=nums[i%len(nums)]
        #     if (_sum - target) in holder:
        #         min_length = min(min_length, i-holder[_sum-target])

        #     holder[_sum] = i 

        #     i+=1

        # if min_length == 10e5:
        #     return - 1
        # return min_length

        # prefix = []
        # holder = {0:1}
        # for i in range(len(nums)*2):
        #     prefix.append(prefix[-1]+nums[i%len(nums)])
        #     if
            

        # print(prefix)
        # return 2

        # prefix = []
        # suffix = []
        # holder = {0:0}
        # min_length = float("inf")
        # for i in range(len(nums)):
        #     if i == 0:
        #         prefix.append(nums[i])
        #         suffix.append(nums[-i-1])
        #     else:
        #         prefix.append(prefix[-1] + nums[i])
        #         suffix.append(suffix[-1] + nums[i])

        #     if prefix[i]-target in holder:
        #         min_length =  min(min_length, i+1 - holder[prefix[i]-target])

        #     holder[prefix[i]] = i+1


        # k = target/prefix[-1]
        # remainder = target - k*prefix[-1]

        # if remainder == 0:
        #     min_length = min(min_length, k*len(nums))

        # for i in range(len(suffix)):
        #     if remainder-suffix[i] in holder:
        #         print(holder)
        #         min_length = min(min_length, i + holder[remainder-suffix[i]]+1 + k*prefix[-1])

        # # return min_length

        # if min_length == float("inf"):
        #     return -1
        
        # return min_length


        