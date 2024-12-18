"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """

        employee_map = dict()
        for index,employee in enumerate(employees):
            employee_map[employee.id] = index

        total_importance = 0

        stack = [id]

        while stack:
            current_id = stack.pop()

            current_employee = employees[employee_map[current_id]]
            total_importance += current_employee.importance

            for sub_id in current_employee.subordinates:
                stack.append(sub_id)

        return total_importance

        