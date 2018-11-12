# -*- coding: utf-8 -*-
import xlrd
import xlwt

#读取task表中第2列任务描述，循环输出所有内容
def exceltask():
    book=xlrd.open_workbook("./testcase.xlsx")  #打开excel表
    #print book.sheet_names()    #输出表的所有sheet名称
    sh=book.sheet_by_index(0)    #读取第一个sheet的信息
    rows=sh.nrows           #所有行
    cols=sh.ncols          #所有列
    for r in range(1,rows):   #循环输出低从第2行开始，所有内容
            print sh.cell_value(r,0)
            print sh.cell_value(r,1)
            print sh.cell_value(r,2)
            print sh.cell_value(r, 3)
            print sh.cell_value(r, 4)
            print sh.cell_value(r, 5)

exceltask()