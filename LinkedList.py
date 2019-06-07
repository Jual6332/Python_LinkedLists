import node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size=0
    def addNodeAscending(self,data):
        # 1. Create new Node
        newNode = node.SinglyNode(data)
        # 2. Add Node to the head
        if self.head is None or data < self.head.getData():
            newNode.setNextNode(self.head)
            self.head = newNode
            return
        # 3. Traverse the list to the end
        prev, curr = self.head, self.head.getNextNode()
        while curr is not None and curr.getData()<data:
            prev = curr
            curr = curr.getNextNode()
        # 4. Change the next of last Node to new node
        prev.setNextNode(newNode)
        newNode.setNextNode(curr)
        self.size+=1
    def getSize(self):
        return self.size
    def traverse(self):
        string="Head="
        curr = self.head
        # Loop through LL
        while curr:
            string+=str(curr.getData())+">>"
            curr = curr.getNextNode()
        string+="end"
        print(string)

    '''
    def deleteNode(self,node):
        temp = head
        # Case 1: Node to be deleted is at the head of LL
        if (temp is not None):
            head = head.next
            temp = None
            return
        # Case 2: Node is in the middle or end of the LL
        while next != None:
            if node.val == temp.val:
                break;
            prev = temp
            temp = temp.next
        # Case 3: Node was not found in LL
        if (temp == None):
            return
        prev.next = temp.next
        temp = None
    '''
