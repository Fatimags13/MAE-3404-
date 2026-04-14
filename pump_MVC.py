# -*- coding: utf-8 -*-
# Pump_MVC.py  -  Model / View / Controller  (PyQt6)

import numpy as np
import PyQt6.QtWidgets as qtw
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from LeastSquares import LeastSquaresFit_Class


# =============================================================================
class Pump_Model():
    """Stores all pump data."""
    def __init__(self):
        self.PumpName  = ""
        self.FlowUnits = ""
        self.HeadUnits = ""
        self.FlowData  = np.array([])
        self.HeadData  = np.array([])
        self.EffData   = np.array([])
        self.HeadCoefficients        = np.array([])
        self.EfficiencyCoefficients  = np.array([])
        self.LSFitHead = LeastSquaresFit_Class()
        self.LSFitEff  = LeastSquaresFit_Class()


# =============================================================================
class Pump_Controller():
    """Mediates between Model and View."""
    def __init__(self):
        self.Model = Pump_Model()
        self.View  = Pump_View()

    def ImportFromFile(self, data):
        """
        File format:
          line 0  - pump name
          line 1  - column headers (flow head efficiency)
          line 2  - units           (gpm ft %)
          line 3+ - numeric data
        """
        self.Model.PumpName  = data[0].strip()
        units                = data[2].split()
        self.Model.FlowUnits = units[0].strip()
        self.Model.HeadUnits = units[1].strip()
        self.SetData(data[3:])
        self.updateView()

    def SetData(self, data):
        """Parse numeric rows into arrays then fit polynomials."""
        self.Model.FlowData = np.array([])
        self.Model.HeadData = np.array([])
        self.Model.EffData  = np.array([])
        for line in data:
            line = line.strip()
            if not line:
                continue
            cells = line.split()
            self.Model.FlowData = np.append(self.Model.FlowData, float(cells[0]))
            self.Model.HeadData = np.append(self.Model.HeadData, float(cells[1]))
            self.Model.EffData  = np.append(self.Model.EffData,  float(cells[2]))
        self.LSFit()

    def LSFit(self):
        """Quadratic fit for Head, cubic fit for Efficiency."""
        self.Model.LSFitHead.x = self.Model.FlowData
        self.Model.LSFitHead.y = self.Model.HeadData
        self.Model.LSFitHead.LeastSquares(2)

        self.Model.LSFitEff.x = self.Model.FlowData
        self.Model.LSFitEff.y = self.Model.EffData
        self.Model.LSFitEff.LeastSquares(3)

    def setViewWidgets(self, w):
        self.View.setViewWidgets(w)

    def updateView(self):
        self.View.updateView(self.Model)


# =============================================================================
class Pump_View():
    """Populates widgets and draws the matplotlib chart."""
    def __init__(self):
        self.LE_PumpName  = qtw.QLineEdit()
        self.LE_FlowUnits = qtw.QLineEdit()
        self.LE_HeadUnits = qtw.QLineEdit()
        self.LE_HeadCoefs = qtw.QLineEdit()
        self.LE_EffCoefs  = qtw.QLineEdit()
        self.ax     = None
        self.canvas = None

    def setViewWidgets(self, w):
        (self.LE_PumpName,
         self.LE_FlowUnits,
         self.LE_HeadUnits,
         self.LE_HeadCoefs,
         self.LE_EffCoefs,
         self.ax,
         self.canvas) = w

    def updateView(self, Model):
        self.LE_PumpName.setText(Model.PumpName)
        self.LE_FlowUnits.setText(Model.FlowUnits)
        self.LE_HeadUnits.setText(Model.HeadUnits)
        self.LE_HeadCoefs.setText(Model.LSFitHead.GetCoeffsString())
        self.LE_EffCoefs.setText(Model.LSFitEff.GetCoeffsString())
        self.DoPlot(Model)

    def DoPlot(self, Model):
        """Dual-axis plot: Head left, Efficiency right."""
        headx, heady, headRSq = Model.LSFitHead.GetPlotInfo(2, npoints=500)
        effx,  effy,  effRSq  = Model.LSFitEff.GetPlotInfo(3,  npoints=500)

        ax1 = self.ax
        ax1.clear()

        # Left y-axis: Head
        line1, = ax1.plot(headx, heady, 'k--',
                          label='Head($R^2={:.3f}$)'.format(headRSq))
        pts1,  = ax1.plot(Model.FlowData, Model.HeadData,
                          'ko', markersize=6, label='Head')
        ax1.set_xlabel('Flow Rate ({})'.format(Model.FlowUnits))
        ax1.set_ylabel('Head ({})'.format(Model.HeadUnits))

        # Right y-axis: Efficiency
        ax2 = ax1.twinx()
        line2, = ax2.plot(effx, effy, 'k:',
                          label='Efficiency($R^2={:.3f}$)'.format(effRSq))
        pts2,  = ax2.plot(Model.FlowData, Model.EffData,
                          'k^', markersize=6, label='Efficiency')
        ax2.set_ylabel('Efficiency (%)')

        ax1.set_title('Pump Head and Efficiency Curves')

        # Combined legend
        handles = [line1, pts1, line2, pts2]
        labels  = [h.get_label() for h in handles]
        ax1.legend(handles, labels, loc='upper right', fontsize=8)

        self.canvas.draw()
