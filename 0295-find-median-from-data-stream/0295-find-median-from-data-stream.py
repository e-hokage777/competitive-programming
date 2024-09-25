class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.right_size = 0
        self.left_size = 0
    
    def add(self, num):
        if not self.root:
            self.root = TreeNode(num)
        else:
            if num <= self.root.val:
                self.left_size += 1
            else:
                self.right_size += 1

            parent = self.root
            current = self.root
            while current:
                parent = current
                if num > current.val: current = current.right
                else: current = current.left

            if num > parent.val: parent.right = TreeNode(num)
            else: parent.left = TreeNode(num)

        # if num == 3:
        #     print(self.right_size , self.left_size, self.root.val)
        self.balance()

    def balance(self):
        if self.right_size > self.left_size:
            parent = self.root
            current = self.root.right
            while current.left:
                parent = current
                current = current.left
            ## connect right children to parent
            parent.left = current.right
            ## make inorder successor parent
            current.left = self.root
            current.right = self.root.right if self.root.right != current else None
            self.root.right = None
            self.root = current
            parent.left = None
            self.right_size -= 1
            self.left_size += 1
                

        elif self.left_size - self.right_size > 1:
            parent = self.root
            current = self.root.left
            while current.right:
                parent = current
                current = current.right
        
            ## connect left children to parent
            parent.right = current.left
            ## make inorder predecessor parent
            current.right = self.root
            current.left = self.root.left if self.root.left != current else self.root.left.left
            self.root.left = None
            self.root = current
            parent.right = None
            self.left_size -= 1
            self.right_size += 1




    def find_inorder_predecessor(self):
        current = self.root.left
        while current and current.right:
            current = current.right
        return current.val

    def size(self):
        return self.left_size + self.right_size + 1


class MedianFinder(object):

    def __init__(self):
        self.bst = BST()
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.bst.add(num)

        

    def findMedian(self):
        """
        :rtype: float
        """
        size = self.bst.size()

        if size%2:
            return self.bst.root.val
        else:
            return (self.bst.root.val + self.bst.find_inorder_predecessor())/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()