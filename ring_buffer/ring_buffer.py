from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Note: tail is most recent...
        pass

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
        pass

    def append(self, item):
        pass

    def get(self):
        pass
