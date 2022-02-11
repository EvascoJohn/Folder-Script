import os
import logging
from tkinter import filedialog
from tkinter import * 

"""
@author: John Carlo Evasco
"""
current_directory = os.curdir


class FolderObj(object):

	def __init__(self, foldername, subfolders):
		self.foldername = foldername
		self.subfolders = subfolders


def browse_button():
    filename = filedialog.askdirectory()
    return filename


#reads text file and turns it to a list by splitting each text by a new line
def read_text_file(textfile):
	items = []
	with open(textfile) as txtfile:
		for subject in txtfile.read().split("\n"):
			logging.info(f"reads {subject} from {textfile}")
			if subject == "":
				pass
			items.append(subject)
	return items


#reads text file and turns it to a list by splitting each text by a new line and spliting it with coma for acronyms
def read_subjects_with_acronym(textfile):
	items = []
	with open(textfile) as txtfile:
		for subject in txtfile.read().split("\n"):
			if subject == "":
				pass
			items.append({"Subject_Name":subject.split(",")[0],"Subject_Acronym":subject.split(",")[1]})
	return items


#creates a folder with premade sub folders
def make_folder_with_subfolders(path ,foldername, subfolderslist):
	""" returns a list of dictionary """
	try:
		if path == "" or  path ==".":
			pass
		else:
			os.mkdir(os.path.join(path,foldername))
			logging.info(f"creates folder {os.path.join(path, foldername)}")
			for folder in subfolderslist:
				os.mkdir(os.path.join(os.path.join(path, foldername),folder))
				logging.info(f"creates folder {os.path.join(os.path.join(path, foldername),folder)}")
	except:
		pass
	

def run():
	""" run """
	logging.basicConfig(filename="LOGS.log", level=logging.DEBUG)
	root = Tk()
	root.withdraw()
	user_chosen_location = browse_button()
	for subject in read_text_file("Subjects.txt"):
		make_folder_with_subfolders(os.path.normpath(user_chosen_location), subject, read_text_file("CommonSubFolders.txt"))

run()
