
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)


name = 'colt'
[char.upper() for char in name]
print(name)

friends = ['ashley','laura']
print([friend[0].upper() for friend in friends])

nums = [1 ,2 ,3]
print([str(num) + "HELLOOOOOOOO" for num in nums])

#With conditional logic within
numbers2 = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers2 if num%2 == 0 ]
odds = [num for num in numbers2 if num%2 != 0]
print([num*2 if num % 2 == 0 else num/2 for num in numbers])
print(evens)
print(odds)

with_vowels = "This is so much fun!"
print(' '.join(char for char in with_vowels if char not in "aeiou"))

#using slice [::-1]
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome("abba"))