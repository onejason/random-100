import random
import matplotlib.pyplot as plt 

keys = range(1,101)
values = [0]*100

record = dict(zip(keys,values))

for x in range(10000):
   r = random.randint(1,100)
   record[r] = record[r] + 1

sorted_keys = []
sorted_values = []

for key, value in sorted(record.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
    sorted_keys.append(key)
    sorted_values.append(value)

plt.bar(range(len(record)), sorted_values)
plt.xticks(range(len(record)), sorted_keys)
plt.show() 
