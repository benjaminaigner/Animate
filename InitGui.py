# -*- coding: utf-8 -*-

"""@package InitGui
This module is used by FreeCAD to add the `Animate` workbench.

When the module is imported by FreeCAD, the `Animate` workbench class is added
to FreeCAD Gui. The `Animate` class encapsulates all necessary workbench
behavior and changes to the FreeCAD Gui.
"""

import FreeCAD
import FreeCADGui


class Animate(FreeCADGui.Workbench):
    """
Animate workbench class according to the PythonWorkbench template.

This class represents the workbench in the FreeCAD Gui i.e. it imports
commands, shows them on a toolbar and in a menu when workbench is activated.
It contains information to make and item in the workbench toolbar listbox.

Attributes:
    Icon: A path to an image to be shown on the workbench toolbar.
    MenuText: A str text to be shown in the listbox on the workbench toolbar.
    ToolTip: A str tooltip for the `Animate` workbench.
    list: A list of str which are the names of imported commands.
    """

    def __init__(self):
        """
Initialization method for `Animate` workbench.

A class instance is created, an static attributes `Icon`, `MenuText` and
`ToolTip` are added to the class. The `Icon` is a path to an image to be shown
on the workbench toolbar. The `MenuText` is a str text to be shown in
the listbox on the workbench toolbar. The `ToolTip` is a str tooltip
for the `Animate` workbench.
        """
        import os
        self.__class__.Icon = os.path.join(FreeCAD.getHomePath(), "Mod",
                                           "Animate", "Resources", "Icons",
                                           "Animate.xpm")
        self.__class__.MenuText = "Animate"
        self.__class__.ToolTip = "Animation workbench"

    def Initialize(self):
        """
Method used to setup workbench upon being selected on the workbench toolbar.

This function is executed when user clicks on `Animate` workbench in
the workbench listbox situated on the workbench toolbar. After that commands
are added to the FreeCAD Gui by importing their modules. The names
of imported commands are then saved in the `list` attribute.
Afterwards a toolbar and a menu with some of those commands are created.
        """
        FreeCAD.Console.PrintError("Whatever\n")
        # import here all the needed files that create your FreeCAD commands
        import Server
        import Control
        import Trajectory
        # A list of command names created in the line above
        self.list = ["ServerCommand", "ControlCommand", "TrajectoryCommand"]
        # creates a new toolbar with your commands
        self.appendToolbar("Animate", self.list)
        # creates a new menu
        self.appendMenu("Animate", self.list)
        # appends a submenu to an existing menu
        # self.appendMenu(["An existing Menu","My submenu"], self.sublist)

    def Activated(self):
        """
This function is executed when the workbench is activated.

For now it's used just to inform a user about the fact via console message.
        """
        FreeCAD.Console.PrintMessage("Animate workbench activated\n")

    def Deactivated(self):
        """
This function is executed when the workbench is deactivated.

For now it's used just to inform a user about the fact via console message.
        """
        FreeCAD.Console.PrintMessage("Animate workbench deactivated\n")

    def ContextMenu(self, recipient):
        """
Method to add custom commands to a context menu with respect to a recipient.

This method is executed whenever the user right-clicks in a Tree View or the
View box. It's possible to only add commands via `self.appendContextMenu()`.

Args:
    recipient: A str equal to "Tree" or "View" according to where user clicked.
        """
        # Log who is the recipient
        # FreeCAD.Console.PrintLog("Preparing context menu for " + recipient
        #                          + "\n")
        # Add commands to the context menu if necessary
        # self.appendContextMenu("My commands", self.list)
        pass

    def GetClassName(self):
        """
Mandatory method for full python workbenches.

Returns:
    A str with C++ binding class for this workbench.
        """
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(Animate())
