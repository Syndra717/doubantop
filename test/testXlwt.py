# *-* coding = utf-8 *-*
# @Time : 2020/7/23 上午1:13
# @Author : 杨欣
# @File : testXlwt.py
# @Software : PyCharm
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("sheet1")
row = 1
while row <= 9:
    col = 1
    while col <= row:
        worksheet.write(row-1, col-1, "%d * %d = %d" % (col, row, col * row))
        col += 1
    print("")
    row += 1
workbook.save("chegnfabiao.xls")
