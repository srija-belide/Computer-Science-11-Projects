#Digits and sums
#By Srija Belide
#map function is used  to convert each number into int from the input
# it is useful as it returns an iterator where each item is the result of applying int
#input.split() allows the large string to be broken into substrings by space
x, y = map(int, input().split())
#now integer values are assigned to x and y
#this for loop helps to get all the possible numbers within the range
for i in range(x,y+1):
    #i is converted to str so that indexing can be done
    i_str = str(i)
    #decision statements are used to see if the i is equal to the sum of the cubes of the digits
    if i == int(i_str[0])**3 + int(i_str[1])**3 + int(i_str[2])**3:
        print(i)
        
      