#-*-coding:utf-8-*-
import re
import json
import os

#计数器可以实现每次读取给定数目的数据，便于中断后从断点继续读取
def get_counter(): #获取计数器数值,在第一次处理前，为-1，处理完一个文件后为0
    if os.path.exists('counter.txt'):
        f = open('counter.txt','r')
        temp = f.readlines()
        f.close()
        if temp:
            counter = int(temp[0])
            return counter
        else:
            return 0
    else:
        f = open('counter.txt','w')
        f.write('-1')
        f.close()
        return -1

def search(filename,mynum):
    p = r'"html".+"(.+)".+"time"'
    p2 = r'[◥●≥≤⑦⑥③④②①■·！？。，＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏]'
    p3 = r'[A-Za-z0-9\!\%\[\]\,\():@]'
    pattern = re.compile(p)
    c_symbol_pattern = re.compile(p2)
    inputfile=open(filename,'r',encoding='utf-8')
    counter = get_counter()
    print(counter)
    mydict = {}
    if counter == -1:
        counter = 0
    else:
        with open("data.txt","r") as datafile:
            for line in datafile:
                mydict = json.loads(line)
    hzfile = open('hz.txt','r')
    c_dict = {}
    for line in hzfile:
        for i in range(len(line)):
            c_dict[line[i]] = 0
    temp = counter
    temp1 = 0
    for line in inputfile:
        temp1 = temp1+1
        if(temp1 <= temp):
            continue
        counter=counter+1
        if(temp1 >= mynum+temp):
            continue
        html_list=re.findall(pattern, line)
        for i in html_list:
            k = re.sub(re.compile('℃'),'摄氏度', i) #将数字等转为汉字，字母和标点转为空格
            k = re.sub(re.compile('0'),'零', k)
            k = re.sub(re.compile('〇'),'零', k)
            k = re.sub(re.compile('1'),'一', k)
            k = re.sub(re.compile('2'),'二', k)
            k = re.sub(re.compile('3'),'三', k)
            k = re.sub(re.compile('4'),'四', k)
            k = re.sub(re.compile('5'),'五', k)
            k = re.sub(re.compile('6'),'六', k)
            k = re.sub(re.compile('7'),'七', k)
            k = re.sub(re.compile('8'),'八', k)
            k = re.sub(re.compile('9'),'九', k)
            k = re.sub(re.compile('\.'),'点', k)
            k = re.sub(re.compile('\/'),'每', k)
            k = re.sub(re.compile('-'),'至', k)
            k = re.sub(re.compile('\/'),'每', k)
            k = re.sub(re.compile(p2), ' ', k)
            k = re.sub(re.compile(p3), ' ', k)
            k = re.sub(re.compile(r'[A-Za-z]'), ' ', k)
            k = re.sub(re.compile(r'[\s\n\r]+'),' ', k)
            for j in range(len(k)-1):
                if(k[j] in c_dict) and (k[j+1] in c_dict): #判断是否在一二级汉字表中
                    pre = k[j]
                    _next = k[j+1]
                    if(pre in mydict):
                        mydict[pre][0] += 1.0
                        if(_next in mydict[pre][1]):
                            mydict[pre][1][_next] += 1.0
                        else:
                            mydict[pre][1][_next] = 1.0
                    else:
                        mydict[pre] = [1.0, {}]
                        mydict[pre][1][_next] = 1.0

    print(counter)
    if temp1==counter:
        counter = 0
    with open("data.txt","w") as f:
    	json.dump(mydict,f)
    f1 = open('counter.txt','w')
    f1.write(str(counter))
    f1.close()
    inputfile.close()
    hzfile.close()

search('2016-01.txt', 200000)
search('2016-02.txt', 200000)
search('2016-03.txt', 200000)
search('2016-04.txt', 200000)
search('2016-05.txt', 200000)
search('2016-06.txt', 200000)
search('2016-07.txt', 200000)
search('2016-08.txt', 200000)
search('2016-09.txt', 200000)
search('2016-10.txt', 200000)
search('2016-11.txt', 200000)
