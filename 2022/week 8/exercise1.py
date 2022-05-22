# Affan Fareed
# CIS-2532-NET02
# Week 8 Homework - Implementing a Stack using Singly Linked List
# Due 10/17/21 @ 11:59:00PM




class Node:
    def __init__(self,data):
        self.data = data
        self.next = None




#   peek() and pop() methods
class Stack:
     

    def __init__(self):
        self.head = None
     
    # Check if the stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False


    def push(self,data):

        if self.head == None:
            self.head=Node(data)
             
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
     
    def pop(self):

        # check
        # NOTE RECURSIVE TEST , NOT SURE WHAT IT EXACTLY DOES
        # if self.isempty():
        #     return None
        # else:
        #     current = self.head
        #     self.head = current.next
        #     print( current.data)
        #     self.pop()
        #     self.head = current
        #     print(self.head.data , current.data)


        if self.isempty():
            return None
        else:
            current = self.head
            self.head = current.next
            current.next = None
            return current.data

        # else remove the head node, and make the preceeding on the new head node
        # set the popped node equal to the current head
        # set the current head equal to the next node (making the second node, now the head))
        # set the reference to the next node of the popped node, equal to none (removing it from the list)
        # return the data of the popped node
        
     
    def peek(self):
        return self.head.data







    def display(self):
         
        current_node = self.head
        if self.isempty():
            print("Stack is empty, nothing to print out")
         
        else:
            output_string = ""
            while(current_node != None): 
                output_string += f'{current_node.data} --> '
                current_node = current_node.next
            output_string += str( current_node )
            print(output_string)
            return output_string


# main creates a stack, and then tests all of the class methods
def main():

    # create a stack and push 5 elements to it
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    # show the stack elements
    print('\nThe Stack after pushing the 5 elements')
    stack.display()
    print("\n")

    # pop 3 elements off of that stack
    popped_1 = stack.pop()
    popped_2 = stack.pop()
    popped_3 = stack.pop()
    popped_nums = [popped_1, popped_2, popped_3]

    if popped_nums != [5,4,3]:
        print("Your pop method is not correct. 5, 4, 3 are the expected values")
        return

    # print the 3 popped elements
    print('The three popped elements are:  {0} {1} {2}\n'.format(popped_1, popped_2, popped_3))

    # print list after the popping
    print('The linked list after popping 3 elements')
    stack.display()
    print("\n")
    
    # return the current top element
    currentTop = stack.peek()

    if currentTop != 2:
        print("Your peek method is not correct, it needs to return the data of the current top element. Expecting 2")
        return
    
    print('The current top stack element is {0}\n'.format(currentTop))

    print("You have completed the assignment successfully\n")


if __name__ == "__main__":
    main()