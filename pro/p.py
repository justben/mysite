#功能说明：给末尾无换行符的文件添加换行符、删除数据文件中的空行和注释行
#2017.05.12版
def openfile(file_name):

    import re
    file = []
    
    f = open(file_name)
    f.seek(0,0)
    f_lines = list(f)
    num = len(f_lines)

    #给未添加换行符的末尾添加换行符
    num_last = len(f_lines[num-1])
    
    last = f_lines[num-1][num_last-1]
    if last != 'n' and last != '\n':
        f_lines[num-1] = f_lines[num-1]+'\n'
    i = num-1
    
    while i >= 0:
        if f_lines[i] == '\n' or f_lines[i][0] == '#':
            f_lines.pop(i)
        i -= 1

    num = len(f_lines)

    i = 0
    while i < num:
        x = re.split(',|\n', f_lines[i])
        n = len(x) - 1
        x.pop(n)
        x.append('\n')
        file.append(x)
        num_filei = len(file[i])

        j = 1
        nnum = len(file[i]) - 1

        #while j < nnum:
            #file[i][j] = float(file[i][j])
            #print(file[i][j])
            #j += 1
            
        i += 1

    return file
def p(ff):
	file = openfile('pro/data.txt')
	f = openfile(ff)
	num = len(file)
	print(f[0])
	numf = len(f)
	i = 0
	j = 0
	out = []
	while i < numf:
		while j < num:
		    if f[i][0] == file[j][0]:#修改file[j][1]：0或1
		        out.append(file[j][0]+','+file[j][1]+','+file[j][2]+','+file[j][3]+','+file[j][4]+','+file[j][5]+','+file[j][6]+'\n')
		        j = num
		    else:
		        j += 1
		i += 1
		j = 0

	f_write = open('file/result.txt','w')
	for i in out:
		f_write.write(i)

	f_write.close()

