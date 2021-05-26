import requests
import sys
b=[]
def get_token(url1,username,password):
    r = requests.get(url1, auth=(username,password))
    a=r.json()['continuationToken']
    while a:
        b.append(a)
        u = nexus_repostory_url
        return get_token(u+'&continuationToken='+ a,username,password )
    return b

nexus_repostory_url=str(sys.argv[1])
username=str(sys.argv[2])
password=str(sys.argv[3])
print("{} {} {}".format(nexus_repostory_url,username,password))
gettokens = get_token(nexus_repostory_url,username,password)
print(gettokens)
