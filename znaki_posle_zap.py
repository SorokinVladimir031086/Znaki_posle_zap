import pandas
import telebot
from openpyxl import Workbook
import numpy as np

list2=[]
list4=[]
list6=[]
r1=[]
r2=[]
fighter1=[]
fighter2=[]
p1=[]
p2=[]
dohod=[]
date = []
time = []
Player1 = []
Player2 = []
totalscore = []
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []
winP1 = []
winP2 = []
F = []
B = []
NoFB = []

excel_data_df = pandas.read_excel('result_mk10_0221.xlsx')
ddf = pandas.DataFrame(excel_data_df)
df=ddf.loc[(ddf['NoFB'] <= 3.5) & (ddf['NoFB'] >= 2) ]
print(df)


for i in df.Player1.unique():
    df1 =df.loc[df['Player1'] == i]
    print(df1)
    for j in df1.Player2.unique():
        df2 = df1.loc[df1['Player2'] == j]
        print(df2)
        list1 = df2['Fatality'].to_list()
        print(list1)

        for list in list1:
            try:
                print(len(str(list).split('.')[1].rstrip('0')))
                list2.append(len(str(list).split('.')[1].rstrip('0')))
            except:
                print(0)
                list2.append(0)
        print(list2)

        list3 = df2['Brutality'].to_list()
        for list in list3:
            try:
                print(len(str(list).split('.')[1].rstrip('0')))
                list4.append(len(str(list).split('.')[1].rstrip('0')))
            except:
                print(0)
                list4.append(0)
        print(list4)

        list5 = df2['NoFB'].to_list()
        for list in list5:
            try:
                print(len(str(list).split('.')[1].rstrip('0')))
                list6.append(len(str(list).split('.')[1].rstrip('0')))
            except:
                print(0)
                list6.append(0)
        print(list6)


        df2['znaki_fat'] = np.array(list2)
        df2['znaki_brut'] = np.array(list4)
        df2['znaki_nofb'] = np.array(list6)
        df3 = df2.loc[(df2['znaki_fat'] == 3) & (df2['znaki_brut'] == 2) & (df2['znaki_nofb'] == 2)]



        print(df3)
        try:
            df3 = df3.loc[df3['Fatality']<df3['Brutality']]
            print(df3)
            for i in df3['Date'].to_list():
                date.append(i)
            for i in df3['Time'].to_list():
                time.append(i)



            for i in df3['Player1'].to_list():
                fighter1.append(i)
            for i in df3['Player2'].to_list():
                fighter2.append(i)
            for i in df3['TotalScore'].to_list():
                totalscore.append(i)
            for i in df3['R1'].to_list():
                r1.append(i)
            for i in df3['R2'].to_list():
                r2.append(i)
            for i in df3['R3'].to_list():
                r3.append(i)
            for i in df3['R4'].to_list():
                r4.append(i)
            for i in df3['R5'].to_list():
                r5.append(i)
            for i in df3['R6'].to_list():
                r6.append(i)
            for i in df3['R7'].to_list():
                r7.append(i)
            for i in df3['R8'].to_list():
                r8.append(i)
            for i in df3['R9'].to_list():
                r9.append(i)


            for i in df3['Fatality'].to_list():
                F.append(i)
            for i in df3['Brutality'].to_list():
                B.append(i)
            for i in df3['NoFB'].to_list():
                NoFB.append(i)







        except:
            print('empty')






        list2.clear()
        list4.clear()
        list6.clear()
        df3['Player1'].to_list().clear()
        df3['Player2'].to_list().clear()
        df3['Date'].to_list().clear()
        df3['Time'].to_list().clear()
        df3['R1'].to_list().clear()
        df3['R2'].to_list().clear()
        df3['Fatality'].to_list().clear()
        df3['Brutality'].to_list().clear()
        df3['NoFB'].to_list().clear()


df = pandas.DataFrame.from_dict(
    {'Date': date, 'Time': time, 'Fighter1': fighter1, 'Fighter2': fighter2, 'TotalScore': totalscore, 'R1': r1, 'R2': r2, 'R3': r3, 'R4': r4, 'R5': r5, 'R6': r6, 'R7': r7, 'R8': r8, 'R9': r9, 'Fatality': F, 'Brutality': B, 'NoFB': NoFB })
df.to_excel('result_zpz.xlsx', header=True, index=False)





