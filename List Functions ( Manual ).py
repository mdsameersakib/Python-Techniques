# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        user = input("").split(" ")
        
        if user[0]=="insert":#━━━━━━━━━━━━━━━━━━ .insert(index,value) -- inserts item into index
            l.insert(int(user[1]),int(user[2])) 
            
        elif user[0]=="remove":#━━━━━━━━━━━━━━━━ .remove(value) -- removes first found item 
            l.remove(int(user[1]))
            
        elif user[0]=="sort":#━━━━━━━━━━━━━━━━━━ .sort() -- sorts a list
            l.sort()
            
        elif user[0]=="append":#━━━━━━━━━━━━━━━━ .append(value) -- adds a item to end of list
            l.append(int(user[1]))
            
        elif user[0]=="pop":#━━━━━━━━━━━━━━━━━━━ .pop(index) -- removes item from index
            l.pop()
            
        elif user[0]=="reverse":#━━━━━━━━━━━━━━━ .reverse() -- reverses the list
            l.reverse()
            
        elif user[0]=="print": 
                    print(l)
