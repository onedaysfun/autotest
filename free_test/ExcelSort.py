import openpyxl
import os


path = f'/Users/bytedance/Downloads'
os.chdir(path)


workbook = openpyxl.load_workbook('sv5-全字段-复杂排序全视图样张(2).xlsx')


sheet = workbook['12000行，部分行可见']

count = 0
for i in range(2, 6039):
    a = f'B{i}'
    b = f'B{i+1}'
    if int(sheet[a].value) < int(sheet[b].value):
        print(sheet[a].value)
        print(sheet[b].value)
        print("\n")
        count += 1
print(sheet.dimensions)
print(count)