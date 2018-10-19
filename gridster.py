
# Author: Pierce Brooks

class Guy(object):
	def __init__(self, number):
		self.number = number
		self.grid = None
		self.x = None
		self.y = None
		
	def get_number(self):
		return self.number
		
	def get_at(self):
		return [self.x, self.y]
		
	def put_at(self, grid, x, y):
		self.grid = grid
		if not (grid == None):
			self.x = x
			self.y = y
		else:
			self.x = None
			self.y = None
		
	def erase(self):
		if (self.grid == None):
			return False
		return self.grid.put_guy_at(self.x, self.y, None)
		
	def move_left(self):
		if (self.grid == None):
			return False
		if (self.x == 0):
			return False
		grid = self.grid
		self.erase()
		return grid.put_guy_at(self.x-1, self.y, self)
		
	def move_right(self):
		if (self.grid == None):
			return False
		if (self.x == self.grid.get_width()-1):
			return False
		grid = self.grid
		self.erase()
		return grid.put_guy_at(self.x+1, self.y, self)
		
	def move_up(self):
		if (self.grid == None):
			return False
		if (self.y == 0):
			return False
		grid = self.grid
		self.erase()
		return grid.put_guy_at(self.x, self.y-1, self)
		
	def move_down(self):
		if (self.grid == None):
			return False
		if (self.y == self.grid.get_height()-1):
			return False
		grid = self.grid
		self.erase()
		return grid.put_guy_at(self.x, self.y+1, self)
		
	def move(self, offset):
		if (self.grid == None):
			return False
		x = offset[0]
		y = offset[1]
		success = True
		if not (x == 0):
			for i in range(abs(x)):
				if (x < 0):
					if not (self.move_left()):
						success = False
						break
				else:
					if not (self.move_right()):
						success = False
						break
		if not (success):
			return False
		if not (y == 0):
			for i in range(abs(y)):
				if (y < 0):
					if not (self.move_up()):
						success = False
						break
				else:
					if not (self.move_down()):
						success = False
						break
		return success

class Grid(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.guys = []
		for x in range(self.width):
			self.guys.append([])
			for y in range(self.height):
				self.guys[x].append(None)
		self.indent = "  "
		
	def check_position(self, x, y):
		if ((x == None) or (y == None)):
			return False
		if ((x < 0) or (x >= self.get_width())):
			return False
		if ((y < 0) or (y >= self.get_height())):
			return False
		return True
	
	def get_draw(self):
		draw = ""
		width = (self.width*2)+1
		height = (self.height*2)+1
		guy_x = 0
		guy_y = 0
		for y in range(height):
			draw += self.indent
			for x in range(width):
				horizontal_check = False
				vertical_check = False
				if (x%2 == 0):
					horizontal_check = True
				if (y%2 == 0):
					vertical_check = True
				if not ((horizontal_check) or (vertical_check)):
					guy = self.get_guy_at(guy_x, guy_y)
					draw += " "
					if not (guy == None):
						draw += str(guy.get_number())[0]
					else:
						draw += " "
					draw += " "
					guy_x += 1
					if (guy_x == self.width):
						guy_y += 1
						guy_x = 0
				else:
					if ((horizontal_check) and (vertical_check)):
						draw += "+"
					else:
						if (horizontal_check):
							draw += "|"
						else:
							draw += "---"
			draw += "\n"
		return draw
		
	def do_draw(self):
		print(self.get_draw())
		
	def get_width(self):
		return self.width
		
	def get_height(self):
		return self.height
		
	def get_guys(self):
		return self.guys
		
	def get_guy_at(self, x, y):
		#print("get@"+str(x)+","+str(y))
		if not (self.check_position(x, y)):
			return None
		return self.get_guys()[x][y]
		
	def put_guy_at(self, x, y, guy):
		#print("put@"+str(x)+","+str(y))
		if not (self.check_position(x, y)):
			return False
		self.guys[x][y] = guy
		if not (guy == None):
			guy.put_at(self, x, y)
		return True
		
	def erase_guys(self):
		for x in range(self.width):
			for y in range(self.height):
				self.put_guy_at(x, y, None)
		
def draw_grid(grid):
	grid.do_draw()

def make_grid(width, height):
	return Grid(width, height)
	
def make_guy(number):
	return Guy(number)
	
def put_guy_on_grid_at(x, y, guy, grid):
	return grid.put_guy_at(x, y, guy)
	
def move_guy_left(guy):
	return guy.move_left()

def move_guy_right(guy):
	return guy.move_right()
	
def move_guy_up(guy):
	return guy.move_up()
	
def move_guy_down(guy):
	return guy.move_down()
	