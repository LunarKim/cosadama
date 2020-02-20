def read_file ():
	while True:
		file_name = str(input('파일이름을 입력하라'))
		try:
			f = open(file_name,'r')
		except IOError:
				print('파일을 찾지 못했습니다.')
				continue
		else:
			print('파일을 찾았습니다.')
			data = 	f.read()
			print(data)
			f.close()
			break
