class SLinkedListNode:
    # an instance of this class is a node in a Single Linked List
    # a node has a reference to data and reference to next
    def __init__(self,initData,initNext):
        self.data = initData
        self.next = initNext
        
    def getNext(self):  # returns the next of node
        return self.next
    
    def getData(self):  # returns the data in the node
        return self.data
    
    def setData(self,newData):  # changes the data in the node
        self.data = newData
        
    def setNext(self,newNext):  # reassign the current to next
        self.next = newNext


class SLinkedList:
    # an instance of this class is a Singly-Linked List object
    # it has reference to the first node in the list
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self,item):
        # adds an item at the end of the list
        new_node = SLinkedListNode(item,None)
        current = self.head  # Start the traversal
        if self.size == 0:  # check if list is empty
            self.add(item)
        else:
            while (current.getNext()!=None):
                current= current.getNext() # traversing the list
            current.setNext(new_node)
            self.size = self.size +1

    def insert(self,pos,item):
        # inserts the item at pos
        # pos should be a positive number (or zero) of type int
        # TO DO: write assert statement that tests if pos is int
        # TO DO: write assert statement that tests that pos is not negative
        assert type(pos)==type(0),' enter and integer'
        assert int(pos)>=0,'enter an integer greater then or equal to 0'
        node = SLinkedListNode(item,pos)
        if pos==0:
            SLinkedList.add(self,item)
        elif pos == self.size:
            SLinkedList.append(self,item)
        else:
            current = self.head
            previous = None
            found = False
            position = 0
            while not found and current!=None and (position < pos):
                previous = current
                current = current.getNext()
                position+=1
                if position==pos:
                    found = True
            new_item  = node
            previous.setNext(new_item)
            node.setNext(current)
            self.size+=1

    def remove(self,item):
        # remove the node containing the item from the list
        if self.size == 0:
            raise Exception('List is Empty')
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            raise Exception('Item not in list')
        else:
            if previous == None: # the item is in the first node of the list
                self.head = current.getNext()
            else: # item is not in the first node
                previous.setNext(current.getNext())
            self.size = self.size -1
            
    def index(self,item):
        # finds the location of the item in the list
        if self.size == 0:
            raise Exception('List is empty')
        position = 0
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                position = position + 1
        if found:
            return position
        else:
            return 'Item not found'
        
    def pop(self):
        # removes the node from the end of the list and returns the item 
        if self.size == 0:
            raise Exception('List is empty')
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size = self.size - 1
        return current.getData()
    
    def __str__(self):
        # returns a string representation of the list
        current = self.head
        string = ''
        while current != None:
            string = string + str(current.getData())+'->'
            current = current.getNext()
        return string
    
    def getSize(self):
        return self.size

    def add(self,item):
        # adds an item at the start of the list
        new_node = SLinkedListNode(item,None)
        new_node.setNext(self.head)
        self.head = new_node
        self.size = self.size + 1

    def add_2(self,item1,item2):
        # item is the new head
        node1 = SLinkedListNode(item1,None)
        node2 =SLinkedListNode(item2,None)
        node1.setNext(self.head)
        node2.setNext(node1)
        self.head = node2
        self.size+=2

    def pop_2(self):
        # pop two elements from the end
        if self.size==0 or self.size==1:
            raise Exception('list is empty')
        if self.size == 2:
            self.tail = None
            self.head = None
            return self.tail,self.head
        current = self.head
        prev = None
        index = 0
        found = False
        while not found and current is not None:
            if index == (self.size-2):
                found = True
            else:
                prev = current
                current = current.getNext()
                index += 1
        prev.setNext(None)
        self.tail = prev
        self.size -= 2
        return current.getData(),current.getNext().getData()

    def search(self,item):
        current = self.head
        found = False
        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def isEmpty(self):
        return self.size==0

    def length(self):
        return self.size

    def pop1(self,pos=None):
        assert type(pos) == type(0) or type(pos) == type(None), ' enter an integer'
        assert int(pos) <= self.size, 'index not in list bud'
        index = 0
        current = self.head
        prev = None
        found = False
        while current is not None and not found:
            if index == pos:
                found = True
            else:
                prev = current
                current = current.getNext()
                index += 1
        if self.size == 0: # if at head
            self.head = None
        elif pos == None:  # check at the end
            current = self.pop()
            return current
        elif pos == 0:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
        return current.getData()

    def multi_pop_from_start(self, number):
        assert type(number) == type(0)
        assert number<=self.size
        current = self.head
        i=0
        while i < number:
            current = current.getNext()
            i += 1
        self.head = current

    def multiPop(self,number):
        assert type(number) == type(0)
        assert number <= self.size , 'to many elements to pop'
        assert self.size >= number, 'not enough elements in list'
        result = []
        current = self.head
        prev = current
        i = 0
        found = False
        while current is not None and not found:
            if i == (self.size-number):
                found = True
            else:
                prev = current
                current = current.getNext()
                i+=1
                # result.append(current.getNext().getData())

        if number == self.size:
            self.head = None
        else:
            prev.setNext(None)
        self.size -= number
        return result


def main():
    # Testing Singly-Linked List
    # slist = SLinkedList()
    # slist.add(2)
    # slist.add(4)
    # slist.add('A')
    # slist.append(77)
    # slist.append(6)
    # slist.append('Z')
    # # slist.add_2('bitch','nigga')
    # print('Original List:', slist.getSize(), 'elements')
    # print(slist)
    # print()
    # slist.insert(0,'start')
    # print('After inserting the word start at position 0:', slist.getSize(), 'elements')
    # print(slist)
    # print()
    # slist.insert(7,'end')
    # print('After inserting the word end at position 7:', slist.getSize(), 'elements')
    # print(slist)
    # print()
    # slist.insert(4,'middle')
    # # slist.insert(2,'bitch')
    # print('After inserting middle at position 4:', slist.getSize(), 'elements')
    # print(slist)
    # slist.pop_2()
    # print(slist)
    # x = SLinkedList()
    # x.add(1)
    # x.add_2(2,3)
    # print(x)
    # print(x.pop_2())
    # print(x)
    # print(x.search(3))
    y = SLinkedList()
    for i in range(5):
        for j in range(5):
            # print(i,j)
            y.add_2(i,j)
    # y.add_2(1,2)
    # y.add_2(3,4)
    # y.add_2(5,6)
    print(y)
    # print(y.pop1(0))
    # y.multi_pop_from_start(6)
    print(y.pop())
    # print(y.pop())
    print(y)


    
if __name__=="__main__":
    main()
