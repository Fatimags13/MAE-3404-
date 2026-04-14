# -*- coding: utf-8 -*-
# PumpCurve_GUI.py  -  Main application entry point  (PyQt6)

import sys
import os
from pathlib import Path

import PyQt6.QtWidgets as qtw
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from pump import Ui_Form
from Pump_MVC import Pump_Controller


class PumpCurve_GUI_Class(Ui_Form, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pump Curve Calculator")

        self.FilePath = os.getcwd()
        self.FileName = ""

        # Embed matplotlib canvas into the output grid
        self.canvas = FigureCanvasQTAgg(
            Figure(figsize=(5, 3), tight_layout=True, frameon=True)
        )
        self.ax = self.canvas.figure.add_subplot()
        self.GL_Output.addWidget(self.canvas, 5, 0, 1, 4)

        # Create controller and pass widgets to it
        self.myPump = Pump_Controller()
        self.setViewWidgets()

        # Connect signals
        self.PB_Exit.clicked.connect(self.Exit)
        self.CMD_Open.clicked.connect(self.ReadAndCalculate)

        self.show()

    def setViewWidgets(self):
        w = [
            self.LE_PumpName,
            self.LE_FlowUnits,
            self.LE_HeadUnits,
            self.LE_HeadCoefs,
            self.LE_EffCoefs,
            self.ax,
            self.canvas,
        ]
        self.myPump.setViewWidgets(w)

    def ReadAndCalculate(self):
        if self.OpenFile():
            with open(self.FileName, 'r') as f:
                data = f.readlines()
            self.myPump.ImportFromFile(data)

    def OpenFile(self):
        fname, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "Open Pump Data File",
            self.FilePath,
            "Text Files (*.txt);;All Files (*.*)"
        )
        if fname:
            self.FileName = fname
            self.FilePath = str(Path(fname).parent)
            self.TE_Filename.setText(self.FileName)
            return True
        return False

    def Exit(self):
        qapp.exit()


def main():
    gui = PumpCurve_GUI_Class()
    qapp.exec()


if __name__ == "__main__":
    qapp = qtw.QApplication(sys.argv)
    main()
