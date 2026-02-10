import streamlit as st

st.title("Projet : Détection d'anomalies dans des pièces industrielles")
st.sidebar.title("Table des matières")

pages=["Présentation de base de données MVTec", "EDA", "Classification de type d'objet", "ML : Détection d'anomalies", "CNN : Classification binaire d'anomalies et segmentation", "CNN: classification multi-classe d'anomalies", "Conclusion et pérspectives"]

page=st.sidebar.radio("Navigation", pages)


if page == pages[0] : 
  # Makhlouf
  st.write("### Présentation de base de données MVTec")

if page == pages[1] : 
  # Suzy
  st.write("### EDA")

if page == pages[2] : 
  # Suzy
  st.write("### Classification de type d'objet")

if page == pages[3] : 
  # Karine
  st.write("### ML: Détection d'anomalies")

if page == pages[4] : 
  # Makhlouf
  st.write("### CNN: Classification binaire d'anomalies et segmentation")

if page == pages[5] : 
  # Karine
  st.write("### CNN: Classification multi-classe d'anomalies")

if page == pages[6] : 
  # Toute le monde ?
  st.write("### Conclusion et pérspectives")


