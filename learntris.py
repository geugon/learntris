#!/usr/bin/env python

def transpose(matrix):
	return map(list, zip(*matrix))


class Board():
	def __init__(self,rows=22,cols=10):
		self._rows = rows
		self._cols = cols
		self._empty = [['.']*self._rows]*self._cols
		self._data = self._empty
		self._score = 0
		self._nlines = 0
	def __str__(self):
		return '\n'.join([' '.join(row) for row in transpose(self._data)])

	def set_from_command_line(self):
		self._data = list(transpose( [raw_input().split() for i in xrange(self._rows)] ))
	def empty(self):
		self._data = self._empty
	def score(self):
		return self._score
	def nlines(self):
		return self._nlines
		

if __name__ == "__main__":
	cmd = ''
	board = Board()
	while cmd!='q':
		cmd=raw_input()
		if cmd=='p': print board
		if cmd=='g': board.set_from_command_line()
		if cmd=='c': board.empty()
		if cmd=='?s': print board.score()
		if cmd=='?n': print board.nlines()
