import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
name = random.randint(0,len(friends) - 1)
print(friends[name])

# choice method
print(random.choice(friends))