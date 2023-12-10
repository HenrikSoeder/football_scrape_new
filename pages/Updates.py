import streamlit as st
import pandas as pd
import mysql.connector
from getpass import getpass
import numpy as np


st.set_page_config(page_title = "Updates",
                   page_icon = "🔁")

pd.set_option('display.max_colwidth', None)

df = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/neu_alles_übersicht.xlsx")
df_bild = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/neue_bilder_übersicht.xlsx")
df_text = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/neue_texte_übersicht.xlsx")


bilder = list(df_bild["Verein"].values)
texte = list(df_text["Verein"].values)


                                                ########## Website #########


#Auswahl
input = st.sidebar.selectbox("Liga", ["1. Bundesliga", "2. Bundesliga", "3. Bundesliga"])
input_2 = st.sidebar.selectbox("Verein", set(list(df["Verein"][df["Liga"] == input])))

if input_2 == None:
    output = "https://www.imago-images.de/bild/st/0101729064/s.jpg"
    background_image = f'''<style>
    [data-testid="stAppViewContainer"] {{
        background-image: url({output});
        background-size: cover;
    }}

    </style>
    '''
    st.markdown(background_image, unsafe_allow_html = True)
    
    #Titel
    st.markdown(f"<h1 style='font-size: 130px;position:relative; left: 580px;text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>Heute Nichts Neues</h1>", unsafe_allow_html=True)


else: 
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
    st.markdown(f"<h1 style='font-size: 80px;position:relative; left:-100px;text-shadow: 1px 3px 1px rgba(0, 0, 0, 1.0)'>{input_2}</h1>", unsafe_allow_html=True)


    # Content (Überblick)
    #Liga Platzierung
    platzierung = str(df["Platzierung"][df["Verein"] == input_2])
    output = platzierung[4:-36].strip()

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

    st.markdown(html_code.format(image), unsafe_allow_html=True)



    # Seperator 
    st.write("**________________________________________________________________________________________**")

    # Szenen Namen
    verein = str(df["Verein"][df["Verein"] == input_2])
    output_1 = verein[4:-28]


    szene = str(df["Name"][df["Verein"] == input_2])
    output_2 = szene[4:-26]

    st.write(f"<h1 style='font-size: 50px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>{output_2}</h1>", unsafe_allow_html=True)
    # Seperator 
    st.write("**________________________________________________________________________________________**")



    # Aktuelle Bilder




    if input_2 in texte and input_2 in bilder:

        
        bilder_titel = str(df["Bild Titel"][df["Verein"] == input_2])
        output_4 = bilder_titel[4:-32]

        st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Neuste Bilder: </h1>", unsafe_allow_html=True)
        st.write(f"<h1 style='font-size: 21px;'>{output_4}</h1>", unsafe_allow_html=True)


        bilder = str(df["Neuste Bilder"][df["Verein"] == input_2])
        output_5 = bilder[4:-34]
        st.write(f"[Link]({output_5})")


        # Seperator (light)
        st.write("___")


        text_titel = str(df["Text Titel"][df["Verein"] == input_2])
        output_6 = text_titel[4:-32]

        st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Neuster Inhalt: </h1>", unsafe_allow_html=True)
        st.write(f"<h1 style='font-size: 21px;'>{output_6}</h1>", unsafe_allow_html=True)


        text= str(df["Neuster Text"][df["Verein"] == input_2])
        output_7 = text[4:-34]
        st.write(f"[Link]({output_7})")

        # Seperator 
        st.write("**________________________________________________________________________________________**")
    


    elif input_2 in bilder and input_2 not in texte:

        bilder_titel = str(df["Bild Titel"][df["Verein"] == input_2])
        output_4 = bilder_titel[4:-32]

        st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Neuste Bilder: </h1>", unsafe_allow_html=True)
        st.write(f"<h1 style='font-size: 21px;'>{output_4}</h1>", unsafe_allow_html=True)


        bilder = str(df["Neuste Bilder"][df["Verein"] == input_2])
        output_5 = bilder[4:-34]
        st.write(f"[Link]({output_5})")


        # Seperator (light)
        st.write("___")



    # Neuster Text

    elif input_2 in texte and input_2 not in bilder:
        text_titel = str(df["Text Titel"][df["Verein"] == input_2])
        output_6 = text_titel[4:-32]

        st.write(f"<h1 style='font-size: 30px;text-shadow: 1px 1px 1px rgba(0, 0, 0, 1.0)'>Neuster Inhalt: </h1>", unsafe_allow_html=True)
        st.write(f"<h1 style='font-size: 21px;'>{output_6}</h1>", unsafe_allow_html=True)


        text= str(df["Neuster Text"][df["Verein"] == input_2])
        output_7 = text[4:-34]
        st.write(f"[Link]({output_7})")

        # Seperator 
        st.write("**________________________________________________________________________________________**")
    
    
    
    