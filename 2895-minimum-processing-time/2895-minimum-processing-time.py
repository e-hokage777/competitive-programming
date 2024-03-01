class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        ## sorting processor times
        processorTime.sort()
        ## sorting tasks
        tasks.sort(reverse=True)

        print(processorTime)
        print(tasks)

        max_time = 0
        processor_ind = 0
        for i in range(len(tasks)):
            if i != 0 and i%4 == 0:
                processor_ind += 1

            if tasks[i] + processorTime[processor_ind] > max_time:
                max_time = tasks[i] + processorTime[processor_ind]

        return max_time
        