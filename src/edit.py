#-*-coding:utf-8-*-
import re
import json
from pypinyin import pinyin, lazy_pinyin

#多音字处理的修正
pinyinfilename = input()
hzfilename = input()
f1 = open(pinyinfilename, 'r')
f2 = open(hzfilename, 'r')
p = r'(.+?)[\s]'
pattern = re.compile(p)
flag = 0
tempstr = ""
pinyinlist=[]
editdict = {}
list1 = f1.readlines()
list2 = f2.readlines()
for i in range(len(list1)):
    if i>len(list2)-1:
        break
    pinyinlist = re.findall(pattern, list1[i])
    list2[i] = re.sub(re.compile(r'[\s]+?'),'', list2[i])
    for j in range(len(list2[i])):
        if j == 0:
            continue
        else:
            mylist = lazy_pinyin(list2[i][j-1]+list2[i][j])
            if mylist[0]!=pinyinlist[j-1].lower() or mylist[1]!=pinyinlist[j].lower():
                mystr = list2[i][j-1]+list2[i][j]
                templist = [pinyinlist[j-1].lower(), pinyinlist[j].lower()]
                if mystr in editdict:
                    if templist in editdict[mystr]:
                        continue
                    else:
                        editdict[mystr].append(templist)
                else:
                    editdict[mystr] = []
                    editdict[mystr].append(templist)
with open("edit.txt","w") as f:
    json.dump(editdict,f)
