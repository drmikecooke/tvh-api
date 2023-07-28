from .api import getAPI

def chlist(tvh):
	return [item["val"] for item in getAPI(tvh,"channel/list")["entries"]]
