

# Rules apply to classes
# Strength of interaction depends on each cell

class Type:

    def __init__(self):
        """
        pass
        """
        pass

class Cell(Type):

    def __init__(self, cell_no, pos_i, pos_j,
                 cell_type=0, color=(0,0,0),
                 prolif_rate=0.0,
                 alpha=1.0
                 ):
        """
        Init
        """

        super().__init__()

        self.cell_no = cell_no
        self.cell_type = cell_type
        self.x = pos_i
        self.y = pos_j

        self.color = color
        self.alpha = alpha

    def __repr__(self):
        """
        Representation
        """

        return "<Cell {0}, pos_x: {1}, pos_y: {2} cell_type: {3}>".format(
                    self.cell_no,
                    self.cell_type,
                    self.x, self.y
                )

    def get_survival_rate(self):
        """
        Survival Rate
        """
        pass


class Fibroblast(Cell):

    def __init__(self, cell_no, pos_i, pos_j,
                 cell_type=0, color=(100,100,100),
                 prolif_rate=0.0
                 ):
        """
        Init
        """

        super().__init__(cell_no, pos_i, pos_j, cell_type, color, prolif_rate)

        self.CXCR4 = 0.3
        self.CXCL12 = 0.3
        self.IL_6 = 0.1
        self.VCAM = 0.1
        self.ICAM = 0.2


class Nk(Cell):

    def __init__(self, cell_no, pos_i, pos_j,
                 cell_type=1, color=(100,0,10),
                 prolif_rate=0.0,
                 ):
        """
        Init
        """

        # super().__init__()
        super().__init__(cell_no, pos_i, pos_j, cell_type, color, prolif_rate)

        self.HLA_1 = False
        self.PD_1 = False
        self.KLRG_1 = False


class Plasma(Cell):

    def __init__(
            self, cell_no, pos_i, pos_j,
                 cell_type=2, color=(0,200,0),
                 prolif_rate=1.0
                 ):
        """
        Init
        """

        # super().__init__()
        super().__init__(cell_no, pos_i, pos_j, cell_type, color, prolif_rate)

class MacroPhage(Cell):

    def __init__(self, cell_no, pos_i, pos_j,
                 cell_type=3, color=(0,0,0),
                 prolif_rate=0.0
                 ):
        """
        Init
        """

        super().__init__(cell_no, pos_i, pos_j, cell_type, color, prolif_rate)

    pass

class MegaKaryoCyte(Cell):

    def __init__(self, cell_no, pos_i, pos_j,
                 cell_type=4, color=(0,100,10),
                 prolif_rate=0.0
                 ):
        """
        Init
        """

        super().__init__(cell_no, pos_i, pos_j, cell_type, color, prolif_rate)

    pass

class T(Cell):

    def __init__(self, cell_no, pos_i, pos_j,
                 cell_type=5, color=(100,10,10),
                 prolif_rate=0.0
                 ):
        """
        Init
        """

        # super().__init__()
        super().__init__(cell_no, pos_i, pos_j, cell_type, color, prolif_rate)

        self.APRIL = 0.5
        self.BAFF = 0.5


class Water(Cell):

    def __init__(self, cell_no, pos_i, pos_j,
                 cell_type=-1, color=(0,0,255),
                 prolif_rate=0.0
                 ):
        """
        Init
        """

        super().__init__(cell_no, pos_i, pos_j, cell_type,
                color, prolif_rate, alpha=0.1)
