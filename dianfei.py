import requests
import re


def feiyong(sushe):
    #返回一个列表，第一个元素表示基本账户，第二个元素表示电补账户，第三个表示总余额
    data = {'fjmc': sushe}
    html = requests.post('http://210.45.193.244:8080/admin/sys!chaxun.action', data)
    find_str = r'\t.+元'
    p = re.compile(find_str)
    fei_list = p.findall(html.text)
    qian = []
    for i in fei_list:
        qian.append(i.split('\t')[6].split('元')[0])
    return qian


if __name__ == '__main__':
    sushe = '2-34-319' #2表示花津校区，34表示宿舍楼号，319表示宿舍号
    result = feiyong(sushe)
    print(sushe, ':', result)