# -*- coding: utf-8 -*-
def by_values(args):
    return args[1]

def count_ip(file):
    dic_ip={}
    with open(file,'r') as f:
        for line in f:
            a = line.strip()
            #print(a)
            if a in dic_ip.keys():
                dic_ip[a] = dic_ip[a] + 1
            else:
                dic_ip[a] = 1
    list_ip = sorted(dic_ip.items(),key=lambda x:x[1],reverse=True)
    fw = open('result.txt','w')
    for i in range(len(list_ip)):
        fw.writelines(list_ip[i][0]+'\n')
        #print(list_ip[i][0])
    fw.close()
    #return list_ip

count_ip('ip_ad.txt')