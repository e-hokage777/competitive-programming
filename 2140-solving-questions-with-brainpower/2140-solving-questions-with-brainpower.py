class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """

        n = len(questions)
        scores = [x[0] for x in questions]

        result = 0
        for i in range(n-1, -1, -1):
            score, brainpower = questions[i]
            if i < n-1:
                scores[i] = max(scores[i], scores[i+1])
            if i+brainpower+1 < n:
                scores[i] = max(score + scores[i+brainpower+1], scores[i])

        return scores[0]