import streamlit as st
import Extract as e
import Transform as t
import show

# Chargement des stations
selector = e.Station_Selector("data/meteo_ids.csv")
stations_df = selector.stations_df

# Interface utilisateur : choix de la station
st.title("🌤️ Météo Toulouse Métropole")
st.subheader("Sélectionnez une station météo")

station_names = [f"{i + 1}. {row['dataset_id']}" for i, row in stations_df.iterrows()]
selected_index = st.selectbox("Stations disponibles :", range(len(station_names)), format_func=lambda i: station_names[i])

# Récupération du dataset_id
dataset_id = stations_df.loc[selected_index, 'dataset_id']

# Appel API
api = e.Call_API(dataset_id)
api.fetch()

# Conversion en DataFrame
converter = e.To_DataFrame(api.data, dataset_id)
df = converter.convert()

# Affichage brut du DataFrame
st.write("📋 Données brutes :", df)

# Transformation
record = t.Record_Info(df)
viewer = show.Show_Info(record)

# Interface utilisateur : choix des infos à afficher
st.subheader("📌 Informations météo à afficher")


if st.checkbox("🏙️ Ville"):
    st.write(viewer.record.ville())

if st.checkbox("🆔 Station"):
    st.write(viewer.record.dataset_id())

if st.checkbox("🌡️ Température"):
    st.write(viewer.record.temperature())

if st.checkbox("💧 Humidité"):
    st.write(viewer.record.humidite())

if st.checkbox("📊 Pression"):
    st.write(viewer.record.pression())

if st.checkbox("🕒 Dernière mis à jour"):
    st.write(viewer.record.heure_de_paris())
