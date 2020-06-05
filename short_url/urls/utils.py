import base62

def encode(url):
    url_encoded = base62.encode(url)
    return url_encoded

def decode(url):
    url_decoded = base62.decode(url)
    return url_decoded
