# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Python/Scripts/ServerGui/UiFiles/ServerGui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from util import ListWidget


class Ui_ServerGui(object):
    def setupUi(self, ServerGui):
        ServerGui.setObjectName("ServerGui")
        ServerGui.resize(1000, 715)
        ServerGui.setBaseSize(QtCore.QSize(1000, 715))
        font = QtGui.QFont()
        font.setKerning(True)
        ServerGui.setFont(font)
        ServerGui.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(ServerGui)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setBaseSize(QtCore.QSize(0, 0))
        self.splitter.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.splitter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.splitter.setAutoFillBackground(False)
        self.splitter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.listWidget = ListWidget(self.splitter)
        self.listWidget.setBaseSize(QtCore.QSize(0, 0))
        self.listWidget.setObjectName("listWidget")
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 83, 188))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.output_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.output_label.setFont(font)
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")
        self.verticalLayout.addWidget(self.output_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkbox_label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.checkbox_label.setFont(font)
        self.checkbox_label.setObjectName("checkbox_label")
        self.horizontalLayout.addWidget(self.checkbox_label)
        self.say_checkbox = QtWidgets.QCheckBox(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.say_checkbox.setFont(font)
        self.say_checkbox.setText("")
        self.say_checkbox.setObjectName("say_checkbox")
        self.horizontalLayout.addWidget(self.say_checkbox)
        self.input_lineedit = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.input_lineedit.setFont(font)
        self.input_lineedit.setObjectName("input_lineedit")
        self.horizontalLayout.addWidget(self.input_lineedit)
        self.execute_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.execute_button.setFont(font)
        self.execute_button.setObjectName("execute_button")
        self.horizontalLayout.addWidget(self.execute_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.verticalLayout_2.addWidget(self.start_button)
        self.restart_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.restart_button.setFont(font)
        self.restart_button.setObjectName("restart_button")
        self.verticalLayout_2.addWidget(self.restart_button)
        self.reload_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.reload_button.setFont(font)
        self.reload_button.setObjectName("reload_button")
        self.verticalLayout_2.addWidget(self.reload_button)
        self.kill_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.kill_button.setFont(font)
        self.kill_button.setObjectName("kill_button")
        self.verticalLayout_2.addWidget(self.kill_button)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.ram_progress_bar = QtWidgets.QProgressBar(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ram_progress_bar.setFont(font)
        self.ram_progress_bar.setProperty("value", 24)
        self.ram_progress_bar.setObjectName("ram_progress_bar")
        self.horizontalLayout_4.addWidget(self.ram_progress_bar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cpu_progress_bar = QtWidgets.QProgressBar(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.cpu_progress_bar.setFont(font)
        self.cpu_progress_bar.setProperty("value", 24)
        self.cpu_progress_bar.setObjectName("cpu_progress_bar")
        self.horizontalLayout_3.addWidget(self.cpu_progress_bar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.gui_usage_progress_bar = QtWidgets.QProgressBar(self.tab)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.gui_usage_progress_bar.setFont(font)
        self.gui_usage_progress_bar.setProperty("value", 24)
        self.gui_usage_progress_bar.setObjectName("gui_usage_progress_bar")
        self.horizontalLayout_2.addWidget(self.gui_usage_progress_bar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.current_config_combo_box = QtWidgets.QComboBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_config_combo_box.sizePolicy().hasHeightForWidth())
        self.current_config_combo_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.current_config_combo_box.setFont(font)
        self.current_config_combo_box.setObjectName("current_config_combo_box")
        self.horizontalLayout_8.addWidget(self.current_config_combo_box)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.java_version_combo_box = QtWidgets.QComboBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.java_version_combo_box.sizePolicy().hasHeightForWidth())
        self.java_version_combo_box.setSizePolicy(sizePolicy)
        self.java_version_combo_box.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.java_version_combo_box.setFont(font)
        self.java_version_combo_box.setObjectName("java_version_combo_box")
        self.horizontalLayout_6.addWidget(self.java_version_combo_box)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.min_ram_label = QtWidgets.QLabel(self.tab_3)
        self.min_ram_label.setMinimumSize(QtCore.QSize(150, 0))
        self.min_ram_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.min_ram_label.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.min_ram_label.setFont(font)
        self.min_ram_label.setObjectName("min_ram_label")
        self.verticalLayout_10.addWidget(self.min_ram_label)
        self.max_ram_label = QtWidgets.QLabel(self.tab_3)
        self.max_ram_label.setMinimumSize(QtCore.QSize(150, 0))
        self.max_ram_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.max_ram_label.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.max_ram_label.setFont(font)
        self.max_ram_label.setObjectName("max_ram_label")
        self.verticalLayout_10.addWidget(self.max_ram_label)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.min_ram_slider = QtWidgets.QSlider(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_ram_slider.sizePolicy().hasHeightForWidth())
        self.min_ram_slider.setSizePolicy(sizePolicy)
        self.min_ram_slider.setOrientation(QtCore.Qt.Horizontal)
        self.min_ram_slider.setObjectName("min_ram_slider")
        self.verticalLayout_9.addWidget(self.min_ram_slider)
        self.max_ram_slider = QtWidgets.QSlider(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_ram_slider.sizePolicy().hasHeightForWidth())
        self.max_ram_slider.setSizePolicy(sizePolicy)
        self.max_ram_slider.setOrientation(QtCore.Qt.Horizontal)
        self.max_ram_slider.setObjectName("max_ram_slider")
        self.verticalLayout_9.addWidget(self.max_ram_slider)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.jar_file_line_edit = QtWidgets.QLineEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jar_file_line_edit.sizePolicy().hasHeightForWidth())
        self.jar_file_line_edit.setSizePolicy(sizePolicy)
        self.jar_file_line_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.jar_file_line_edit.setFont(font)
        self.jar_file_line_edit.setText("")
        self.jar_file_line_edit.setObjectName("jar_file_line_edit")
        self.horizontalLayout_9.addWidget(self.jar_file_line_edit)
        self.jar_file_button = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jar_file_button.sizePolicy().hasHeightForWidth())
        self.jar_file_button.setSizePolicy(sizePolicy)
        self.jar_file_button.setObjectName("jar_file_button")
        self.horizontalLayout_9.addWidget(self.jar_file_button)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.custom_arguments_line_edit = QtWidgets.QLineEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_arguments_line_edit.sizePolicy().hasHeightForWidth())
        self.custom_arguments_line_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.custom_arguments_line_edit.setFont(font)
        self.custom_arguments_line_edit.setText("")
        self.custom_arguments_line_edit.setObjectName("custom_arguments_line_edit")
        self.horizontalLayout_10.addWidget(self.custom_arguments_line_edit)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.create_server_config_button = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_server_config_button.sizePolicy().hasHeightForWidth())
        self.create_server_config_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.create_server_config_button.setFont(font)
        self.create_server_config_button.setObjectName("create_server_config_button")
        self.verticalLayout_11.addWidget(self.create_server_config_button)
        self.launch_server_button = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.launch_server_button.sizePolicy().hasHeightForWidth())
        self.launch_server_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.launch_server_button.setFont(font)
        self.launch_server_button.setObjectName("launch_server_button")
        self.verticalLayout_11.addWidget(self.launch_server_button)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.server_options_table = QtWidgets.QTableWidget(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.server_options_table.setFont(font)
        self.server_options_table.setObjectName("server_options_table")
        self.server_options_table.setColumnCount(2)
        self.server_options_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.server_options_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.server_options_table.setHorizontalHeaderItem(1, item)
        self.verticalLayout_20.addWidget(self.server_options_table)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_14.addWidget(self.label_6)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.whitelist_list_widget = QtWidgets.QListWidget(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.whitelist_list_widget.setFont(font)
        self.whitelist_list_widget.setObjectName("whitelist_list_widget")
        self.verticalLayout_12.addWidget(self.whitelist_list_widget)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.add_whitelist_line_edit = QtWidgets.QLineEdit(self.tab_4)
        self.add_whitelist_line_edit.setObjectName("add_whitelist_line_edit")
        self.horizontalLayout_11.addWidget(self.add_whitelist_line_edit)
        self.add_whitelist_button = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_whitelist_button.setFont(font)
        self.add_whitelist_button.setObjectName("add_whitelist_button")
        self.horizontalLayout_11.addWidget(self.add_whitelist_button)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout_14.addLayout(self.verticalLayout_12)
        self.horizontalLayout_12.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_15.addWidget(self.label_9)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.ops_list_widget = QtWidgets.QListWidget(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ops_list_widget.setFont(font)
        self.ops_list_widget.setObjectName("ops_list_widget")
        self.verticalLayout_13.addWidget(self.ops_list_widget)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.add_op_line_edit = QtWidgets.QLineEdit(self.tab_4)
        self.add_op_line_edit.setObjectName("add_op_line_edit")
        self.horizontalLayout_13.addWidget(self.add_op_line_edit)
        self.add_op_button = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_op_button.setFont(font)
        self.add_op_button.setObjectName("add_op_button")
        self.horizontalLayout_13.addWidget(self.add_op_button)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.verticalLayout_15.addLayout(self.verticalLayout_13)
        self.horizontalLayout_12.addLayout(self.verticalLayout_15)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_18.addWidget(self.label_10)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.banned_players_list_widget = QtWidgets.QListWidget(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.banned_players_list_widget.setFont(font)
        self.banned_players_list_widget.setObjectName("banned_players_list_widget")
        self.verticalLayout_16.addWidget(self.banned_players_list_widget)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.add_banned_player_line_edit = QtWidgets.QLineEdit(self.tab_4)
        self.add_banned_player_line_edit.setObjectName("add_banned_player_line_edit")
        self.horizontalLayout_16.addWidget(self.add_banned_player_line_edit)
        self.add_banned_player_button = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_banned_player_button.setFont(font)
        self.add_banned_player_button.setObjectName("add_banned_player_button")
        self.horizontalLayout_16.addWidget(self.add_banned_player_button)
        self.verticalLayout_16.addLayout(self.horizontalLayout_16)
        self.verticalLayout_18.addLayout(self.verticalLayout_16)
        self.horizontalLayout_12.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_19.addWidget(self.label_11)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.banned_ips_list_widget = QtWidgets.QListWidget(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.banned_ips_list_widget.setFont(font)
        self.banned_ips_list_widget.setObjectName("banned_ips_list_widget")
        self.verticalLayout_17.addWidget(self.banned_ips_list_widget)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.add_banned_ip_line_edit = QtWidgets.QLineEdit(self.tab_4)
        self.add_banned_ip_line_edit.setObjectName("add_banned_ip_line_edit")
        self.horizontalLayout_17.addWidget(self.add_banned_ip_line_edit)
        self.add_banned_ip_button = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_banned_ip_button.setFont(font)
        self.add_banned_ip_button.setObjectName("add_banned_ip_button")
        self.horizontalLayout_17.addWidget(self.add_banned_ip_button)
        self.verticalLayout_17.addLayout(self.horizontalLayout_17)
        self.verticalLayout_19.addLayout(self.verticalLayout_17)
        self.horizontalLayout_12.addLayout(self.verticalLayout_19)
        self.verticalLayout_20.addLayout(self.horizontalLayout_12)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        ServerGui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ServerGui)
        self.statusbar.setObjectName("statusbar")
        ServerGui.setStatusBar(self.statusbar)

        self.retranslateUi(ServerGui)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ServerGui)

    def retranslateUi(self, ServerGui):
        _translate = QtCore.QCoreApplication.translate
        ServerGui.setWindowTitle(_translate("ServerGui", "Server Gui - iBlitzkriegi"))
        self.checkbox_label.setText(_translate("ServerGui", "Say"))
        self.execute_button.setText(_translate("ServerGui", "Execute"))
        self.start_button.setText(_translate("ServerGui", "Start"))
        self.restart_button.setText(_translate("ServerGui", "Restart"))
        self.reload_button.setText(_translate("ServerGui", "Reload"))
        self.kill_button.setText(_translate("ServerGui", "Kill"))
        self.label_3.setText(_translate("ServerGui", "Ram Usage"))
        self.label_4.setText(_translate("ServerGui", "CPU Usage"))
        self.label_5.setText(_translate("ServerGui", "GUI Usage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ServerGui", "Console"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ServerGui", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ServerGui", "IP"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ServerGui", "Time Joined"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ServerGui", "Whitelisted"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ServerGui", "OP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ServerGui", "Players"))
        self.label_2.setText(_translate("ServerGui", "Current Configuration"))
        self.label.setText(_translate("ServerGui", "Java Version"))
        self.min_ram_label.setText(_translate("ServerGui", "Min. Ram: "))
        self.max_ram_label.setText(_translate("ServerGui", "Max. Ram: "))
        self.label_7.setText(_translate("ServerGui", "JAR file:"))
        self.jar_file_button.setText(_translate("ServerGui", "..."))
        self.label_8.setText(_translate("ServerGui", "Custom arguments:"))
        self.create_server_config_button.setText(_translate("ServerGui", "Create new server configuration"))
        self.launch_server_button.setText(_translate("ServerGui", "Launch Server"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ServerGui", "Startup"))
        item = self.server_options_table.horizontalHeaderItem(0)
        item.setText(_translate("ServerGui", "Name"))
        item = self.server_options_table.horizontalHeaderItem(1)
        item.setText(_translate("ServerGui", "Value"))
        self.label_6.setText(_translate("ServerGui", "Whitelisted Players"))
        self.add_whitelist_button.setText(_translate("ServerGui", "Add"))
        self.label_9.setText(_translate("ServerGui", "Ops"))
        self.add_op_button.setText(_translate("ServerGui", "Add"))
        self.label_10.setText(_translate("ServerGui", "Banned Players"))
        self.add_banned_player_button.setText(_translate("ServerGui", "Add"))
        self.label_11.setText(_translate("ServerGui", "Banned Ips"))
        self.add_banned_ip_button.setText(_translate("ServerGui", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("ServerGui", "Server Options"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServerGui = QtWidgets.QMainWindow()
    ui = Ui_ServerGui()
    ui.setupUi(ServerGui)
    ServerGui.show()
    sys.exit(app.exec_())
