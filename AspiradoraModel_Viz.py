from AspiradoraModel import *
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer, VisualizationElement
from AspiradoraModel import AspiradoraModel, AspiradoraAgent
from CeldaSuciaAgent import CeldaSuciaAgent


def aspecto_agentes(agente):
    if isinstance(agente, AspiradoraAgent):
        aspecto = {
            "Shape": "circle",
            "Filled": "true",
            "r": 0.8,
            "Color": "red",
            "Layer": 1
        }

    elif isinstance(agente, CeldaSuciaAgent):
        if agente.is_dirty:
            aspecto = {
                "Shape": "circle",
                "Filled": "true",
                "r": 0.3,
                "Color": "black",
                "Layer": 2
            }

        else:
            aspecto = {
                "Shape": "circle",
                "Filled": "true",
                "r": 0.4,
                "Color": "white",
                "Layer": 0
            }

    return aspecto


grid = CanvasGrid(aspecto_agentes, 10, 10, 500)

server = ModularServer(AspiradoraModel,
                       [grid],
                       'Aspiradora Model',
                       {'agents': 10, 'sucias': 30, 'M': 10, 'N': 10})
server.port = 8521
server.launch()
