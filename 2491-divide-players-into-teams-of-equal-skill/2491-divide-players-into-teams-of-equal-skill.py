class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """

        skill.sort()

        l = 0
        r = len(skill) - 1
        common_skill = skill[l] + skill[r]
        chemistry = skill[l] * skill[r]
        l+=1
        r-=1
        while l < r:
            if skill[l] + skill[r] == common_skill:
                chemistry += skill[l] * skill[r]
            else:
                chemistry = -1
                break

            l+=1
            r-=1

        return chemistry

        