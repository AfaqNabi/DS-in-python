class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):  # returns the data in the node
        return self.data

    def setData(self, newData):  # Reassign data of the node
        self.data = newData

    def getNext(self):  # get the next reference of the node
        return self.next

    def getPrevious(self):  # get previous reference of the node
        return self.previous

    def setNext(self, newNext):  # reassign the current to next
        self.next = newNext

    def setPrevious(self, newPrevious):  # reassign the current to previous
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def search(self, item):  # find a given item in the list
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        # find the index of the given item
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index

    def remove(self, item):
        # find and remove the item
        # TODO:
        current = self.head
        previous = None
        found = False
        while not found and current is not None:  # traverse the list
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous == None:  # if item is at the head
                self.head = current.getNext()
            else:  #
                previous.setNext(current.getNext())  # set the next of previous to next of current
            if (current.getNext() != None):  # Check if end of list
                current.getNext().setPrevious(previous)  # the previous of the next of current is assigned to previous
            else:
                self.tail = previous  # if item at tail
            self.size -= 1  # decrement size

    def append(self, item):
        # add item to the end of the list
        temp = DLinkedListNode(item, None, None)
        if (self.head == None):
            self.head = temp
        else:
            self.tail.setNext(temp)
        temp.setPrevious(self.tail)

        self.tail = temp
        self.size += 1

    def insert(self, pos, item):
        # insert item at pos
        assert type(pos) == type(0), ' enter and integer'
        assert int(pos) >= 0, 'enter an integer greater then or equal to 0'
        assert int(pos) <= self.size, 'index out of range'
        if pos == 0:
            DLinkedList.add(self, item)
        elif pos == self.size:
            DLinkedList.append(self, item)
        else:  # traverse the list to find the position
            current = self.head
            prev = None
            index = 0
            found = False
            newNode = DLinkedListNode(item, None, None)
            while not found and current != None:
                if index == pos:
                    found = True
                else:
                    prev = current
                    current = current.getNext()
                    index += 1
            newNode.setNext(current)  # set the nex of new node to current
            newNode.setPrevious(prev)  # set the previous of new node to previous
            prev.setNext(newNode)  # set the next of previous to new node
            current.setPrevious(newNode)  # set the previous of next to new node

    def pop1(self):
        # removes and returns the last item form the list
        # no need for traversal remove from the end
        current = self.tail  # set current to the end of the list
        self.tail.setNext(None)  # set the next of new tail to None
        self.tail = current.getPrevious()  # reassign the tail to the previous of the current
        self.size -= 1  # decrement size of list
        return current.getData()

    def pop(self, pos=None):
        # removes and returns the item in the given position.
        # TODO:
        # Hint - incorporate pop1 when no pos argument is given
        assert type(pos) == type(0) or type(pos) == type(None), ' enter an integer'
        if type(pos) == type(0):
            assert int(pos) >= 0, 'enter pos int'
            assert abs(pos) <= self.getSize(), 'index not in list'
        if pos is None:
            return self.pop1()
        item = self.getItem(pos)
        self.remove(item)
        return item

        # current = self.head
        # prev = None
        # found = False
        # index = 0
        # if pos is None:
        #     return self.pop1()
        # while not found:
        #     if index == pos:
        #         found = True
        #     else:
        #         prev = current
        #         current = current.getNext()
        #         index += 1
        # if prev is None:  # this means pos is at the head so remove the self.head
        #     self.head = current.getNext()
        #     current.setPrevious(None)
        # else:
        #     prev.setNext(current.getNext())  # if in middle somewhere the next of previous is set to the next of current
        # if current.getNext() is not None:
        #     current.getNext().setPrevious(prev)  # the previous of the next of current is assigned to previous
        # elif current.getNext() is None:
        #     self.tail = prev
        # self.size -= 1

        # return current.getData()
        # assert type(pos) == type(0) or type(pos) == type(None), ' enter an integer'
        # if type(pos) == type(0):
        #     assert int(pos) >= 0, 'enter pos int'
        #     assert abs(pos) <= self.getSize(), 'index not in list'

        # current = self.head
        # index = 0
        # while index<pos:
        #     current = current.getNext()
        #     index+=1
        # self.remove(current.getData())
        # return current.getData()

    def searchLarger(self, item):
        # returns the position of the first element that is larger than item, or -1 if there is no larger item.
        assert type(item) == type(0)
        current = self.head
        prev = None
        found = False
        index = 0
        while not found and current.getNext() is not None:
            if current.getData() > item:
                found = True
            else:
                prev = current
                current = current.getNext()
                index += 1
        if not found:
            return -1
        return index

    def getSize(self):  # returns the number of items in the list
        return self.size

    def getItem(self, pos):
        # returns the item at the given position.
        # An exception should be raised if the
        # position is outside of the list.
        assert type(pos) == type(0), ' enter and integer'
        if pos>0:
            assert pos < self.size, 'index not in list'
        elif pos<0:
            assert pos>= (-self.size),'index out of range'
        current = self.head
        index = 0
        while current is not None:
            x = abs(index - self.size)
            # print(x)
            if pos < 0:
                if abs(pos) == x:
                    return current.getData()
            if index == pos:
                return current.getData()
            current = current.getNext()
            index += 1

    def peek(self):
        # returns the first element in the list
        return self.head.getData()

    def clear1(self):
        # clears all elements in the list until the list is empty
        current = self.head
        while current is not None:
            self.remove(current.getData())
            current = current.getNext()

    def add(self, item):
        # add an item to the beginning of the list
        new_node = DLinkedListNode(item, self.head, None)
        if self.head != None:  # if the list is not empty
            self.head.setPrevious(new_node)
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def add_two(self, item1, item2):
        # item2 is the new head
        node1 = DLinkedListNode(item1,None,None)
        node2 = DLinkedListNode(item2, None, None)
        if self.size == 0:
            self.head = node2
            node2.setNext(node1)
            node1.setPrevious(node2)
            self.tail = node1
        else:
            node1.setNext(self.head)
            self.head.setPrevious(node1)
            node1.setPrevious(node2)
            node2.setNext(node1)
            self.head = node2
        self.size+=2

    def multi_pop(self):
        # pop two things form the end
        assert self.size>=2,'list too small'
        current = self.tail  # set current to the end of the list
        second_last = current.getPrevious()  # get the second last elemnt
        self.tail = second_last.getPrevious()  # set the tail to the previous of second last
        self.tail.setNext(None)  # set the next of tail to None so now current and second last are delted by the garbage collector
        self.size -= 2  # decrement size of list
        return current.getData(),second_last.getData()  # return the deleted elements

    def __str__(self):  # returns a string of the elements in the doubly-linked list,
        # TODO:
        current = self.head
        x = []
        string = ''
        while current != None:
            string = string + str(current.getData()) + ' '
            x.append(str(current.getData()))
            current = current.getNext()
        x = ' '.join(x)
        return x


def test():
    linked_list = DLinkedList()

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add('World')
    linked_list.add('Hello')

    is_pass = (str(linked_list) == 'Hello World')
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = DLinkedList()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0, i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"

    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"

    for i in range(0, 199):
        x = int_list.pop()
        if x != 999 - i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test"

    int_list.insert(7, 801)

    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"

    linkedlist = DLinkedList()
    # linkedlist.add('bitch')
    # linkedlist.add_two('a','b')
    # linkedlist.add_two('c','d')
    linkedlist.add(1)
    linkedlist.add(2)
    linkedlist.add(3)
    linkedlist.add(4)
    # linkedlist.remove(5)
    # x = str(linkedlist) == 'd c b a'
    print(linkedlist.getItem(-1))
    # print(x)
    # print(str(linkedlist))
    # # linkedlist.multi_pop()
    # print(linkedlist.pop(2))
    print(str(linkedlist))



    if is_pass == True:
        print("=========== Congratulations! Your have finished exercise 2! ============")


if __name__ == '__main__':
    test()
