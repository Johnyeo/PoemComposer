# coding:utf-8

list = [5,2,5,1,8,3]

def bubbleSort(ls):
    # 冒泡排序
    total = len(ls)
    for n in range(total):
       for m in range(total):
           if ls[n] > ls[m]:
               pass
           elif ls[n] < ls[m]:
               ls[n],ls[m] = ls[m],ls[n]
           else:
               pass
    return ls

def cocktailSort(ls):
    # 鸡尾酒排序
    pass
