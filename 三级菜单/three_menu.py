#!/urs/bin/env python
# -*- coding:utf-8 -*-

data ={
    '北京':{
         '海淀区':{
             '颐和园', '圆明园遗址公园', '旧土城遗址公园', '大钟寺'
         },
        '东城区':{
            '劳动人民文化宫', '老舍纪念馆', '柳荫公园', '青年湖公园'
        },
        },
    '浙江':{
        '杭州':{
            '西湖', '西溪湿地', '宋城', '钱塘江', '南宋御街',
        },
        '绍兴':{
            '柯岩风景区、大禹陵、东湖、鲁迅故里',
        },
        },
    '山东':{
        '济南':{
            '趵突泉 大明湖 千佛山 芙蓉街(小吃街)',
        },
        '青岛':{
            '栈桥,小鱼山,海底世界,第一海水浴场,八大关风景区, 花石楼',
        },
        },
}

flag = True

while flag:
    for i in data:
        print(i)
    choose1 = input(">")

    if choose1 == "q":
        flag = False

    while flag:
        for j in data[choose1]:
            print("\t", j)

        choose2 = input(">>")
        if choose2 == 'b':
            break
        elif choose2 == 'q':
            flag = False

        while flag:
            for k in data[choose1][choose2]:
                print("\t\t",k)

            choose3 = input(">>>")
            if choose3 == 'b':
                break
            elif choose3 == 'q':
                flag = False