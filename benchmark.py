from timeit import default_timer as timer
import os
import pickle
from dicttoxml import dicttoxml
import xmltodict
import json
import msgpack
import yaml
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

serialize_times = []
deserialize_times = []
sizes = []
data = [{"name": "John", "age": 30, "city": "New York"},
{"name": "Bob", "age": 20, "city": "Boston"},
{"name": "Linda", "age": 40, "city": "Los Angeles"}]

# Picle benchmark
start = timer()
pdata = pickle.dump(data, open("data.p", "wb"))
end = timer()
serialize_times.append(end - start)

start = timer()
pdata = pickle.load(open("data.p", "rb"))
end = timer()
deserialize_times.append(end - start)

sizes.append(os.stat('data.p').st_size)

# XML benchmark
start = timer()
xml = dicttoxml(data)
f = open("data.xml","w")
f.write(xml.decode())
f.close()
end = timer()
serialize_times.append(end - start)

start = timer()
with open('data.xml', 'r') as f:
    xmldata = xmltodict.parse(f.read(), dict_constructor=dict)
end = timer()
deserialize_times.append(end - start)

sizes.append(os.stat('data.xml').st_size)

# JSON benchmark
start = timer()
with open('data.json', 'w') as f:
    json.dump(data, f, sort_keys=True)
end = timer()
serialize_times.append(end - start)

start = timer()
with open('data.json', 'r') as f:
    jsondata = json.load(f)
end = timer()
deserialize_times.append(end - start)

sizes.append(os.stat('data.json').st_size)

# MessagePack benchmark
start = timer()
with open('data.msgpack', 'wb') as f:
    msgpack.pack(data, f)
end = timer()
serialize_times.append(end - start)

start = timer()
with open('data.msgpack', 'rb') as f:
    msgdata = msgpack.unpack(f)
end = timer()
deserialize_times.append(end - start)

sizes.append(os.stat('data.msgpack').st_size)

# YAML benchmark
start = timer()
with open('data.yaml', 'w') as f:
    yaml.dump(data, f)
end = timer()
serialize_times.append(end - start)

start = timer()
with open('data.yaml') as f:
    ymldata = yaml.safe_load(f)
end = timer()
deserialize_times.append(end - start)

sizes.append(os.stat('data.yaml').st_size)

# Make serialization speed graph
labels = ['Pickle', 'XML', 'JSON', 'MessagePack', 'YAML']

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, serialize_times, width, label='Serialize')
rects2 = ax.bar(x + width/2, deserialize_times, width, label='De-serialize')

ax.set_ylabel('Time (s)')
ax.set_title('Speed')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()

# Make file size graph
labels = ['Pickle', 'XML', 'JSON', 'MessagePack', 'YAML']

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x, sizes, width, label='Size')

ax.set_ylabel('Size (bytes)')
ax.set_title('Speed')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend().set_visible(False)

fig.tight_layout()

plt.show()