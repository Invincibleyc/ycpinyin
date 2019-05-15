#-*-coding:utf-8-*-
import re

filename1 = input()
filename2 = input()
f1 = open(filename1,'r', encoding='utf-8')
f2 = open(filename2,'r', encoding='utf-8')
list1 = f1.readlines()
list2 = f2.readlines()
n1 = 0.0
n2 = 0.0
t1 = 0.0
t2 = 0.0
for i in range(len(list1)):
    n1 += 1.0
    if i > len(list2)-1:
        break
    list1[i] = re.sub(re.compile(r'[\s]+?'),'', list1[i])
    list2[i] = re.sub(re.compile(r'[\s]+?'),'', list2[i])
    if len(list1[i])!=len(list2[i]):
        print("error"+" "+str(len(list1[i]))+" "+str(len(list2[i])))
        break
    t1 += len(list1[i])
    temp = 0.0
    for j in range(len(list1[i])):
        if list1[i][j]==list2[i][j]:
            temp+=1.0
            t2 += 1.0
    if temp== len(list1[i]):
        n2 += 1.0

print(t2/t1)
print(n2/n1)
