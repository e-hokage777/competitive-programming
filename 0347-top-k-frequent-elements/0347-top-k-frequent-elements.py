from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = Counter(nums)
        values = []
        holder = dict()
        for key,v in counter.items():
            values.append(v)
            holder[v] = key


        def bucket_sort(values):
            buckets = [[] for _ in range(len(values)+1)]
            min_val = min(values)
            max_val = max(values)


            

            for val in values:
                index = len(values) * (val - min_val)/max_val
                buckets[index].append(val)

            result = []
            for bucket in buckets:
                bucket.sort()
                result.extend(bucket)

            return result

        ans = []        
        values_sorted = bucket_sort(values)


        for i in range(k):
            ans.append(holder[values_sorted[-i-1]])

        return ans

        
        