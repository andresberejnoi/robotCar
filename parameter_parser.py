
class parser(object):
	"""
	Accepted parameters:
	rate:float -> a rate for the background average function
	minArea:int -> minimum area in pixels that a blob must have in order to be recognized
	res:640x420 -> the resolution of the video coming from the camera
	numCount:10 -> number of significant blobs to keep track of
	"""
	def __init__(self):
		"""Reads parameters for the Computer Vision program """
		self.params = {"rate":None,
				"minArea":None,
				"res":None,
				"numCount":None,
				"path":0}

	def read_file(self, filename):
		"""
		Opens file and reads the parameters.
		Format must be correct.
		"""
		file_handler = open(filename)
		for line in file_handler:
			key,val = line.rstrip().split(":")
			#if the parameter has already been added,then its value is updated
			if key in self.params:
				self.params[key]=val
			else:
				print("Key {0} incorrect".format(key))
		
		self._parse()


	def _parse(self):
		"""Makes sure that parameter values have the right data type"""
		self.params["rate"]=float(self.params["rate"])
		self.params["numCount"]=int(self.params["numCount"])
		self.params["minArea"]=int(self.params["minArea"])
		self.params["res"] = [int(pxs) for pxs in self.params["res"].split("x") ]

	def get_params(self):
		"""Returns the dictionary containing the parameters"""
		return self.params
