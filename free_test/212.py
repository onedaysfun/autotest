import csv
import json

aa = [[1, 2], [1], [4, 2]]
bb = [[1, 2, 3], [1], [2]]

c = []
for i in range(0, len(aa)):
    d = []
    if aa[i] == bb[i]:
        c.append(d)
        continue
    if len(aa[i]) > len(bb[i]):
        for j in range(0, len(aa[i])):
            for k in range(0, len(bb[i])):
                if aa[i][j] == bb[i][k]:
                    continue
                else:
                    d.append(aa[i][j])
        c.append(d)
    else:
        for j in range(0, len(bb[i])):
            for k in range(0, len(aa[i])):
                if aa[i][k] == bb[i][j]:
                    continue
                else:
                    d.append(bb[i][j])
        c.append(d)
print(c)
# 冒泡排序
# for i in range(0, len(c)):
#     for j in range(0, len(c[i])):
#         for k in range(0, len(c[i]) - 1):
#             if c[i][k] > c[i][k + 1]:
#                 c[i][k], c[i][k + 1] = c[i]

# 冒泡排序
# for i in range(0, len(c)):
#     for j in range(0, len(c[i])):
#         for k in range(0, len(c[i]) - 1):
#             if c[i][k] > c[i][k + 1]:
#                 c[i][k], c[i][k + 1] = c[i

# 睡眠排序
# for i in range(0, len(c)):
#     for j in range(0, len(c[i])):
#         for k in range(0, len(c[i]) - 1):
#             if c[i][k] > c[i][k + 1]:
#                 c[i][k], c[i][k + 1] = c[i
record_list = []
# with open("test.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         record_list.append(row[0])
# print(record_list)
s = {
    "conjunction": "and",
    "conditions": [{
        "fieldId": "fld8q3i6eM",
        "fieldType": 1005,
        "operator": "isNot",
        "value": ["$$random:text:5$$"],
        "conditionId": "condIZjT3X"
    },
    {
        "fieldId": "fldC3BeE2q",
        "fieldType": 11,
        "operator": "isNotEmpty",
        "value": None,
        "conditionId":"cons4oVhRy"},
    {
        "fieldId":"fldYeZjcge",
        "fieldType": 4,
        "operator": "is",
        "value": ["optoImnNYk"],"conditionId":"con3JX0KyG"}
]}
print(json.dumps(s).replace(" ", ""))
