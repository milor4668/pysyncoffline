#
# ============================================================================
#
# Classe de gestion de la toolbar
#
# ============================================================================
# Auteur : Stéphane PRIGENT
# Date   : 4 Juin 2023
# ============================================================================
#
# Import 
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

#import config

class ToolBar:
    def __init__(self,myToolBar):
        self.myToolBar = myToolBar
        self.createButtons()
        return

    def createButtons(self):
        self.button_plus = QAction(QIcon("icons/plus.png"),
                                             "Ajouter une source")
        self.button_plus.setStatusTip("Ajouter une source")
        self.button_plus.triggered.connect(self.onMyToolBarButtonPlus)
        self.button_plus.setCheckable(False)
        self.myToolBar.addAction(self.button_plus)
        return
        
    def onMyToolBarButtonPlus(self):
        print('onMyToolBarButtonPlus')
        loader = QUiLoader()
        self.dialog = loader.load("ui/dialogAjout.ui", None)
        self.dialog.exec_()
