words = ["hello", "world"]

wordset_1 = set(words[0])
wordset_2 = set(words[1])

shared = wordset_1 & wordset_2
unique_1 = wordset_1 - wordset_2
unique_2 = wordset_2 - wordset_1

print(shared)
print(unique_1)
print(unique_2)
