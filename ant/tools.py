import decimal
from operator import itemgetter, attrgetter

def saveError():
    quit()

def fetchResult(res):
    res_dic = []
    for row in res:
        if row != None or row != '':
            res_dic.append(row)
    return res_dic

def assembleResult(key, res):
    dic = {}
    for s in res:
        if key == 'schema':
            dic[s[0]] = str(s[1]) + '|' + str(s[2]) + '|' + str(s[3]) + '|' + str(s[4])
        elif key == 'notInnodb':
            str1 = s[0] + '.' + s[1]
            dic[str1] = s[2]
        elif key == 'top10':
            str1 = s[0] + '|' + s[1]
            str2 = str(s[2]) + '|' + str(s[3]) + '|' + str(s[4]) + '|' + str(s[5])
            dic[str1] = str2

    return dic

def saveLog():
    quit()


def sortTop10(dic):
    list = []
    info_tuples = []
    for ip, info in dic.items():
        for k, v in info.items():
            nkey = ip + '|' + k

            info_tuples.append((nkey, decimal.Decimal(v.split('|')[0]), decimal.Decimal(v.split('|')[1]),
                                decimal.Decimal(v.split('|')[2]), decimal.Decimal(v.split('|')[3])))

    new = sorted(info_tuples, key=itemgetter(4, 2), reverse=True)
    for i in range(0, 10):
        list.append(new[i])

    return list