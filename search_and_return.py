from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("search_keyword")
sc = SparkContext(conf=conf)


def search(keyword, path):
    text_file = sc.textFile(path + '/wikiIF.txt')
    res_list = text_file.map(lambda line: line.split("\t")).filter(lambda x: x[0] == keyword)
    res = res_list.collect()
    res1 = res[0][1]
    res1 = eval(res1)
    with open('./temp.txt', 'w', encoding='utf-8') as f:
        for i in res1:
            f.write(i[0] + ' ' + i[1] + ' ' + str(i[2]))
            f.write('\n')


def show(path):
    text_file2 = sc.textFile(path + '/temp.txt')
    res2 = text_file2.map(lambda line: line.split(' ')).map(lambda x: (x[2], (x[0], x[1]))).sortByKey(False)
    res2 = res2.collect()
    print(res2)


if __name__ == '__main__':
    pa = f"file:///home/mrding/PycharmProjects/分布式course/final_pj"
    keyw = input("input the word you want to search:")
    search(keyw, pa)
    show(pa)
