class HistoryItem:
    def __init__(self, page, index):
        self.page = page
        self.index = index
        self.prev = None
        self.next = None

class BrowserHistory(object):

    def __init__(self, homepage):
        self.history = HistoryItem(homepage, 0)
        self.count = 1
        """
        :type homepage: str
        """
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """

        new_page = HistoryItem(url, self.count)
        self.history.next = new_page
        new_page.prev = self.history
        self.history = new_page

        self.count = self.history.index + 1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        steps = min(self.history.index, steps)

        while self.history.prev and steps > 0:
            self.history = self.history.prev
            steps-=1

        return self.history.page
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        steps = min(self.count - self.history.index - 1, steps)

        while self.history.next and steps > 0:
            self.history = self.history.next
            steps-=1

        return self.history.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)