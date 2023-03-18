import csv

# öffnet die Datasource und speichert alle Daten in eine DicList ab
with open('./data/ogd_minergie_tg_20230308.csv', newline='') as datasource:
        reader_minenergie = csv.DictReader(datasource, delimiter=';')
        dics_imenergie = list(reader_minenergie)

# nimt die gespeicherten Daten und gibt jeweils die Daten einer Spalte zurück
def getDataListMinenergie(column):
    
    dataList = []
    
    for dic_imenergie in dics_imenergie:
        dataList.append(dic_imenergie.get(column))
        
    return dataList

with open('./data/solarenergiepotential_tg_gemeinden.csv', newline='') as datasource:
        reader_solar = csv.DictReader(datasource, delimiter=';')
        dics_solar = list(reader_solar)

def getDataListSolar(column):
    
    dataList = []
    
    for dic_solar in dics_solar:
        dataList.append(dic_solar.get(column))
        
    return dataList