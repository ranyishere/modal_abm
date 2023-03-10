from cell_types import *
import random
from deepcopy import copy


class Rule:

    def __init__(self):
        """
        Self
        """
        pass

    def apply(self, lhs):
        """
        Runs Interaction
        """

        for key, value in lhs.items():

            if type(value) == Fibroblast:
                pass

            elif type(value) == Nk:
                pass

            elif type(value) == Plasma:
                pass

            elif type(value) == MacroPhage:
                pass

            elif type(value) == MegaKaryoCyte:
                pass

            elif type(value) == T:
                pass

            else:
                pass


class FibroblastRule(Rule):

    def __init__(self):
        """
        Init
        """
        pass

    def apply(self, lhs):
        """
        Run
        """

        survival
        for key, value in lhs.items():

            if type(value) == Fibroblast:
                pass

            elif type(value) == Nk:
                pass

            elif type(value) == Plasma:
                pass

            elif type(value) == MacroPhage:
                pass

            elif type(value) == MegaKaryoCyte:
                pass

            elif type(value) == T:
                pass

            else:
                pass


class NkRule(Rule):

    def __init__(self):
        """
        Init
        """
        pass

    def apply(self, lhs):
        """
        Run
        """

        for key, value in lhs.items():

            if type(value) == Fibroblast:
                pass

            elif type(value) == Nk:
                pass

            elif type(value) == Plasma:
                pass

            elif type(value) == MacroPhage:
                pass

            elif type(value) == MegaKaryoCyte:
                pass

            elif type(value) == T:
                pass

            else:
                pass


class PlasmaRule(Rule):

    def __init__(self):
        """
        Init
        """
        pass

    def apply(self, lhs):
        """
        Run
        """

        rhs = lhs
        for key, value in lhs.items():

            if type(value) == Fibroblast:
                pass

            elif type(value) == Nk:
                pass

            elif type(value) == Plasma:
                pass

            elif type(value) == MacroPhage:
                pass

            elif type(value) == MegaKaryoCyte:
                pass

            elif type(value) == T:
                pass

            elif type(value) == Water:

                x_pos = value.x
                y_pos = value.y
                cur_cell_no = value.cell_no


                prolif = random.random()
                if prolif >= 0.5:

                    new_cell = Plasma(cur_cell_no, x_pos)
                    rhs[key] = new_cell

                else:
                    pass

            else:
                pass

        return rhs


class MacroPhageRule(Rule):

    def __init__(self):
        """
        Init
        """
        pass

    def apply(self, lhs):
        """
        Run
        """

        for key, value in lhs.items():

            if type(value) == Fibroblast:
                pass

            elif type(value) == Nk:
                pass

            elif type(value) == Plasma:
                pass

            elif type(value) == MacroPhage:
                pass

            elif type(value) == MegaKaryoCyte:
                pass

            elif type(value) == T:
                pass

            else:
                pass


class MegaKaryoCyteRule(Rule):

    def __init__(self):
        """
        Init
        """
        pass

    def apply(self, lhs):
        """
        Run
        """

        for key, value in lhs.items():

            if type(value) == Fibroblast:
                pass

            elif type(value) == Nk:
                pass

            elif type(value) == Plasma:
                pass

            elif type(value) == MacroPhage:
                pass

            elif type(value) == MegaKaryoCyte:
                pass

            elif type(value) == T:
                pass

            else:
                pass


class TCellRule(Rule):

    def __init__(self):
        """
        Init
        """
        pass

    def apply(self, lhs):
        """
        Run
        """

        for key, value in lhs.items():

            if type(value) == Fibroblast:
                pass

            elif type(value) == Nk:
                pass

            elif type(value) == Plasma:
                pass

            elif type(value) == MacroPhage:
                pass

            elif type(value) == MegaKaryoCyte:
                pass

            elif type(value) == T:
                pass

            else:
                pass
