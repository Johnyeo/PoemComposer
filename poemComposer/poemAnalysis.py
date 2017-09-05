# coding:utf-8
import random
import re
import urllib
from urllib import request


# 从古诗文网的名句页爬取古诗,第一个参数是页数，第二个参数是条数。p如果超过范围，则随机一个。num大于1则生产一个list
from poemComposer import rawPoem


def getPoem(p = 0, num = 1):
    #  p是古诗文网的页数,114页一共
    #  如果p = 0 则传入随机数。如果p = 具体数字则传入具体的数字
    if  p > 114 or p <=0:
        pageRange = range(1, 115)
        p = random.sample(pageRange, 1)
        p = str(p[0])
    else:
        p = str(p)
    url = 'http://so.gushiwen.org/mingju/Default.aspx?p=%s&c=&t='% p
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               }
    req = request.Request(url,data=None,headers = headers)
    response = request.urlopen(req)
    page = response.read()
    page = page.decode('utf-8')
    pattern = re.compile(r'[\u4e00-\u9fa5].*(?=</a><span )')
    match_list = re.findall(pattern, page, )
    result = random.sample(match_list, num)
    if num == 1:
        return result[0]
    elif num <= 0:
        return match_list
    else:
        return result

def getCertainLength(tar_str,num = 0):
    if num <= 0:
        return tar_str
    else:
        result = tar_str[0:num]
        return result

def splitPoem(tar_str):
    tar_str = tar_str.replace('，',' ')
    tar_str = tar_str.replace('。',' ')
    tar_str = tar_str.replace('？',' ')
    tar_str = tar_str.replace('；',' ')
    tar_str = tar_str.replace('！',' ')
    result = tar_str.split()
    return result

def spiderAllPoem():
    for p in range(1,115):

        poemlist = getPoem(p, 0)
        i = 1
        for s in poemlist:
            with open('poem.txt', 'a') as f:
                i_str  = str(i)
                f.write(i_str)
                try:
                    f.write(s)
                except UnicodeEncodeError as e:
                    print("含有生僻字: %s" % s)
                    f.write("**********")
                f.write('\n')
                i += 1

        with open('poem.txt', 'a') as f:
            p_str = str(p)
            f.write(p_str)
            f.write('\n')

        print("page %d finished" % p)

def findDuplicateWords():
    with open("poem.txt",'r') as f:
        source_str = f.read()
    a_str = source_str
    result = []
    passlist = ['、','\n','，','。']
    for i in range(len(a_str)):
        if a_str == '':
            break
        else:
            n_str = a_str[-1]
            if n_str in passlist:
                a_str = a_str[:-1]
            else:
                t = 0
                for m_str in a_str:
                    if n_str == m_str:
                        t += 1
                    else:
                        pass
                result.append((n_str,t))
                a_str = a_str.replace(n_str,'')

    return result

def getWordFrequency(ls):
    # 冒泡排序
    total = len(ls)
    for n in range(total):
       for m in range(total):
           if ls[n][1] < ls[m][1]:
               pass
           elif ls[n][1] > ls[m][1]:
               ls[n],ls[m] = ls[m],ls[n]
           else:
               pass
    return ls

def getPinyinFromDict(w):
    with open('C:\\Users\\张垚\\PycharmProjects\\yunshangguoxue\\poemComposer\\pinyindict.txt','r',encoding='utf-8') as f:
        pinyindict = f.read()
    i = pinyindict.find(w)
    s = ''
    str = ''
    while s != ',':
        str += s
        s = pinyindict[i + 1]
        i += 1

    return str

def formatPinyin(word):
    res = word
    for w in word:
        if w in rawPoem.tone:
            i = rawPoem.tone.index(w)
            if i>0 and i<5:
                tone = rawPoem.tone.index(w)
                res = word.replace(w,'a')+str(tone)
            if i>5 and i<10:
                tone = rawPoem.tone.index(w)-5
                res = word.replace(w,'o')+str(tone)
            if i>10 and i<15:
                tone = rawPoem.tone.index(w) - 10
                res = word.replace(w,'e')+str(tone)
            if i>15 and i<20:
                tone = rawPoem.tone.index(w) - 15
                res = word.replace(w,'i')+str(tone)
            if i>20 and i<25:
                tone = rawPoem.tone.index(w) - 20
                res = word.replace(w,'u')+str(tone)
            if i>25 and i<30:
                tone = rawPoem.tone.index(w) - 25
                res = word.replace(w,'v')+str(tone)

    return res

def formatDict():
    with open('C:\\Users\\张垚\\PycharmProjects\\yunshangguoxue\\poemComposer\\pinyindict.txt','r',encoding='utf-8') as f:
        pinyindict = f.read()
    dict_ls = pinyindict.split(',')
    new_dict_ls = []
    i = 1
    for word in dict_ls:
        if word == '':
            continue
        pinyin = word[1:]
        pinyin = formatPinyin(pinyin)
        tone = pinyin[-1]
        new_dict_ls.append((word[0],pinyin,tone))
    return new_dict_ls

def fetchVowel(word):
    vowel = ''
    for i in rawPoem.initials:
        if i == word[0]:
            if word[1] == 'h':
                return (i+'h',word[2:])
            else:
                return (i, word[1:])




# print (fetchVowel('shi'))

print(formatDict())

# spiderAllPoem()
# print(getPoem(69,0))
# sum = findDuplicateWords()
# print (getWordFrequency(sum))


