class SinglyNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNextNode(self):
        return self.next
    def setData(self,val):
        self.data = val
    def setNextNode(self,nextNode):
        self.next = nextNode
