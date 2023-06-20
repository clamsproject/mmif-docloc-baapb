
# TODO: this value should be configurable via environment variable
RESOVLER_ADDRESS='localhost:20202'

def resolve(docloc):
    scheme = 'baapb'
    if docloc.startswith(f'{scheme}://'):
        guid, document_type = docloc[len(scheme)+3:].rsplit('.', 1)
        # TODO: for now, just return a dummy file path
        if 'video' in document_type.lower():
            return '/path/to/cpb-aacip_15-99p2w600.mp4'
        elif 'audio' in document_type.lower():
            return '/path/to/cpb-aacip_15-99p2w600.mp3'
        elif 'text' in document_type.lower():
            return '/path/to/cpb-aacip_15-99p2w600.txt'
    else:
        raise ValueError(f'cannot handle document location scheme: {docloc}')

