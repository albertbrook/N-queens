class Queen(object):
	num = 0

	def __init__(self, count):
		self.count = count
		self.chess = [[0] * self.count for _ in range(self.count)]
		self.seek()

	def seek(self, row=0):
		if row == self.count:
			self.print_chess()
			self.reset(row - 1)
			return
		for col in range(self.count):
			if self.check(row, col):
				self.chess[row][col] = 1
				self.seek(row + 1)
		else:
			self.reset(row - 1)

	def check(self, row, col):
		for i in range(self.count):
			if self.chess[row][i] or self.chess[i][col]:
				return False
			for j in range(self.count):
				if abs(i - row) == abs(j - col) and self.chess[i][j]:
					return False
		else:
			return True

	def reset(self, row):
		for col in range(self.count):
			if self.chess[row][col] == 1:
				self.chess[row][col] = 0
				return

	def print_chess(self):
		self.num += 1
		print("NO.%d" % self.num)
		for row in range(self.count):
			for col in range(self.count):
				print(self.chess[row][col], end=" ")
			print()


if __name__ == "__main__":
	while True:
		try:
			n = int(input("n = "))
			queen = Queen(n)
		except ValueError:
			print("input error")
