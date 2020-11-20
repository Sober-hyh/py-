'''
   @简易计算器
   @2020/11/10
   @BY：第三组
   @实现四则运算以及部分单位运算，平均值运算并且输出式子
'''

#  程序开始

#定义程序所需列表
result = []
result1 = []
result2 = []
result3 = []
result4 = []
pinjun = []
pinjun1 = []
list6 = []

#程序所需的自定义函数
def jia(i, j):
    c = str(i) + '+' + str(j) + '=' + str(i + j)
    p = i + j
    c = str(i) + '+' + str(j) + '=' + str(round(p, 2))
    return c

def jian(i, j):
    c = str(i) + '-' + str(j) + '=' + str(i - j)
    p = i - j
    c = str(i) + '-' + str(j) + '=' + str(round(p, 2))
    return c

def cheng(i, j):
    c = str(i) + '×' + str(j) + '=' + str(i * j)
    p = i * j
    c = str(i) + '×' + str(j) + '=' + str(round(p, 2))
    return c

def chu(i, j):
    c = str(i) + '÷' + str(j) + '=' + str(i / j)
    p = i / j
    c = str(i) + '÷' + str(j) + '=' + str(round(p, 2))
    return c

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def is_number1(s):
    try:
        int(s)
        return True
    except ValueError:
        pass

def cheng500(j):
    o = str(j) + '*' + str(500) + '=' + str(j * 500)
    p = j * 500
    o = str(j) + '*' + str(500) + '=' + str(round(p, 4))
    return o

def cheng1000000(j):
    o = str(j) + '*' + str(1000000) + '=' + str(j * 1000000)
    p = j * 1000000
    o = str(j) + '*' + str(1000000) + '=' + str(round(p, 4))
    return o

def cheng2000(j):
    o = str(j) + '*' + str(2000) + '=' + str(j * 2000)
    p = j * 2000
    o = str(j) + '*' + str(2000) + '=' + str(round(p, 4))
    return o

def cheng2(j):
    o = str(j) + '*' + str(2) + '=' + str(j * 2)
    p = j * 2
    o = str(j) + '*' + str(2) + '=' + str(round(p, 4))
    return o

def cheng10(j):
    o = str(j) + '*' + str(10) + '=' + str(j * 10)
    p = j * 10
    o = str(j) + '*' + str(10) + '=' + str(round(p, 4))
    return o

def cheng100(j):
    o = str(j) + '*' + str(100) + '=' + str(j * 100)
    p = j * 100
    o = str(j) + '*' + str(100) + '=' + str(round(p, 4))
    return o

def cheng1000(j):
    o = str(j) + '*' + str(1000) + '=' + str(j * 1000)
    p = j * 1000
    o = str(j) + '*' + str(1000) + '=' + str(round(p, 4))
    return o

def cheng10000(j):
    o = str(j) + '*' + str(10000) + '=' + str(j * 10000)
    p = j * 10000
    o = str(j) + '*' + str(10000) + '=' + str(round(p, 4))
    return o

def chu2(j):
    o = str(j) + '÷' + str(2) + '=' + str(j / 2)
    p = j / 2
    o = str(j) + '÷' + str(2) + '=' + str(round(p, 4))
    return o

def chu10(j):
    o = str(j) + '÷' + str(10) + '=' + str(j / 10)
    p = j / 10
    o = str(j) + '÷' + str(10) + '=' + str(round(p, 4))
    return o

def chu100(j):
    o = str(j) + '÷' + str(100) + '=' + str(j / 100)
    p = j / 100
    o = str(j) + '÷' + str(100) + '=' + str(round(p, 4))
    return o

def chu1000(j):
    o = str(j) + '÷' + str(1000) + '=' + str(j / 1000)
    p = j / 1000
    o = str(j) + '÷' + str(1000) + '=' + str(round(p, 4))
    return o

def chu10000(j):
    o = str(j) + '÷' + str(10) + '=' + str(j / 10000)
    p = j / 10000
    o = str(j) + '÷' + str(10) + '=' + str(round(p, 6))
    return o

def chu1000000(j):
    o = str(j) + '÷' + str(1000000) + '=' + str(j / 1000000)
    p = j / 1000000
    o = str(j) + '÷' + str(1000000) + '=' + str(round(p, 8))
    return o

def chu500(j):
    o = str(j) + '÷' + str(500) + '=' + str(j / 500)
    p = j / 500
    o = str(j) + '÷' + str(500) + '=' + str(round(p, 5))
    return o

def chu2000(j):
    o = str(j) + '÷' + str(2000) + '=' + str(j / 2000)
    p = j / 2000
    o = str(j) + '÷' + str(2000) + '=' + str(round(p, 6))
    return o

import os
#新建历史记录txt文本
lishi = "C:"
lishi1 = lishi + '历史记录' + '.txt'

print('  欢迎使用第三组制作的计算器')

ci = 0  #初始化计算次数

#主程序开始循环运行
while True:
    print('=========计算器===========')
    print(
        '▍      1.四则计算         ▍\n▍      2.长度换算         ▍\n▍      3.重量换算         ▍\n▍      4.体积换算         ▍\n▍      5.求平均数         ▍\n▍      0.结束程序         ▍\n▍   输入clear清除txt      ▍\n▍  *上一次程序运行记录*     ▍')
    print('=========================')
    h = str(input("请选择:"))
    if h == '1':
        number1 = input('请输入第一个数字:')  # 要求输入第一个数
        if is_number(number1) == True:
            number1 = float(number1)
            number2 = input('请输入第二个数字:')  # 要求输入第二个数
            if is_number(number2) == True:
                number2 = float(number2)
                print("选择你的运算方法（保留两位）："), print("+  1、相加"), print("-  2、相减"), print("×  3、相乘"), print("÷  4、相除"), print(
                    "   0、主菜单")
                method = input('请输入：')  # 要求输入运算方法1-4（加减乘除）
                # 根据输入的运算方法计算并输出结果
                if method == '1':
                    b = jia(number1, number2)
                    print(b)
                    print('算好啦！\n')
                elif method == '2':
                    b = jian(number1, number2)
                    print(b)
                    print('算好啦！\n')
                elif method == '3':
                    b = cheng(number1, number2)
                    print(b)
                    print('算好啦！\n')
                elif method == '4':
                    if number2 == 0:
                        print("除数不能为0！\n")
                        b = ("除数为0的错误计算")
                        ci += 1
                        result.append(b)
                        continue
                    else:
                        b = chu(number1, number2)
                        print(b)
                        print('算好啦！\n')
                elif method == '0':
                    print("返回主菜单\n")

                else:
                    print('输入错误，返回主菜单，请重新输入\n')
                    continue
                ci += 1
                result.append(b)  # 将式子存入列表
            else:
                print('输入错误，请输入数字类型\n')
                continue
        else:
            print('输入错误，请输入数字类型\n')
            continue
    elif h == '0':
        if ci == 0:
            #没有计算输出提示语后退出程序
            print("你一次都没有算过哦！没有式子输出\n感谢使用！程序结束！\n")
            exit(0)
        else:
            #输出次数和式子
            print("您一共运算了 " + str(ci) + " 次\n已统计所有式子：")
            k = -1
            l = -1
            m = -1
            n = -1
            v = -1
            #通过比较判断列表是否存在式子并输出
            if k + 1 < len(result):
                print('\n四则运算：')
                while k + 1 < len(result):
                    ls = result[k]
                    #将式子写入历史记录文本
                    ls1 = open('历史记录.txt', 'a', encoding='utf8')
                    ls1.write('四则运算' + str(ls) + "\n")
                    print(ls)
                    k += 1
            if l + 1 < len(result1):
                print('\n长度换算:')
                while l + 1 < len(result1):
                    print(result1[l])
                    ls1 = open('历史记录.txt', 'a', encoding='utf8')
                    ls1.write('长度换算--' + result1[l] + "\n")
                    l += 1
            if m + 1 < len(result2):
                print('\n重量换算:')
                while m + 1 < len(result2):
                    print(result2[m])
                    ls1 = open('历史记录.txt', 'a', encoding='utf8')
                    ls1.write('重量换算--' + result2[m] + "\n")
                    m += 1
            if n + 1 < len(result3):
                print('\n体积换算:')
                while n + 1 < len(result3):
                    print(result3[n])
                    ls1 = open('历史记录.txt', 'a', encoding='utf8')
                    ls1.write('体积换算--' + result3[n] + "\n")
                    n += 1
            if v + 1 < len(list6):
                print('\n平均数计算:')
                while v + 1 < len(list6):
                    print(list6[v])
                    ls1 = open('历史记录.txt', 'a', encoding='utf8')
                    ls1.write('求平均数--' + list6[v] + "\n")
                    v += 1
            print('\n已将式子写入历史记录.txt')
            print('\n感谢使用！程序结束！\n\n')
            ls1.close()
            exit(0)
    elif h == '2':
        print('请选择当前单位：'), print("1、毫米(mm)"), print("2、厘米(cm)"), print("3、分米(dm)"), print("4、米(m)"), print("5、主菜单")
        list1 = ['1', '2', '3', '4']
        hq1 = str(input('：'))
        if hq1 == '5':
            print('返回主菜单\n')
            continue
        elif hq1 in list1:
            print('请选择换算后单位：')
            print("1、毫米(mm)"), print("2、厘米(cm)"), print("3、分米(dm)"), print("4、米(m)"), print("5、主菜单")
            hh1 = str(input('：'))
            if hh1 == '5':
                print('返回主菜单\n')
                continue
            if hh1 in list1:
                print('请输入换算数字：')
                sz = input('：')
                if is_number(sz) == True and float(sz) > 0:
                    sz = float(sz)
                    if hq1 == '1' and hh1 == '2':
                        jg = chu10(sz)
                        print(jg + '厘米\n')
                        jg = '毫米转换为厘米：' + str(sz) + '毫米' + '÷' + '10' + '=' + str(sz / 10) + '厘米'
                    elif hq1 == '1' and hh1 == '3':
                        jg = chu100(sz)
                        print(jg + '分米\n')
                        jg = '毫米转换为分米：' + str(sz) + '毫米' + '÷' + '100' + '=' + str(sz / 100) + '分米'
                    elif hq1 == '1' and hh1 == '4':
                        jg = chu1000(sz)
                        print(jg + '米\n')
                        jg = '毫米转换为米' + str(sz) + '毫米' + '÷' + '1000' + '=' + str(sz / 1000) + '米'
                    elif hq1 == '2' and hh1 == '1':
                        jg = cheng10(sz)
                        print(jg + '毫米\n')
                        jg = '厘米转换为毫米：' + str(sz) + '毫米' + '×' + '10' + '=' + str(sz * 10) + '毫米'

                    elif hq1 == '2' and hh1 == '3':
                        jg = chu10(sz)
                        print(jg + '分米\n')
                        jg = '厘米转换为分米：' + str(sz) + '厘米' + '÷' + '10' + '=' + str(sz / 10) + '分米'
                    elif hq1 == '2' and hh1 == '4':
                        jg = chu100(sz)
                        print(jg + '米\n')
                        jg = '厘米转换为米：' + str(sz) + '厘米' + '÷' + '100' + '=' + str(sz / 100) + '米'
                    elif hq1 == '3' and hh1 == '1':
                        jg = cheng100(sz)
                        print(jg + '毫米\n')
                        jg = '分米转换为毫米：' + str(sz) + '分米' + '×' + '100' + '=' + str(sz * 100) + '毫米'
                    elif hq1 == '3' and hh1 == '2':
                        jg = cheng10(sz)
                        print(jg + '厘米\n')
                        jg = '分米转换为厘米：' + str(sz) + '分米' + '×' + '10' + '=' + str(sz * 10) + '厘米'
                    elif hq1 == '3' and hh1 == '4':
                        jg = chu10(sz)
                        print(jg + '米\n')
                        jg = '分米转换为米：' + str(sz) + '分米' + '÷' + '10' + '=' + str(sz / 10) + '米'
                    elif hq1 == '4' and hh1 == '1':
                        jg = cheng1000(sz)
                        print(jg + '毫米\n')
                        jg = '米转换为毫米：' + str(sz) + '米' + '*' + '1000' + '=' + str(sz * 1000) + '毫米'
                    elif hq1 == '4' and hh1 == '2':
                        jg = cheng100(sz)
                        print(jg + '厘米\n')
                        jg = '米转换为厘米:' + str(sz) + '米' + '×' + '100' + '=' + str(sz * 100) + '厘米'
                    elif hq1 == '4' and hh1 == '3':
                        jg = cheng10(sz)
                        print(jg + '分米\n')
                        jg = '米转换为分米:' + str(sz) + '米 ' + '×' + '10' + '=' + str(sz * 10) + '分米'
                    elif hq1 == '2' and hh1 == '2':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    elif hq1 == '1' and hh1 == '1':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    elif hq1 == '3' and hh1 == '3':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    elif hq1 == '4' and hh1 == '4':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    else:
                        print('输入错误，返回主菜单！\n')
                        continue
                    ci += 1
                    result1.append(jg)
                else:
                    print('输入错误，请输入整数类型！\n')
                    continue
            else:
                print('输入错误，返回主菜单\n')
                continue
        else:
            print('输入错误，返回主菜单\n')
            continue
    elif h == '3':
        print('请选择当前单位：'), print("1、克(g)"), print("2、千克(kg)"), print("3、吨(t)"), print("4、斤"), print("5、主菜单")
        hq1 = input('：')
        list1 = ['1', '2', '3', '4']
        if hq1 == '5':
            print('返回主菜单\n')
            continue
        elif hq1 in list1:
            print('请选择换算后单位：'), print("1、克(g)"), print("2、千克(kg)"), print("3、吨(t)"), print("4、斤"), print("5、主菜单")
            hh1 = input('：')
            if hh1 == '5':
                print('返回主菜单\n')
                continue
            if hh1 in list1:
                print('请输入换算数字：')
                sz = input('：')
                if is_number(sz) == True and float(sz) > 0:
                    sz = float(sz)
                    if hq1 == '1' and hh1 == '2':
                        jg = chu1000(sz)
                        print(jg + '千克\n')
                        jg = '克转换为千克：' + str(sz) + '克' + '÷' + '1000' + '=' + str(sz / 1000) + '千克'
                    elif hq1 == '1' and hh1 == '3':
                        jg = chu1000000(sz)
                        print(jg + '吨\n')
                        jg = '克转换为千克：' + str(sz) + '克' + '÷' + '100000' + '=' + str(sz / 100000) + '千克'
                    elif hq1 == '1' and hh1 == '4':
                        jg = chu500(sz)
                        print(jg + '斤\n')
                        jg = '克转换为斤：' + str(sz) + '克' + '÷' + '500' + '=' + str(sz / 500) + '斤'
                    elif hq1 == '2' and hh1 == '1':
                        jg = cheng1000(sz)
                        print(jg + '克\n')
                        jg = '千克转换为克：' + str(sz) + '千克' + '×' + '1000' + '=' + str(sz * 1000) + '克'
                    elif hq1 == '2' and hh1 == '3':
                        jg = chu1000(sz)
                        print(jg + '吨\n')
                        jg = '千克转换为吨：' + str(sz) + '千克' + '÷' + '1000' + '=' + str(sz / 1000) + '吨'
                    elif hq1 == '2' and hh1 == '4':
                        jg = cheng2(sz)
                        print(jg + '斤\n')
                        jg = '千克转换为斤：' + str(sz) + '千克' + '×' + '2' + '=' + str(sz * 2) + '斤'
                    elif hq1 == '3' and hh1 == '1':
                        jg = cheng2000(sz)
                        print(jg + '斤\n')
                        jg = '吨转换为斤：' + str(sz) + '吨 ' + '×' + '2000' + '=' + str(sz * 2000) + '斤'
                    elif hq1 == '3' and hh1 == '2':
                        jg = cheng1000(sz)
                        print(jg + '千克\n')
                        jg = '吨转换为千克：' + str(sz) + '吨' + '×' + '1000' + '=' + str(sz * 1000) + '千克'
                    elif hq1 == '3' and hh1 == '1':
                        jp = cheng1000000(sz)
                        print(jg + '克\n')
                        jg = '吨转换为克：' + str(sz) + '吨' + '×' + '1000000' + '=' + str(sz * 1000000) + '克'
                    elif hq1 == '4' and hh1 == '1':
                        jg = cheng500(sz)
                        print(jg + '克\n')
                        jg = '斤转换为克：' + str(sz) + '斤' + '×' + '500' + '=' + str(sz * 500) + '克'
                    elif hq1 == '4' and hh1 == '2':
                        jg = chu2(sz)
                        print(jg + '千克\n')
                        jg = '斤转换为千克：' + str(sz) + '斤' + '÷' + '2' + '=' + str(sz / 2) + '千克'
                    elif hq1 == '4' and hh1 == '3':
                        jg = chu2000(sz)
                        print(jg + '吨\n')
                        jg = '斤转换为吨：' + str(sz) + '斤' + '÷' + '2000' + '=' + str(sz / 2000) + '吨'
                    elif hq1 == '1' and hh1 == '1':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    elif hq1 == '2' and hh1 == '2':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    elif hq1 == '3' and hh1 == '3':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    elif hq1 == '4' and hh1 == '4':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    else:
                        print('输入错误，返回主菜单！\n')
                        continue
                    ci += 1
                    result2.append(jg)
                else:
                    print('输入错误，请输入整数类型！\n')
                    continue
            else:
                print("输入错误，请重新输入！\n")
                continue
        else:
            print("输入错误，请重新输入！\n")
            continue
    elif h == '4':
        print('请选择当前单位：'), print("1、立方厘米(cm³)"), print("2、立方米(m³)"), print("3、升(L)"), print("4、主菜单")
        list2 = ['1', '2', '3']
        hq1 = input('：')
        if hq1 == '4':
            print('返回主菜单\n')
            continue
        elif hq1 in list2:
            print('请选择换算后单位：')
            print('请选择换算前单位：'), print("1、立方厘米(cm³)"), print("2、立方米(m³)"), print("3、升(L)"), print("4、主菜单")
            hh1 = input('：')
            if hh1 == '4':
                print('返回主菜单\n')
                continue
            elif hh1 in list2:
                print('请输入换算数字：\n')
                sz = input('：')
                if is_number(sz) == True and float(sz) > 0:
                    sz = float(sz)
                    if hq1 == '1' and hh1 == '2':
                        jg = chu1000000(sz)
                        print(jg + '立方米\n')
                        jg = '立方厘米转换为立方米：' + str(sz) + '立方厘米' + '÷' + '1000000' + '=' + str(sz / 1000000) + '立方米'
                    elif hq1 == '1' and hh1 == '3':
                        jg = chu1000(sz)
                        print(jg + '升\n')
                        jg = '立方厘米转换为升：' + str(sz) + '立方厘米' + '÷' + '1000' + '=' + str(sz / 1000) + '升'
                    elif hq1 == '2' and hh1 == '1':
                        jg = cheng1000000(sz)
                        print(jg + '立方厘米\n')
                        jg = '立方米转换为立方厘米：' + str(sz) + '立方米' + '×' + '1000000' + '=' + str(sz * 1000000) + '立方厘米'
                    elif hq1 == '2' and hh1 == '3':
                        jg = cheng1000(sz)
                        print(jg + '升\n')
                        jg = '立方米转换为升：' + str(sz) + '立方米' + '×' + '1000' + '=' + str(sz * 1000) + '升'
                    elif hq1 == '3' and hh1 == '1':
                        jg = cheng1000(sz)
                        print(jg + '立方厘米\n')
                        jg = '升转换为立方厘米：' + str(sz) + '升' + '×' + '1000' + '=' + str(sz * 1000) + '立方厘米'
                    elif hq1 == '3' and hh1 == '2':
                        jg = chu1000(sz)
                        print(jg + '立方米\n')
                        jg = '升转换为立方米：' + str(sz) + '升' + '÷' + '1000' + '=' + str(sz / 1000) + '立方米'
                    elif hq1 == '1' and hh1 == '1':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    elif hq1 == '2' and hh1 == '2':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    elif hq1 == '3' and hh1 == '3':
                        print('不支持同单位转换！请重新操作！\n')
                        jg = str('一个同单位转换错误操作')
                    else:
                        print("输入错误，请重新输入！\n")
                        continue
                    ci += 1
                    result2.append(jg)
                else:
                    print('输入错误，请输入正数类型！\n')
                    continue
            else:
                print("输入错误，请重新输入！\n")
                continue
        else:
            print("输入错误，请重新输入！\n")
            continue
    elif h == '5':
        sum = 0
        list3 = []
        n = input('请输入你要求几个数的平均值：')
        r = 0
        zui = zuixiao = zuixiao1= 0
        if is_number1(n) == True:
            n = int(n)
            for i in range(n):
                x = input('请输入一个数字后回车：')
                if is_number(x) == True:
                    r = 1
                    pinjun.append(x)
                    x = float(x)
                    list3.append(x)
                    sum = sum + x
                    zui=max(pinjun)
                    zuixiao=min(pinjun)
                else:
                    print('输入错误，返回主菜单，请输入数字类型！\n')
                    r -= 1
                    break

        else:
            print('请以正整数数字输入次数!\n')
            continue
        if r == 1:
            pj2 = sum / n
            print('总和是：'+str(round(sum,4))+'  平均数是(保留四位)：' + str(round(pj2, 4)))
            print(str(n)+'个数中的最大值是：'+str(zui))
            print(str(n) + '个数中的最小值是：' + str(zuixiao)+'\n')
            ci += 1
            pj1 = str(list3) + '的平均数' + '=' + str(round(pj2, 4))
            list6.append(pj1)
        elif r == 0:
            print('请输入正整数！\n')
            continue
    elif h == 'clear':
        xuanze = input('确定清除历史记录吗？(y/n):')
        if xuanze == 'y' or xuanze == 'Y':
            ls1 = open('历史记录.txt', 'w+', encoding='utf8')
            ls1.truncate()
            ls1.close()
            print('清理完毕!\n')
        elif xuanze == 'n' or xuanze == 'Y':
            print('下次要注意哦！\n返回主菜单')
        else:
            print('选择输入错误,重新来一次吧！\n返回主菜单\n')
            continue
    else:
        print("输入错误，请输入[0-5]区间的数！\n")
        continue
#结束