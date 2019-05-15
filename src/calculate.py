#-*-coding:utf-8-*-
import json

def calculate_rate():
    mydict = {}
    with open("../src/data.txt","r") as datafile:
        for line in datafile:
            mydict = json.loads(line)
    count = []
    for i in range(11):
        count.append(0.0)
    for i in mydict:
        for j in mydict[i][1]:
            temp = mydict[i][1][j]
            if temp<=10.0:
                count[int(temp)] += 1.0
    for i in mydict:
        seen = 0.0
        for j in mydict[i][1]:
            temp = mydict[i][1][j]
            if temp<10.0: #平滑处理，处理次数小于10的词
                mydict[i][1][j] = min(mydict[i][1][j],
                                      (temp+1.0)*count[int(temp)+1]/count[int(temp)])
            mydict[i][1][j] /= mydict[i][0]
            seen += mydict[i][1][j]
        unseen = 0.0
        mydict[i][1][" "] = 0.0
        for k in mydict:
            if k in mydict[i][1]:
                continue
            else:
                unseen += mydict[k][0]
        mydict[i][1][" "] = (1-seen)/unseen #平滑处理，处理次数为0的词

    with open("../src/data.txt","w") as f:
    	json.dump(mydict,f)

calculate_rate()
