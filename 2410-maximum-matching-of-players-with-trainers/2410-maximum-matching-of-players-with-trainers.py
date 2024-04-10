class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """

        players.sort()
        trainers.sort()
        pp = 0
        tp = 0
        count = 0
        for i in range(len(trainers)):
            if trainers[tp] >= players[pp]:
                count+=1
                pp+=1

                if pp >= len(players):
                    break

            tp+=1

        return count



        