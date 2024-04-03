#!/bin/bash
pyside6-uic src/UIs/main_window.ui -o src/UIs/main_window.py --absolute-imports
pyside6-rcc src/res/res.qrc -o src/res/res_rc.py