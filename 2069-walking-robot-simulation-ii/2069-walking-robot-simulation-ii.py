class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.pos = 0
        self.pos_dirs = []
        self.moved = False

        ## possible positions
        for i in range(width):
            if i == 0:
                self.pos_dirs.append((i, 0, "South"))
            else:
                self.pos_dirs.append((i, 0, "East"))
        for i in range(1, height):
            self.pos_dirs.append((width-1, i, "North"))
        for i in range(width-2, -1, -1):
            self.pos_dirs.append((i, height-1, "West"))
        for i in range(height-2, 0, -1):
            self.pos_dirs.append((0, i, "South"))

        print(len(self.pos_dirs))

        


    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.moved = True
        self.pos = (self.pos + num)%len(self.pos_dirs)        

    def getPos(self):
        """
        :rtype: List[int]
        """

        x,y,_  = self.pos_dirs[self.pos]

        return x,y
        

    def getDir(self):
        """
        :rtype: str
        """
        if not self.moved: return "East"
        return self.pos_dirs[self.pos][-1]

        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()