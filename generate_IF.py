from mrjob.job import MRJob
import math
from collections import Counter
from mrjob.protocol import RawProtocol


class Inverted_File(MRJob):
    OUTPUT_PROTOCOL = RawProtocol

    def mapper(self, _, line):
        temp = line.split('\t')
        te = temp[0].split(' ')
        title = te[0]  #　获取题目
        url = te[1]
        text = temp[1]  # 获取正文内容
        words = text.split(' ')  # 预先已经进行过jieba分词，此处生成包含各词的list
        count = Counter(words)  # 用collections包的Counter方法来进行词频统计，高效且方便
        for w in count:
            tf = count[w] * 1.0 / len(words)     # 计算tf项, 并字串化方便之后传递
            tf = str(tf)
            yield w, title + '  ' + url + '  ' + tf   # 输出为(词语，＂题目+url+tf＂字串)

    def reducer(self, w, value):
        temp = '\t'.join(value)
        val = temp.split('\t')    # 将同一个词语对应的"题目+url+tf"字串转化到一个列表内
        ls = []
        count = len(val)  # 统计包含当前词语的文档数
        total_title = 300   # total number of documents
        for ele in val:
            temp2 = ele.split('  ')
            tf_idf = eval(temp2[-1]) * math.log(total_title * 1.0 / count + 1)  # 计算tf-idf值
            # ls.append([''.join(temp2[:-2]), tf_idf])
            ls.append([temp2[0], temp2[1], tf_idf])
        yield w, str(ls)    # 返回形式如：　词语，[题目,url,tf-idf值]


if __name__=='__main__':
    Inverted_File.run()
