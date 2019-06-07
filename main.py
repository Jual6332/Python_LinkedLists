import node
import LinkedList

def main():
    ## 1. Build Linked List
    A = LinkedList.LinkedList()
    A.addNodeAscending(10)
    #A.traverse()
    A.addNodeAscending(15)
    A.addNodeAscending(17)
    A.addNodeAscending(8)
    A.traverse()
    print("Size of Linked List is:"+str(A.getSize()))

if __name__ == "__main__":
    main()
