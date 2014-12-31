import itertools

attribute = [('name', 'character', 20), ('height', 'integer', 50, 200), ('wight', 'integer'), ('SID', 'integer')]

inputs = (100, 'rice', 174, 65)

for attr, val in zip(attribute, inputs):
    print(attr, val)
for attr in attribute:
    if 'SID' in attr:
        primary = attr
        attribute.remove(attr)
        attribute.insert(0, primary)
        break;

global x
list1 = []
def some():
    global x
    x = 10
    list1.append(x)

some()

print("x = ", x)
print("list= ", list1)



#print(attribute)
