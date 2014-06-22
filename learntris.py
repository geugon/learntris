#!/usr/bin/env python

def transpose(matrix):
	return map(list, zip(*matrix))


class Board():
	def __init__(self,rows=22,cols=10):
		self._rows = rows
		self._cols = cols
		self._data = [['.']*self._rows]*self._cols
	def __str__(self):
		return '\n'.join([' '.join(row) for row in transpose(self._data)])
#	def set_from_command_line(self):
#		self._data = transpose( [raw_input().split() for i in xrange(self._rows)] )
		

if __name__ == "__main__":
	cmd = ''
	board = Board()
	while cmd!='q':
		cmd=raw_input()
		if cmd=='p': print board
#		if cmd=='g': board.set_from_command_line()
