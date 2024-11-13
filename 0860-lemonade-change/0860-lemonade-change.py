class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        bills_available = [0,0,0]

        for bill in bills:
            if bill == 5: bills_available[0] += 1
            if bill == 10: bills_available[1] += 1
            if bill == 20: bills_available[2] += 1

            change = bill - 5
            
            if change == 5:
                if not bills_available[0]:
                    return False
                else: bills_available[0]-=1

            if change == 15:
                if bills_available[0] and bills_available[1]:
                    bills_available[0]-=1
                    bills_available[1]-=1
                elif bills_available[0] >= 3:
                    bills_available[0]-=3
                else:
                    return False


        return True
        