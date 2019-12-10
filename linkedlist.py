#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item. """
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions? O(n) for best case and worst case."""
        # TODO: Loop through all nodes and count one for each
        count = 0
        node = self.head
        while node is not None: #loop through all of the nodes
            count += 1 # increase the count of the nodes by 1
            node = node.next # goes to the next node
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions? O(1) for best case and worst case because one item at a time is being appended"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        new_node = Node(item)

        if self.head is None: # if the head is none
            self.head = new_node # set the head to new node (to hold given data)
            self.tail = new_node # set the tail to new node so it can be appended
        else: # if the head is not none
            self.tail.next = new_node # set tail to new_node 
            self.tail = new_node 

        return new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions? O(1) for best and worst case because one item at a time is being prepended"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.head = new_node

        return new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions? O(1)
        TODO: Worst case running time: O(???) Why and under what conditions? O(n)"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            else:
                node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions? O(1) is the best case running time because we check if the first node is not none 
        TODO: Worst case running time: O(???) Why and under what conditions? O(n)"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        current_node = self.head  # the head is located at the current node          
        previous = None

        found = False # keep track of a found item 
      
        while current_node:
            if self.head.data == item:  # if the currents nodes data is equal to an item,
                if self.head.next is not None:  # if there is an item next after the head,
                    self.head = self.head.next # the head is now the next item
                    found = True 
                    break
                else:
                    self.head = None
                    self.tail = None
                    found = True      
                    break

            elif current_node.data == item:
                if current_node == self.tail:
                    previous.next = None
                    self.tail = previous
                    found = True
                    break
                else:
                    previous.next = current_node.next
                    found = True
                    break
                    
            else:
                previous = current_node
                current_node = current_node.next
        if not found: # message will show if it is not found
            raise ValueError('Item not found: {}'.format(item))


    def replace(self, item, new_data):
        """Running time : O(n)"""

        found = False
        current_node = self.head

        while current_node is not None: # while the current node is not empty
            if current_node.data == item: # if the current node is the old data
                current_node.data = new_data # then the current node becomes the new data
                return True
            current_node = current_node.next # then the current node will be the next one
        if not found: # else if there is no current data, then return message
            raise ValueError('Item was not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
