#encoding: utf-8
__author__ = 'yyin'

import os.path, os, re
import read_file, sys
import excel_map
import parse_file

test_filename = 'c:\\users\\yyin\\documents\\github\\deal_brief\\tmp\\test.xls'
out_path = r'e:\\'

class brief:
    Dealowner=u''
    Property=[]
    Licensee=u''
    Comdate=u''
    Enddate=u''
    Category=[]
    Channel=[]
    MG=0
    Payment={}
    Rytrate=0.0
    Selloff=u''

    # def rate_to_txt(self):
        # n=str(self.Rytrate*100)+'%'
        # return unicode(n,'utf-8')

    # def str_to_uni(txt):
        # if type(txt)==str:
            # return unicode(txt,'utf-8')
        # else:
            # return txt

    Template=ur"""Dear Guenther,

Per [Dealowner]'s request, attached is the Merchandise Licensing Agreement for [Property]. Below is the summary of
the agreement. Could you please kindly approve the attached at your earliest convenience? Thanks!


Parties: ODW (Ancillary WFOE) and [Licensee]

Licensed Property: [Property]

Licensed Period: from [Comdate] to [Enddate]

Licensed Articles: [Category]

Licensed channel: [Channel].

Advance/Minimum Guarantee: RMB[MG], among which:
(a)  RMB[Payment_amount] shall be paid [Payment_schedule];
(b)  RMB[Payment_amount] shall be paid by [Payment_schedule]

Royalty Rate: [Rytrate]

Sell-off period: [Selloff]
"""
	# def toBrief(self):
		# n = self.Template
		# n = n.replace('')

		
def brief_output(tgt, template):
	for i in tgt:
		template = template.replace('['+str(i)+']',tgt[i])
	
	out_file=open(os.path.join(out_path,'deal_brief.txt'),'w')
	out_file.write(template)
	out_file.close()
	
		
	
def init(filename):
	#filename = sys.argv[1]
	if os.path.exists(filename) == False:
		return 'Error! File not exists.'
	
	sheet = read_file.excel_open(filename)
	target = brief()
	Map = excel_map.xlsMap2  
	
	#return sheet, target, Map
	tgt1=parse_file.parse1(sheet, Map)
	print tgt1
	brief_output(tgt1, target.template)



	
# if __name__ == '__main__':
	# #init(filename)
	# #sheet, target, Map = init(test_filename)
	# #print target.Template
	# init(test_filename)
	
	
