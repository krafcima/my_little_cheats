import os
from zipfile import ZipFile as zf
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import ctypes

class Rozbal:
	def __init__(self):
		self.pracovnyPriecinok = os.getcwd()
		self.subory = dict()

	def nastavPriecinok(self, priecinok):
		os.chdir(priecinok)
		self.pracovnyPriecinok = os.getcwd()

	def ziskajSubory(self):
		self.subory = dict()
		buff = os.listdir(self.pracovnyPriecinok)
		for i in range(len(buff)):
			r = buff[i].replace('.zip', '')
			if (r == buff[i]):
				if ('zip' in buff):
					self.subory.setdefault(buff[i], True)
			else:
				if ('.zip' in buff[i]):
					self.subory.setdefault(buff[i], False)

	def rozbal(self):
		for nazov, stav in self.subory.items():
			if (stav == False):
				with zf(self.pracovnyPriecinok +'\\' + nazov, 'r') as f:
					f.extractall(self.pracovnyPriecinok +'\\' + nazov.replace('.zip', ''))
					self.subory[nazov] = True
		
	def rozbal2(self, subor):
		with zf(self.pracovnyPriecinok +'\\' + subor, 'r') as f:
			f.extractall(self.pracovnyPriecinok +'\\' + subor.replace('.zip', ''))
			self.subory[subor] = True
		
	def kontrola(self):
		for nazov, stav in self.subory.items():
			if (not stav):
				return False

class Rozbalovac:

	def __init__(self):
		self.rozbalovac = Rozbal()
		self.buttony = {}
		self.polozky = []
		
		self.directory = None
		self.root = Tk()
		self.root.title('EXTRACTOR')
		self.root.geometry('500x500')

		b = Button(self.root, text='VYBER ADRESAR', command=self.directoryName)
		b.pack()

		#b = Button(self.root, text='REFRESH', command=self.refresh)
		#b.pack()

		b = Button(self.root, text='UNZIP CHOOSEN', command=self.unzipPicked)
		b.pack()

		b = Button(self.root, text='UNZIPALL', command=self.unzipAll)
		b.pack()

		menubar = Menu(self.root)

		# create a pulldown menu, and add it to the menu bar
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label='Load', command=self.load)
		filemenu.add_command(label='Save', command=self.uloz)
		filemenu.add_command(label='Exit', command=self.root.destroy)
		menubar.add_cascade(label='File', menu=filemenu)

		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label='About', command=self.About)
		menubar.add_cascade(label='Help', menu=helpmenu)

		# display the menu
		self.root.config(menu=menubar)

		
	def uloz(self):
		pass
	def load(self):
		pass
	def About(self):
		messagebox.showinfo(title='About', message = '''Created by: Marek Krafčik
Version: 1.0
EGUI - it is and GUI interface for zipFile python build in library for ordinary users. ''')
		return
	def Achtung(self):
		return
	def unzipAll(self):
		self.unzipFilesAll()
	def unzipPicked(self):
		self.unzip()

	def directoryName(self):
		self.directory = filedialog.askdirectory()
		self.rozbalovac.nastavPriecinok(self.directory)
		self.getFiles()
		self.drawFiles()
		print(self.directory)

	def refresh(self):
		for i in self.polozky:
			i.destroy()
		self.root.update()
		self.root.after(1000)
		self.drawFiles()

	def getFiles(self):
		if self.directory is not None:
			self.rozbalovac.ziskajSubory()

	def drawFiles(self):
		self.polozky = []
		#self.getFiles()
		pom = list(self.rozbalovac.subory.keys())
		self.buttony = dict()
		for i in range(len(pom)):
			if self.rozbalovac.subory[pom[i]] == False:
				var = BooleanVar()
				w = Checkbutton(self.root, text = pom[i], variable = var)
				w.pack()
				self.polozky.append(w)
				self.buttony[pom[i]] = var
	'''

	'''
	def unzipFilesAll(self):
		self.rozbalovac.rozbal()
		#print(self.rozbalovac.subory)
		self.refresh()
		
	def unzip(self):
		for nazov, stav in self.buttony.items():
			#print('Nazov:\t{}\tstav:\t{}'.format(nazov,stav.get())
				if stav.get() == True:
					self.rozbalovac.rozbal2(nazov)
		self.refresh()

c = Rozbalovac()