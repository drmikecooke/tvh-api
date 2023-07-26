import sys
sys.path.append('../src')

from epg_package.channels import chlist

from pathlib import Path
chf=Path.home()/".epg.conf"
print(chf.is_file())
if chf.is_file():
	with open(chf,"rt") as chsf:
		channels=chsf.read().split("\n")[:-1]
else:
	print("Getting fresh channel list")
	channels=chlist(tvh)
	print("Saving list at:",chf)
	with open(chf,"wt") as chsf:
		chsf.write('\n'.join(channels))
		
print(channels)
