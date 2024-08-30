from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float, weight:float):

	"""
	determining the kind of fish
	
	args:
		length (float) : fish length in cm
		weight (float): fish weight in g
	
	returns:
		dict: dictionary of kindof fish
	"""
	pred = "idk"
	if length > 30.0:
		pred = "도미"
	else:
		pred = "빙어"
	return {
		"pred" : pred,
		"length" : length,
		"weight" : weight}
