numbers = [1,10,5,16,4,9,10,49]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:]
val = numbers[:3]

numbers[4] = 40

# numbers.append(49)
numbers.append(59)

# numbers.insert(3, 79)
numbers.insert(-1,52) 

# numbers.pop()
numbers.pop(0)

# numbers.remove(49)

numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()

print(numbers)
print(letters)

print(len(letters))
print(len(numbers))

print(numbers.count(10))
print(letters.count('a'))

# numbers.clear()

letters.reverse()
numbers.extend(letters)
print(numbers)
