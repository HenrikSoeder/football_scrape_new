import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title = "Daten",
                   page_icon = "📊")


df = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/fanbereich_übersicht.xlsx")
pd.set_option('display.max_colwidth', None)
st.set_option('deprecation.showPyplotGlobalUse', False)



df_daten = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/neu_alles_datum.xlsx")
df_daten.drop("Unnamed: 0.3", axis = 1, inplace = True)
df_daten.drop("Unnamed: 0.2", axis = 1, inplace = True)
df_daten.drop("Unnamed: 0.1", axis = 1, inplace = True)
df_daten.drop("Unnamed: 0", axis = 1, inplace = True)

df_daten["Monat"] = df_daten['Datum'].dt.month
df_daten["Year"] = df_daten['Datum'].dt.year



#Titel
titel = "Daten"
html_code = f"""
<h1 style='font-size: 120px;position:relative; left: 0px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{titel}</h1>
"""
st.markdown(html_code, unsafe_allow_html=True)




tab1, tab2, tab3 = st.tabs(["Monthly", "H2H", "Leagues"])

with tab1:
    col_1, col_2 = st.columns([3,1])
    
    col_1.header("Posts per month")

    
    input = col_2.selectbox("Liga", ["1. Bundesliga", "2. Bundesliga", "3. Bundesliga"])
    input_2 = col_2.selectbox("Verein", list(df["Verein"][df["Liga"] == input]))

    df_line_graph = df_daten[df_daten["Verein"] == input_2].groupby(["Year", "Monat","Verein"]).agg({"Name" : "count"})

    df_line_graph.rename(columns = {"Name" : "Anzahl"}, inplace = True)
    df_line_graph.reset_index(inplace = True)

    x = df_line_graph["Monat"]
    y = df_line_graph["Anzahl"]

    max_ = df_line_graph["Anzahl"].max()

    plt.plot(x,y, linewidth=2, color='black')

    plt.xlabel('Month', fontsize = 12)
    plt.ylabel('Posts', fontsize = 12)
    #plt.title('Posts per month', fontsize = 18)


    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # Obere Achsenlinie entfernen
    ax.spines['right'].set_visible(False)  # Rechte Achsenlinie entfernen
    ax.spines['bottom'].set_visible(True)  # Untere Achsenlinie beibehalten
    ax.spines['left'].set_visible(True)

    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mrz', 'Apr', 'Mai', "Jun", "Jul", "Aug", "Sept", "Okt", "Nov", "Dez"])
    plt.yticks(range(0,max_+2))

    col_1.pyplot()


    logo = str(df["Logo"][df["Verein"] == input_2])
    output = logo[4:-26]
    image = output
    html_code = '''
    <div style="position: relative; left: 0px; top: 00px;">
        <img src="{}" alt="Bild" width="150">
    </div>
    '''

    link = str(df["Vereinsseite"][df["Verein"] == input_2])[4:-34]

    #st.markdown([html_code.format(image)](link), unsafe_allow_html=True)
    col_2.markdown(html_code.format(image), unsafe_allow_html=True)






with tab2:
    st.header("Head to Head comparison")

    col_3, col_4 = st.columns([3,1])



    input = col_4.selectbox("League", ["1. Bundesliga", "2. Bundesliga", "3. Bundesliga"])
    input_2 = col_4.selectbox("Club", list(df["Verein"][df["Liga"] == input]))
    input_5 = col_4.selectbox("Second League", ["1. Bundesliga", "2. Bundesliga", "3. Bundesliga"])
    input_3 = col_4.selectbox("Second Club", list(df["Verein"][df["Liga"] == input_5]))





    df_h2h = df_daten[(df_daten["Verein"] == input_2)|(df_daten["Verein"] == input_3)].groupby(["Verein"]).agg({"Name" : "count"})
    df_h2h.rename(columns = {"Name" : "Anzahl"}, inplace = True)
    df_h2h.reset_index(inplace = True)




    club_a = df_h2h["Anzahl"][df_h2h["Verein"] == input_2].values[0]
    club_b = df_h2h["Anzahl"][df_h2h["Verein"] == input_3].values[0]
    categories = ['Club']


    


    # Breite der Balken
    bar_width = 0.3

    # Indizes für die x-Positionen der Balken
    index = range(len(categories))

    # Bar-Charts nebeneinander erstellen
    plt.bar(index, club_a, width=bar_width, label=input_2, color = "#222A35")
    plt.bar([i + bar_width+ 0.1 for i in index], club_b, width=bar_width, label=input_3, color = "#AFABAB")

    # Kategorien auf der x-Achse setzen
    plt.xticks([i + bar_width/2 for i in index], categories)

    # Achsentitel hinzufügen

    plt.ylabel('Total Posts', fontsize = 14)




    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # Obere Achsenlinie entfernen
    ax.spines['right'].set_visible(False)  # Rechte Achsenlinie entfernen
    ax.spines['bottom'].set_visible(True)  # Untere Achsenlinie beibehalten
    ax.spines['left'].set_visible(True)

    # Legende anzeigen
    #plt.legend()

    # Diagramm anzeigen
    
    
    col_3.pyplot()
   


    logo = str(df["Logo"][df["Verein"] == input_2])
    output = logo[4:-26]
    image = output
    html_code = '''
    <div style="position: relative; left: 80px; top: 00px;">
        <img src="{}" alt="Bild" width="150">
    </div>
    '''

    link = str(df["Vereinsseite"][df["Verein"] == input_2])[4:-34]

    #st.markdown([html_code.format(image)](link), unsafe_allow_html=True)
    col_3.markdown(html_code.format(image), unsafe_allow_html=True)

    logo_2 = str(df["Logo"][df["Verein"] == input_3])
    output = logo_2[4:-26]
    image = output
    html_code = '''
    <div style="position: relative; left: 340px; top: -112px;">
        <img src="{}" alt="Bild" width="150">
    </div>
    '''

    link = str(df["Vereinsseite"][df["Verein"] == input_3])[4:-34]

    #st.markdown([html_code.format(image)](link), unsafe_allow_html=True)
    col_3.markdown(html_code.format(image), unsafe_allow_html=True)




with tab3:
    st.header("Uploads per League")



    df1 = df_daten[df_daten["Liga"]=="1. Bundesliga"]
    df1_g = df1.groupby(["Verein", "Monat"]).agg({"Name":"count"}).reset_index()

    my_dict = {}

    for val in df1_g["Monat"].values:
        x = df1_g[df1_g["Monat"]==val]["Name"].mean()
        my_dict[val] = x
        
    l = pd.DataFrame.from_dict(my_dict, orient="index", columns = ["avg_att"]).reset_index()
    
    df1_done = pd.merge(left = df1, right=l, left_on= "Monat", right_on = "index")


    # Zweite Liga
    df2 = df_daten[df_daten["Liga"]=="2. Bundesliga"]
    df2_g = df2.groupby(["Verein", "Monat"]).agg({"Name":"count"}).reset_index()

    my_dict = {}

    for val in df2_g["Monat"].values:
        x = df2_g[df2_g["Monat"]==val]["Name"].mean()
        my_dict[val] = x
        
    x = pd.DataFrame.from_dict(my_dict, orient="index", columns = ["avg_att"]).reset_index()
    df2_done = pd.merge(left = df2, right=x, left_on= "Monat", right_on = "index")



    # Dritte Liga
    df3 = df_daten[df_daten["Liga"]=="3. Bundesliga"]
    df3_g = df3.groupby(["Verein", "Monat"]).agg({"Name":"count"}).reset_index()

    my_dict = {}

    for val in df3_g["Monat"].values:
        x = df3_g[df3_g["Monat"]==val]["Name"].mean()
        my_dict[val] = x
        
    j = pd.DataFrame.from_dict(my_dict, orient="index", columns = ["avg_att"]).reset_index()
    df3_done = pd.merge(left = df3, right=j, left_on= "Monat", right_on = "index")

    # Concatinating

    df_done = pd.concat([df1_done, df2_done, df3_done])
    df_average = df_done.groupby(["Liga", "Monat"]).agg({"avg_att":"mean"})

    # Final 
    df_average = df_done.groupby(["Liga", "Monat"]).agg({"avg_att":"mean"})
    df_average.rename(columns = {"avg_att" : "average"}, inplace = True)
    df_average.reset_index(inplace = True)


    x1 = df_average["Monat"][df_average["Liga"] == "1. Bundesliga"]
    x2 = df_average["Monat"][df_average["Liga"] == "2. Bundesliga"]
    x3 = df_average["Monat"][df_average["Liga"] == "3. Bundesliga"]

    y1 = df_average["average"][df_average["Liga"] == "1. Bundesliga"]
    y2 = df_average["average"][df_average["Liga"] == "2. Bundesliga"]
    y3 = df_average["average"][df_average["Liga"] == "3. Bundesliga"]



    plt.plot(x1,y1,linewidth=2, color='#00B0F0',  label = "1. Bundesliga")
    plt.plot(x2,y2 ,linewidth=2, color='#222A35', label = "2. Bundesliga")
    plt.plot(x3,y3,linewidth=2,  color='#AFABAB',label = "3. Liga")

    plt.xlabel('Month', fontsize = 11)
    plt.ylabel('Average', fontsize = 11)
    


    max_ = df_average["average"].max()


    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mrz', 'Apr', 'Mai', "Jun", "Jul", "Aug", "Sept", "Okt", "Nov", "Dez"])
    plt.yticks(range(0,11))

    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # Obere Achsenlinie entfernen
    ax.spines['right'].set_visible(False)  # Rechte Achsenlinie entfernen
    ax.spines['bottom'].set_visible(True)  # Untere Achsenlinie beibehalten
    ax.spines['left'].set_visible(True)


    plt.legend()

    st.pyplot()
    