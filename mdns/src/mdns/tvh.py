import urllib.request as ur
from json import loads

statkeys=["ber","ec_bit","ec_block","tc_bit","tc_block","te","cc","unc"]

passman = ur.HTTPPasswordMgrWithDefaultRealm()
authhandler = ur.HTTPDigestAuthHandler(passman)
opener = ur.build_opener(authhandler)
ur.install_opener(opener)

def data(ip,api):
    url=f"http://{ip}:9981/api/{api}"
    passman.add_password(None, url,USER,PWD)
    res = ur.urlopen(url,None,1)
    return loads(res.read())
    
def subs(ip):
    hd=data(ip,"status/subscriptions")
    return [entry['title'] for entry in hd['entries']]

def nxt(ip):
    gd=data(ip,"dvr/entry/grid_upcoming")
    if gd['total']>40:
        print(f'Check all entries for {ip}\n')
    starts=[item['start_real'] for item in gd['entries']]
    return min(starts) if starts else None
        
def status(ip):
    sd=data(ip,'status/inputs')['entries'][0]
    return {key:sd[key] for key in statkeys}
