from .show.build_viewer_list import build_viewer_list
from .transform.record import Record

class Command:
    def execute(self):
        raise NotImplementedError("La méthode execute() doit être implémentée.")


class ExtractCommand(Command):
    def __init__(self, dataset_id, CallApi, ToDataFrame, mapping):
        self.dataset_id = dataset_id
        self.CallApi = CallApi
        self.ToDataFrame = ToDataFrame
        self.mapping = mapping
        self.df = None

    def execute(self):
        api = self.CallApi(self.dataset_id)
        api.fetch()

        ville = self.mapping.get(self.dataset_id, "Inconnue")

        converter = self.ToDataFrame(api.data, self.dataset_id, ville)
        self.df = converter.convert()

        return self.df


class TransformCommand(Command):
    """
    Applique chaque transformer sur un même Record enrichi.
    """
    def __init__(self, df, transformers):
        self.df = df
        self.transformers = transformers

    def execute(self):
        record = Record()

        for transformer in self.transformers:
            record = transformer(record, self.df)

        return record


class ShowCommand(Command):
    def __init__(self, record):
        self.record = record

    def execute(self):
        linked_list = build_viewer_list(self.record)
        linked_list.afficher_liste()
