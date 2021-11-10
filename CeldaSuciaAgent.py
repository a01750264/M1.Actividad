from mesa import Agent


class CeldaSuciaAgent(Agent):
    '''
    Agente que representará una celda sucia
    '''

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.is_dirty = True
