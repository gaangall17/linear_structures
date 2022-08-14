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


#Class for STACK collection
#Collection would use class Node as elements
#Every time we add an element, the previous top become the next node of the new top
#first (top)
#second (top) -> first
#third (top) -> second -> first
class Stack():
    
    def __init__(self):
        self.top = None
        self.size = 0


    def is_empty(self):
        return self.size == 0
    

    def __len__(self):
        return self.size


    def __str__(self):
        text = ""
        first = True
        for element in self:
            if first:
                connector = ''
            else:
                connector = '  >  '
            text = text + connector + str(element)
            first = False
        return text


    def __iter__(self):
        probe = self.top
        while probe:
            element = probe.data
            probe = probe.next
            yield element


    def __contains__(self, item):
        found = False
        for element in self:
            if element == item:
                found = True
        return found


    def __add__(self, stack):

        new_stack = Stack()
        
        aux_list = []
        for element in self:
            aux_list.append(element)
        for i in range(len(self)):
            new_stack.push(aux_list[len(self)-1-i])
        
        aux_list = [] 
        for element in stack:
            aux_list.append(element)
        for i in range(len(stack)):
            new_stack.push(aux_list[len(stack)-1-i])

        return new_stack


    def clear(self):
        self.top = None
        self.size = 0


    def peek(self):
        if self.is_empty():
            item = None
        else:
            item = self.top.data
        return item


    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1


    def pop(self):
        item = None
        if not self.is_empty():
            item = self.top.data
            self.top = self.top.next
            self.size -= 1
        return item


#Class for STACK collection
#Collection would use class Array as elements
#Every time we add an element, the previous top become the next node of the new top
#first (top)
#second (top) -> first
#third (top) -> second -> first
class StackArray():

    def __init__(self, capacity):
        if capacity > 0:
            self.data = Array(capacity)
            self.size = 0
            self.capacity = capacity
        else:
            raise ValueError('Capacity of the stack must be higher than 0')


    def is_empty(self):
        return self.size == 0
    

    def is_full(self):
        return self.size == self.capacity


    def usage(self):
        return round(self.size/self.capacity, 2)


    def __len__(self):
        return self.size


    def __str__(self):
        text = ""
        first = True
        for element in self:
            if first:
                connector = ''
            else:
                connector = '  >  '
            text = text + connector + str(element)
            first = False
        return text


    def __iter__(self):
        top = self.size - 1
        while top >= 0:
            element = self.data[top]
            top -= 1
            yield element


    def __contains__(self, item):
        found = False
        for element in self:
            if element == item:
                found = True
        return found


    def __add__(self, stack):

        new_stack = StackArray(self.capacity + stack.capacity)
        
        aux_list = []
        for element in self:
            aux_list.append(element)
        for i in range(len(self)):
            new_stack.push(aux_list[len(self)-1-i])
        
        aux_list = [] 
        for element in stack:
            aux_list.append(element)
        for i in range(len(stack)):
            new_stack.push(aux_list[len(stack)-1-i])

        return new_stack


    def clear(self):
        self.data = Array(self.capacity)
        self.size = 0


    def peek(self):
        if self.is_empty():
            item = None
        else:
            item = self.data[self.size - 1]
        return item


    def push(self, item):
        if not self.is_full():
            self.size += 1
            self.data[self.size - 1] = item
        else:
            raise ValueError('Stack is already full')


    def pop(self):
        item = None
        if not self.is_empty():
            item = self.data[self.size - 1]
            self.data[self.size -1] = None
            self.size -= 1
        return item


#Class for QUEUE collection based on lists
#first (front) (rear)
#first (front) -> second (rear)
#first (front) -> second -> third (rear)
class ListQueue():

    def __init__(self):
        self.data = list()
        self.rear = 0
        self.front = 0
        self.size = 0
    

    def is_empty(self):
        return self.size == 0
    

    def __len__(self):
        return self.size
    

    def __str__(self):
        text = ""
        first = True
        for element in self:
            if first:
                connector = ''
            else:
                connector = '  >  '
            text = text + connector + str(element)
            first = False
        return text


    def __iter__(self):
        n = self.front
        if not self.is_empty():
            while n <= self.rear:
                element = self.data[n]
                n += 1
                yield element


    def __contains__(self, item):
        found = False
        for element in self:
            if element == item:
                found = True
        return found


    def __add__(self, queue2):
        new_queue = ListQueue()
        for element in self:
            new_queue.add(element)
        for element in queue2:
            new_queue.add(element)
        return new_queue


    def clear(self):
        self.data = list()
        self.rear = 0
        self.front = 0
        self.size = 0


    def peek(self):
        if self.is_empty():
            item = None
        else:
            item = self.data[self.front]
        return item


    def add(self, item):
        if not self.is_empty():
            self.rear += 1
        self.data.append(item)
        self.size += 1


    def pop(self):
        item = None
        if not self.is_empty():
            item = self.data[self.front]
            for i in range(self.rear):
                self.data[i] = self.data[i + 1]
            self.data.pop()
            self.rear -= 1
            self.size -= 1
        return item


#Class for QUEUE collection based on two STACKS
#first (front) (rear)
#first (front) -> second (rear)
#first (front) -> second -> third (rear)
class DoubleStackQueue():

    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def add(self, item):
        self.inbound_stack.append(item)

    def pop(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        
        return self.outbound_stack.pop()


#Class for QUEUE collection based on TwoWayNode
#first (front) (rear)
#first (front) -> second (rear)
#first (front) -> second -> third (rear)
class NodeQueue():

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def add(self, item):
        new_node = TwoWayNode(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1


    def pop(self):
        probe = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return probe.data


