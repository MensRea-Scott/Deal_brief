#encoding: utf-8
import os, os.path, re
import src, win32com.client




def single_parse(sheet, keyword, offset):
#140625 调试通过
	rgA = sheet.Columns.Find(keyword)
	
	if rgA.Value is None:
		return 'ERROR'
	
	# print(n.Row, n.Column)
	# print(n.Row+offset[0],n.Column+offset[1])
	#target = rgA.Offset(1+offset[0], 1+offset[1]).Value
	target = rgA.Offset(offset[0], offset[1])
	
	if target.Value is None:
		return 'No Value Found'
	else:
		return target.Value
	
	
	
def list_parse(sheet, keyword, offset):
	rgA = sheet.Columns.Find(keyword)
	
	if rgA.Value is None:
		return 'ERROR'
	
	print rgA.Row, rgA.Column
	
	result = []
	rgB = rgA.Offset(offset[0],offset[1])
	
	while True:
		n = rgB.Value
		if n is None:
			print 'ERROR: No Value Found'
			break
			#return 'ERROR: No Value Found'
			
		elif n in result:
			rgB = rgB.Offset(2,1)
			continue
		else:
			result.append(n)
		
		rgB = rgB.Offset(2,1)
			
	return result


def parse1(sheet, Map):
	target={}
	
	for i in Map:
		if Map[i][2]=='single':
			print Map[i][0], Map[i][1]
			target[i]=single_parse(sheet, Map[i][0], Map[i][1])
			print '*'*10
		elif Map[i][2]=='list':
			target[i]=list_parse(sheet, Map[i][0],Map[i][1])
	
	return target
	
def load(filename=r'c:\users\yyin\documents\github\deal_brief\tmp\test.xls'):
	xlsApp = win32com.client.Dispatch('Excel.Application')
	xlsApp.Visible = True
	xlsBook = xlsApp.Workbooks.Open(filename)
	sheet = xlsBook.Sheets[0]
	
	return sheet

# sheet=load()
