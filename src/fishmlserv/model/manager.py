import os
def get_model_path():
#	import os...
	#fpath = "~/code/note"
	#pth = os.getcwd()
	#filepath = os.path.join(pth, 'model.pkl')

	mypath = __file__
	print(mypath)
	#/Users/kobatochan/code/fishmlserv/src/fishmlserv/model/manager.py
	dirname = os.path.dirname(mypath)
	#/Users/kobatochan/code/fishmlserv/src/fishmlserv/model
	#modelpath = dirname + "/" + "model.pkl"
	filepath = os.path.join(dirname, "model.pkl")
	
	#from fishmlserv.model.manager import get_model_path
	return filepath
