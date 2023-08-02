from pathlib import Path
from getpass import getpass

comment="# TVH data"
bashrcp=Path.home()/".bashrc"
def addTVH():
	with open(bashrcp,'rt') as bashrc:
		b=bashrc.read()
	bl=b.split('\n')
	if comment in bl:
		ti=bl.index(comment)
		bl.pop(ti)
		bl.pop(ti)
	bl+=[comment,f'export TVH="{input("user: ")}:{getpass("pwd: ")}"']
	with open(bashrcp,"wt") as bashrc:
		bashrc.write('\n'.join(bl))
