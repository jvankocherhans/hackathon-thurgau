import csv

with open('./data/DATASOURCE.CSV', newline='') as datasource:
        reader = csv.DictReader(datasource, delimiter=';')
        dics = list(reader)

def getDataList(column):
    
    dataList = []
    
    for dic in dics:
        dataList.append(dic.get(column))
        
    return dataList

