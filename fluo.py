#!/usr/bin/python3

import sys
import csv
import sqlite3
import fileinput
import re

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE ip (src TEXT, dst TEXT, dp TEXT)')
c.execute('CREATE TABLE dest (dipport TEXT)')

#print("Importing files")

reader = csv.reader(fileinput.input(),skipinitialspace=True)
for row in reader:
	c.execute('INSERT INTO ip VALUES (?,?,?)',(row[0], row[1], row[2]))

conn.commit()

print('digraph structs{')
print('node [shape=ellipse, style=filled, penwidth=0, fontsize=10, width=0,2, height=0,2, fontcolor="black", label""];')
print('edge [len=3];')

c.execute('SELECT src FROM ip GROUP BY src')
for row in c.fetchall():
	print('"'+row[0]+'" [label="'+row[0]+'", fillcolor=red]')

c.execute('SELECT dst FROM ip GROUP BY dst')
for row in c.fetchall():
	print('"'+row[0]+'" [label="'+row[0]+'", fillcolor=lightblue, shape=box]')

c.execute('SELECT dst,dp FROM ip GROUP BY (dst+dp)')
for row in c.fetchall():
	print('"'+str(row[0]) + " " + str(row[1]) + '" [label="'+str(row[1])+'", fillcolor=green]')
	print('"'+str(row[0]) + " " + str(row[1]) + '" -> "'+str(row[0])+'"')

c.execute('SELECT src FROM ip GROUP BY src ORDER BY src ASC')
for row in c.fetchall():
#	c.execute('SELECT COUNT(*),src, dst, dp FROM ip WHERE src LIKE ?',(row[0],))
	c.execute('SELECT COUNT(*),src, dst, dp FROM ip WHERE src LIKE ? GROUP BY dp',(row[0],))
	for line in c.fetchall():
		if (line[0] == 1):
			print('"'+str(line[1])+'" -> "' +str(line[2])+ ' '+ str(line[3])+ '"')
		else:
			print('"'+str(line[1])+'" -> "' +str(line[2])+ ' '+ str(line[3])+ '" [color=red, label="'+str(line[0])+'"]')

print('}')
