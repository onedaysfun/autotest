import json
import time
from common.base64_en_or_decode import base64encode, base64decode, base64_only_decode, base64_only_encode

# 载入源文件
base = open("/Users/bytedance/Downloads/Saas2KA3131741.base", "r")
context: dict = json.loads(base.read())
base.close()

# 替换内容，old/new_str list需长度一致，顺序替换
old_str = [
    # 朱CN
    '7073301286489178113',
    # Peter Parker
    '7255264864845725724',
    # base-mg测试-sg1
    '7316359541086650396'
]

new_str = [
    # 朱贵兵
    '7345310114443690151',
    # 张昂
    '7329730821990908071',
    # 张浩然
    '7329731777805680806'
]
# 获取解密后json
gzip_snapshot = base64decode(context['gzipSnapshot'])
gzip_automation = base64decode(context['gzipAutomation'])
unzip_snapshot_list = []
unzip_automation_list = []


# 替换表格+自动化
str_automation = json.dumps(gzip_automation)
str_snapshot = json.dumps(gzip_snapshot)

# 替换表格+自动化快照
for i in range(0, len(new_str)):
    str_automation = str_automation.replace(old_str[i], new_str[i])
    str_snapshot = str_snapshot.replace(old_str[i], new_str[i])
unzip_automation_list.append(json.loads(str_automation))
unzip_snapshot_list.append(json.loads(str_snapshot))

# 替换仪表盘
unzip_dashboard_list = []
gzip_dashboard = base64decode(context['gzipDashboard'])
####
dashboard_list = []
for snapshot in gzip_dashboard:
    # 重写snapshot
    un_base64_snapshot = base64_only_decode(snapshot['snapshot'])
    for i in range(0, len(new_str)):
        un_base64_snapshot = un_base64_snapshot.replace(old_str[i], new_str[i])
    snapshot['snapshot'] = base64_only_encode(un_base64_snapshot)
    # 重写chart
    charts_list = []
    for chart in snapshot['charts']:
        un_base64_chart = base64_only_decode(chart['snapshot'])
        for i in range(0, len(new_str)):
            un_base64_chart = un_base64_chart.replace(old_str[i], new_str[i])
        chart['snapshot'] = base64_only_encode(un_base64_chart)
        charts_list.append(chart)
    snapshot['charts'] = charts_list
    dashboard_list.append(snapshot)
unzip_dashboard_list = dashboard_list
####
# 组装json
context_new = context
context_new['gzipSnapshot'] = base64encode(unzip_snapshot_list[0])
context_new['gzipAutomation'] = base64encode(unzip_automation_list[0])
#
context_new['gzipDashboard'] = base64encode(unzip_dashboard_list)

print(gzip_dashboard)
print(context_new)

# 新建文件
file_name = "Saas2KA-" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + ".base"
new_file = open(f"/Users/bytedance/Downloads/{file_name}", "w")
new_file.write(json.dumps(context_new))
new_file.close()

