#while loop and for loop

#while loop
# x=1
# while x <6:
#     print(x)
#     x =x+1

# #for loop

# for i in range(6,13):
#     print(i)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'fri', 'sat', 'sun']

for i in days:
    if i.capitalize() =='Tue':
        continue
    if i.capitalize() =='Fri':
        break 
    print(i.capitalize())