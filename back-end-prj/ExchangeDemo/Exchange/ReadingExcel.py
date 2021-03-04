# refference blog 
#https://blog.csdn.net/ly_ysys629/article/details/54428838

#df_obj.ix[1:3] #获取1-3行的数据,该操作叫切片操作,获取行数据
#df_obj.ix[columns_index] #获取列的数据
#df_obj.ix[1:3，[1,3]]#获取1列3列的1~3行数据
#df_obj[columns].drop_duplicates() #剔除重复行数据



import pandas as pd
#Data_set = pd.read_excel('D:\\Users\\wuqi2\\Desktop\\PSD\\201803221000Wistron TNB PRC PSD 20180321.xlsx', 'PSD', index_col=None, na_values=['NA'])

ds = pd.read_excel('D:\\Users\\wuqi2\\Desktop\\PSD\\tester.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print('Excel Data set is:')
print(str(ds))
#get cell(4,3)
print('dataobject')
print(ds.ix[2:3,[0]])
print(ds.ix[2:3,[1]])
print(ds.ix[2:3,[2]])#datatime

print('datatypes:')
print(ds.ix[2:3,[0]].dtypes)
print(ds.ix[2:3,[1]].dtypes)
print(ds.ix[2:3,[2]].dtypes )#datatime

print('data.values')
print(ds.ix[2:3,[0]].values)
print(ds.ix[2:3,[1]].values)
print(ds.ix[2:3,[2]].values)#datatime
#get column 1,3
#column1 =  row.ix[1]
#print('column1 is: ')
#print(str(column1))
#column3 =
