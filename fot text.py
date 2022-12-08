# Both can be done using list comprehension:
# 1) Max 20 characters:
wordlist = ["hi what's up home di", 'Oh wise master kakar', 'hello have a da']

new_list = [item[:20] for item in wordlist]
print(new_list)
# 2) Max 3 words:

new_list = [' '.join(item.split()[:3]) for item in wordlist if item]
# >>> new_list
print(new_list)
# ["hi what's up", 'Oh wise master', 'hello have a']