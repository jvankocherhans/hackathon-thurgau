import csv

# öffnet die Datasource und speichert alle Daten in eine DicList ab
with open('./data/DATASOURCE.CSV', newline='') as datasource:
        reader = csv.DictReader(datasource, delimiter=';')
        dics = list(reader)

# nimt die gespeicherten Daten und gibt jeweils die Daten einer Spalte zurück
def getDataList(column):
    
    dataList = []
    
    for dic in dics:
        dataList.append(dic.get(column))
        
    return dataList