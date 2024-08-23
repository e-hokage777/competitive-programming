class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_len = 1
        holder = [0]*len(nums)
        
        for i in range(len(nums)):
            subs = []
            for j in range(i):
                if nums[i] > nums[j]:
                    count, length = holder[j]
                    subs.append((length+1,count))

            if not subs:
                holder[i] = (1,1)
                continue

            subs.sort(reverse=True)
            longest = subs[0][0]

            max_len = max(max_len, longest)


            longest_count = 0
            for l,c in subs:
                if l == longest:
                    longest_count += c

            holder[i] = (longest_count, longest)

        result = 0
        for c, l in holder:
            if l == max_len:
                result += c

        return result


        