                                          
import streamlit as st
import pandas as pd
import mysql.connector
from getpass import getpass
import numpy as np
from PIL import Image, ImageFilter
import requests
from io import BytesIO


st.set_page_config(page_title = "Kurven Texte",
                   page_icon = "⚽️")


                                                ############ Homepage #########

#Hintergrundbild 
hintergrund = "https://media.eintracht.de/image/upload/ar_3:2,c_fill,dpr_1.0,f_auto,g_xy_center,q_40,w_1100,x_w_mul_0.50,y_h_mul_0.39/v1687966216/eintracht-frankfurt-deutsche-bank-park-nordwestkurve-umbau-austausch-sitzschalen-schwarz-05-71ff.jpg"
#hintergrund = "/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/homepage.webp"
output = hintergrund
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
titel = "Kurven Texte"
html_code = f"""
<h1 style='font-size: 120px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{titel}</h1>
"""
st.markdown(html_code, unsafe_allow_html=True)

                                            ############### Deutsch ####################
#InfoText
#text = """"Kurven Texte" ist eine in 2023 erstelle Seite die es sich zur Aufgabe gemacht hat die Beiträge der Fußballszenen in Deutschland gesammelt an einem Ort zugänglich zu machen.
#"""
#html_code = f"""
#<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>
#"""
#st.markdown(html_code, unsafe_allow_html=True)

#text = """Hierbei wird allerdings lediglich auf die Beiträge und Websiten der jeweilligen Gruppen selbst verwiesen und keine Fotos, Texte ö.ä. selbst hochgeladen. 
#"""

#html_code = f"""
#<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

#"""
#st.markdown(html_code, unsafe_allow_html=True)

text = """"Kurven Texte" soll eine Alternative zu sämtlichen dubiosen Kanälen sein, die nur aus Eigeninteresse handeln und sich aus Profitgier dem Text- und Bildmaterial der deutschen Kurven bedienen.
"""

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
#st.markdown(html_code, unsafe_allow_html=True)

text = """Ebenso wird es hier keine Kommentar Spalte geben, welche für die Verbreitung von menschenfeindliche Äußerungen oder Halbwahrheiten missbraucht wird. 
"""

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
#st.markdown(html_code, unsafe_allow_html=True)




#st.write("")
text = """ 
Im Abschnitt "Inhalte" finden sich Information über (fast) jeden Club der ersten drei Ligen und sein Kurve. """

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
#st.markdown(html_code, unsafe_allow_html=True)

text = """  
Der Abschnitt "Updates" beinhaltet nur die neu hochgeladenen Beiträge und wird täglich aktualisiert """

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
#st.markdown(html_code, unsafe_allow_html=True)

text = """ 
Der Abschnitt "Chatbot" ermöglicht schnelleren und gezielteren Zugriff auf die Informationen im Abschnitt "Updates" """

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
#st.markdown(html_code, unsafe_allow_html=True)



                                ################# Englisch ##################
#InfoText
text = """"Kurven Texte" is Website created 2023, where you can find information about most of the german football clubs and their fans.
"""

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
st.markdown(html_code, unsafe_allow_html=True)

text = """However, reference is only made to the contributions and websites of the respective groups themselves and no photos, texts, etc. uploaded diretcly on the Website. 
"""

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
st.markdown(html_code, unsafe_allow_html=True)

st.write("")
text = """ 
In the “Contents” section you will find information about (almost) every club in the first three leagues and their fans. """

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
st.markdown(html_code, unsafe_allow_html=True)

text = """  
The Updates section only includes newly uploaded posts and is updated daily"""

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
st.markdown(html_code, unsafe_allow_html=True)

text = """ 
The Chatbot section provides faster and more targeted access to the information in the "Updates" section"""

html_code = f"""
<h1 style='font-size: 26px;position:relative; left: 50px; top: 0; text-shadow: 6px 6px 6px rgba(0, 0, 0, 1.5);'>{text}</h1>

"""
st.markdown(html_code, unsafe_allow_html=True)









