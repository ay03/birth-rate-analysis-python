#FINAL DRAFT
import pandas as pd
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import CHAR
import PySimpleGUI as sg

df=pd.read_excel(r'birthrate.xlsx')
print(df.head(20))

def graph_select():
    print("\n1.  Line Graph")
    print("2.  Bar Graph")
    print("3.  Pie Chart")
    g = int(input("\nPlease choose any one: "))
    return g;

def graph_line(tab,n,xlabel,ylabel):
    if n!=False:
        tab[n].plot(kind='line')
    else:
        tab.plot(kind='line')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def graph_bar(tab,n,xlabel,ylabel):
    if n!=False:
        tab[n].plot(kind='bar')
    else:
        tab.plot(kind='bar')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def graph_pie(tab,n,label,ptitle):
    if n!=False:
        tab[n].plot(kind='pie', y='births')
    else:
        tab.plot(kind='pie', y='births')
    plt.title(ptitle)
    plt.show()

    
def fixed_year_for_state(n,g):
    fyfs = df.pivot_table('births', index='state', columns='year', aggfunc='sum')
    print(fyfs.head())
    if(g==1):
        graph_line(fyfs,n,"States","Total births in the year "+str(n))
    elif(g==2):
        graph_bar(fyfs,n,"States","Total births in the year "+str(n))
    elif(g==3):
        graph_pie(fyfs,n,fyfs.index,"Total births in the year "+str(n))
    
def fixed_year_for_month(n,g):
    fyfm = df.pivot_table('births', index='month', columns='year', aggfunc='sum')
    print(fyfm.head())
    if(g==1):
        graph_line(fyfm,n,"Months","Total births in the year "+str(n))
    elif(g==2):
        graph_bar(fyfm,n,"Months","Total births in the year "+str(n))
    elif(g==3):
        graph_pie(fyfm,n,fyfm.index,"Total births in the year "+str(n))
    
def fixed_year_for_day(n,g):
    fyfd = df.pivot_table('births', index='day', columns='year', aggfunc='sum')
    print(fyfd.head())
    if(g==1):
        graph_line(fyfd,n,"Days","Total births in the year "+str(n))
    elif(g==2):
        graph_bar(fyfd,n,"Days","Total births in the year "+str(n))
    elif(g==3):
        graph_pie(fyfd,n,fyfd.index,"Total births in the year "+str(n))
    
def fixed_year_gender_ratio(n,g): 
    fygr = df.pivot_table('births', index='gender', columns='year', aggfunc='sum')
    print(fygr.head())
    if(g==1):
        fygr = df.pivot_table('births', index='year', columns='gender', aggfunc='sum')
        graph_line(fygr,False,"Gender","Total births in the year "+str(n))
    elif(g==2):
        graph_bar(fygr,n,"Gender","Total births in the year "+str(n))
    elif(g==3):
        graph_pie(fygr,n,fygr.index,"Total births in a year "+str(n))

        

def fixed_loc_for_year(l,g):
    flfy = df.pivot_table('births', index='year', columns='state', aggfunc='sum')
    print(flfy.head())
    if(g==1):
        graph_line(flfy,l,"Years","Total births in the state "+l)
    elif(g==2):
        graph_bar(flfy,l,"Years","Total births in the state "+l)
    elif(g==3):
        graph_pie(flfy,l,flfy.index,"Total births in the year "+l)
    
def fixed_loc_for_month(l,g):
    flfm = df.pivot_table('births', index='month', columns='state', aggfunc='sum')
    print(flfm.head())
    if(g==1):
        graph_line(flfm,l,"Months","Total births in the state "+l)
    elif(g==2):
        graph_bar(flfm,l,"Months","Total births in the state "+l)
    elif(g==3):
        graph_pie(flfm,l,flfm.index,"Total births in the year "+l)
    
def fixed_loc_for_day(l,g):
    flfd = df.pivot_table('births', index='day', columns='state', aggfunc='sum')
    print(flfd.head())
    if(g==1):
        graph_line(flfd,l,"Days","Total births in the state "+l)
    elif(g==2):
        graph_bar(flfd,l,"Days","Total births in the state "+l)
    elif(g==3):
        graph_pie(flfd,l,flfd.index,"Total births in the year "+l)
    
def fixed_loc_gender_ratio(l,g): 
    flgr = df.pivot_table('births', index='gender', columns='state', aggfunc='sum')
    print(flgr.head())
    if(g==1):
        flgr = df.pivot_table('births', index='state', columns='gender', aggfunc='sum')
        graph_line(flgr,False,"Gender","Total births in the year "+l)
    elif(g==2):
        graph_bar(flgr,l,"Gender","Total births in the year "+l)
    elif(g==3):
        graph_pie(flgr,l,flgr.index,"Total births in a year "+l)


def year_wise(g):
    yw = df.pivot_table('births', index='year', aggfunc='sum')
    print(yw.head())
    if(g==1):
        graph_line(yw,False,"Years","Total births")
    elif(g==2): 
        graph_bar(yw,False,"Years","Total births")
    elif(g==3):
        yw = yw.groupby(['year']).sum()
        graph_pie(yw,False,yw.index,"Total births")
    
def month_wise(g):
    mw = df.pivot_table('births', index='month', aggfunc='sum')
    print(mw.head())
    if(g==1):
        graph_line(mw,False,"Months","Total births")
    elif(g==2): 
        graph_bar(mw,False,"Months","Total births")
    elif(g==3):
        mw = mw.groupby(['month']).sum()
        graph_pie(mw,False,mw.index,"Total births")
    
def day_wise(g):
    dw = df.pivot_table('births', index='day', aggfunc='sum')
    print(dw.head())
    if(g==1):
        graph_line(dw,False,"Days","Total births")
    elif(g==2): 
        graph_bar(dw,False,"Days","Total births")
    elif(g==3):
        dw = dw.groupby(['day']).sum()
        graph_pie(dw,False,dw.index,"Total births")

def gender_ratio(g): #line,bar
    gr = df.pivot_table('births', index='gender', aggfunc='sum')
    if(g==1):
        gr = df.pivot_table('births', index='year', columns='gender', aggfunc='sum')
        graph_line(gr,False,"Gender","Total births")
    elif(g==2): 
        graph_bar(gr,False,"Gender","Total births")
    elif(g==3):
        gr = gr.groupby(['gender']).sum()
        graph_pie(gr,False,gr.index,"Total births")
    
def loc_wise(g):
    lw = df.pivot_table('births', index='state', aggfunc='sum')
    print(lw.head())
    if(g==1):
        graph_line(lw,False,"State","Total births")
    elif(g==2): 
        graph_bar(lw,False,"State","Total births")
    elif(g==3):
        lw = lw.groupby(['state']).sum()
        graph_pie(lw,False,lw.index,"Total births")


#main    
print("BIRTH-RATE ANALYSIS USING PYTHON")

while(1):
    print("\n1. FIXED YEAR")
    print("2. FIXED LOCATION")
    print("3. OVERALL")
    print("4. ADD VALUES")
    print("5. EXIT")

    choice1 = int(input("\nPlease choose any one: "))

    if(choice1 == 1):
        print("\n1.  1970 \t11. 1980 \t21. 1990 \t31. 2000")
        print("\n2.  1971 \t12. 1981 \t22. 1991 \t32. 2001")
        print("\n3.  1972 \t13. 1982 \t23. 1992 \t33. 2002")
        print("\n4.  1973 \t14. 1983 \t24. 1993 \t34. 2003")
        print("\n5.  1974 \t15. 1984 \t25. 1994 \t35. 2004")
        print("\n6.  1975 \t16. 1985 \t26. 1995 \t36. 2005")
        print("\n7.  1976 \t17. 1986 \t27. 1996 \t37. 2006")
        print("\n8.  1977 \t18. 1987 \t28. 1997 \t38. 2007")
        print("\n9.  1978 \t19. 1988 \t29. 1998 \t39. 2008")
        print("\n10. 1979 \t20. 1989 \t30. 1999 \t40. 2009")
        choice2 = int(input("\nPlease choose any one: "))
        
        n=1969+choice2
        print("1. State-wise birthrate")
        print("2. Month-wise birthrate")
        print("3. Day-wise birthrate")
        print("4. Year-wise Gender Ratio")
        choice4 = int(input("\nPlease choose any one: "))
        g=graph_select()
        
        if(choice4==1):
            fixed_year_for_state(n,g)
        if(choice4==2):
            fixed_year_for_month(n,g)
        if(choice4==3):
            fixed_year_for_day(n,g)
        if(choice4==4):
            fixed_year_gender_ratio(n,g)


    if(choice1 == 2):
        print("\n1.  Uttar Pradesh")
        print("2.  Maharashtra")
        print("3.  Madhya Pradesh")
        print("4.  West Bengal")
        print("5.  Tamil Nadu")
        choice2 = int(input("\nPlease choose any one: "))
        if(choice2==1):
            l='Uttar Pradesh'
        elif(choice2==2):
            l='Maharashtra'
        elif(choice2==3):
            l='Madhya Pradesh'
        elif(choice2==4):
            l='West Bengal'
        else:
            l='Tamil Nadu'
            
        print("1. Year-wise birthrate")
        print("2. Month-wise birthrate")
        print("3. Day-wise birthrate")
        print("4. State-wise Gender Ratio")
        choice4 = int(input("\nPlease choose any one: "))
        g=graph_select()
        
        if(choice4==1):
            fixed_loc_for_year(l,g)
        if(choice4==2):
            fixed_loc_for_month(l,g)
        if(choice4==3):
            fixed_loc_for_day(l,g)
        if(choice4==4):
            fixed_loc_gender_ratio(l,g)

        
    if(choice1 == 3):
        print("1. Year vs Births")
        print("2. Month vs Births")
        print("3. Days vs Births")
        print("4. Gender Ratio")
        print("5. Maximum to Minimum birth rate (location wise)")
        #print("6. Average Births")
        choice2 = int(input("\nPlease choose any one: "))
        g=graph_select()
        
        if(choice2 == 1):
            year_wise(g)
        if(choice2 == 2):
            month_wise(g)
        if(choice2 == 3):
            day_wise(g)
        if(choice2 == 4):
            gender_ratio(g)
        if(choice2 == 5):
            loc_wise(g)
        '''if(choice2 == 6):
            #avg birth of each year
            df_birth=df.groupby('year')['births'].mean().to_frame().reset_index()
            df_birth.columns=['year','avg_births']
            df_birth.head(25)
            sns.distplot(df_birth['avg_births'])
            plt.show()'''
            
#gui        
    if(choice1 == 4):
        # Add some color to the window
        sg.theme('DarkTeal10')


        EXCEL_FILE = 'birthrate.xlsx'
        df = pd.read_excel(EXCEL_FILE)

        layout = [
            [sg.Text('Please fill out the following fields:')],
            [[sg.Text('Year    '), sg.Combo([1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,
                                    1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,
                                    1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,
                                    2000,2001,2002,2003,2004,2005,2006,2007,2008,2009],key='year')]],
            [sg.Text('Month  '), sg.Combo([1,2,3,4,5,6,7,8,9,10,11,12],key='month')],
            [sg.Text('Gender'), sg.Combo(['M', 'F'], key='gender')],
            [sg.Text('Day     '), sg.Combo([1,2,3,4,5,6,7],key='day')],
            [sg.Text('State   '), sg.Combo(["Uttar Pradesh",
                                    "Maharashtra",
                                    "Madhya Pradesh",
                                    "West Bengal",
                                    "Tamil Nadu"],key='state')],
            [sg.Text('Births  '), sg.Input(key='births')],
    
            [sg.Submit(), sg.Button('Clear'), sg.Exit()]
        ]

        window = sg.Window('BIRTH RATE ANALYSIS INSERTION', layout)

        def clear_input():
            for key in values:
                window[key]('')
            return None


        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Clear':
                clear_input()
            if event == 'Submit':
                new_record = pd.DataFrame((values), index=[0])
                df = pd.concat([df, new_record], ignore_index=True)
                df.to_excel(EXCEL_FILE, index=False)
                sg.popup('Data saved!')
                clear_input()
        
        window.close()

    if(choice1 == 5):
        exit(0)
    
    
