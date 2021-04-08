import pprint

message = 'It was the best of times, it was the worst of times.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count)