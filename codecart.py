class SM():
	shoe_cost=None
	shirt_cost=None
	def __init__(self):
		self.shoe_qty=0
		self.shirt_qty=0
	def add(self,item,qty):
		if qty>0:
			if item == 'SHOE':
				self.shoe_qty=qty
				print(self.shoe_qty)
			elif item == 'SHIRT':
				self.shirt_qty=qty
				print(self.shirt_qty)

			else:
				print(-1)
		else:
			print(-1)
	def remove(self,item):
		if item == 'SHOE':
			self.shoe_qty=-1
		elif item == 'SHIRT':
			self.shirt_qty=-1
		else:
			print(-1)
	def print_qty(self,item):
		if item == 'SHOE':
			if self.shoe_qty > -1:
				print(self.shoe_qty)
			else:
				print(0)
		elif item == 'SHIRT':
			if self.shirt_qty >-1:
				print(self.shirt_qty)
			else:
				print(0)
		else:
			print(0)
	def incr(self,item,qty):
		if qty>0:
			if item == 'SHOE':
				if self.shoe_qty ==-1:
					print(-1)
				elif self.shoe_qty !=-1:
					self.shoe_qty+=qty
					print(qty)
				else:
					print(-1)
			elif item == 'SHIRT':
				if self.shirt_qty ==-1:
					print(-1)
				elif self.shirt_qty !=-1:
					self.shirt_qty+=qty
					print(qty)
				else:
					print(-1)
		else:
			print(-1)

	def dcr(self,item,qty):
		if qty>0:
			if item == 'SHOE':
				if self.shoe_qty ==-1:
					print(-1)
				elif self.shoe_qty !=-1:
					self.shoe_qty-=qty
					print(qty)
				else:
					print(-1)
			elif item == 'SHIRT':
				if self.shirt_qty ==-1:
					print(-1)
				elif self.shirt_qty !=-1:
					self.shirt_qty-=qty
					print(qty)
				else:
					print(-1)
		else:
			print(-1)

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
class S():
	def __init__(self):
		self.shoe_qty=0
		self.shirt_qty=0
	def add(self,item,qty):
		if qty>0:
			if item == 'SHOE':
				self.shoe_qty=qty
				print(self.shoe_qty)
			elif item == 'SHIRT':
				self.shirt_qty=qty
				print(self.shirt_qty)
			else:
				print(-1)
		else:
			print(-1)
	def remove(self,item):
		if item == 'SHOE':
			self.shoe_qty=-1
		elif item == 'SHIRT':
			self.shirt_qty=-1
		else:
			print(-1)
	def incr(self,item,qty):
		if qty>0:
			if item == 'SHOE':
				if self.shoe_qty ==-1:
					print(-1)
				elif self.shoe_qty !=-1:
					self.shoe_qty+=qty
					print(qty)
				else:
					print(-1)
			elif item == 'SHIRT':
				if self.shirt_qty ==-1:
					print(-1)
				elif self.shirt_qty !=-1:
					self.shirt_qty+=qty
					print(qty)
				else:
					print(-1)
		else:
			print(-1)

	def dcr(self,item,qty):
		if qty>0:
			if item == 'SHOE':
				if self.shoe_qty ==-1:
					print(-1)
				elif self.shoe_qty !=-1:
					self.shoe_qty-=qty
					print(qty)
				else:
					print(-1)
			elif item == 'SHIRT':
				if self.shirt_qty ==-1:
					print(-1)
				elif self.shirt_qty !=-1:
					self.shirt_qty-=qty
					print(qty)
				else:
					print(-1)
		else:
			print(-1)
	def amount(self,shirt_cost,shirt_qty,shoe_cost,shoe_qty):
		if shirt_qty <=0:
			shirt_qty =0
		if shoe_qty <=0:
			shoe_qty =0
		ans=(shirt_qty*shirt_cost)+(shoe_qty*shoe_cost)
		return ans




T=int(input())
while(T):
	T-=1
	sm=SM()
	s=S()
	add=[]
	add_c=[]
	while True:
		inp=input().split(' ')
		if inp[0]=='END':
			break
		elif inp[0] == 'CMD' :
			if inp[1] == 'SM':
				if inp[2] == 'ADD':
					if inp[2] not in add:
						sm.add(inp[3],int(inp[4]))
						add.append(inp[3])
					else:
						print(-1)
				elif inp[2] == 'REMOVE':
					if inp[3] in add:
						sm.remove(inp[3])
						s.remove(inp[3])
						add.remove(inp[3])
						print(1)
					else:
						print(-1)
				elif inp[2] == 'GET_QTY':
					sm.print_qty(inp[3])
				elif inp[2] == 'INCR':
					if inp[3] in add:
						sm.incr(inp[3],int(inp[4]))
					else:
						print(-1)
				elif inp[2] == 'DCR':
					if inp[3] in add:
						if inp[3] == 'SHOE' and sm.shoe_qty-int(inp[4]) >=0:
							sm.dcr(inp[3],int(inp[4]))
							if sm.shoe_qty <=s.shoe_qty:
								s.shoe_qty=sm.shoe_qty
						elif inp[3] == 'SHIRT' and sm.shirt_qty - int(inp[4]) >=0:
							sm.dcr(inp[3],int(inp[4]))
							if sm.shirt_qty <=s.shirt_qty:
								s.shirt_qty=sm.shirt_qty
						else:
							print(-1)
					else:
						print(-1)
				elif inp[2] == 'SET_COST':
					if inp[3] == 'SHIRT':
						sm.shirt_cost = int(inp[4])
						ans=float(sm.shirt_cost)
						ans=round(ans,1)
						print(ans)
					elif inp[3] == 'SHOE':
						sm.shoe_cost = int(inp[4])
						ans=float(sm.shoe_cost)
						ans=round(ans,1)
						print(ans)
					else:
						print(-1)
				else:
					print(-1)
		#==============================================
			elif inp[1] == 'S':
				if inp[2] == 'ADD':
					if inp[2] not in add_c:
						s.add(inp[3],int(inp[4]))
						add_c.append(inp[3])
					else:
						print(-1)
				elif inp[2] == 'REMOVE':
					if inp[3] in add_c:
						s.remove(inp[3])
						add_c.remove(inp[3])
						print(1)
					else:
						print(-1)
				elif inp[2] == 'INCR':
					if inp[3] in add_c:
						if inp[3] == 'SHOE':
							if sm.shoe_qty >= s.shoe_qty+int(inp[4]):
								s.incr(inp[3],int(inp[4]))
							else:
								print(-1)
						elif inp[3] == 'SHIRT':
							if sm.shirt_qty >= (s.shirt_qty+int(inp[4])):
								s.incr(inp[3],int(inp[4]))
							else:
								print(-1)
					else:
						print(-1)
				elif inp[2] == 'DCR':
					if inp[3] in add_c:
						if inp[3] == 'SHOE' and s.shoe_qty-int(inp[4]) >=0:
							s.dcr(inp[3],int(inp[4]))
						elif inp[3] == 'SHIRT' and s.shirt_qty-int(inp[4]) >=0:
							s.dcr(inp[3],int(inp[4]))
						else:
							print(-1)
					else:
						print(-1)
				elif inp[2] == 'GET_ORDER_AMOUNT':
					ans=s.amount(sm.shirt_cost,s.shirt_qty,sm.shoe_cost,s.shoe_qty)
					# ans=round(ans,2)
					#print(f'shirt_qty{s.shirt_qty}')
					#print(f'shoe_qty{s.shoe_qty}')
					print("{:.2f}".format(ans))
				else:
					print(-1)
			else:
				print(-1)

		else:
			pass

	





	

