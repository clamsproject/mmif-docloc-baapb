import requests
import os

if 'BAAPB_RESOLVER_ADDRESS' in os.environ:
    RESOLVER_ADDRESS = os.environ['BAAPB_RESOLVER_ADDRESS']
else:
    RESOLVER_ADDRESS = 'localhost:5000'


def resolve(docloc):
    scheme = 'baapb'
    if docloc.startswith(f'{scheme}://'):
        guid, document_type = docloc[len(scheme)+3:].rsplit('.', 1)
        url = 'http://' + RESOLVER_ADDRESS + '/searchapi'
        r = requests.get(url, params={'guid': guid, 'file':document_type})
        if 199 < r.status_code < 299:
            return r.text
        else:
            raise ValueError(f'cannot resolve document location: "{docloc}", '
                             f'is the resolver running at "{RESOLVER_ADDRESS}"?')
    else:
        raise ValueError(f'cannot handle document location scheme: "{docloc}"')

