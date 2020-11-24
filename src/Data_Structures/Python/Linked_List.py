class Link(object):

    def __init__(self,data=None):
        self._data = data
        self._link = None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data=None):
        self._data = data
    
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, next=None):
        if next == None:
            return False
        else:
            self._link = next
    
    def __str__(self):
        link_data = list()
        node = self
        while node != None:
            link_data.append(node.data)
            node = node.link
        return str(link_data)

class Linear_Linked_List(Link):

    def __init__(self, data=None):
        super().__init__(data)
    
def insert_front(head, data=None):
    if head.data == None and head.link == None:
        head.data = data
        return True, head
    else:
        new_node = Linear_Linked_List(data)
        new_node.link = head
        return True, new_node
        
def insert_rear(head, data=None):
    if head.data == None and head.link == None:
        head.data = data
        return True, head
    else:
        new_node = Linear_Linked_List(data)
        node = head
        while node.link != None:
            node = node.link
        node.link = new_node
        return True, head

def delete_front(head):        
    if head == None:
        return False, None, "Underflow"
    else:
        return True, head.link, head.data

def delete_rear(head):
    if head == None:
        return False, None, "Underflow"
    if head.link == None:
        return True, None, head.data
    else:
        second_last = head
        while second_last.link.link != None:
            second_last = second_last.link
        data = second_last.link.data
        second_last.link = None
        return True, head, data

def delete_specific(head, data=None):
    current = head.next
    prev = head.next
    while current:
        if current.data == data:
            if current == head.tail:
                head.tail = current.next
            else:
                prev.next = current.next
            self.count -= 1
            return
        prev = current
        current = current.next

def search_node(head, data=None):
    if data == None:
        return False, "Invalid Argument"
    if head == None:
        return True , [None]
    else:
        node = head
        pos = list()
        i = 0
        while node.link != None:
            if node.data == data:
                pos.append(i)
            node = node.link
            i += 1
        if len(pos)==0:
            return True, [None]
        else:
            return True, pos

def main():
    li = Linear_Linked_List()
    print(str(li))
    li = insert_front(li, 5)[1]
    print(str(li))
    li = insert_rear(li, 4)[1]
    print(str(li))
    li = insert_front(li, 3)[1]
    print(str(li))
    li = insert_rear(li, 2)[1]
    print(str(li))
    li = insert_front(li, 1)[1]
    print(str(li))
    li = insert_rear(li, 0)[1]
    print(str(li))
    print(search_node(li, 2))
    li = delete_front(li)[1]
    print(str(li))
    li = delete_rear(li)[1]
    print(str(li))
    li = delete_front(li)[1]
    print(str(li))
    li = delete_rear(li)[1]
    print(str(li))
    li = delete_front(li)[1]
    print(str(li))
    li = delete_rear(li)[1]
    print(str(li))

main()