#encoding: utf-8

import win32com.client
import os, os.path
import excel_map as MAP
import sys
#import src

def excel_open(file_path):
#the file_path must be an absolute path
	xlsApp = win32com.client.Dispatch('Excel.Application')
	xlsApp.Visible = False
	xlsBook = xlsApp.Workbooks.Open(file_path)
	xlsSheet = xlsBook.Sheets[0]
	
	return xlsSheet
	

def load_map():
	xlsMap = MAP.excel_map()
	
	return xlsMap




