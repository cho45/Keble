#!/Applications/FreeCAD.app/Contents/MacOS/FreeCAD -c -P

import Idf

doc = App.newDocument("sketch")
App.ActiveDocument = doc

Idf.process_emn(doc, "./KeyModule-R.emn")
