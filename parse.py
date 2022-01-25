fil = open('result', 'r')
numb = []
for l in fil:
	t = l.split(' ')
	numb.append(t)
min_ = min(numb)
print(min_)
