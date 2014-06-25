#!/usr/bin/env python

from copy import copy
from itertools import repeat

def transpose(matrix):
	return map(list, zip(*matrix))


class Tetris(object):
	def __init__(self,rows=22,cols=10):
		self._nrows = rows
		self._ncols = cols
		self._board = Board(rows,cols)
		self._score = Score()
		self._piece = None
		self._location = None

	def process(self,cmd):

		#Bad input convention causes collision for 'P', so order matters for these two
		if cmd=='P': print self._board
		elif cmd.istitle():
			self._piece = Piece(cmd)
			self._board.place(self._piece)

		#Other commands
		elif cmd=='g': self._board.set_from_command_line()
		elif cmd=='c': self._board.clear()
		elif cmd=='s': self.step()
		elif cmd==')': self._piece.rotate_cw()
		elif cmd=='(': self._piece.rotate_ccw()
		elif cmd==';': print ''
		elif cmd=='p': print self._board
		elif cmd=='t': print self._piece
		elif cmd=='?s': print self._score.score
		elif cmd=='?n': print self._score.nlines

	def step(self):
		(score,nlines) = self._board.step()
		self._score.score += score
		self._score.nlines += nlines



class Score(object):
	def __init__(self):
		self.score = 0
		self.nlines = 0
	

class TextGraphic(object):
	def __str__(self):
		return '\n'.join([' '.join(row) for row in transpose(self._data)])


class Piece(TextGraphic):
	def __init__(self,style):
		self._data = None
		if style=='I': self._data = [['.','c','.','.']]*4
		elif style=='O': self._data = [['y','y']]*2
		elif style=='Z': self._data = [['r','.','.'],['r','r','.'],['.','r','.']]
		elif style=='S': self._data = [['.','g','.'],['g','g','.'],['g','.','.']]
		elif style=='J': self._data = [['b','b','.'],['.','b','.'],['.','b','.']]
		elif style=='L': self._data = [['.','o','.'],['.','o','.'],['o','o','.']]
		elif style=='T': self._data = [['.','m','.'],['m','m','.'],['.','m','.']]
	def rotate_cw(self):
		self._data = transpose(self._data)
		self._data.reverse()
	def rotate_ccw(self):
		self._data.reverse()
		self._data = transpose(self._data)
	def nrows(self): return len(self._data[0])
	def ncols(self): return len(self._data)


class Board(TextGraphic):
	def __init__(self,rows,cols):
		self._rows = rows
		self._cols = cols
		self._empty = [	list(repeat('.',self._rows)) for _ in range(self._cols) ]
		self._data = self._empty
		self._fixed = self._empty

	def place(self, piece):
		self._data = copy(self._fixed)
		for r in range(piece.nrows()):
			for c in range(piece.ncols()):
				if piece._data[c][r]!='.':
					self._data[c+4][r] = copy(piece._data[c][r]).upper()

	def set_from_command_line(self):
		self._fixed = transpose( [raw_input().split() for i in xrange(self._rows)] )
		self._data = copy(self._fixed)

	def clear(self):
		self._data = copy(self._empty)
		self._fixed = copy(self._empty)

	def step(self):
		new_data = []
		score = 0
		nlines = 0
		for row in transpose(self._data):
			if '.' not in row:
				new_data.append(['.']*self._cols)
				score += 100
				nlines += 1
			else:
				new_data.append(row)
		self._data = transpose(new_data)
		return score, nlines


def input_generator():
	while True:
		for cmd in raw_input().split():
			yield cmd


if __name__ == "__main__":
	tetris = Tetris()
	for cmd in input_generator():
		if cmd=='q': break
		tetris.process(cmd)
