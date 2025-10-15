numbers = {1,2,3,4}
numbers2 = {2,3,4,5}

numbers.add(6)
numbers.remove(3)
print(numbers.union(numbers2))
print(numbers.intersection(numbers2))
print(numbers.symmetric_difference(numbers2))
print(numbers.difference(numbers2))
