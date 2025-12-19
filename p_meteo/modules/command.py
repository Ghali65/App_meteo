# modules/command.py

class Command:
    """
    Interface de base pour toutes les commandes.
    Chaque commande doit implémenter execute().
    """
    def execute(self):
        raise NotImplementedError("La méthode execute() doit être implémentée.")


class ExtractCommand(Command):
    """
    Commande d'extraction : exécute CallApi + fetch + ToDataFrame.
    """
    def __init__(self, dataset_id, CallApi, ToDataFrame):
        self.dataset_id = dataset_id
        self.CallApi = CallApi
        self.ToDataFrame = ToDataFrame
        self.df = None

    def execute(self):
        api = self.CallApi(self.dataset_id)
        api.fetch()

        converter = self.ToDataFrame(api.data, self.dataset_id)
        self.df = converter.convert()

        return self.df


class TransformCommand(Command):
    """
    Commande de transformation : exécute toutes les classes T*.
    """
    def __init__(self, df, transformers):
        self.df = df
        self.transformers = transformers
        self.results = []

    def execute(self):
        for transformer in self.transformers:
            self.results.append(transformer(self.df))
        return self.results


class ShowCommand(Command):
    """
    Commande d'affichage : construit et exécute la LinkedList.
    """
    def __init__(self, viewers, LinkedList, Link):
        self.viewers = viewers
        self.LinkedList = LinkedList
        self.Link = Link

    def execute(self):
        if not self.viewers:
            return

        # Création de la liste chaînée
        linked_list = self.LinkedList(self.Link(self.viewers[0]))

        for viewer in self.viewers[1:]:
            linked_list.ajouter_maillon(self.Link(viewer))

        # Exécution du pipeline d'affichage
        linked_list.afficher_liste()
