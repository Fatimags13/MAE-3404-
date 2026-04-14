# -*- coding: utf-8 -*-
# pump.py  -  converted from pump.ui for PyQt6

from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(696, 796)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        # --- Input GroupBox ---
        self.GB_Input = QtWidgets.QGroupBox(Form)
        self.GB_Input.setMaximumHeight(135)
        self.GB_Input.setObjectName("GB_Input")

        self.gridLayout = QtWidgets.QGridLayout(self.GB_Input)
        self.gridLayout.setObjectName("gridLayout")

        self.LBL_Filename = QtWidgets.QLabel(self.GB_Input)
        self.LBL_Filename.setObjectName("LBL_Filename")
        self.gridLayout.addWidget(self.LBL_Filename, 0, 0, 1, 1)

        self.TE_Filename = QtWidgets.QTextEdit(self.GB_Input)
        self.TE_Filename.setMinimumHeight(20)
        self.TE_Filename.setObjectName("TE_Filename")
        self.gridLayout.addWidget(self.TE_Filename, 0, 1, 1, 1)

        self.CMD_Open = QtWidgets.QPushButton(self.GB_Input)
        self.CMD_Open.setObjectName("CMD_Open")
        self.gridLayout.addWidget(self.CMD_Open, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.GB_Input)

        # --- Output GroupBox ---
        self.GB_Output = QtWidgets.QGroupBox(Form)
        self.GB_Output.setObjectName("GB_Output")

        self.GL_Output = QtWidgets.QGridLayout(self.GB_Output)
        self.GL_Output.setObjectName("GL_Output")

        self.LBL_PumpName = QtWidgets.QLabel(self.GB_Output)
        self.LBL_PumpName.setObjectName("LBL_PumpName")
        self.GL_Output.addWidget(self.LBL_PumpName, 0, 0, 1, 1)

        self.LE_PumpName = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_PumpName.setObjectName("LE_PumpName")
        self.GL_Output.addWidget(self.LE_PumpName, 0, 1, 1, 3)

        self.LBL_FlowUnits = QtWidgets.QLabel(self.GB_Output)
        self.LBL_FlowUnits.setObjectName("LBL_FlowUnits")
        self.GL_Output.addWidget(self.LBL_FlowUnits, 1, 0, 1, 1)

        self.LE_FlowUnits = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_FlowUnits.setObjectName("LE_FlowUnits")
        self.GL_Output.addWidget(self.LE_FlowUnits, 1, 1, 1, 1)

        self.LBL_HeadUnits = QtWidgets.QLabel(self.GB_Output)
        self.LBL_HeadUnits.setObjectName("LBL_HeadUnits")
        self.GL_Output.addWidget(self.LBL_HeadUnits, 1, 2, 1, 1)

        self.LE_HeadUnits = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_HeadUnits.setObjectName("LE_HeadUnits")
        self.GL_Output.addWidget(self.LE_HeadUnits, 1, 3, 1, 1)

        self.LBL_HeadCoefs = QtWidgets.QLabel(self.GB_Output)
        self.LBL_HeadCoefs.setObjectName("LBL_HeadCoefs")
        self.GL_Output.addWidget(self.LBL_HeadCoefs, 2, 0, 1, 1)

        self.LE_HeadCoefs = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_HeadCoefs.setObjectName("LE_HeadCoefs")
        self.GL_Output.addWidget(self.LE_HeadCoefs, 2, 1, 1, 3)

        self.LBL_EffCoefs = QtWidgets.QLabel(self.GB_Output)
        self.LBL_EffCoefs.setObjectName("LBL_EffCoefs")
        self.GL_Output.addWidget(self.LBL_EffCoefs, 3, 0, 1, 1)

        self.LE_EffCoefs = QtWidgets.QLineEdit(self.GB_Output)
        self.LE_EffCoefs.setObjectName("LE_EffCoefs")
        self.GL_Output.addWidget(self.LE_EffCoefs, 3, 1, 1, 3)

        self.W_Plot = QtWidgets.QWidget(self.GB_Output)
        self.W_Plot.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.W_Plot.setObjectName("W_Plot")
        self.GL_Output.addWidget(self.W_Plot, 5, 0, 1, 4)

        self.PB_Exit = QtWidgets.QPushButton(self.GB_Output)
        self.PB_Exit.setObjectName("PB_Exit")
        self.GL_Output.addWidget(self.PB_Exit, 6, 2, 1, 1)

        self.verticalLayout.addWidget(self.GB_Output)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _tr = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_tr("Form", "Pump Curve Calculator"))
        self.GB_Input.setTitle(_tr("Form", "Input"))
        self.LBL_Filename.setText(_tr("Form", "Filename"))
        self.CMD_Open.setText(_tr("Form", "Read File and Calculate"))
        self.GB_Output.setTitle(_tr("Form", "Output"))
        self.LBL_PumpName.setText(_tr("Form", "Pump Name"))
        self.LBL_FlowUnits.setText(_tr("Form", "Flow Units"))
        self.LBL_HeadUnits.setText(_tr("Form", "Head Units"))
        self.LBL_HeadCoefs.setText(_tr("Form", "Head Coefficients"))
        self.LBL_EffCoefs.setText(_tr("Form", "Efficiency Coefficients"))
        self.PB_Exit.setText(_tr("Form", "Exit"))
