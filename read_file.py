#encoding: utf-8

import win32com.client
import os, os.path


def excel_open(file_path):
#the file_path must be an absolute path
	xlsApp = win32com.client.Dispatch('Excel.Application')
	xlsApp.Visible = False
	xlsBook = xlsApp.Workbooks.Open(file_path)
	
	return xlsBook
