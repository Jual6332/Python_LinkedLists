import node
import LinkedList

def main():
    ## 1. Build Linked List
    A = LinkedList.LinkedList()
    A.addNodeAscendingt(10)
    #A.traverse()
    A.addNodeAscendingt(15)
    A.addNodeAscendingt(17)
    A.addNodeAscendingt(8)
    A.traverse()
    print("Size of Linked List is:"+str(A.getSize()))

if __name__ == "__main__":
    main()
