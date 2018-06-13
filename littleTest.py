import os, openpyxl
os.chdir('D:/Drive/Code/ATBSWP/Chapter_12')
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,11):   # creade some data in column A
    sheet['A'+str(i)] = i

refObj = openpyxl.chart.Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10)
seriesObj = openpyxl.chart.Series(refObj, title='First series')

chartObj = openpyxl.chart.LineChart()
chartObj.title = 'My first Chart'
chartObj.append(seriesObj)

sheet.add_chart(chartObj,'C5')
wb.save('sampleChart.xlsx')