import streamlit as st
import pandas as pd
import time


st.set_page_config(page_title = "Chatbot",
                   page_icon = "🤖")


pd.set_option('display.max_colwidth', None)


            ######### Funktionen ###########

def lower(row):
    return row.lower()




            ########## Dataframes ###########
df = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/fanbereich_übersicht.xlsx")
df_bild_new = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/neue_bilder_übersicht.xlsx")
df_text_new = pd.read_excel("/Users/henriksoeder/Documents/Arbeit/Python/Football_Scrape/Tabellen/neue_texte_übersicht.xlsx")



vereine_alle   = list(df["Verein"])
vereine_texte  = list(df_text_new["Verein"])
vereine_bilder = list(df_bild_new["Verein"])

vereine_alle_stand = [x.lower() for x in vereine_alle]
vereine_texte_stand = [x.lower() for x in vereine_texte]
vereine_bilder_stand = [x.lower() for x in vereine_bilder]

df["Verein"] = df["Verein"].apply(lower)
df_text_new["Verein"] = df_text_new["Verein"].apply(lower)
df_bild_new["Verein"] = df_bild_new["Verein"].apply(lower)



            ############# Bot ##############

                            #### Anleitung
# Initialize Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat history
for message in st.session_state.messages:
    with st.chat_message(name = message["role"], avatar = message["avatar"]):
        st.markdown(message["content"])


# Start

with st.chat_message(name = "assistent", avatar = "⚽️"):
    st.write("Hallo !")
    st.write('Nenne den Namen des Vereins über den du ein Update erhalten möchtest oder "allgemein" für ein allgemeines Update')

if prompt := st.chat_input("Type..."):
    # Display user message in chat message container
    with st.chat_message(name = "Benutzer", avatar = "✏️"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "avatar" : "✏️", "content": prompt})


    if "Allgemein".lower().strip() in prompt.lower().strip() or "update".lower().strip() in prompt.lower().strip():
        response_bild = f"Neue Bilder wurden hochgeladen von: "
        response_text = f"Neue Texte wurden hochgeladen von: "
        
        # Display assistant response in chat message container
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            st.markdown(response_bild)
            if len(vereine_bilder) == 0:
                st.markdown("Niemand")
            else:
                st.markdown(vereine_bilder)
            
            st.markdown(response_text)
            if len(vereine_texte) == 0:
                st.markdown("Niemand")
            else: 
                st.markdown(vereine_texte)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant","avatar" : "⚽️", "content": response_bild})
            st.session_state.messages.append({"role": "assistant","avatar" : "⚽️", "content": vereine_bilder})
            st.session_state.messages.append({"role": "assistant","avatar" : "⚽️", "content": response_text})
            st.session_state.messages.append({"role": "assistant","avatar" : "⚽️", "content": vereine_texte})



    # Neue Texte und neue Bilder
    elif prompt.lower().strip() in vereine_texte_stand and prompt.lower().strip() in vereine_bilder_stand:
        text_titel = df_text_new["Text Titel"][df_text_new["Verein"] == prompt.lower()].values[0]
        bild_titel = df_bild_new["Bild Titel"][df_bild_new["Verein"] == prompt.lower()].values[0]

        # Display assistant response in chat message container
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            response_text = f'{prompt.title()} hat heute einen neuen Text hochgeladen mit dem Titel: "{text_titel}"'
            response_bild = f'{prompt.title()} hat heute auch neue Bilder hochgeladen mit dem Titel: "{bild_titel}"'
            st.markdown(response_text)
            st.markdown(response_bild)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response_text})
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response_bild})

        # Link 
        bild_link = str(df_text_new["Neuste Bilder"][df_text_new["Verein"] == prompt.lower()])[4:-35]
        text_link = str(df_text_new["Neuster Text"][df_text_new["Verein"] == prompt.lower()])[4:-34]
        
        # Display assistant response in chat message container
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            response_bild = f"Hier ist der link zu den Bildern: {bild_link}"
            response_text = f"Und hier ist der link zum Text: {text_link}"
            st.markdown(response_bild)
            st.markdown(response_text)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response_text})
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response_bild})
    
    
    #Nur neue Texte 
    elif prompt.lower().strip() in vereine_texte_stand:
        text_titel = df_text_new["Text Titel"][df_text_new["Verein"] == prompt.lower()].values[0]
        # Display assistant response in chat message container
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            response_text = f'{prompt.title()} hat heute einen neuen Text hochgeladen mit dem Titel: "{text_titel}"'
            st.markdown(response_text)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response_text})
        
        # Link
        text_link = str(df_text_new["Neuster Text"][df_text_new["Verein"] == prompt.lower()])[4:-34]
        
        # Display assistant response in chat message container 
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            response_text = f"Hier ist der link zum Text: {text_link}"
            st.markdown(response_text)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response_text})

    elif prompt.lower().strip() in vereine_bilder_stand:
        bild_titel = df_bild_new["Bild Titel"][df_bild_new["Verein"] == prompt.lower()].values[0]
        # Display assistant response in chat message container
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            response_bild = f'{prompt.title()} hat heute neue Bilder hochgeladen mit dem Titel: "{bild_titel}"'
            st.markdown(response_bild)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response_bild})

        # Link
        bild_link = str(df_bild_new["Neuste Bilder"][df_bild_new["Verein"] == prompt.lower()])[4:-35]
        
        # Display assistant response in chat message container 
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            response_bild = f"Hier ist der link zu den Bildern: {bild_link}"
            st.markdown(response_bild)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response_bild})

    elif prompt.lower().strip() in vereine_alle_stand:
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            response = f"{prompt} hat leider heute nichts neues veröffentlicht"
            st.markdown(response)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response})

    else:
        with st.chat_message(name = "assistent", avatar = "⚽️"):
            response = "Ich habe dich leider nicht richtig verstanden"
            st.markdown(response)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "avatar" : "⚽️","content": response})



    