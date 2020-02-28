from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Note: tail is most recent...
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif len(self.storage) == self.capacity and self.current == self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        else:
            self.current.insert_after(item)
            self.storage.length += 1 # Needed because I just used a ListNode method!
            self.current = self.current.next
            self.storage.delete(self.current.next)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # loop over head -> tail, appending to list_buffer_contents
        current = self.storage.head
        while current != None:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.current_index = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current_index] = item
        self.current_index = self.current_index + 1 if self.current_index < len(self.storage) - 1 else 0

    def get(self):
        # to_print = []
        # for item in self.storage:
        #     if item != None:
        #         to_print.append(item)

        # vvv This is faster! vvv
        to_print = self.storage
        for i in reversed(range((len(self.storage)))):
            if to_print[i] == None:
                to_print = to_print[:-1]
            else:
                break
        
        return to_print

# Advantages of the above method:
# - It's much easier to write!
# - The array is of a small size, known in advance.*
# - No more memory need be allocated than absolutely required.*

# *This sort of thing is usually a problem with arrays!

# Disadvantages:
# - The entire array is stored in memory at all times (?).
