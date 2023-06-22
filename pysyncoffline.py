#!/usr/bin/env python3
# ============================================================================
#
#   Outil de récupération de données :
#    - rpm
#    - deb
#    - images docker
#    - applications
#
# ============================================================================
# Auteur : S. PRIGENT
# Date   : 4 Juin 2023
# ============================================================================
#
# Fichiers d'import
# ----------------------------------------------------------------------------
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

# Import local
import toolbar
import tree


# Fonction main
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    loader = QUiLoader()
    app = QApplication(sys.argv)
    window = loader.load("ui/pysyncoffline.ui", None)

    myToolBar = toolbar.ToolBar(window.toolBar)

    myTree = tree.Tree(window.treeWidget)

    window.show()
    sys.exit(app.exec_())

# ============================================================================
