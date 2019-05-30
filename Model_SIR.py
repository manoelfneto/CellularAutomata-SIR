import random
import sys
import pygame


class ModelSIR:

    def __init__(self, screen_width=800, screen_height=600, cell_size=10, black=(0, 0, 0), red=(255, 0, 0),
                 white=(255, 255, 255), green = (0, 155, 0), max_fps=1):

        pygame.init()
        self.width = screen_width
        self.height = screen_height
        self.cell_size = cell_size
        self.black = black
        self.red = red
        self.white = white
        self.green = green

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clear_screen()
        pygame.display.flip()

        self.max_fps = max_fps

        self.active_grid = 0
        self.num_cols = int(self.width / self.cell_size)
        self.num_rows = int(self.height / self.cell_size)
        self.grids = []
        self.init_grids()
        self.set_grid()

        self.paused = False
        self.game_over = False

    def init_grids(self):

        def create_grid():
            rows = []
            for row_num in range(self.num_rows):
                list_of_columns = [0] * self.num_cols
                rows.append(list_of_columns)
            return rows
        self.grids.append(create_grid())
        self.grids.append(create_grid())

    def set_grid(self, value=None, grid=0):
        states = [0,0,0,0,0,0,1,0,0,1]
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if value is None:
                    cell_value = random.choice(states)
                else:
                    cell_value = value
                self.grids[grid][r][c] = cell_value

    def draw_grid(self):
        self.clear_screen()
        for c in range(self.num_cols):
            for r in range(self.num_rows):

                if self.grids[self.active_grid][r][c] == 0:
                    color = self.white   # estado inicial suscetivel

                elif self.grids[self.active_grid][r][c] == 1 or \
                        self.grids[self.active_grid][r][c] == 2 \
                        or self.grids[self.active_grid][r][c] == 3 \
                        or self.grids[self.active_grid][r][c] == 4 \
                        or self.grids[self.active_grid][r][c] == 5 \
                        or self.grids[self.active_grid][r][c] == 6 \
                        or self.grids[self.active_grid][r][c] == 7: # estados de infeccao
                    color = self.red
                elif self.grids[self.active_grid][r][c] == 8:
                    color = self.red  # estado de transicao para recuperado
                else:
                    color = self.green  # estado recuperado

                pygame.draw.circle(self.screen,
                                   color,
                                   (int(c * self.cell_size + (self.cell_size / 2)),
                                    int(r * self.cell_size + (self.cell_size / 2))),
                                   int(self.cell_size / 2),
                                   0)
        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill(self.black)

    def get_cell(self, row_num, col_num):
        try:
            cell_value = self.grids[self.active_grid][row_num][col_num]
        except:
            cell_value = 0
        return cell_value

    def check_cell_neighbors(self, row_index, col_index):
        num_infect_neigh = 0

        one = self.get_cell(row_index - 1, col_index - 1)
        two = self.get_cell(row_index - 1, col_index)
        three = self.get_cell(row_index - 1, col_index + 1)
        four = self.get_cell(row_index, col_index - 1)
        five = self.get_cell(row_index, col_index + 1)
        six = self.get_cell(row_index + 1, col_index - 1)
        seven = self.get_cell(row_index + 1, col_index)
        eight = self.get_cell(row_index + 1, col_index + 1)

        # verificando se o vizinho esta infectado
        if self.grids[self.active_grid][row_index][col_index] == 0:
            if one == 1 or one == 2 or one == 3 or one == 4 or one == 5 or one == 6 or one == 7:
                num_infect_neigh = num_infect_neigh + 1
            if two == 1 or two == 2 or two == 3 or two == 4 or two == 5 or two == 6 or two == 7:
                num_infect_neigh = num_infect_neigh + 1
            if three == 1 or three == 2 or three == 3 or three == 4 or three == 5 or three == 6 or three == 7:
                num_infect_neigh = num_infect_neigh + 1
            if four == 1 or four == 2 or four == 3 or four == 4 or four == 5 or four == 6 or four == 7:
                num_infect_neigh = num_infect_neigh + 1
            if five == 1 or five == 2 or five == 3 or five == 4 or five == 5 or five == 6 or five == 7:
                num_infect_neigh = num_infect_neigh + 1
            if six == 1 or six == 2 or six == 3 or six == 4 or six == 5 or six == 6 or six == 7:
                num_infect_neigh = num_infect_neigh + 1
            if seven == 1 or seven == 2 or seven == 3 or seven == 4 or seven == 5 or seven == 6 or seven == 7:
                num_infect_neigh = num_infect_neigh + 1
            if eight == 1 or eight == 2 or eight == 3 or eight == 4 or eight == 5 or eight == 6 or eight == 7:
                num_infect_neigh = num_infect_neigh + 1

        # trocando de estado suscetivel(0) -> infectado(1-7) -> recuperado(9)
        # 8 eh o estado de transicao
        if self.grids[self.active_grid][row_index][col_index] == 0:
            if num_infect_neigh > 3:
                return 1
            if num_infect_neigh <= 3:
                return 0
        elif self.grids[self.active_grid][row_index][col_index] == 1 or \
                self.grids[self.active_grid][row_index][col_index] == 2 or\
                self.grids[self.active_grid][row_index][col_index] == 3 or\
                self.grids[self.active_grid][row_index][col_index] == 4 or \
                self.grids[self.active_grid][row_index][col_index] == 5 or \
                self.grids[self.active_grid][row_index][col_index] == 6 or \
                self.grids[self.active_grid][row_index][col_index] == 7:
            return self.grids[self.active_grid][row_index][col_index] + 1
        elif self.grids[self.active_grid][row_index][col_index] == 8:
            return 9
        elif self.grids[self.active_grid][row_index][col_index] == 9:
            return 9

        return self.grids[self.active_grid][row_index][col_index]

    def update_generation(self):
        self.set_grid(0, self.inactive_grid())
        for r in range(self.num_rows ):
            for c in range(self.num_cols ):
                next_gen_state = self.check_cell_neighbors(r, c)
                self.grids[self.inactive_grid()][r][c] = next_gen_state
        self.active_grid = self.inactive_grid()


    def inactive_grid(self):
        return (self.active_grid + 1) % 2

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("key pressed")
                if event.unicode == ' ':
                    print("Toggling pause.")
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                elif event.unicode == 'r':
                    print("Randomizing grid.")
                    self.active_grid = 0
                    self.set_grid(None, self.active_grid)  # randomize
                    self.set_grid(0, self.inactive_grid())  # set to 0
                    self.draw_grid()
                elif event.unicode == 'q':
                    print("Exiting.")
                    self.game_over = True
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            if self.game_over:
                return

            self.handle_events()

            if not self.paused:
                self.update_generation()
                self.draw_grid()

            clock.tick(self.max_fps)

if __name__ == '__main__':
    game = ModelSIR()
    game.run()