# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 21:47:14 2022

Gibt Zufallszahlen mit fester, einstellbarer Summe aus. 

@author: Laura
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("Zufallszahlengenerator")

#Number Input, Zahleneingabe:

my_expander_Zahlen = st.expander("Eingabe von Gesamtsumme, \
                                 Mittelwert und Varianz")
with my_expander_Zahlen:
    Summe = st.number_input("Gesamtsumme eingeben",100)
    
    col11, col12 = st.columns(2)
    Mittelwert = col11.slider("Mittelwert",5.,10.,7.)
    Varianz = col12.slider("Varianz",0.1,5.,1.)
    Anzahl = int(np.round(Summe/Mittelwert))
    st.write("daraus berechnete Anzahl an Verkäufen = " , Anzahl)
    st.write("Anzahl = Summe/Mittelwert" )
    



st.success("eingegebene Werte: \n \n Summe = %.1f €, Mittelwert = %.1f €, \
           Varianz = %.1f € \n \n daraus ergeben sich %s Verkäufe" \
           %(Summe, Mittelwert,Varianz, Anzahl))



my_expander_minmax = st.expander(label='Minimal- und Maximalwerte für \
                                 einzelne Verkäufe definieren:')
with my_expander_minmax:
    col1, col2 = st.columns(2)
    col1.text("Minimum")
    Wert_min = col1.number_input("Minimalwert eingeben, z.B. 2",2)
    col2.text("Maximum")
    Wert_max = col2.number_input("Maximalwert eingeben, z.B. 2",15)

st.success("Der gewählte Preis liegt zwischen: min = %.1f € und max = %.1f €" %(Wert_min,Wert_max))



#########################################################################

#Erstellen der Zufallsdaten zum Testen der Verteilung
Stichprobengröße = 200000
data = np.random.normal(Mittelwert, Varianz, Stichprobengröße)


# Berechnung der Zufallszahlen:
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
            if x>Wert_min and x<Wert_max:
                X_sum = X_sum + x
                x_list.append(x)
                i = i+1
                
        last_x = np.round(Summe-X_sum,1)
        print("Summe bis hier = %s, letztes x = %s"%(X_sum,last_x))
        if last_x<Wert_min or last_x>Wert_max: 
            print('please repeat')
        else:
            x_list.append(last_x)
        
        if len(x_list)==Anzahl:
            x_list_new = [x_list[r][0] for r in range(len(x_list))]
            return x_list_new
            Fertig = True
        if Anzahl_Versuche > 300:
            #st.error("Fehler: die Parameter (Mittelwert, Varianz und Grenzen) sind schlecht gewählt (siehe Gaußkurve), bitte ändern")
            Fertig = True



x = gibZufallszahlen(Summe,Anzahl,Mittelwert,Varianz)

# Plotten der Daten

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.hist(data,bins=120)
ax1.plot([Mittelwert,Mittelwert], [0, 6500],c='k')
ax1.plot([Wert_min,Wert_min], [0, 6500],c='r')
ax1.plot([Wert_max,Wert_max], [0, 6500],c='r')
ax1.annotate("Mittelwert", (Mittelwert-1.2,6600),c='k')
ax1.annotate("min", (Wert_min-0.4,6600),c='r')
ax1.annotate("max", (Wert_max-0.4,6600),c='r')
ax1.set_ylim(0,7000)
ax1.set_xlabel("Verkaufswert \n \n rote Linien: Grenzen für Zufallszahlen")
ax1.set_ylabel("Anzahl")


if x != None:
    ax2.hist(x,bins=Anzahl)
    ax2.plot([Mittelwert,Mittelwert], [0, 8],c='k')
    ax2.annotate("Mittelwert", (Mittelwert+0.25,8),c='k')
    ax2.set_xlabel("Verkaufswert ")
    ax2.set_ylabel("Anzahl")
    
    export = str(x[0])   
    for ii in range(len(x)-1):
        export = export + "\n" + str(x[ii+1])  

    st.pyplot(fig)
    st.success("Zahlen: %s" %x)
    st.download_button(label = "Download der Zufallszahlen", data = export, file_name="Zufallszahlen.txt")

else:
    st.error("Berechnung nicht möglich, Bitte Parameter (Mittelwert, Varianz und Grenzen) anpassen - siehe Verteilung links")
    st.pyplot(fig)

st.warning("Anmerkung: Die Zahlen werden beim Klick auf Download jedes Mal neu gewählt.")
