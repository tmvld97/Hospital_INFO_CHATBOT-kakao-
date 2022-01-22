import openpyxl
import pandas as pd
# xlsx = pd.read_excel('final_train.xlsx')
# xlsx.to_csv('final_train.csv', index=False)

f = open('add_trans_2.txt', 'r',encoding= 'utf-8')
f2 = open('add_csv2.txt', 'a',encoding= 'utf-8')

for i in f :
    a = i.replace("0000","")
    b = a.replace("\t\t",",")
    c = b.replace("\t","")
    f2.write(c.replace("\n","")+'\n')

#
# f = open('add_total_trans.txt', 'r',encoding= 'utf-8')
# list = f.readlines()
#
# f.close()
# #
# file = openpyxl.load_workbook("final_train.xlsx")
# sheet = file.active
# # #
# def ex() :
#     for i in range(1, len(list)+1) :
#         list1 = list[i-1].split(',')
#         print(list1)
#         # for k in range(1, len(list1)+1) :
#             # sheet[chr(k+64) + str(i)].value = list1[k-1]
# #     file.save("final_train.xlsx")
# ex()