# -*- coding: utf-8 -*-
import wx
import wx.xrc
import time
import pyperclip

import os
import sys
import platform

import data

###########################################################################
## Class MyFrame1
###########################################################################


class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PocLibrary", pos = wx.DefaultPosition, size = wx.Size( 300,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 300,150 ), wx.Size( 300,150 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"请选择查询的模块：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_comboBox1Choices = data.module_list
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"请选择！", wx.DefaultPosition, wx.Size( 150,-1 ), m_comboBox1Choices, 0 )
		bSizer1.Add( self.m_comboBox1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1.Bind(wx.EVT_BUTTON, self.select_module)

		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def select_module(self, event):
		global module

		module = self.m_comboBox1.GetValue()

		if module in data.module_list:
			win = MyFrame2(parent=None)
			win.Show()
			time.sleep(0.5)
			self.Destroy()
		else:
			temp_win = MyFrame3(parent=None)
			temp_win.Show()

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PocLibrary - Produced by Coldsnap", pos = wx.DefaultPosition, size = wx.Size( 800,750 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,750 ), wx.Size( 800,750 ) )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"请选择查询的POC/EXP：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		wSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_comboBox2Choices = self.setchoices(module)

		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"请选择！", wx.DefaultPosition, wx.Size( 500,-1 ), m_comboBox2Choices, 0 )
		wSizer1.Add( self.m_comboBox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2.Bind(wx.EVT_BUTTON, self.selectPoc)

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"漏洞信息：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		wSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(700, 200), 0 | wx.TE_READONLY | wx.TE_MULTILINE)
		self.m_textCtrl1.Enable(True)
		self.m_textCtrl1.SetMinSize(wx.Size(700, 200))
		self.m_textCtrl1.SetMaxSize(wx.Size(700, 200))

		wSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"利用信息：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		wSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400, 200), 0 | wx.TE_READONLY | wx.TE_MULTILINE)
		self.m_textCtrl2.Enable(True)
		self.m_textCtrl2.SetMinSize(wx.Size(700, 200))
		self.m_textCtrl2.SetMaxSize(wx.Size(700, 200))

		wSizer1.Add(self.m_textCtrl2, 0, wx.ALL, 5)

		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"利用内容：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		wSizer1.Add( self.m_staticText71, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(700, 200), 0 | wx.TE_READONLY | wx.TE_MULTILINE)
		self.m_textCtrl3.Enable(True)
		self.m_textCtrl3.SetMinSize(wx.Size(700, 200))
		self.m_textCtrl3.SetMaxSize(wx.Size(700, 200))

		wSizer1.Add(self.m_textCtrl3, 0, wx.ALL, 5)

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"复制利用内容", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		wSizer1.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		wSizer1.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button7.Bind(wx.EVT_BUTTON, self.copyCode)

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"重新选择模块", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		wSizer1.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		wSizer1.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button8.Bind(wx.EVT_BUTTON, self.back)

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"退出程序", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		wSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		wSizer1.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button9.Bind(wx.EVT_BUTTON, self.exit)

		self.SetSizer( wSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

# MyFrame1窗体模块参数送到MyFrame2创建对应窗体
	def setchoices(self, module):
		if module == "Drupal":
			return data.drupalchoice
		elif module == "F5":
			return data.f5choice
		elif module == "Fastjson":
			return data.fastjsonchoice
		elif module == "Jboss":
			return data.jbosschoice
		elif module == "Nexus":
			return data.nexuschoice
		elif module == "Shiro":
			return data.shirochoice
		elif module == "Apache-Solr":
			return data.solrchoice
		elif module == "Spring":
			return data.springchoice
		elif module == "Struts2":
			return data.struts2choice
		elif module == "Tomcat":
			return data.tomcatchoice
		elif module == "Weblogic":
			return data.weblogicchoice
		elif module == "Linux-local":
			return data.linuxchoice
		elif module == "Webmin":
			return data.webminchoice
		elif module == "IIS":
			return data.iischoice

# MyFrame2窗体选择POC/EXP后获取具体选项
	def selectPoc(self, event):

		str = self.m_comboBox2.GetValue()

		if str in data.drupalchoice:
			self.readfile(str)
		elif str in data.f5choice:
			self.readfile(str)
		elif str in data.jbosschoice:
			self.readfile(str)
		elif str in data.nexuschoice:
			self.readfile(str)
		elif str in data.shirochoice:
			self.readfile(str)
		elif str in data.solrchoice:
			self.readfile(str)
		elif str in data.springchoice:
			self.readfile(str)
		elif str in data.struts2choice:
			self.readfile(str)
		elif str in data.tomcatchoice:
			self.readfile(str)
		elif str in data.weblogicchoice:
			self.readfile(str)
		elif str in data.fastjsonchoice:
			self.readfile(str)
		elif str in data.linuxchoice:
			self.readfile(str)
		elif str in data.webminchoice:
			self.readfile(str)
		elif str in data.iischoice:
			self.readfile(str)
		else:
			temp_win = MyFrame3(parent=None)
			temp_win.Show()

# Windows下pyinstaller包含资源后在程序运行时产生临时文件夹，该函数返回资源临时文件夹地址
	def source_path(self, relative_path):
		# 是否Bundle Resource
		if getattr(sys, 'frozen', False):
			base_path = sys._MEIPASS # IDE运行报错，仅生成exe可执行文件时生效
		else:
			base_path = os.path.abspath(".")
		return os.path.join(base_path, relative_path)

# 根据MyFrame2传回的具体POC/EXP读取对应文件
	def readfile(self, str):

		os_name = platform.system()

		if os_name == 'Windows':
			vuln_file = open(self.source_path('Library/') + module + "/" + str + "_vul.txt", encoding="utf-8")
			info_file = open(self.source_path('Library/') + module + "/" + str + ".txt", encoding="utf-8")
			code_file = open(self.source_path('Library/') + module + "/" + str, encoding="utf-8")

			self.m_textCtrl1.SetValue(vuln_file.read())
			vuln_file.close()

			self.m_textCtrl2.SetValue(info_file.read())
			info_file.close()

			self.m_textCtrl3.SetValue(code_file.read())
			code_file.close()

		elif os_name == 'Darwin':

			vuln_file = open(os.getcwd() + "/Library/" + module + "/" + str + "_vul.txt", encoding="utf-8")
			info_file = open(os.getcwd() + "/Library/" + module + "/" + str + ".txt", encoding="utf-8")
			code_file = open(os.getcwd() + "/Library/" + module + "/" + str, encoding="utf-8")

			self.m_textCtrl1.SetValue(vuln_file.read())
			vuln_file.close()

			self.m_textCtrl2.SetValue(info_file.read())
			info_file.close()

			self.m_textCtrl3.SetValue(code_file.read())
			code_file.close()

# Copy功能对应的事件处理函数
	def copyCode(self, event):
		pyperclip.copy(self.m_textCtrl3.GetValue())

# Back功能对应的事件处理函数
	def back(self, event):
		win = MyFrame1(parent=None)
		win.Show()
		time.sleep(0.5)
		self.Destroy()

# Exit功能对应的事件处理函数
	def exit(self, event):
		time.sleep(0.5)
		self.Destroy()

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 200,100 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 200,100 ), wx.Size( 200,100 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"\n\n错误，请重新选择！", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer3.Add( self.m_staticText19, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass
