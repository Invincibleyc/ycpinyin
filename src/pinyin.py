#-*-coding:utf-8-*-
import re
import json
from pypinyin import pinyin, lazy_pinyin

def ask_words(mydict, word0, word1): #获取词的概率
    if word0 in mydict:
        if word1 in mydict[word0][1]:
            return mydict[word0][1][word1]
        else:
            if word1 in mydict:
                return mydict[word0][1][" "]*mydict[word1][0] #出现次数为0的词的概率
            else:
                return 0.0
    else:
        return 0.0

def get_pin_yin_dict(): #获取拼音汉字表，存入dict
    f = open('../src/pinyin.txt', 'r')
    p = r'(.+?)[\s]'
    pattern = re.compile(p)
    pinyindict = {}
    for line in f:
        pinyinlist = re.findall(pattern, line)
        pinyindict[pinyinlist[0]] = []
        for i in range(len(pinyinlist)):
            if i>0:
                pinyindict[pinyinlist[0]].append(pinyinlist[i])

    f.close()
    return pinyindict

def showresult(searchlist, f): #输出转换结果，并写入文件
    maxn = 0.0
    maxc = ''
    n = len(searchlist)-1
    for i in searchlist[n]:
        if searchlist[n][i][0]>=maxn:
            maxn = searchlist[n][i][0]
            maxc = i
    reslist=[]
    res = maxc
    reslist.append(maxc)
    maxc = searchlist[n][maxc][1]
    reslist.append(maxc)
    res = maxc+' '+res
    flag = n
    flag-=1
    while flag>0:
        if maxc==' ':
            break
        maxc = searchlist[flag][maxc][1]
        reslist.append(maxc)
        res = maxc+' '+res
        flag-=1
    for i in range(len(reslist)): #倒序写入文件
        if(reslist[len(reslist)-1-i]!=' '):
            f.write(reslist[len(reslist)-1-i].encode('utf-8'))
    f.write('\r\n'.encode('utf-8'))
    print(res)
    return reslist

def judge(word1, word2, pinyinlist, i, editdict): #判断词的拼音与给定拼音是否相符
    mystr = word1+word2
    templist = [pinyinlist[i-1].lower(), pinyinlist[i].lower()]
    mylist = lazy_pinyin(word1+word2)
    if mystr in editdict:
        if templist in editdict[mystr]:
            return True
    if mylist[0]==pinyinlist[i-1].lower() and mylist[1]==pinyinlist[i].lower():
        return True
    else:
        return False

def work(inputfile, outputfile): #将拼音转化为汉字
    mydict = {}
    with open("../src/data.txt","r") as datafile:
        for line in datafile:
            mydict = json.loads(line)
    editdict = {}
    with open("../src/edit.txt","r") as editfile:
        for line in editfile:
            editdict = json.loads(line)
    f = open(inputfile, 'r', encoding='utf-8')
    f1 = open(outputfile, 'wb')
    p = r'(.+?)[\s]'
    pattern = re.compile(p)
    pinyindict=get_pin_yin_dict()
    for line in f:
        line = line+' '
        searchlist=[]
        inputlist = re.findall(pattern, line)
        if len(inputlist)==0:
            continue
        for i in inputlist:
            i = i.lower()
            temp = {}
            for j in pinyindict[i]:
                temp[j] = []
                temp[j].append(0.0)
                temp[j].append(' ')
            searchlist.append(temp)
        for i in range(len(searchlist)): #遍历节点，更新权值
            if i > 0:
                if i==1:
                    for j in searchlist[1]:
                        for k in searchlist[i-1]:
                            if searchlist[i][j][0]!=0.0:
                                temp_res = searchlist[0][k][0]*ask_words(mydict, k, j)
                                if not judge(k, j, inputlist, i, editdict):
                                    continue
                                if temp_res>searchlist[i][j][0]:
                                    searchlist[i][j][0] = temp_res
                                    searchlist[i][j][1] = k
                            else:
                                if not judge(k, j, inputlist, i, editdict):
                                    continue
                                searchlist[i][j][0]= searchlist[i-1][k][0]*ask_words(mydict,k,j)
                                searchlist[i][j][1] = k
                else:
                    for j in searchlist[i]:
                        for k in searchlist[i-1]:
                            temp_res = searchlist[i-1][k][0]*ask_words(mydict, k, j)
                            if not judge(k, j, inputlist, i, editdict):
                                continue
                            if temp_res>searchlist[i][j][0]:
                                searchlist[i][j][0]=temp_res
                                searchlist[i][j][1]=k
            else:
                for j in searchlist[0]:
                    if j in mydict:
                        searchlist[0][j][0]=mydict[j][0]
                    else:
                        searchlist[0][j][0]=0.0
        showresult(searchlist, f1)
        print(line)
    f.close()
    f1.close()

inputfile = input()
outputfile = input()
work(inputfile, outputfile)
