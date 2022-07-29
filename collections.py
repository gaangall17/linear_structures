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
    