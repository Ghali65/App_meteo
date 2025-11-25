import json
import Extract as e
import Transform as t
import show as s


def main() -> None:
    """Script principal pour exécuter l'extraction, la transformation et l'affichage."""

    # Charger la configuration
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    csv_path = config["csv_path"]

    # Étapes d'extraction
    selector = e.Station_Selector(csv_path)
    dataset_id = selector.choose()

    api = e.Call_API(dataset_id)
    api.fetch()

    converter = e.To_DataFrame(api.data, dataset_id)
    df = converter.convert()

    # Transformation
    record = t.Record_Info(df)

    # Affichage unitaire
    viewer = s.Show_Info(record)
    viewer.display_all()


if __name__ == "__main__":
    main()
