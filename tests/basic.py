import sys
sys.path.append('../src')

import tvhAPI_pkg.api
tvhAPI_pkg.api.setUSR()

print(tvhAPI_pkg.api.getAPI(input("tvh: "),"status/subscriptions"))
