该项目为“人工智能导论”的作业。
以新浪新闻为语料，基于统计学习，实现了简易的拼音输入法。

文件目录如下：
│  readme.txt
│  拼音输入法作业报告-计61-叶翀-2016011387.doc
│
├─bin
├─data
│      input.txt
│      output.txt
│
└─src
        answer.txt
        calculate.py
        contrast.py
        data.txt
        edit.py
        edit.txt
        hz.txt
        pinyin.py
        pinyin.txt
        processing.py

其中，data目录下，各个文件作用如下：
input.txt      输入文件样例
output.txt     输出文件样例

其中，src目录下，各个文件作用如下：
answer.txt     自行测试中，拼音对应汉字的正确结果
calculate.py   根据语料处理结果计算概率
contrast.py    输入两个文件名，输出逐字对比的准确率和整句的准确率
data.txt       存储概率计算结果，格式为json
edit.py        多音字处理的修正
edit.txt       存储多音字修正所用的dict，格式为json
hz.txt         一二级汉子表
pinyin.py      用户提供输入文件名和输出文件名，将拼音转为汉字
processing.py  处理语料

运行pinyin.py,输入输入文件名和输出文件名，则将转化结果保存到输出文件中。