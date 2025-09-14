name = 'Sadık'
surname = 'Turan'
age = 36

greeting = 'My name is '+ name +' '+ surname +' and \nI am '+ str(age) +' years old'
# \n ifadesi alt satıra geçme ifadesi

length = len(greeting) # len komutu kelimenin kaç harfli olduğunu söyler(0) dahil
 
# print(greeting)
# print(greeting[0])
# print(greeting[3])
# print(greeting[length-1])
# print(greeting[-1])

# print(greeting[3:])
# print(greeting[:16])

print(greeting[2:40:2])
print(greeting[2:40:3])

