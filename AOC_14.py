from collections import Counter

# file = 'test14.txt'
file = 'input14.txt'
mapping = {}


with open(file) as f:
    lines = f.readlines()
    template = lines[0].strip()
    for line in lines[2:]:
        key, insert = line.strip().split(" -> ")
        data[key] = insert
        mapping[key] = (key[0] + insert, insert + key[1])

C1 = Counter()
for i in range(len(template) - 1):
    C1[template[i] + template[i + 1]] += 1


steps = 40
CF = Counter()
for s in range(steps+1):
    CF = Counter()
    for k in C1:
        CF[k[0]] += C1[k]
    CF[template[-1]] += 1
    C2 = Counter()
    for key in C1:
        if key in mapping.keys():
            key1, key2 = mapping[key]
            C2[key1] += C1[key]
            C2[key2] += C1[key]

    C1 = C2

print(max(CF.values())-min(CF.values()))
