import jieba
import re


if __name__ == '__main__':
    indoc = 0   # show if in some document
    r = {}  # 将文件修改成｛(网页名称,url)，内容｝的形式并储存在字典中
    with open('./wiki_88', 'r', encoding='utf-8') as f:
        for line in f:
            if "<doc" in line:
                indoc = 1
                text = []
                url = re.findall(r'url="(.*?)"', line)[0]
                title = re.findall(r'title="(.*?)">$', line)[0]
                key = (title, url)
                r[key] = text
            elif "</doc>" in line:
                indoc = 0
                text = ''.join(r[key])
                text = jieba.cut(text, cut_all=False)  # 预先使用jieba库进行分词处理，方便之后倒排文档的构建
                r[key] = ' '.join(text)
                if len(r) >= 50:
                    with open('./wiki_process.txt', 'a', encoding='utf-8') as f1:
                        for i in r.keys():
                            f1.write(i[0] + ' ' + i[1] + '\t' + r[i])
                            f1.write('\n')
                    r = {}   # clear the cache and write in the file
            elif line == "\n":
                continue
            elif not line:   # end of file
                if r:
                    with open('./wiki_process.txt', 'a', encoding='utf-8') as f1:
                        for i in r.keys():
                            f1.write(i[0] + ' ' + i[1] + '\t' + r[i])
                            f1.write('\n')
                break
            elif indoc == 1 and key is not None:
                li = line.strip('\n')
                r[key].append(li)
