#!/usr/bin/env python

def transpose(matrix):
	return map(list, zip(*matrix))


class Tetris(object):
	def __init__(self,rows=22,cols=10):
		self._nrows = rows
		self._ncols = cols
		self._board = Board(rows,cols)
		self._score = Score()
		self._piece = None

	def print_score(self): print self._score.score
	def print_nlines(self): print self._score.nlines
	
	def set_board_from_command_line(self): self._board.set_from_command_line()
	def clear_board(self): self._board.clear()
	def print_board(self): print self._board

	def step(self):
		(score,nlines) = self._board.step()
		self._score.score += score
		self._score.nlines += nlines

	def set_piece(self,style): self._piece = Piece(style)
	def print_piece(self): print self._piece


class Score(object):
	def __init__(self):
		self.score = 0
		self.nlines = 0
	

class TextGraphic(object):
	def __init__(self): pass
	def __str__(self):
		return '\n'.join([' '.join(row) for row in transpose(self._data)])


class Piece(TextGraphic):
	def __init__(self,style):
		self._data = None
		if style=='I': self._data = [['.','c','.','.']]*4
		if style=='O': self._data = [['y','y']]*2


class Board(TextGraphic):
	def __init__(self,rows,cols):
		self._rows = rows
		self._cols = cols
		self._empty = [['.']*self._rows]*self._cols
		self._data = self._empty


	def set_from_command_line(self):
		self._data = list(transpose( [raw_input().split() for i in xrange(self._rows)] ))

	def clear(self):
		self._data = self._empty

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


if __name__ == "__main__":
	cmd = ''
	tetris = Tetris()
	while cmd!='q':
		cmd=raw_input()
		if cmd=='p': tetris.print_board()
		if cmd=='g': tetris.set_board_from_command_line()
		if cmd=='c': tetris.clear_board()
		if cmd=='s': tetris.step()
		if cmd=='I': tetris.set_piece('I')
		if cmd=='O': tetris.set_piece('O')
		if cmd=='t': tetris.print_piece()
		if cmd=='?s': tetris.print_score()
		if cmd=='?n': tetris.print_nlines()
