# FINAL DRAFT: Birth Rate Analysis and Visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

# Load the Excel dataset
df = pd.read_excel('birthrate.xlsx')
print(df.head(20))  # Preview first 20 rows

# Ask user to select the type of graph
def graph_select():
    print("\n1.  Line Graph")
    print("2.  Bar Graph")
    print("3.  Pie Chart")
    return int(input("\nPlease choose any one: "))

# Plot line graph
def graph_line(tab, n, xlabel, ylabel):
    if n is not False:
        tab[n].plot(kind='line')
    else:
        tab.plot(kind='line')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Plot bar graph
def graph_bar(tab, n, xlabel, ylabel):
    if n is not False:
        tab[n].plot(kind='bar')
    else:
        tab.plot(kind='bar')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Plot pie chart
def graph_pie(tab, n, label, ptitle):
    if n is not False:
        tab[n].plot(kind='pie', y='births')
    else:
        tab.plot(kind='pie', y='births')
    plt.title(ptitle)
    plt.show()

# Fixed year analysis - state-wise
def fixed_year_for_state(n, g):
    table = df.pivot_table('births', index='state', columns='year', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, n, "States", f"Total births in the year {n}")
    elif g == 2:
        graph_bar(table, n, "States", f"Total births in the year {n}")
    elif g == 3:
        graph_pie(table, n, table.index, f"Total births in the year {n}")

# Fixed year analysis - month-wise
def fixed_year_for_month(n, g):
    table = df.pivot_table('births', index='month', columns='year', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, n, "Months", f"Total births in the year {n}")
    elif g == 2:
        graph_bar(table, n, "Months", f"Total births in the year {n}")
    elif g == 3:
        graph_pie(table, n, table.index, f"Total births in the year {n}")

# Fixed year analysis - day-wise
def fixed_year_for_day(n, g):
    table = df.pivot_table('births', index='day', columns='year', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, n, "Days", f"Total births in the year {n}")
    elif g == 2:
        graph_bar(table, n, "Days", f"Total births in the year {n}")
    elif g == 3:
        graph_pie(table, n, table.index, f"Total births in the year {n}")

# Fixed year analysis - gender ratio
def fixed_year_gender_ratio(n, g):
    table = df.pivot_table('births', index='gender', columns='year', aggfunc='sum')
    print(table.head())
    if g == 1:
        temp = df.pivot_table('births', index='year', columns='gender', aggfunc='sum')
        graph_line(temp, False, "Gender", f"Total births in the year {n}")
    elif g == 2:
        graph_bar(table, n, "Gender", f"Total births in the year {n}")
    elif g == 3:
        graph_pie(table, n, table.index, f"Total births in a year {n}")

# Fixed location analysis - year-wise
def fixed_loc_for_year(l, g):
    table = df.pivot_table('births', index='year', columns='state', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, l, "Years", f"Total births in the state {l}")
    elif g == 2:
        graph_bar(table, l, "Years", f"Total births in the state {l}")
    elif g == 3:
        graph_pie(table, l, table.index, f"Total births in the state {l}")

# Fixed location analysis - month-wise
def fixed_loc_for_month(l, g):
    table = df.pivot_table('births', index='month', columns='state', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, l, "Months", f"Total births in the state {l}")
    elif g == 2:
        graph_bar(table, l, "Months", f"Total births in the state {l}")
    elif g == 3:
        graph_pie(table, l, table.index, f"Total births in the state {l}")

# Fixed location analysis - day-wise
def fixed_loc_for_day(l, g):
    table = df.pivot_table('births', index='day', columns='state', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, l, "Days", f"Total births in the state {l}")
    elif g == 2:
        graph_bar(table, l, "Days", f"Total births in the state {l}")
    elif g == 3:
        graph_pie(table, l, table.index, f"Total births in the state {l}")

# Fixed location analysis - gender ratio
def fixed_loc_gender_ratio(l, g):
    table = df.pivot_table('births', index='gender', columns='state', aggfunc='sum')
    print(table.head())
    if g == 1:
        temp = df.pivot_table('births', index='state', columns='gender', aggfunc='sum')
        graph_line(temp, False, "Gender", f"Total births in the state {l}")
    elif g == 2:
        graph_bar(table, l, "Gender", f"Total births in the state {l}")
    elif g == 3:
        graph_pie(table, l, table.index, f"Total births in the state {l}")

# Overall year-wise birth trend
def year_wise(g):
    table = df.pivot_table('births', index='year', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, False, "Years", "Total births")
    elif g == 2:
        graph_bar(table, False, "Years", "Total births")
    elif g == 3:
        table = table.groupby(['year']).sum()
        graph_pie(table, False, table.index, "Total births")

# Overall month-wise birth trend
def month_wise(g):
    table = df.pivot_table('births', index='month', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, False, "Months", "Total births")
    elif g == 2:
        graph_bar(table, False, "Months", "Total births")
    elif g == 3:
        table = table.groupby(['month']).sum()
        graph_pie(table, False, table.index, "Total births")

# Overall day-wise birth trend
def day_wise(g):
    table = df.pivot_table('births', index='day', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, False, "Days", "Total births")
    elif g == 2:
        graph_bar(table, False, "Days", "Total births")
    elif g == 3:
        table = table.groupby(['day']).sum()
        graph_pie(table, False, table.index, "Total births")

# Overall gender ratio
def gender_ratio(g):
    table = df.pivot_table('births', index='gender', aggfunc='sum')
    if g == 1:
        temp = df.pivot_table('births', index='year', columns='gender', aggfunc='sum')
        graph_line(temp, False, "Gender", "Total births")
    elif g == 2:
        graph_bar(table, False, "Gender", "Total births")
    elif g == 3:
        table = table.groupby(['gender']).sum()
        graph_pie(table, False, table.index, "Total births")

# Overall location-wise analysis
def loc_wise(g):
    table = df.pivot_table('births', index='state', aggfunc='sum')
    print(table.head())
    if g == 1:
        graph_line(table, False, "State", "Total births")
    elif g == 2:
        graph_bar(table, False, "State", "Total births")
    elif g == 3:
        table = table.groupby(['state']).sum()
        graph_pie(table, False, table.index, "Total births")



# -----------------------------
#  Main Program Interaction
# -----------------------------

print("BIRTH-RATE ANALYSIS USING PYTHON")

while True:
    print("\n1. FIXED YEAR")
    print("2. FIXED LOCATION")
    print("3. OVERALL")
    print("4. ADD VALUES")
    print("5. EXIT")

    choice1 = int(input("\nPlease choose any one: "))

    if choice1 == 1:
        print("\n1.  1970 \t11. 1980 \t21. 1990 \t31. 2000")
        print("2.  1971 \t12. 1981 \t22. 1991 \t32. 2001")
        print("3.  1972 \t13. 1982 \t23. 1992 \t33. 2002")
        print("4.  1973 \t14. 1983 \t24. 1993 \t34. 2003")
        print("5.  1974 \t15. 1984 \t25. 1994 \t35. 2004")
        print("6.  1975 \t16. 1985 \t26. 1995 \t36. 2005")
        print("7.  1976 \t17. 1986 \t27. 1996 \t37. 2006")
        print("8.  1977 \t18. 1987 \t28. 1997 \t38. 2007")
        print("9.  1978 \t19. 1988 \t29. 1998 \t39. 2008")
        print("10. 1979 \t20. 1989 \t30. 1999 \t40. 2009")

        choice2 = int(input("\nPlease choose any one: "))
        n = 1969 + choice2

        print("\n1. State-wise birthrate")
        print("2. Month-wise birthrate")
        print("3. Day-wise birthrate")
        print("4. Year-wise Gender Ratio")

        choice4 = int(input("\nPlease choose any one: "))
        g = graph_select()

        if choice4 == 1:
            fixed_year_for_state(n, g)
        elif choice4 == 2:
            fixed_year_for_month(n, g)
        elif choice4 == 3:
            fixed_year_for_day(n, g)
        elif choice4 == 4:
            fixed_year_gender_ratio(n, g)

    elif choice1 == 2:
        print("\n1.  Uttar Pradesh")
        print("2.  Maharashtra")
        print("3.  Madhya Pradesh")
        print("4.  West Bengal")
        print("5.  Tamil Nadu")

        choice2 = int(input("\nPlease choose any one: "))
        states = {
            1: 'Uttar Pradesh',
            2: 'Maharashtra',
            3: 'Madhya Pradesh',
            4: 'West Bengal',
            5: 'Tamil Nadu'
        }
        l = states.get(choice2, 'Uttar Pradesh')

        print("\n1. Year-wise birthrate")
        print("2. Month-wise birthrate")
        print("3. Day-wise birthrate")
        print("4. State-wise Gender Ratio")

        choice4 = int(input("\nPlease choose any one: "))
        g = graph_select()

        if choice4 == 1:
            fixed_loc_for_year(l, g)
        elif choice4 == 2:
            fixed_loc_for_month(l, g)
        elif choice4 == 3:
            fixed_loc_for_day(l, g)
        elif choice4 == 4:
            fixed_loc_gender_ratio(l, g)

    elif choice1 == 3:
        print("\n1. Year vs Births")
        print("2. Month vs Births")
        print("3. Days vs Births")
        print("4. Gender Ratio")
        print("5. Maximum to Minimum birth rate (location wise)")

        choice2 = int(input("\nPlease choose any one: "))
        g = graph_select()

        if choice2 == 1:
            year_wise(g)
        elif choice2 == 2:
            month_wise(g)
        elif choice2 == 3:
            day_wise(g)
        elif choice2 == 4:
            gender_ratio(g)
        elif choice2 == 5:
            loc_wise(g)

    elif choice1 == 4:
        # -----------------------------
        #  GUI Form for Data Entry
        # -----------------------------
        sg.theme('DarkTeal10')

        EXCEL_FILE = 'birthrate.xlsx'
        df = pd.read_excel(EXCEL_FILE)

        layout = [
            [sg.Text('Please fill out the following fields:')],
            [sg.Text('Year'), sg.Combo(list(range(1970, 2010)), key='year')],
            [sg.Text('Month'), sg.Combo(list(range(1, 13)), key='month')],
            [sg.Text('Day'), sg.Combo(list(range(1, 8)), key='day')],
            [sg.Text('Gender'), sg.Combo(['M', 'F'], key='gender')],
            [sg.Text('State'), sg.Combo(['Uttar Pradesh', 'Maharashtra', 'Madhya Pradesh', 'West Bengal', 'Tamil Nadu'], key='state')],
            [sg.Text('Births'), sg.Input(key='births')],
            [sg.Submit(), sg.Button('Clear'), sg.Exit()]
        ]

        window = sg.Window('BIRTH RATE ANALYSIS - INSERT RECORD', layout)

        def clear_input():
            for key in values:
                window[key]('')
            return None

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'Clear':
                clear_input()
            if event == 'Submit':
                new_record = pd.DataFrame([values])
                df = pd.concat([df, new_record], ignore_index=True)
                df.to_excel(EXCEL_FILE, index=False)
                sg.popup('Data saved successfully!')
                clear_input()

        window.close()

    elif choice1 == 5:
        print("Exiting...")
        break
    
