# Found This amazing thing...
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
# Output
(1, 'sugar')
(2, 'spice')
(3, 'everything nice')

# Another example 
x = [1,2,3,4,5]
y = [6,7,8,9,0]
print(list(zip(x,y)))

# gives output 
[(1, 6), (2, 7), (3, 8), (4, 9), (5, 0)]

# We can also do this
z = [x] + [y]
for i in zip(*z):
  print(i)
  
# Output:
(1, 6)
(2, 7)
(3, 8)
(4, 9)
(5, 0)
