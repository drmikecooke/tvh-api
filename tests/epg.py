import sys
sys.path.append('../src')

from tvhAPI_pkg.epg import main
from tvhAPI_pkg.api import setUSR
setUSR()

main()
