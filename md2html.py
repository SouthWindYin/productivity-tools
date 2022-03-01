import markdown as md
import sys

if len(sys.argv)<3:
    print('请输入markdown文件和输出文件名')
    sys.exit()
print(sys.argv)
file=sys.argv[1]
target=sys.argv[2]

header='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body lang="zh">
'''
footer='''
</body>
</html>
'''

with open(file,'r',encoding='utf-8') as f:
    html=md.markdown(f.read())

with open(target,'w',encoding='utf-8') as fw:
    fw.write(header+html+footer)

print('转换完成')