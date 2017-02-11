import os
from zipfile import ZipFile as rar
def priecinky(c):
	pole = c
	res = []
	for i in range(len(pole)):
		if '.zip' not in pole[i]:
			if '.txt' not in pole[i]:
				if '.py' not in pole[i]:
					res.append(pole[i])
	return res
r = os.listdir(os.getcwd())
done  = priecinky(r)
for i in range(len(r)):
	pom = ''
	if '.zip' in r[i]:
		pom = r[i].replace('.zip','') 
		with rar(os.getcwd()+'\\' +r[i], 'r') as f:
			f.extractall(os.getcwd()+'\\' +r[i].replace('.zip', ''))
			done.append(pom)
for i in range(len(done)):
	with open(os.getcwd()+'\data.txt', 'a') as f:
		print('{}.) {}'.format(i,done[i]), file = f)

print('>>>I am DONE<<<')
