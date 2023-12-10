import streamlit as st
import pandas as pd
import mysql.connector
from getpass import getpass
import numpy as np

st.set_page_config(page_title = "Inhalte",
                   page_icon = "📒")

pd.set_option('display.max_colwidth', None)

df = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/fanbereich_übersicht.xlsx")

#establishing a connection to a database
password = "Flottbek43a"

#Setting the database fix
cnx = mysql.connector.connect(user = "root",
                             password = password,
                             host = "localhost",
                             database = "sakila")
cnx.is_connected()
cursor = cnx.cursor()
query = (""" USE Bundesliga;""")
cursor.execute(query)

                                                ########## Website #########

# Sidebar
#st.sidebar.title("Auswahl")

#Auswahl
input = st.sidebar.selectbox("Liga", ["1. Bundesliga", "2. Bundesliga", "3. Bundesliga"])
input_2 = st.sidebar.selectbox("Verein", list(df["Verein"][df["Liga"] == input]))


#Auswahl ohne sidebar
#input = col1.selectbox("Liga", set(list(df["Liga"])))
#input_2 = col1.selectbox("Verein", list(df["Verein"][df["Liga"] == input]))


#Hindergrund und Titel
hintergund = str(df["Hintergrundbild"][df["Verein"] == input_2])
output = hintergund[4:-37]
background_image = f'''<style>
[data-testid="stAppViewContainer"] {{
    background-image: url({output});
    background-size: cover;
}}

</style>
'''

#Hintergrundbild
st.markdown(background_image, unsafe_allow_html = True)

#Titel
st.markdown(f"<h1 style='font-size: 80px;position:relative; left:-100px;text-shadow: 1px 3px 1px rgba(0, 0, 0, 1.0);'>{input_2}</h1>", unsafe_allow_html=True)


# Content (Überblick)
#Liga Platzierung
platzierung = str(df["Platzierung"][df["Verein"] == input_2])
output = platzierung[4:-32].strip()

liga = str(df["Liga"][df["Verein"] == input_2])
output_liga = liga[4:-25].strip()
st.markdown(f"<h1 style='font-size: 35px; position:relative; left:-50px;top: -20px;'>{output_liga}, {output}. Platz</h1>", unsafe_allow_html=True)



# Bild (Logo)
logo = str(df["Logo"][df["Verein"] == input_2])
output = logo[4:-26]
image = output
html_code = '''
<div style="position: fixed; left: 1150px; top: 100px;">
    <img src="{}" alt="Bild" width="250">
</div>
'''

link = str(df["Vereinsseite"][df["Verein"] == input_2])[4:-34]

#st.markdown([html_code.format(image)](link), unsafe_allow_html=True)
st.markdown(html_code.format(image), unsafe_allow_html=True)



# Seperator 
st.write("**________________________________________________________________________________________**")


#Content (Fanbereich)
#st.write(f"<h1 style='font-size: 60px;'>Fanbereich</h1>", unsafe_allow_html=True)

# Namen
verein = str(df["Verein"][df["Verein"] == input_2])
output_1 = verein[4:-28]


szene = str(df["Name"][df["Verein"] == input_2])
output_2 = szene[4:-26]

st.write(f"<h1 style='font-size: 50px;'>{output_2}</h1>", unsafe_allow_html=True)
# Seperator 
st.write("**________________________________________________________________________________________**")

# Website
website = str(df["Fanseite"][df["Verein"] == input_2])
output_3 = website[4:-29]

st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Website: </h1>", unsafe_allow_html=True)
st.write(f"[Link]({output_3})")


# Seperator 
st.write("________________________________________________________________________________________")


# Aktuelle Bilder
bilder_titel = str(df["Bild Titel"][df["Verein"] == input_2])
output_4 = bilder_titel[4:-32]

st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Letzte Bilder: </h1>", unsafe_allow_html=True)
st.write(f"<h1 style='font-size: 21px;'>{output_4}</h1>", unsafe_allow_html=True)


bilder = str(df["Neuste Bilder"][df["Verein"] == input_2])
output_5 = bilder[4:-34]
st.write(f"[Link]({output_5})")


# Seperator (light)
st.write("___")



# Neuster Text
text_titel = str(df["Text Titel"][df["Verein"] == input_2])
output_6 = text_titel[4:-32]

st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Letzter Inhalt: </h1>", unsafe_allow_html=True)
st.write(f"<h1 style='font-size: 21px;'>{output_6}</h1>", unsafe_allow_html=True)


text= str(df["Neuster Text"][df["Verein"] == input_2])
output_7 = text[4:-34]
st.write(f"[Link]({output_7})")

# Seperator 
st.write("**________________________________________________________________________________________**")


#Content (Statistiken)
st.write(f"<h1 style='font-size: 50px;'>Statistiken</h1>", unsafe_allow_html=True)


# Seperator 
st.write("**________________________________________________________________________________________**")


# Gründungsjahr
gründungsjahr= df["Gründungsjahr"][df["Verein"] == input_2].values[0]
output = str(gründungsjahr)
st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Gründungsjahr:</h1>", unsafe_allow_html=True)
st.write(f"<h1 style='font-size: 26px;'>{output}</h1>", unsafe_allow_html=True)

# Seperator (light)
st.write("___")

# Mitglieder
mitglieder = df["Mitgliederzahl"][df["Verein"] == input_2].values[0]
output = str(mitglieder)
st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Mitglieder:</h1>", unsafe_allow_html=True)
st.write(f"<h1 style='font-size: 26px;'>{output}00</h1>", unsafe_allow_html=True)

# Seperator (light)
st.write("___")

# Zuschauer pro Spiel

df_2 = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/zuschauer_infos.xlsx")
df_3 = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/zuschauer_infos_3.xlsx")

if input == "3. Bundesliga":
    zuschauer = df_3["Zuschauerschnitt"][df_3["Verein"] == input_2].values[0]
    output = str(zuschauer)[0:-2]
    st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Zuschauerschnitt</h1>", unsafe_allow_html=True)
    st.write(f"<h1 style='font-size: 26px;'>{output}00</h1>", unsafe_allow_html=True)

else:
    zuschauer = df_2["Zuschauerschnitt"][df_2["Verein"] == input_2].values[0]
    output = str(zuschauer)[0:-2]
    st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Zuschauerschnitt</h1>", unsafe_allow_html=True)
    st.write(f"<h1 style='font-size: 26px;'>{output}00</h1>", unsafe_allow_html=True)


# Seperator (light)
st.write("___")


query = (f"""Select avg(goals_total) as average_goals
        from bundesliga_database
        where home_team_name = "{str(input_2)}" or away_team_name = "{str(input_2)}" ;""")
cursor.execute(query)
results = cursor.fetchall()
output = str(results)[11:-7]

st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Tore pro Spiel:</h1>", unsafe_allow_html=True)
st.write(f"<h1 style='font-size: 26px;'>{output}</h1>", unsafe_allow_html=True)

# Seperator 
st.write("**________________________________________________________________________________________**")


tickets = str(df["Ticketing"][df["Verein"] == input_2])[4:-31]
output = tickets
st.link_button("🎟️ Tickets", output)


