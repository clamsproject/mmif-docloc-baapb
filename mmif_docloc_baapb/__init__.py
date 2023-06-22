import requests
import os

if 'RESOLVER_ADDRESS' in os.environ:
    RESOLVER_ADDRESS = os.environ['RESOLVER_ADDRESS']
else:
    RESOLVER_ADDRESS='localhost:5000'

def resolve(docloc):
    scheme = 'baapb'
    if docloc.startswith(f'{scheme}://'):
        guid, document_type = docloc[len(scheme)+3:].rsplit('.', 1)
        url = 'http://' + RESOLVER_ADDRESS + '/searchapi'
        r = requests.get(url, params={'guid': guid, 'file':document_type})
        return r.text
    else:
        raise ValueError(f'cannot handle document location scheme: {docloc}')

