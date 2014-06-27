#encoding: utf-8

# class excel_map:
	# Dealowner = {u'Category Manager':(1,3)}
	# Property = {u'Licensed Properties':(2,3)}
	# Licensee = {u'Licensee Name':(1,3)}
	# Comdate = {u'Contract Start Date':(1,3)}
	# Enddate = {u'Contract End Date':(1,3)}
	# Category = {u'Licensed Articles':(3,1)}
	# #MG = {}
	# #Payment={}
	# Rytrate = {u'Royalty Rate':(1,0)}
	# Selloff = {u'Sell Off Date':(0,2)}

# xlsMap = {'Dealowner': [u'Category Manager',(0,2),'single'], 
    # 'Property': [u'Licensed Properties',(1,2),'list'], 
	# 'Licensee': [u'Licensee Name',(0,2),'single'], 
	# 'Comdate': [u'Contract Start Date',(0,2),'single'], 
	# 'Enddate': [u'Contract End Date',(0,2),'single'], 
	# 'Category': [u'Licensed Articles',(2,0),'list'], 
	# 'Rytrate': [u'Royalty Rate',(1,0),'single'], 
	# 'Selloff': [u'Sell Off Date',(0,2),'single']
# }
	
xlsMap2 = {'Dealowner': [u'Category Manager',(1,3),'single'], 
    'Property': [u'Licensed Properties',(2,3),'list'], 
	'Licensee': [u'Licensee Name',(1,3),'single'], 
	'Comdate': [u'Contract Start Date',(1,3),'single'], 
	'Enddate': [u'Contract End Date',(1,3),'single'], 
	'Category': [u'Licensed Articles',(3,1),'list'], 
	'Rytrate': [u'Royalty Rate/授权金比例',(2,1),'list'], 
	'Selloff': [u'Sell Off Days',(1,3),'single']
}#140625 调试通过