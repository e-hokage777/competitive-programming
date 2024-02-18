class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        results_dict = dict()
        for win,loss in matches:
            results_dict[win] = results_dict.get(win, 0)
            results_dict[loss] = results_dict.get(loss, 0) + 1

        no_losses = []
        one_loss = []
        for key in results_dict:
            if results_dict[key] == 0:
                no_losses.append(key)
            
            if results_dict[key] == 1:
                one_loss.append(key)

        return [sorted(no_losses), sorted(one_loss)]