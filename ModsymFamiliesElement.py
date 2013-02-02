class ModsymFamiliesElement(Element):
	def d(self):
		return self.data[0].d

	## This function returns a number between 0 and p-2 which represents which 	
	## disc in weight the family is supported on -- the integer i corresponds to the
	## disc with characters with finite order part omega^i
	def disc(self):
		return self.data[0].parent._disc

	def change_d(self,new_d):
		v=[self.data[r].change_d(new_d) for r in range(self.ngens())]
        return ModsymFamiliesElement(self.level,v,self.manin)
    
	def specialize(self,k):
		v=[]
		for j in range(0,len(self.data)):
			v=v+[self.data[j].specialize(k)]
		return modsym_dist_aws(self.level,v,self.manin)
		"""Should we normalzie, so we get a modsym_dist?"""
	

	def normalize(self):
		v=[]
		for j in range(0,len(self.data)):
			v=v+[self.data[j].normalize()]

	def vector_of_total_measures(self):
		"""returns the vector comprising of the total measure of each distribution defining Phi"""
		v=[]
		for j in range(0,self.ngens()):
			v=v+[self.data[j].moments[0]]
		return v
		"""I am not sure it should be here"
