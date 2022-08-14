import random

### Class to represent an array
class Array:

    ## Constructor declaring capacity and fill value
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
        self.n = 0
        self.max = capacity - 1
    
    ## Return the size of the array. It is used by len() function
    def __len__(self):
        return len(self.items)
    
    ## Return items as string. It is used by print() function
    def __str__(self):
        return str(self.items)

    ## Methods for iterator
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            item = self.items[self.n]
            self.n += 1
            return item
        else:
            raise StopIteration

    ## Return an specific item by its index. It is used by [] comand
    def __getitem__(self, index):
        return self.items[index]
    
    ## Set a new value on an specific index. It is used by [] comand
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    ## Fill with random numbers
    def setrand(self, low, high):
        for i in range(len(self)):
            self.items[i] = random.randrange(low, high)
    
    ## Fill with sequence
    def setseq(self, first_value, step):
        for i in range(len(self)):
            self.items[i] = first_value + i*step
    
    ## Return total sum of numeric items
    def sum(self):
        sum = 0
        for item in self:
            try:
                sum += item
            except TypeError:
                pass
        return sum


### Class to represent an array of 2 dimensions
class Grid():

    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
    
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])

    def shape(self):
        return (self.get_height(), self.get_width())
    
    def getrow(self, index):
        return self.data[index]

    ## Return items as string  
    def __str__(self):
        result = ''
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col])
                result += ' '        
            result += "\n"
        
        return result

    ## Fill grid with random numbers
    def setrand(self, low, high):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] = random.randrange(low, high)


### Class to represent an array of 3 dimensions
class Cube():

    def __init__(self, rows, columns, layers, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
            for column in range(columns):
                self.data[row][column] = Array(layers, fill_value)
    
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])

    def get_deep(self):
        return len(self.data[0][0])

    def shape(self):
        return (self.get_height(), self.get_width(), self.get_deep())
    
    def getrow(self, index):
        return self.data[index]

    ## Return items as string  
    def __str__(self):
        result = ''
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += '[ '
                for layer in range(self.get_deep()):
                    result += str(self.data[row][col][layer])
                    result += ' '
                result += '] '
            result += "\n"  
        return result

    ## Fill cube with random numbers
    def setrand(self, low, high):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for layer in range(self.get_deep()):
                    self.data[row][col][layer] = random.randrange(low, high)


##Class to represent a node
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


##Class for singly linked list
class SinglyLinkedList():
    def __init__(self):

        #tail is the parameter where we add the first node
        #as we are going to assign nodes to the list, it will always show a 'data' and a 'next'
        #next value would iterate in order as they were added, always starting in tail
        #first_value
        #second_value <- fisrt_value
        #third_value <- second_value <- first_value
        
        self.tail = None
        self.head = None
        self.size = 0
    
    def append(self, data):
        node = Node(data)

        #If list is empty -> node is assigned to tail
        if self.tail == None:
            self.tail = node

        #If list is not empty
        else:
            current = self.tail

            #We iterate until we reach final node
            while current.next:
                current = current.next
            
            #We assign new value next to last node
            current.next = node
        
        self.head = node
        self.size += 1
    
    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val
        
    def delete(self, data):
        current = self.tail
        previous = self.tail

        #Iterating in the list
        while current:

            #if any node equals value to delete
            if current.data == data:

                #If it is the first node, we assign its next node (second) as tail (first)
                if current == self.tail:
                    self.tail = current.next
                
                #If it is not the first node, we assign its next node as next node of the previous node
                else:
                    previous.next = current.next
                    if current == self.head:
                        self.head = previous
            
            previous = current
            current = current.next
    
    def search(self, data):
        found = False
        for node in self.iter():
            if data == node:
                found = True
        return found
    
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

    def __str__(self):
        text = ""
        first = True
        for data in self.iter():
            if not(first):
                connector = ' <- '
            else:
                connector = ''
            text = str(data) + connector + text
            first = False
        return text  

    #Method to get data from an specific position
    def __getitem__(self, index):
        
        if index >= self.size or index < 0:
            raise IndexError
        
        probe = self.tail
        probe_position = self.size - 1

        while probe:
            if probe_position == index:
                return probe.data
            probe = probe.next
            probe_position -= 1
    
    #Method to insert data in an specific position
    def __setitem__(self, index, new_item):
        
        if index >= self.size or index < 0:
            raise IndexError
        
        probe = self.tail
        probe_position = self.size - 1

        while probe:
            if probe_position == index:
                probe.data = new_item
            probe = probe.next
            probe_position -= 1

    #Method to insert new node in a specific position
    def insert_node(self, index, data):
        
        if index > self.size or index < 0:
            raise IndexError
        
        if index == 0:
            self.append(data)
        elif index == self.size:
            new_node = Node(data, self.tail)
            self.tail = new_node
            self.size += 1
        else:
            new_node = Node(data)
            probe = self.tail
            probe_position = self.size - 1
            while probe:
                if probe_position == index:
                    new_node.next = probe.next
                    probe.next = new_node
                probe = probe.next
                probe_position -= 1
            self.size += 1

    #Method to insert in last position
    def insert_last(self, data):
        self.insert_node(self.size, data)

    #Method to delete a node in a specific position
    def delete_node(self, index):
        
        if index >= self.size or index < 0:
            raise IndexError
        
        if index == self.size - 1:
            self.tail = self.tail.next
            self.size -= 1
        else:
            previous_probe = self.tail
            probe = self.tail
            probe_position = self.size - 1
            while probe:
                if probe_position == index:
                    previous_probe.next = probe.next
                    if probe_position == 0:
                        self.head = previous_probe
                previous_probe = probe
                probe = probe.next
                probe_position -= 1
            self.size -= 1


##Class for circular linked list
class CircularLinkedList():

    def __init__(self):

        #tail is the parameter where we add the first node
        #as we are going to assign nodes to the list, it will always show a 'data' and a 'next'
        #next value would iterate in order as they were added, always starting in tail
        #head value (last value) would reference the first
        # ... first_value (head)(tail) <- first_value (head)(tail)
        # ... first_value (tail) <- second_value (head) <- fisrt_value (tail)
        # ... first_value (tail) <- third_value (head) <- second_value <- first_value (tail)
        
        self.tail = None
        self.head = None
        self.size = 0
    

    def append(self, data):
        node = Node(data)

        #If list is empty -> node is assigned to tail
        if self.tail == None:
            self.tail = node

        #If list is not empty
        else:
            current = self.tail

            #We iterate until we reach final node
            while current.next:
                if self.head == current:
                    break
                current = current.next
            
            #We assign new value next to last node
            current.next = node
        
        self.head = node
        self.head.next = self.tail
        self.size += 1
    

    def iter(self):
        current = self.tail

        while current:
            val = current.data
            yield val
            if self.head == current:
                break
            current = current.next


    def __str__(self):
        text = ""
        for data in self.iter():
            connector = ' <- '
            text = connector + str(data) + text
        text = "... " + str(self.tail.data) + text
        return text


#Child class of Node with a previous atribute
class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
    

#Class for a Double linked list
#This list would be created from head to tail, but it could be iterated
#from head to tail or from tail to head
#first (head)(tail)
#first (head) <-> second (tail)
#first (head) <-> second <-> third (tail)
class DoubleLinkedList():

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0
    

    def append(self, data):
        node = TwoWayNode(data)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.previous = current
        
        self.tail = node
        self.size += 1
    

    def size(self):
        return str(self.size)
    

    def iter_forward(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val


    def iter_reverse(self):
        current = self.tail

        while current:
            val = current.data
            current = current.previous
            yield val
    

    def __str__(self):
        text = ""
        first = True
        for data in self.iter_forward():
            if not(first):
                connector = ' <-> '
            else:
                connector = ''
            text = text + connector + str(data)
            first = False
        text += "  :  "
        text_reverse = ""
        first = True
        for data in self.iter_reverse():
            if not(first):
                connector = ' <-> '
            else:
                connector = ''
            text_reverse =  str(data) + connector + text_reverse
            first = False
        text += text_reverse
        return text
    

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
    

    def __getitem__(self, index):
        
        if index >= self.size or index < 0:
            raise IndexError
        
        probe = self.head
        probe_position = 0

        while probe:
            if probe_position == index:
                return probe.data
            probe = probe.next
            probe_position += 1
    

    def __setitem__(self, index, new_item):
        
        if index >= self.size or index < 0:
            raise IndexError
        
        probe = self.head
        probe_position = 0

        while probe:
            if probe_position == index:
                probe.data = new_item
            probe = probe.next
            probe_position += 1
    

    def insert_node(self, index, data):
        
        if index > self.size or index < 0:
            raise IndexError
        
        if index == self.size:
            self.append(data)
        else:
            new_node = TwoWayNode(data)
            probe = self.head
            probe_position = 0
            while probe:
                if probe_position == index:
                    new_node.next = probe
                    new_node.previous = probe.previous
                    if probe.previous:
                        probe.previous.next = new_node
                    if index == 0:
                        self.head = new_node
                    probe.previous = new_node
                probe = probe.next
                probe_position += 1
            self.size += 1


    def delete_node(self, index):
        
        if index >= self.size or index < 0:
            raise IndexError
        
        previous_probe = self.head.previous
        probe = self.head
        next_probe = self.head.next
        probe_position = 0

        while probe:
            if probe_position == index:
                if previous_probe:
                    previous_probe.next = probe.next
                if next_probe:
                    next_probe.previous = probe.previous
                if index == 0:
                    self.head = probe.next
                if index == self.size -1:
                    self.tail = probe.previous
            previous_probe = probe
            probe = probe.next
            if probe:
                next_probe = probe.next
            probe_position += 1
        self.size -= 1
            