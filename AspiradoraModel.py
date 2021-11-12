from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from CeldaSuciaAgent import CeldaSuciaAgent


class AspiradoraAgent(Agent):
    '''
    Agente que representa a la aspiradora
    '''

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.pasos = 0

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.pasos += 1
        print(self.pasos)

    def aspirar(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            for i in cellmates:
                if isinstance(i, CeldaSuciaAgent):
                    # Aspirar la celda
                    if i.is_dirty == True:
                        i.is_dirty = False

    def step(self):
        # Aquí va el paso del agente
        self.move()
        self.aspirar()


class AspiradoraModel(Model):
    '''
    Modelo de las apiradoras
    '''

    def __init__(self, agents, sucias, M, N):
        self.num_agents = agents
        self.grid = MultiGrid(N, M, True)
        self.schedule = RandomActivation(self)
        self.running = True
        self.cell_count = M * N
        self.porcentaje_sucias = sucias
        self.celdas_sucias = int((sucias * self.cell_count)/100)

        # Crear aspiradoras
        for i in range(self.num_agents):
            a = AspiradoraAgent(i, self)
            self.schedule.add(a)

            # Agregar el agente a las coordenadas [1,1]
            x = 1
            y = 1

            self.grid.place_agent(a, (x, y))

        # Crear celdas sucias
        for i in range(self.num_agents, self.num_agents + self.celdas_sucias):
            cs = CeldaSuciaAgent(i, self)
            self.schedule.add(cs)

            # Agregar las celdas sucias en celdas aleatorias
            xs = self.random.randrange(self.grid.width)
            ys = self.random.randrange(self.grid.height)

            self.grid.place_agent(cs, (xs, ys))

    def step(self):
        '''
        Avanzar un paso en el modelo.
        '''
        self.schedule.step()
