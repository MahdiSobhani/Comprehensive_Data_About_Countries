import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('D:\My\Project\international-migration-December-2022.csv')

x.rename(columns={'country_of_residence':'From','standard_error':'P_Error','year_month':'Year'},inplace=True)
x["estimate"].fillna(0 , inplace=True)

class Data_Migration:

    def Migratory_Each_Contry():

        Total={}                                    
        for i in x.index:
            Total[x['From'].loc[i]] = Total.get(x['From'].loc[i] , x['estimate'].loc[i]) + x['estimate'].loc[i]

        Total_Sort=[]
        for k,v in Total.items():
            Total_Sort.append((v,k))

        print(3 * '\n')
        print('                            ____The Statistics Of Migration 250 Contries____')
        print(100*'_')

        X=1
        Total_Sort = sorted(Total_Sort,reverse=True)
        for i in Total_Sort:
            print(f'{X}){i[1]} = {int(i[0])}')
            X +=1
        print(50*'_')


    def Migration_Types():

        Provisional,Evermore=0,0
        for i in x.index:

            if x['status'].loc[i] == 'Final':
                Evermore +=x['estimate'].loc[i]

            elif x['status'].loc[i] == 'Provisional':
                Provisional +=x['estimate'].loc[i]

        print('Population  :',int(Provisional + Evermore))
        print('Evermore    :',int(Evermore))
        print('Provisional :',int(Provisional))

        P_Evermore = (Evermore / (Provisional + Evermore)) * 100
        print('%.2f'%P_Evermore,'% Is Evermore')

        P_Provisional = (Provisional / (Provisional + Evermore)) * 100             
        print('%.2f'%P_Provisional,' % Is Provisional')


    def Migration_Basement_Years():

        z,t=[],[]                                               
        for i in x.index:
            z.append(x['Year'].loc[i])

        for i in z:
            t.append(int(i[:4]))

        x['Year'] = t 

        a,b,c,d,e,f,g=0,0,0,0,0,0,0
        for i in x.index:

            if x['Year'].loc[i] <= 2003:
                a += int(x['estimate'].loc[i])

            elif  2003 < x['Year'].loc[i] <= 2006:
                b += int(x['estimate'].loc[i])

            elif 2006 < x['Year'].loc[i] <= 2009:
                c += int(x['estimate'].loc[i])

            elif 2009 < x['Year'].loc[i] <= 2012:
                d += int(x['estimate'].loc[i]) 

            elif 2012 < x['Year'].loc[i] <= 2015:
                e += int(x['estimate'].loc[i])

            elif 2015 < x['Year'].loc[i] <= 2018:
                f += int(x['estimate'].loc[i])

            elif 2018 < x['Year'].loc[i]:
                g += int(x['estimate'].loc[i])

        Z = a + b + c + d + e + f + g
        plt.style.use('Solarize_Light2')
        me = [a,b,c,d,e,f,g]                  
        option = [2003,2006,2009,2012,2015,2018,2021]

        plt.pie(me ,labels=option , colors=['g','y','b','r','orange','c','hotpink'],autopct='%1.1f%%')

        plt.title('The Statistics Of Migration Base On Year\n')
        plt.legend(title='____info____')   
                                                                                            
        plt.show()

Data_Migration.Migratory_Each_Contry()
Data_Migration.Migration_Types()
Data_Migration.Migration_Basement_Years()
