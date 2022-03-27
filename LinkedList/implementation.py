class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val
    
    def set_data(self, val):
        self.val = val
        
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0 # number of Nodes in list
    
    def get_count(self):
        return self.count
    
    def insert(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
    
    def find(self, val):
        item = self.head
        while(item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()
    
    def deleteAt(self, idx):
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
        
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(318)
itemlist.insert(9)
itemlist.dump_list()

itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
print("Finding item: ", itemlist.find(4))
itemlist.dump_list()
