# Let's learn about list comprehensions! 
# You are given three integers x,y and  representing the dimensions of a cuboid along with an integer n. 
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 

# **SOLVE**
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
ans = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(ans)

# l = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k!=n:
#                 l.append([i,j,k])
# print(l) gives the same output as ans
