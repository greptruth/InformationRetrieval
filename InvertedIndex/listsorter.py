import json

fout = open('output1.txt','w+');
with open('output.txt', 'r') as myfile:
    data=myfile.read().split('\n')
for i in range(len(data)):
	data[i] = data[i].split('  \t  ');
data = sorted(data, key=lambda tup: (tup[0],tup[1]))

dict = {}
dict[data[0][0]]=[data[0][1]]
for k in range(1,len(data)):
	if data[k][0] == data[k-1][0]:
		dict[data[k][0]].append(data[k][1])
	else:
		dict[data[k][0]] = [data[k][1]]

with open('dump.json','w') as  outfile:
	json.dump(dict, outfile)

