# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:56:29 2020

@author: Mrs_Youssef
"""

import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('C:/Users/Mrs_Youssef/Desktop/SII INTERNSHIP/week2/csv/pone.0125795.s003.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('C:/Users/Mrs_Youssef/Desktop/SII INTERNSHIP/week2/csv/your_csv_file.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()

