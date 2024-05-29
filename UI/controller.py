import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.stato = None

    def handleCalcola(self, e):
        self._view._txt_result.clean()
        self._model.buildGraph(int(self._view._txtAnno.value))
        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato."))
        self._view._txt_result.controls.append(ft.Text(f"Nodi: {len(self._model._graph.nodes)}; Archi: {len(self._model._graph.edges)}"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getPartiConnesse()} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito il dettaglio dei nodi:"))
        for node in self._model._graph.nodes:
            vicini = self._model._graph.degree[node]
            self._view._txt_result.controls.append(ft.Text(f"{node} -- {vicini} vicini."))
        self._view._btnRaggiungibili.disabled = False
        self.popolaStati()
        self._view.update_page()

    def handleRaggiungibili(self, e):
        if self._view._ddStato.value is None or self._view._ddStato == "":
            self._view.create_alert("Inserire uno stato!")
            return
        else:
            self._view._txt_result.clean()
            raggiungibili = self._model.getDFSNodes(self.stato)
            for node in raggiungibili:
                self._view._txt_result.controls.append(ft.Text(f"{node}"))
            self._view.update_page()

    def popolaStati(self):
        nodi = self._model._graph.nodes
        for n in nodi:
            self._view._ddStato.options.append(ft.dropdown.Option(key=n.StateNme, data=n, on_click=self.read_stato))
        self._view.update_page()

    def read_stato(self, e):
        self.stato = e.control.data
