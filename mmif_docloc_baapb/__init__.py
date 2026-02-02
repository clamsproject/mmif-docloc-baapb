import requests
import os
import secrets

RESOVLER_ADDRESS_ENVVAR = 'BAAPB_RESOLVER_ADDRESS'
if RESOVLER_ADDRESS_ENVVAR in os.environ:
    RESOLVER_ADDRESS = os.environ[RESOVLER_ADDRESS_ENVVAR]
else:
    RESOLVER_ADDRESS = 'localhost:5000'

_cache = {}


def resolve(docloc):
    if docloc in _cache:
        return _cache[docloc]
    scheme = 'baapb'
    if docloc.startswith(f'{scheme}://'):
        guid, document_type = docloc[len(scheme)+3:].rsplit('.', 1)
        url = 'http://' + RESOLVER_ADDRESS + '/searchapi'
        r = requests.get(url, params={'guid': guid, 'file':document_type})
        if 199 < r.status_code < 299:
            # when there are multiple files with the query guid, just return the first one
            results = r.json()
            if results:
                path = results[0]
            else:
                # return a seemingly valid but non-existent path when no results found
                # salt with random chars to prevent potential directory traversal attacks
                salt = secrets.token_hex(16)
                path = f'/_NOTFOUND_{salt}/{guid}.{document_type}'
            _cache[docloc] = path
            return path
        else:
            raise ValueError(f'cannot resolve document location: "{docloc}", '
                             f'is the resolver running at "{RESOLVER_ADDRESS}"?')
    else:
        raise ValueError(f'cannot handle document location scheme: "{docloc}"')

if __name__ == '__main__':
    import sys
    print(resolve(sys.argv[1]))

