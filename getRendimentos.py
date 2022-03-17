import csv
import os
from re import sub
from decimal import Decimal

dirfiles = os.listdir()
quotechar = '"'
delimiter = ","
newline ="\n"
nFieldsCSV = 1
dirs = []
for file in dirfiles:
    if os.path.isdir(file): dirs.append(file)
for folder in dirs:
    dirfiles = os.listdir(folder)
    newcsv=''
    totalAcumulado = 0
    for file in dirfiles:
        if(file!="mensal.csv"):
            path = folder+"/"+file
            with open(path, newline='',encoding='utf-8') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                #print(spamreader)

                i=0

                lenCabecalho = 0
                for row in spamreader:
                    j=0
                    for field in row:
                        if j<len(row)-1:
                            #print(', '.join(row))
                            if "R$" in field:
                                field = field.replace("R$","")
                                field = field.strip()
                            newcsv+=quotechar+''.join(field)+quotechar+delimiter
                            j+=1
                        else:
                            if(i!=0):
                                money = field.replace(",",".")
                                value = Decimal(sub(r'[^\d.]', '', money))
                                totalAcumulado+=value
                            else:
                                i+=1
                            if "R$" in field:
                                field = field.replace("R$","")
                                field = field.strip()
                            newcsv+=quotechar+''.join(field)+quotechar+newline
                            lenCabecalho = len(row)
                            j+=1
                
    i=0
    for i in range(0,lenCabecalho):

        if(i==lenCabecalho-1):
            strTemp = str(totalAcumulado)
            strTotalAcumulado = strTemp.replace(".",",")
            newcsv+=quotechar+strTotalAcumulado+quotechar+newline
        elif(i==lenCabecalho-2):
            newcsv+=quotechar+'Total'+quotechar+delimiter
        else:
            newcsv+=quotechar+''+quotechar+delimiter
                # strTemp = str(totalAcumulado)
                # strTotalAcumulado = strTemp.replace(".",",")
                # newcsv+='"Total","'+strTotalAcumulado+'"'
    path2save=folder+"/"+"mensal.csv"
    f = open(path2save,'w', newline='', encoding='utf-8')
    f.write(newcsv)
    print(totalAcumulado)
    f.close()
                