# File: q1.py
# Author: Yuhao Ye
# Date: 06/13/2020
# Section: 529006730(UIN)
# E-mail: yeyuhao1234@tamu.edu
# Description:
# This program takes the edges of the boxes
# and calculate the sum of all edges and the volume
# of the box

edges = input("Enther the edge lengths of a box ( in ft ): ").split()
print()
total_edges = 4 *(float(edges[0]) + float(edges[1]) + float(edges[2]))
volume = float(edges[0]) * float(edges[1]) * float(edges[2])
print(f'The sum of all edges of the box is { round(total_edges,4) } ft.')
print(f'The volume of the box is {round(volume,4)} cubic ft.')
