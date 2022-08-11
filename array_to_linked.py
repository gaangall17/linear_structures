from collections import Array, SinglyLinkedList

example_array = Array(5)
example_array.setrand(1,10)

print(example_array)

example_linked = SinglyLinkedList()

for i in range(len(example_array)):
    example_linked.append(example_array[-1-i])

print(example_linked)