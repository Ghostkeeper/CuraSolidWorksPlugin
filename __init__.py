# Copyright (c) 2016 Thomas Karl Pietrowski

import os
import sys

third_party_dir = os.path.join(os.path.split(__file__)[0], "3rd_party")
if os.path.isdir(third_party_dir):
    sys.path.append(third_party_dir)

win32_dir = os.path.join(os.path.split(__file__)[0], "3rd_party", "win32")
if os.path.isdir(win32_dir):
    sys.path.append(win32_dir)
win32_dir = os.path.join(os.path.split(__file__)[0], "3rd_party", "win32", "lib")
if os.path.isdir(win32_dir):
    sys.path.append(win32_dir)
win32_dir = os.path.join(os.path.split(__file__)[0], "3rd_party", "pypiwin32_system32")
if os.path.isdir(win32_dir):
    sys.path.append(win32_dir)

from UM.Platform import Platform

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("CuraDassaultSystemesPlugins")

if Platform.isWindows():
    # For installation check
    import winreg
    # The reader plugin itself
    from . import SolidWorksReader


def getMetaData():
    metaData = {"mesh_reader": [],
                }
    
    if SolidWorksReader.is_any_sldwks_installed():
        metaData["mesh_reader"] += [{
                                        "extension": "SLDPRT",
                                        "description": i18n_catalog.i18nc("@item:inlistbox", "SolidWorks part file")
                                    },
                                    {
                                        "extension": "SLDASM",
                                        "description": i18n_catalog.i18nc("@item:inlistbox", "SolidWorks assembly file")
                                    },
                                    ]

    # TODO:
    # Needs more documentation on how to convert a CATproduct in CATIA using COM API
    #
    #{
    #    "extension": "CATProduct",
    #    "description": i18n_catalog.i18nc("@item:inlistbox", "CATproduct file")
    #}
    
    return metaData

def register(app):
    # Solid works only runs on Windows.
    plugin_data = {}
    if Platform.isWindows():
        reader = SolidWorksReader.SolidWorksReader()
        # TODO: Feature: Add at this point an early check, whether readers are available. See: reader.areReadersAvailable()
        if SolidWorksReader.is_any_sldwks_installed():
            plugin_data["mesh_reader"] = reader
        from .DialogHandler import DialogHandler
        plugin_data["extension"] = DialogHandler()
    return plugin_data
