class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        scores = dict()
        one_count = sum(nums)
        zero_count = 0
        max_score = 0
        max_scores = []
        
        scores[0] = one_count
        max_score = one_count

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                one_count -= 1

            score = zero_count + one_count

            if score > max_score:
                max_score = score

            scores[i+1] = score
            

        for k in scores:
            if scores[k] == max_score:
                max_scores.append(k)


        return max_scores
        