#!/bin/python3
from typing import Counter


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next != None and current_node.next.data != data:
            current_node = current_node.next
        # If we have found our data, make the previousious pointer skip it
        if current_node.next != None:
            current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node != None:
            # end = just previousents a \n new line character for each print
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("End")

    def length(self):
        numOfNodes = 0
        current_node = self.head
        while current_node != None:
            numOfNodes += 1
            current_node = current_node.next
        return numOfNodes

    def reverse(self):
        
        previous = None
        current = self.head
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
            
        current_node = previous
        while current_node != None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("End")
        self.head = previous

    def print_nth_element(self, n):
        
        current = self.head
        count = 1
        while current != None:
            if count == n:
                print(current.data)
                return
            count += 1
            current = current.next
        print("Index out of range")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append("A")
    ll.append("B")
    ll.append("C")
    ll.append("D")
    ll.append("E")
    ll.append("F")
    ll.append("G")
    ll.append("H")
    ll.append("I")
    ll.append("J")
    ll.append("K")

    print("Original List:")
    ll.print_list()

    print("Length of List:", ll.length())

    ll.reverse()
    ll.print_list()
    ll.print_nth_element(2)
    ll.print_nth_element(6)