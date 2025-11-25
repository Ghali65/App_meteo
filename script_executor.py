import Extract as e
import Transform as t
import show as s


def main() -> None:
    """Script principal pour exécuter l'extraction, la transformation et l'affichage."""

    # Étapes d'extraction
    selector = e.Station_Selector("data/meteo_ids.csv")
    dataset_id = selector.choose()

    api = e.Call_API(dataset_id)
    api.fetch()

    converter = e.To_DataFrame(api.data, dataset_id)
    df = converter.convert()

    # Transformation
    record = t.Record_Info(df)

    # Affichage unitaire
    viewer = s.Show_Info(record)

    print("\n--- Affichage personnalisé ---")
    viewer.display_ville()
    viewer.display_dataset_id()
    viewer.display_temperature()
    viewer.display_humidite()
    viewer.display_pression()
    viewer.display_heure_de_paris()


if __name__ == "__main__":
    main()
