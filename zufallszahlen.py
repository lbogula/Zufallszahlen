# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 21:47:14 2022

@author: Laura
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("Zufallszahlengenerator")

st.header("Eingabe der Zahlen")

Summe = st.slider("Gesamtsumme",1,100)
st.write("Gesamtsumme =", Summe)

Anzahl = st.slider("Anzahl Verkäufe",1,100)
st.write("Anzahl Verkäufe =", Anzahl)

Varianz = st.slider("Varianz",0.1,5.)
st.write("Varianz =", Varianz)


# SelectBox
#occupation = st.selectbox("Bitte wählen", ["Mittelwert manuell eingeben","Mittelwert berechnen"])
#st.write("You selected this option:", occupation)

#if st.button("Mittelwert manuell eingeben"):
#    Mittelwert = st.text_input("Enter name please","")
    

#else:
Mittelwert = Summe/Anzahl
    
    
st.write("Mittelwert=", Mittelwert)
if Mittelwert > 10:
    st.warning("Mittelwert ist sehr groß! Bitte prüfe die Eingaben")
    
#Summe = 700
#Anzahl = 100
#Mittelwert = 7



st.write("Mittelwert = %.1f €, Varianz = %.1f € " %(Mittelwert,Varianz))


#########################################################################

st.subheader("Visualisierung: So sieht die gewählte Verteilung aus (bei großer Stichprobe)")
#Erstellen der Zufallsdaten zum Testen der Verteilung
Stichprobengröße = 150000

data = np.random.normal(Mittelwert, Varianz, Stichprobengröße)

#hist_values = np.histogram(data)[0]
#st.bar_chart(hist_values)

fig, ax = plt.subplots()
ax.hist(data,bins=Anzahl)
ax.plot([Mittelwert,Mittelwert], [0, 8000],c='k')

st.pyplot(fig)




# Mit Schleife bis es aufgeht:
def gibZufallszahlen(Summe,Anzahl,Mittelwert,Varianz):
    Fertig = False
    Anzahl_Versuche = 0
    
    while Fertig == False:
        Anzahl_Versuche = Anzahl_Versuche + 1
        x_list = []
        X_sum = 0
        i=0
        while i < (Anzahl-1):
            x = np.round(np.random.normal(Mittelwert,Varianz,1),1)
            if x>2 and x<15:
                X_sum = X_sum + x
                x_list.append(x)
                i = i+1

        last_x = np.round(Summe-X_sum,1)
        print("Summe bis hier = %s, letztes x = %s"%(X_sum,last_x))
        if last_x<2 or last_x>15: 
            print('please repeat')
        else:
            x_list.append(last_x)
        #print(len(x_list))
        
        if len(x_list)==Anzahl:
            x_list_new = [x_list[r][0] for r in range(len(x_list))]
            return x_list_new
            Fertig = True
        if Anzahl_Versuche > 30:
            print("zu viele Versuche")
            Fertig = True



x = gibZufallszahlen(Summe,Anzahl,Mittelwert,Varianz)
st.write(x)

fig2, ax1 = plt.subplots()
ax1.hist(x,bins=Anzahl)
ax1.plot([Mittelwert,Mittelwert], [0, 8],c='k')

st.pyplot(fig2)
