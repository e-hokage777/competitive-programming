class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        
        num_boxes = len(boxes)
        min_operations = []

        
        for i in range(num_boxes):
            operation_count = 0
            for j in range(num_boxes):
                if i == j: continue
                elif boxes[j] == "1": operation_count += abs(i-j)

            min_operations.append(operation_count)
            operation_count = 0

        return min_operations