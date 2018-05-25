
def Judge_key(dictA,key):
	try:
		if key in list(dictA.keys()):
			return True
		else:
			return False
	except:
		return False
def Judge_keys(dictA,keys):
	if len(keys)==1:
		Key_bool = Judge_key(dictA,keys[0])
	else:
		dict_tmp = dictA
		for index in range(len(keys)):
			Key_bool = Judge_key(dict_tmp,keys[index])
			if Key_bool:
				dict_tmp = dict_tmp[keys[index]]
			else:
				break
	return Key_bool

def merge_dicts(*dict_args):
	result={}
	for dictionary in dict_args:
		result.update(dictionary)
	return result
def addtodict(dictA, key, val):
    dictA.update({key: val})
def addtodict2(dictA, keyA, keyB, val):
    if keyA in dictA.keys():
        addtodict(dictA[keyA], keyB, val)
    else:
        dictA.update({keyA: {keyB: val}})
def addtodict3(dictA, keyA, keyB, keyC, val):
    if keyA in dictA.keys():
        addtodict2(dictA[keyA], keyB, keyC, val)
    else:
        dictA.update({keyA: {keyB: {keyC: val}}})


def addtodict4(dictA, keyA, keyB, keyC, keyD, val):
    if keyA in dictA.keys():
        addtodict3(dictA[keyA], keyB, keyC, keyD, val)
    else:
        dictA.update({keyA: {keyB: {keyC: {keyD: val}}}})

def addtodict5(dictA, keyA, keyB, keyC, keyD, keyE,val):
    if keyA in dictA.keys():
        addtodict4(dictA[keyA],keyB, keyC, keyD, keyE, val)
    else:
        dictA.update({keyA:{keyB:{keyC:{keyD:{keyE:val}}}}})

def addtodict6(dictA, keyA, keyB, keyC, keyD, keyE,keyF,val):
	if keyA in dictA.keys():
		addtodict5(dictA[keyA],keyB, keyC, keyD, keyE,keyF,val)
	else:
		dictA.update({keyA:{keyB:{keyC:{keyD:{keyE:{keyF:val}}}}}})

def ISdict(dictA,num=0):
	if isinstance(dictA,dict):
		num+=1
		if len(dictA.keys())==0:
			return num
		else:
			pass
		key = list(dictA.keys())[0]
		num=ISdict(dictA[key],num)
	else:
		pass
	return num

def dict_pop_null(dictA):
	num = ISdict(dictA)
	if num<=1:
		pass
	elif num==2:
		for key in list(dictA.keys()):
			if len(dictA[key].keys())==0:
				dictA.pop(key)
			else:
				pass
	else:
		for key in list(dictA.keys()):
			dict_pop_null(dictA[key])
def Print_dict_dict(dictA):
	for key,value in dictA.items():
		print("%s\t%s\n"%(str(key),str(value)))

def Print_dict_dict2(dictA):
	for keyA in dictA.keys():
		for keyB,valueb in dictA[keyA].items():
			print("%s\t%s\t%s\n"%(str(keyA),str(keyB),valueb))
def Print_dict_dict3(dictA):
	for keyA in dictA.keys():
		for keyB in dictA[keyA].keys():
			for keyC,value in dictA[keyA][keyB].items():
				print("%s\t%s\t%s\t%s\n"%(str(keyA),str(keyB),str(keyC),value))
def Print_dict_dict4(dictA):
	for keyA in dictA.keys():
		for keyB in dictA[keyA].keys():
			for keyC in dictA[keyA][keyB].keys():
				for keyD,value in dictA[keyA][keyB][keyC].items():
					print("%s\t%s\t%s\t%s\t%s\n"%(str(keyA),str(keyB),str(keyC),str(keyD),value))

def Print_dict_dict5(dictA):
	for keyA in dictA.keys():
		for keyB in dictA[keyA].keys():
			for keyC in dictA[keyA][keyB].keys():
				for keyD in dictA[keyA][keyB][keyC].keys():
					for keyE,value in dictA[keyA][keyB][keyC][keyD].items():
						print("%s\t%s\t%s\t%s\t%s\t%s\n"%(str(keyA),str(keyB),str(keyC),str(keyD),str(keyE),value))
def Print_dict_dict6(dictA):
	for keyA in dictA.keys():
		for keyB in dictA[keyA].keys():
			for keyC in dictA[keyA][keyB].keys():
				for keyD in dictA[keyA][keyB][keyC].keys():
					for keyE in dictA[keyA][keyB][keyC][keyD].keys():
						for keyF,value in dictA[keyA][keyB][keyC][keyD][keyE].items():
							print("%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(str(keyA),str(keyB),str(keyC),str(keyD),str(keyE),str(keyF),value))

