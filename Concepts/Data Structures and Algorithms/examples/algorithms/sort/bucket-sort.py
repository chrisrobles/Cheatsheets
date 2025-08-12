# Bucket Sort
values = [0,1,1,0,0,1,1]

# Create buckets
counts = [0,0]

# Fill buckets
for value in values:
    counts[value] += 1
    
# Sort buckets
i = 0
for type_val in range(len(counts)):
    count_of_type = counts[type_val]
    for _ in range(count_of_type):
        values[i] = type_val
        i += 1

print(values)