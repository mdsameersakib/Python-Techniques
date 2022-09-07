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
        if user[0]=="insert":
            l.insert(int(user[1]),int(user[2]))   
        elif user[0]=="remove":
            l.remove(int(user[1]))
        elif user[0]=="sort":
            l.sort()
        elif user[0]=="append":
            l.append(int(user[1]))            
        elif user[0]=="pop":
            l.pop()
        elif user[0]=="print":
            print(l)
        elif user[0]=="reverse":
            l.reverse()
