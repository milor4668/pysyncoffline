#
# ============================================================================
#
# Classe de gestion de l'arbre
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

#import config

class Tree:
    def __init__(self,myTree):
        self.myTree = myTree
        self.createDirectory()
        return

    def show(self):
        print(self.myTree)
        return

    def createDirectory(self):
        #self.myTree.setHeaderLabels(["header"])
        tree_widget_item1 = QTreeWidgetItem(["item1"])
        tree_widget_item1.setCheckState(0, Qt.Unchecked)
        tree_widget_item1.addChild(QTreeWidgetItem(["item1_2"]))
        tree_widget_item2 = QTreeWidgetItem(["item2"])
        tree_widget_item2.addChild(QTreeWidgetItem(["item2_2"]))
        self.myTree.addTopLevelItem(tree_widget_item1)
        self.myTree.addTopLevelItem(tree_widget_item2)
        return
