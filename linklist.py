

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            temp = self.head
            while temp:
                last_node = temp
                temp = temp.next
            last_node.next = Node(item)
        self.size += 1
    
    def insert(self, index, item):
        if index >= self.size:
            print("Invalid Index")
        elif index == 0:
            temp = self.head
            self.head = Node(item)
            self.head.next = temp
            self.size += 1
        
        else:
            temp = self.head 
            prev_index = 1
            while prev_index < index:
                temp = temp.next
                prev_index += 1

            temp1 = temp.next
            temp.next = Node(item)
            temp.next.next = temp1
            self.size += 1

    def remove(self, item):
        pass

    def get(self, index):
        if index >= self.size:
            print("Invalid syntex")
        else :
            i = 0
            temp = self.head
            while i < index:
                temp = temp.next
                i += 1
            return temp.data
            
        

    

    def pop(self, index):
        if index >= self.size:
            print("Invalid Index") 
        elif index == 0:
            self.head = self.head.next
            self.size -= 1

        else:
            previndex = 1
            temp = self.head
            while previndex < index:
                temp = temp.next
                previndex += 1
            
            temp.next = temp.next.next
            self.size -= 1
    
    def reverse(self):
        temp = self.head
        prev = None
        while temp:
            current = temp
            temp = temp.next
            current.next = prev
            prev = current
        self.head = current
            
            
    def length(self):
        return self.size

            
        

    def __str__(self):
        ls = []
        temp = self.head
        while temp:
            ls.append(temp.data)
            temp = temp.next

        return str(ls)
    

        

def main() -> None:
    ls = LinkedList()
    arr = [34, 34, 3, 56, 45, 3, 6, 45, 34, 45, 645, 34, 5]
    for i in arr:
        ls.append(i)
    ls.pop(0)
    ls.pop(0)
    ls.pop(0)
    ls.pop(0)
    for i in range(ls.size):
        print(ls.get(i))
    




   
    
if __name__ == '__main__':
    main()



        
        