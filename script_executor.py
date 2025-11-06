import Extract as e
import Transform as t
import show as s

# Étapes d'extraction
selector = e.StationSelector("data/meteo_ids.csv")
dataset_id = selector.choose()

api = e.CallAPI(dataset_id)
api.fetch()

converter = e.ToDataFrame(api.data, dataset_id)
df = converter.convert()

# Transformation
record = t.Record(df)

# Affichage unitaire
show = s.Show(record)

print("\n--- Affichage personnalisé ---")
show.display_ville()
show.display_dataset_id()
show.display_temperature()
show.display_humidite()
show.display_pression()
show.display_heure_de_paris()

